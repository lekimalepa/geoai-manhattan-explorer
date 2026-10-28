🗽 GeoAI Manhattan Explorer
A Natural Language Spatial Query System for Manhattan neighbourhood analysis using GeoAI, Streamlit, OpenStreetMap and GeoPandas.

Overview
GeoAI Manhattan Explorer combines:

Geographic Information Systems (GIS)
OpenStreetMap data
Natural Language Queries
Interactive Web Mapping
to allow users to explore Manhattan neighbourhoods through simple English questions.

Examples include:

How many restaurants are there in Chelsea?
What kind of neighbourhood is SoHo?
Show cafes in SoHo.
Which neighbourhood has the most restaurants?
What food options are near the Financial District?
The system analyses spatial datasets and displays results on interactive maps.

Features
Natural language spatial queries
Neighbourhood profiling
Amenity analysis
Interactive Folium maps
Restaurant and café exploration
Spatial ranking framework
GeoAI-inspired neighbourhood intelligence
Technologies Used
Python
Streamlit
GeoPandas
Folium
OpenStreetMap
Shapely
OSMnx
NumPy
Pandas
Project Structure
geoai-manhattan-explorer/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── manhattan_nta.geojson
│   └── osm_pois_manhattan.geojson
│
├── src/
│   ├── agent.py
│   ├── analytics.py
│   ├── data_loader.py
│   └── mapping.py
│
├── notebooks/
│   └── GEOAI project.ipynb
│
├── docs/
│   └── DATA_PIPELINE.md
│
└── screenshots/
Data Sources
Manhattan Neighbourhood Boundaries
Source:

New York City Open Data
OpenStreetMap Amenities
Source:

OpenStreetMap (OSM)
Retrieved using OSMnx
The datasets are stored in:

data/
├── manhattan_nta.geojson
└── osm_pois_manhattan.geojson
Further details are available in:

docs/DATA_PIPELINE.md
Installation
Clone the repository:

git clone https://github.com/lekimalepa/geoai-manhattan-explorer.git
Move into the project directory:

cd geoai-manhattan-explorer
Install dependencies:

pip install -r requirements.txt
Running Locally
Start the Streamlit application:

streamlit run app.py
Open the provided local URL in your browser.

Example Queries
Neighbourhood Analysis
What kind of neighbourhood is SoHo?
Amenity Counts
How many restaurants are there in Chelsea?
Interactive Mapping
Show cafes in SoHo
Rankings
Which neighbourhood has the most restaurants?
Development Workflow
The project was developed using:

GeoPandas spatial analysis
OpenStreetMap amenity extraction
Neighbourhood Tabulation Areas (NTAs)
Interactive Folium mapping
Streamlit deployment
The complete exploratory workflow is documented in:

notebooks/GEOAI project.ipynb
Future Enhancements
LLM-assisted neighbourhood summaries
Neighbourhood comparison engine
Real-time OpenStreetMap updates
Additional Manhattan insights
Advanced GeoAI reasoning workflows
Multi-city support
Author
Lekima Maka

GeoAI, Spatial Analytics, Data Science and Geographic Information Systems.

License
This project is provided for educational and research purposes.