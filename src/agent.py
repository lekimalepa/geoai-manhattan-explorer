# src/agent.py

import re

from src.analytics import (
    count_pois,
    rank_neighbourhoods,
    summarise_neighbourhood_simple,
    nearby_food
)

from src.mapping import (
    restaurant_map,
    amenity_map,
    neighbourhood_map,
    nearby_food_map,
    ranking_map
)


# ==================================================
# INTENT IDENTIFICATION
# ==================================================

def identify_intent(query):

    q = query.lower()

    if "how many" in q:
        return "count"

    if "show" in q:
        return "show"

    if "most" in q:
        return "rank"

    if "compare" in q:
        return "compare"

    if (
        "nearby" in q
        or "food options" in q
        or "financial district" in q
    ):
        return "nearby"

    if (
        "what kind of neighbourhood" in q
        or "describe" in q
        or "tell me about" in q
    ):
        return "describe"

    return "unknown"


# ==================================================
# EXTRACT AMENITY
# ==================================================

def extract_amenity(query):

    q = query.lower()

    amenities = [
        "restaurant",
        "cafe",
        "bar",
        "bank",
        "school",
        "hospital"
    ]

    for amenity in amenities:

        if amenity in q:

            return amenity

    return None


# ==================================================
# EXTRACT NEIGHBOURHOOD
# ==================================================

def extract_neighbourhood(query):

    match = re.search(
        r"in (.+?)\??$",
        query,
        re.IGNORECASE
    )

    if match:

        return match.group(1).strip()

    return None


# ==================================================
# MAIN AGENT
# ==================================================

def run_agent(
    query,
    pois_gdf,
    nta_gdf
):

    intent = identify_intent(query)

    amenity = extract_amenity(query)

    q = query.lower()

    # ==================================================
    # COUNT
    # ==================================================

    if intent == "count":

        if amenity:

            neighbourhood = extract_neighbourhood(query)

            if neighbourhood:

                nta_name, n = count_pois(
                    category=amenity,
                    neighbourhood=neighbourhood,
                    pois_gdf=pois_gdf
                )

                m = amenity_map(
                    amenity,
                    neighbourhood,
                    pois_gdf
                )

                return {
                    "query_type": "count",
                    "message":
                        f"There are {n} "
                        f"{amenity}s in "
                        f"{nta_name}.",
                    "map": m
                }

    # ==================================================
    # SHOW
    # ==================================================

    if intent == "show":

        if amenity:

            neighbourhood = extract_neighbourhood(query)

            if neighbourhood:

                m = amenity_map(
                    amenity,
                    neighbourhood,
                    pois_gdf
                )

                return {
                    "query_type": "show",
                    "message":
                        f"Showing "
                        f"{amenity}s in "
                        f"{neighbourhood}.",
                    "map": m
                }

    # ==================================================
    # DESCRIBE
    # ==================================================

    if intent == "describe":

        match = re.search(
            r"(?:is|describe|about)\s+(.+?)\??$",
            query,
            re.IGNORECASE
        )

        if match:

            neighbourhood = (
                match.group(1)
                .strip()
            )

            summary = (
                summarise_neighbourhood_simple(
                    neighbourhood,
                    pois_gdf
                )
            )

            m = neighbourhood_map(
                neighbourhood,
                nta_gdf
            )

            return {
                "query_type": "describe",
                "message": summary,
                "map": m
            }

    # ==================================================
    # NEARBY FOOD
    # ==================================================

    if intent == "nearby":

        lat = 40.706
        lon = -74.011

        radius = 1000

        restaurants, cafes = nearby_food(
            lat,
            lon,
            radius,
            pois_gdf
        )

        m = nearby_food_map(
            restaurants,
            cafes,
            lat,
            lon,
            radius
        )

        return {
            "query_type": "nearby",
            "message":
                f"Found "
                f"{len(restaurants)} restaurants "
                f"and "
                f"{len(cafes)} cafes within "
                f"{radius} metres.",
            "map": m
        }

    # ==================================================
    # RANK
    # ==================================================

    if intent == "rank":

        category = amenity or "restaurant"

        ranking = rank_neighbourhoods(
            category,
            pois_gdf
        )

        if len(ranking) > 0:

            top_area = ranking.index[0]

            count = ranking.iloc[0]

            m = ranking_map(
                top_area,
                nta_gdf
            )

            return {
                "query_type": "rank",
                "message":
                    f"{top_area} has the most "
                    f"{category}s "
                    f"({count}).",
                "map": m
            }

    # ==================================================
    # COMPARE
    # ==================================================

    if intent == "compare":

        return {
            "query_type": "compare",
            "message":
                "Neighbourhood comparison "
                "will be added in V3.1.",
            "map": None
        }

    # ==================================================
    # DEFAULT
    # ==================================================

    return {
        "query_type": "unknown",
        "message":
            "I don't yet know how to answer "
            "that question.",
        "map": None
    }