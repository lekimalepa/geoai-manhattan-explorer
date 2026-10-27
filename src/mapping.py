# src/mapping.py

import folium
from folium.plugins import MarkerCluster


# ==================================================
# GENERIC AMENITY MAP
# ==================================================

def amenity_map(
    category,
    neighbourhood,
    pois_gdf
):
    """
    Display amenities in a neighbourhood.
    """

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

    if subset.empty:
        return None

    if subset.crs.to_epsg() != 4326:
        subset = subset.to_crs(4326)

    center_lat = subset.geometry.y.mean()
    center_lon = subset.geometry.x.mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=14
    )

    cluster = MarkerCluster().add_to(m)

    for _, row in subset.iterrows():

        folium.Marker(
            [
                row.geometry.y,
                row.geometry.x
            ],
            popup=f"{category.title()}",
            icon=folium.Icon(
                color="blue"
            )
        ).add_to(cluster)

    return m


# ==================================================
# RESTAURANT MAP
# ==================================================

def restaurant_map(
    neighbourhood,
    pois_gdf
):
    """
    Wrapper around amenity_map()
    for restaurants.
    """

    return amenity_map(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_gdf
    )


# ==================================================
# NEIGHBOURHOOD MAP
# ==================================================

def neighbourhood_map(
    neighbourhood,
    nta_gdf
):
    """
    Display NTA neighbourhood boundary.
    """

    subset = nta_gdf[
        nta_gdf["ntaname"]
        .str.contains(
            neighbourhood,
            case=False,
            na=False
        )
    ]

    if subset.empty:
        return None

    if subset.crs.to_epsg() != 4326:
        subset = subset.to_crs(4326)

    centroid = subset.geometry.iloc[0].centroid

    m = folium.Map(
        location=[
            centroid.y,
            centroid.x
        ],
        zoom_start=14
    )

    folium.GeoJson(
        subset,
        style_function=lambda x: {
            "fillColor": "orange",
            "color": "red",
            "weight": 3,
            "fillOpacity": 0.3
        }
    ).add_to(m)

    return m


# ==================================================
# NEARBY FOOD MAP
# ==================================================

def nearby_food_map(
    restaurants,
    cafes,
    lat,
    lon,
    radius_m=1000
):
    """
    Nearby food search map.
    """

    m = folium.Map(
        location=[lat, lon],
        zoom_start=15
    )

    # Search location

    folium.Marker(
        [lat, lon],
        popup="Search Location",
        icon=folium.Icon(
            color="green"
        )
    ).add_to(m)

    # Search radius

    folium.Circle(
        location=[lat, lon],
        radius=radius_m,
        color="green",
        weight=3,
        fill=False
    ).add_to(m)

    # CRS conversion

    if (
        restaurants.crs is not None
        and restaurants.crs.to_epsg() != 4326
    ):
        restaurants = restaurants.to_crs(
            4326
        )

    if (
        cafes.crs is not None
        and cafes.crs.to_epsg() != 4326
    ):
        cafes = cafes.to_crs(
            4326
        )

    cluster = MarkerCluster().add_to(m)

    # Restaurants

    for _, row in restaurants.iterrows():

        folium.Marker(
            [
                row.geometry.y,
                row.geometry.x
            ],
            popup="Restaurant",
            icon=folium.Icon(
                color="red"
            )
        ).add_to(cluster)

    # Cafes

    for _, row in cafes.iterrows():

        folium.Marker(
            [
                row.geometry.y,
                row.geometry.x
            ],
            popup="Cafe",
            icon=folium.Icon(
                color="blue"
            )
        ).add_to(cluster)

    return m


# ==================================================
# RANKING MAP
# ==================================================

def ranking_map(
    neighbourhood,
    nta_gdf
):
    """
    Highlight top-ranked neighbourhood.
    """

    return neighbourhood_map(
        neighbourhood,
        nta_gdf
    )