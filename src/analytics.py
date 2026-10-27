# src/analytics.py

import geopandas as gpd
from shapely.geometry import Point


def count_pois(
    category,
    neighbourhood,
    pois_gdf
):
    subset = pois_gdf[
        (
            pois_gdf["amenity"]
            .str.lower()
            == category.lower()
        )
        &
        (
            pois_gdf["ntaname"]
            .str.contains(
                neighbourhood,
                case=False,
                na=False
            )
        )
    ]

    n = len(subset)

    if n == 0:
        return None, 0

    nta_name = subset.iloc[0]["ntaname"]

    return nta_name, n


def rank_neighbourhoods(
    category,
    pois_gdf
):
    ranking = (
        pois_gdf[
            pois_gdf["amenity"]
            .str.lower()
            == category.lower()
        ]
        .groupby("ntaname")
        .size()
        .sort_values(
            ascending=False
        )
    )

    return ranking


def summarise_neighbourhood_simple(
    neighbourhood,
    pois_gdf
):

    subset = pois_gdf[
        pois_gdf["ntaname"]
        .str.contains(
            neighbourhood,
            case=False,
            na=False
        )
    ]

    if subset.empty:
        return "Neighbourhood not found."

    top = (
        subset["amenity"]
        .value_counts()
        .head(10)
    )

    summary = (
        f"{neighbourhood} contains "
        f"{len(subset)} mapped amenities.\n\n"
        f"Top amenity categories:\n"
    )

    for amenity, count in top.items():

        summary += (
            f"- {amenity}: {count}\n"
        )

    return summary


def nearby_food(
    lat,
    lon,
    radius_m,
    pois_gdf
):
    pois_proj = pois_gdf.to_crs(2263)

    point = gpd.GeoSeries(
        [Point(lon, lat)],
        crs="EPSG:4326"
    ).to_crs(2263)

    nearby = pois_proj[
        pois_proj.distance(
            point.iloc[0]
        ) <= radius_m
    ]

    restaurants = nearby[
        nearby["amenity"] == "restaurant"
    ]

    cafes = nearby[
        nearby["amenity"] == "cafe"
    ]

    return restaurants, cafes