GeoAI Manhattan Explorer
A Natural Language Spatial Query System for Manhattan neighbourhood analysis.

Overview
GeoAI Manhattan Explorer combines Geographic Information Systems (GIS), OpenStreetMap data, and Natural Language Queries to allow users to explore Manhattan neighbourhoods interactively.

Users can ask questions such as:

How many restaurants are there in Chelsea?
What kind of neighbourhood is SoHo?
Show cafes in SoHo
Which neighbourhood has the most restaurants?
The system analyses spatial datasets and displays results on interactive maps.

Features
Natural language spatial queries
Neighbourhood profiling
Amenity analysis
Interactive Folium maps
Restaurant and café exploration
Spatial ranking and comparison framework
Technologies
Python
Streamlit
GeoPandas
Folium
OpenStreetMap
Shapely
Project Structure
geoai-manhattan-explorer/
│
├── app.py
├── requirements.txt
├── src/
│   ├── agent.py
│   ├── analytics.py
│   ├── data_loader.py
│   └── mapping.py
│
├── data/
│   ├── manhattan_nta.geojson
│   └── osm_pois_manhattan.geojson
│
└── screenshots/



Installation
pip install -r requirements.txt

Run Locally
streamlit run app.py


Future Enhancements
LLM-assisted neighbourhood summaries
Neighbourhood comparison engine
Real-time OpenStreetMap updates
Advanced GeoAI reasoning workflows