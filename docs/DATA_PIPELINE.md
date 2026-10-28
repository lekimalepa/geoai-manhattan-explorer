Data Pipeline
This document explains how the GeoAI Manhattan Explorer datasets were created.

Overview
The application uses two datasets:

Manhattan neighbourhood boundaries
Manhattan OpenStreetMap Points of Interest (POIs)
The files are stored in:
Data Sources
1. Manhattan Neighbourhood Tabulation Areas (NTAs)

Source:

https://data.cityofnewyork.us

Dataset:

NYC Neighbourhood Tabulation Areas (NTAs)

The dataset was filtered to retain only:

Manhattan neighbourhoods
Standard NTA polygons

2. OpenStreetMap Amenities

Source:

https://www.openstreetmap.org

Downloaded using:

Python
osmnx.features_from_place()

Location:

Python
"Manhattan, New York City, New York, USA"

Tags:

Python
{"amenity": True}

Only point geometries were retained.

Processing Workflow
Download POIs
raw_pois = ox.features_from_place(
    "Manhattan, New York City, New York, USA",
    tags={"amenity": True}
)


Keep only points
pois = raw_pois[
    raw_pois.geometry.geom_type == "Point"
]


Save as GeoJSON
pois.to_file(
    "data/osm_pois_manhattan.geojson",
    driver="GeoJSON"
)


Download Manhattan Neighbourhoods

response = requests.get(
    "https://data.cityofnewyork.us/resource/9nt8-h7nd.geojson"
)

Filter:
boroname == "Manhattan"

and
ntatype == "0"

Save:
manhattan.to_file(
    "data/manhattan_nta.geojson",
    driver="GeoJSON"
)


Dataset Statistics

Current repository version:

4,326 OpenStreetMap POIs
327 KB NTA boundary dataset



Reproducibility

The datasets can be recreated using:

Python
GeoPandas
OSMnx
Requests

See:
notebooks/GEOAI project.ipynb


Purpose

These datasets support:

Natural-language neighbourhood queries
Restaurant and café searches
Spatial ranking
Neighbourhood profiling
Interactive Folium maps

within the GeoAI Manhattan Explorer application.

--- # Step 4: Commit it to GitHub After saving the file: ```bash git add docs/DATA_PIPELINE.md git commit -m "Added data pipeline documentation" git push