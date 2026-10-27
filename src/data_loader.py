# src/data_loader.py

import geopandas as gpd


def load_data():

    manhattan = gpd.read_file(
        "data/manhattan_nta.geojson"
    )

    pois = gpd.read_file(
        "data/osm_pois_manhattan.geojson"
    )

    pois = pois.to_crs(
        manhattan.crs
    )

    pois_with_nta = gpd.sjoin(
        pois,
        manhattan[
            ["ntaname", "geometry"]
        ],
        how="left",
        predicate="within"
    )

    if "index_right" in pois_with_nta.columns:

        pois_with_nta = (
            pois_with_nta
            .drop(
                columns=["index_right"]
            )
        )

    return manhattan, pois_with_nta