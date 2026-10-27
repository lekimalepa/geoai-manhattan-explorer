from src.agent import run_agent
from src.data_loader import load_data

manhattan, pois_with_nta = load_data()

result = run_agent(
    "What food options are near the Financial District?",
    pois_with_nta
)

print(result)
from src.data_loader import load_data
from src.agent import run_agent

manhattan, pois_with_nta = load_data()

result = run_agent(
    "What food options are near the Financial District?",
    pois_with_nta
)

print(result)
import inspect
from src.agent import run_agent

print(inspect.getsource(run_agent))
import nbformat

nb = nbformat.read(
    "notebooks/GEOAI_Project.ipynb",
    as_version=4
)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == "code":
        print(f"\n===== CELL {i} =====\n")
        print(cell.source)
import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            print(os.path.join(root, file))
import nbformat

with open(
    "GEOAI project.ipynb",
    "r",
    encoding="utf-8"
) as f:

    nb = nbformat.read(
        f,
        as_version=4
    )

print(
    f"Notebook contains {len(nb.cells)} cells"
)
`
import nbformat

with open(
    "GEOAI project.ipynb",
    "r",
    encoding="utf-8"
) as f:

    nb = nbformat.read(
        f,
        as_version=4
    )

print(
    f"Notebook contains {len(nb.cells)} cells"
)
import json

with open(
    "GEOAI project.ipynb",
    "r",
    encoding="utf-8"
) as f:

    notebook = json.load(f)

keywords = [
    "def run_agent",
    "def nearby_food",
    "def nearby_food_map",
    "def count_pois",
    "def summarise_neighbourhood_simple"
]

for cell in notebook["cells"\]:

    if cell["cell_type"] == "code":

        source = "".join(cell["source"])

        for keyword in keywords:

            if keyword in source:

                print("\n" + "=" * 80)
                print(keyword)
                print("=" * 80)
                print(source)
                break
import json

with open(
    "GEOAI project.ipynb",
    "r",
    encoding="utf-8"
) as f:

    notebook = json.load(f)

keywords = [
    "def run_agent",
    "def nearby_food",
    "def nearby_food_map",
    "def count_pois",
    "def summarise_neighbourhood_simple"
]

for cell in notebook["cells"\]:

    if cell["cell_type"] == "code":

        source = "".join(cell["source"])

        for keyword in keywords:

            if keyword in source:

                print("\n" + "=" * 80)
                print(keyword)
                print("=" * 80)
                print(source)

                break
import json

with open(
    "GEOAI project.ipynb",
    "r",
    encoding="utf-8"
) as f:

    notebook = json.load(f)

keywords = [
    "def run_agent",
    "def nearby_food",
    "def nearby_food_map",
    "def count_pois",
    "def summarise_neighbourhood_simple"
]

for cell in notebook["cells"\]:

    if cell["cell_type"] == "code":

        source = "".join(cell["source"])

        for keyword in keywords:

            if keyword in source:

                print("\n" + "=" * 80)
                print(keyword)
                print("=" * 80)
                print(source)

                break
import json

with open(
    "GEOAI project.ipynb",
    "r",
    encoding="utf-8"
) as f:

    notebook = json.load(f)

for cell in notebook["cells"\]:

    if cell["cell_type"] == "code":

        source = "".join(cell["source"])

        if "def run_agent" in source:
            print(source)
import json

with open(
    "GEOAI project.ipynb",
    "r",
    encoding="utf-8"
) as f:

    notebook = json.load(f)

for cell in notebook["cells"]:

    if cell["cell_type"] == "code":

        source = "".join(cell["source"])

        if "def run_agent" in source:
            print(source)
from src.data_loader import load_data
from src.agent import run_agent

manhattan, pois_with_nta = load_data()

result = run_agent(
    "What food options are near the Financial District?",
    pois_with_nta
)

print(result)
from src.data_loader import load_data
from src.agent import run_agent

manhattan, pois_with_nta = load_data()

result = run_agent(
    "What food options are near the Financial District?",
    pois_with_nta
)

print(result)
print(type(result))
`
from src.data_loader import load_data
from src.agent import run_agent

manhattan, pois_with_nta = load_data()

result = run_agent(
    "What food options are near the Financial District?",
    pois_with_nta
)

print(result)
print(type(result))
import src.agent

print(src.agent.__file__)
import inspect
from src.agent import run_agent

print(inspect.getsource(run_agent))
from importlib import reload

import src.agent

reload(src.agent)

from src.agent import run_agent
result = run_agent(
    "What food options are near the Financial District?",
    pois_with_nta
)

print(result)
print(type(result))
import src.agent

print(src.agent.__file__)

import inspect
from src.agent import run_agent

print(inspect.getsource(run_agent))
q2 = "How many restaurants are there in the Upper West Side?"

print(f"Query: {q2}\n")

answer2 = run_agent(q2, pois_gdf)

print(answer2)
%whos
import geopandas as gpd

for name, obj in globals().items():
    if isinstance(obj, gpd.GeoDataFrame):
        print(name)
print(pois.head())

print("\nColumns:")
print(pois.columns.tolist())
print(pois.columns)
import inspect
print(inspect.getsource(annotate_ntas))
import inspect

print(inspect.getsource(count_pois))
print(manhattan.columns.tolist())
import geopandas as gpd

pois_with_nta = gpd.sjoin(
    pois,
    manhattan[['ntaname', 'geometry']],
    how='left',
    predicate='within'
)

print(pois_with_nta.columns)
print(pois_with_nta.head())
def count_pois(category, neighbourhood, pois_gdf):

    result = pois_gdf[
        (pois_gdf["amenity"].str.lower() == category.lower())
        &
        (
            pois_gdf["ntaname"]
            .str.lower()
            .str.contains(neighbourhood.lower(), na=False)
        )
    ]

    count = len(result)

    if count > 0:
        nta_name = result["ntaname"].iloc[0]
    else:
        nta_name = neighbourhood

    return nta_name, count
q2 = "How many restaurants are there in the Upper West Side?"

print(f"Query: {q2}\n")

nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Upper West Side",
    pois_gdf=pois_with_nta
)

print(
    "[1] count_pois(category='restaurant', "
    "neighbourhood='Upper West Side')"
)

print(
    f"→ {nta_name}: {n} POIs in category 'restaurant'"
)

print(
    f"Answer: There are {n} restaurants in the Upper West Side."
)
q_test = "How many restaurants are there in SoHo?"

print(f"Query: {q_test}\n")

nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="SoHo",
    pois_gdf=pois_with_nta
)

print(
    "[1] count_pois(category='restaurant', "
    "neighbourhood='SoHo')"
)

print(
    f"→ {nta_name}: {n} POIs in category 'restaurant'"
)

print(
    f"Answer: There are {n} restaurants in SoHo."
)
q_test = "How many restaurants are there in the Financial District?"

print(f"Query: {q_test}\n")

nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Financial District",
    pois_gdf=pois_with_nta
)

print(
    "[1] count_pois(category='restaurant', "
    "neighbourhood='Financial District')"
)

print(
    f"→ {nta_name}: {n} POIs in category 'restaurant'"
)

print(
    f"Answer: There are {n} restaurants in the Financial District."
)
q_test = "How many restaurants are there in SoHo?"
run_agent(q_test)
def run_agent(query):

    q = query.lower()

    if "how many restaurants" in q:

        neighbourhoods = [
            "Upper West Side",
            "SoHo",
            "Financial District"
        ]

        for nb in neighbourhoods:
            if nb.lower() in q:

                nta_name, n = count_pois(
                    category="restaurant",
                    neighbourhood=nb,
                    pois_gdf=pois_with_nta
                )

                return (
                    f"There are {n} restaurants in {nb}."
                )

    return "I don't yet know how to answer that question."
import geopandas as gpd

pois_with_nta = gpd.sjoin(
    pois,
    manhattan[['ntaname', 'geometry']],
    how='left',
    predicate='within'
)

print(pois_with_nta.columns)
print(pois_with_nta.head())
def count_pois(category, neighbourhood, pois_gdf):

    result = pois_gdf[
        (pois_gdf["amenity"].str.lower() == category.lower())
        &
        (
            pois_gdf["ntaname"]
            .str.lower()
            .str.contains(neighbourhood.lower(), na=False)
        )
    ]

    count = len(result)

    if count > 0:
        nta_name = result["ntaname"].iloc[0]
    else:
        nta_name = neighbourhood

    return nta_name, count
q2 = "How many restaurants are there in the Upper West Side?"

print(f"Query: {q2}\n")

nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Upper West Side",
    pois_gdf=pois_with_nta
)

print(
    "[1] count_pois(category='restaurant', "
    "neighbourhood='Upper West Side')"
)

print(
    f"→ {nta_name}: {n} POIs in category 'restaurant'"
)

print(
    f"Answer: There are {n} restaurants in the Upper West Side."
)
q_test = "How many restaurants are there in the Financial District?"

print(f"Query: {q_test}\n")

nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Financial District",
    pois_gdf=pois_with_nta
)

print(
    "[1] count_pois(category='restaurant', "
    "neighbourhood='Financial District')"
)

print(
    f"→ {nta_name}: {n} POIs in category 'restaurant'"
)

print(
    f"Answer: There are {n} restaurants in the Financial District."
)
q_test = "How many restaurants are there in SoHo?"
run_agent(q_test)
def run_agent(query):

    q = query.lower()

    if "how many restaurants" in q:

        neighbourhoods = [
            "Upper West Side",
            "SoHo",
            "Financial District"
        ]

        for nb in neighbourhoods:
            if nb.lower() in q:

                nta_name, n = count_pois(
                    category="restaurant",
                    neighbourhood=nb,
                    pois_gdf=pois_with_nta
                )

                return (
                    f"There are {n} restaurants in {nb}."
                )

    return "I don't yet know how to answer that question."
nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="SoHo",
    pois_gdf=pois_with_nta
)

print(nta_name)
print(n)
nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="SoHo",
    pois_gdf=pois_with_nta
)

print(nta_name)
print(n)
import re

def run_agent(query):

    q = query.lower()

    if "how many restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:
            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category="restaurant",
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            return (
                f"There are {n} restaurants in {nta_name}."
            )

    return "I don't yet know how to answer that question."
run_agent("How many restaurants are there in SoHo?")
run_agent("How many restaurants are there in Chelsea?")
run_agent("How many restaurants are there in Harlem?")
run_agent("How many restaurants are there in Upper West Side?")
for nb in ["SoHo", "Chelsea", "Harlem", "Upper West Side"\]:
    try:
        nta_name, n = count_pois(
            category="restaurant",
            neighbourhood=nb,
            pois_gdf=pois_with_nta
        )
        print(f"{nb} -> {nta_name}: {n}")
    except Exception as e:
        print(f"{nb}: {e}")
import re

def run_agent(query):

    q = query.lower()

    if "how many restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:
            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category="restaurant",
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            return f"There are {n} restaurants in {nta_name}."

    return "I don't yet know how to answer that question."
run_agent("How many restaurants are there in SoHo?")
run_agent("How many restaurants are there in Chelsea?")
run_agent("How many restaurants are there in Harlem?")
run_agent("How many restaurants are there in Upper West Side?")
for nb in ["SoHo", "Chelsea", "Harlem", "Upper West Side"]:
    try:
        nta_name, n = count_pois(
            category="restaurant",
            neighbourhood=nb,
            pois_gdf=pois_with_nta
        )
        print(f"{nb} -> {nta_name}: {n}")
    except Exception as e:
        print(f"{nb} -> ERROR: {e}")
import inspect

print(inspect.getsource(run_agent))
import re

def run_agent(query):

    print("Received:", query)

    q = query.lower()

    if "how many restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:
            neighbourhood = m.group(1).strip()

            print("Extracted neighbourhood:", neighbourhood)

            nta_name, n = count_pois(
                category="restaurant",
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            print("Matched NTA:", nta_name)

            return f"There are {n} restaurants in {nta_name}."

    return "I don't yet know how to answer that question."
run_agent("How many restaurants are there in SoHo?")
run_agent("How many restaurants are there in SoHo?")
run_agent("How many restaurants are there in Chelsea?")
run_agent("How many restaurants are there in Harlem?")
print(run_agent("How many restaurants are there in SoHo?"))
print(run_agent("How many restaurants are there in Chelsea?"))
print(run_agent("How many restaurants are there in Harlem?"))
queries = [
    "How many restaurants are there in SoHo?",
    "How many restaurants are there in Chelsea?",
    "How many restaurants are there in Harlem?",
    "How many restaurants are there in Upper West Side?"
]

for q in queries:
    print(run_agent(q))
import matplotlib.pyplot as plt

def show_neighbourhood_map(neighbourhood):

    nta = manhattan[
        manhattan["ntaname"].str.contains(
            neighbourhood,
            case=False,
            na=False
        )
    ]

    if nta.empty:
        print(f"Neighbourhood '{neighbourhood}' not found.")
        return

    fig, ax = plt.subplots(figsize=(10, 10))

    manhattan.boundary.plot(
        ax=ax,
        color="lightgrey",
        linewidth=0.5
    )

    nta.plot(
        ax=ax,
        color="red",
        alpha=0.7
    )

    ax.set_title(f"Neighbourhood: {neighbourhood}")

    plt.show()
print(f"There are {n} restaurants in {nta_name}.")
show_neighbourhood_map("SoHo")
show_neighbourhood_map("Chelsea")
show_neighbourhood_map("Upper West Side")
def run_agent(query):

    print("Received:", query)

    q = query.lower()

    if "how many restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category="restaurant",
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            print(
                f"Answer: There are {n} restaurants in {nta_name}."
            )

            show_neighbourhood_map(neighbourhood)

            return (
                f"There are {n} restaurants in {nta_name}."
            )

    return "I don't yet know how to answer that question."
run_agent("How many restaurants are there in SoHo?")
def show_restaurants_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    restaurants = pois_with_nta[
        (pois_with_nta["element"] == "restaurant")
        &
        (pois_with_nta["ntaname"] == nta_name)
    ]

    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    fig, ax = plt.subplots(figsize=(10, 10))

    manhattan.boundary.plot(
        ax=ax,
        color="lightgrey"
    )

    nta.plot(
        ax=ax,
        color="lightblue",
        alpha=0.5
    )

    restaurants.plot(
        ax=ax,
        color="red",
        markersize=8
    )

    ax.set_title(
        f"{n} Restaurants in {nta_name}"
    )

    plt.show()
show_restaurants_map("Chelsea")
print(pois_with_nta.columns)
nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Chelsea",
    pois_gdf=pois_with_nta
)

print("NTA Name:", nta_name)

restaurants = pois_with_nta[
    (pois_with_nta["amenity"] == "restaurant") &
    (pois_with_nta["ntaname"] == nta_name)
]

print("Restaurant records found:", len(restaurants))
print(
    pois_with_nta["ntaname"]
    .dropna()
    .unique()[:20]
)
pois_with_nta[
    pois_with_nta["ntaname"].str.contains(
        "Chelsea",
        case=False,
        na=False
    )
].head()
def show_restaurants_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    print(f"NTA: {nta_name}")
    print(f"Restaurants: {n}")

    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ]

    print("Rows returned:", len(restaurants))

    if restaurants.empty:
        print("No restaurant points found.")
        return

    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    fig, ax = plt.subplots(figsize=(10, 10))

    manhattan.boundary.plot(
        ax=ax,
        color="lightgrey"
    )

    nta.plot(
        ax=ax,
        color="lightblue",
        alpha=0.5
    )

    restaurants.plot(
        ax=ax,
        color="red",
        markersize=12
    )

    ax.set_title(
        f"{n} Restaurants in {nta_name}"
    )

    plt.show()
show_restaurants_map("Chelsea")
print("NTA:", nta_name)
print("Rows:", len(restaurants))
print(restaurants.crs)
print(restaurants.geometry.head())
print(restaurants.geometry.isna().sum())
restaurants.plot(figsize=(8,8))
plt.show()
def show_restaurants_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ].copy()

    # Remove missing geometries
    restaurants = restaurants[
        restaurants.geometry.notnull()
    ]

    print(f"NTA: {nta_name}")
    print(f"Restaurant points: {len(restaurants)}")

    if len(restaurants) == 0:
        print("No restaurant points found.")
        return

    fig, ax = plt.subplots(figsize=(10,10))

    manhattan.boundary.plot(
        ax=ax,
        color="lightgrey",
        linewidth=0.5
    )

    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    if not nta.empty:
        nta.plot(
            ax=ax,
            color="lightblue",
            alpha=0.5
        )

    # Plot x/y explicitly
    ax.scatter(
        restaurants.geometry.x,
        restaurants.geometry.y,
        c="red",
        s=10,
        label="Restaurants"
    )

    plt.title(f"{n} Restaurants in {nta_name}")
    plt.legend()
    plt.show()
show_restaurants_map("Chelsea")
m = restaurant_map("Chelsea")
m
restaurants.plot(figsize=(8,8))
restaurants.plot(figsize=(8,8))
plt.show()
def show_restaurants_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ].copy()

    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    fig, ax = plt.subplots(figsize=(10,10))

    # Plot all neighbourhood boundaries
    manhattan.boundary.plot(
        ax=ax,
        color="lightgrey",
        linewidth=0.5
    )

    # Highlight selected neighbourhood
    if len(nta) > 0:
        nta.plot(
            ax=ax,
            color="lightblue",
            alpha=0.5
        )

    # Plot restaurant points using scatter
    ax.scatter(
        restaurants.geometry.x,
        restaurants.geometry.y,
        color="red",
        s=10,
        label="Restaurants"
    )

    ax.set_title(
        f"{n} Restaurants in {nta_name}"
    )

    ax.legend()

    plt.show()
show_restaurants_map("Chelsea")
print(f"There are {n} restaurants in {nta_name}.")
show_restaurants_map(neighbourhood)
run_agent("How many restaurants are there in Chelsea?")
m = restaurant_map("Chelsea")
m
import folium

def restaurant_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ].copy()

    if restaurants.empty:
        print("No restaurants found.")
        return None

    centre = restaurants.geometry.unary_union.centroid

    m = folium.Map(
        location=[centre.y, centre.x],
        zoom_start=14
    )

    for _, row in restaurants.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=3,
            color="red",
            fill=True,
            fill_opacity=0.8,
            popup=row["amenity"]
        ).add_to(m)

    return m
m = restaurant_map("Chelsea")
m
restaurants = pois_with_nta[
    (pois_with_nta["amenity"] == "restaurant") &
    (pois_with_nta["ntaname"] == "Chelsea-Hudson Yards")
]

print(len(restaurants))
folium.GeoJson(
    nta.__geo_interface__,
    style_function=lambda x: {
        "fillColor": "lightblue",
        "color": "blue",
        "weight": 2,
        "fillOpacity": 0.3
    }
).add_to(m)
import folium

def restaurant_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ].copy()

    if restaurants.empty:
        print("No restaurants found.")
        return None

    centre = restaurants.geometry.unary_union.centroid

    m = folium.Map(
        location=[centre.y, centre.x],
        zoom_start=14
    )

    for _, row in restaurants.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=3,
            color="red",
            fill=True,
            fill_opacity=0.8,
            popup=row["amenity"]
        ).add_to(m)

    return m
m = restaurant_map("Chelsea")
m
restaurants = pois_with_nta[
    (pois_with_nta["amenity"] == "restaurant") &
    (pois_with_nta["ntaname"] == "Chelsea-Hudson Yards")
]

print(len(restaurants))
folium.GeoJson(
    nta.__geo_interface__,
    style_function=lambda x: {
        "fillColor": "lightblue",
        "color": "blue",
        "weight": 2,
        "fillOpacity": 0.3
    }
).add_to(m)
import folium

def restaurant_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    # NTA polygon
    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    # Restaurant points
    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ]

    if restaurants.empty:
        print("No restaurants found.")
        return None

    # Centre map
    centre = restaurants.geometry.unary_union.centroid

    m = folium.Map(
        location=[centre.y, centre.x],
        zoom_start=14
    )

    # Add neighbourhood boundary
    if not nta.empty:
        folium.GeoJson(
            nta.__geo_interface__,
            style_function=lambda x: {
                "fillColor": "lightblue",
                "color": "blue",
                "weight": 2,
                "fillOpacity": 0.3
            }
        ).add_to(m)

    # Add restaurant points
    for _, row in restaurants.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=3,
            color="red",
            fill=True,
            fill_opacity=0.8
        ).add_to(m)

    return m
m = restaurant_map("Chelsea")
m
restaurant_map("SoHo")
import re
from IPython.display import display

def run_agent(query):

    q = query.lower()

    if "how many restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category="restaurant",
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            print(f"Answer: There are {n} restaurants in {nta_name}.")

            # Display interactive map
            mapp = restaurant_map(neighbourhood)

            if mapp is not None:
                display(mapp)

            return f"There are {n} restaurants in {nta_name}."

    return "I don't yet know how to answer that question."
run_agent("How many restaurants are there in Chelsea?")
import folium

def restaurant_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ].copy()

    if restaurants.empty:
        print("No restaurants found.")
        return None

    centre = restaurants.geometry.unary_union.centroid

    m = folium.Map(
        location=[centre.y, centre.x],
        zoom_start=14
    )

    # Neighbourhood boundary
    if not nta.empty:
        folium.GeoJson(
            nta.__geo_interface__,
            style_function=lambda x: {
                "fillColor": "lightblue",
                "color": "blue",
                "weight": 2,
                "fillOpacity": 0.3
            }
        ).add_to(m)

    # Restaurant points
    for _, row in restaurants.iterrows():

        # Use name column if available
        name = row.get("name", "Restaurant")

        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=4,
            color="red",
            fill=True,
            fill_opacity=0.8,
            popup=name
        ).add_to(m)

    return m
print(pois_with_nta.columns)
pois_with_nta.head()
popup=f"Restaurant ID: {row['id']}"
import re
from IPython.display import display

def run_agent(query):

    q = query.lower()

    # COUNT RESTAURANTS
    if "how many restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category="restaurant",
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            print(f"There are {n} restaurants in {nta_name}.")

            display(restaurant_map(neighbourhood))

            return f"There are {n} restaurants in {nta_name}."

    # SHOW RESTAURANTS
    if "show restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            display(restaurant_map(neighbourhood))

            return f"Showing restaurants in {neighbourhood}."

    return "I don't yet know how to answer that question."
import folium

def restaurant_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    restaurants = pois_with_nta[
        (pois_with_nta["amenity"] == "restaurant") &
        (pois_with_nta["ntaname"] == nta_name)
    ]

    if restaurants.empty:
        return None

    centre = restaurants.geometry.unary_union.centroid

    m = folium.Map(
        location=[centre.y, centre.x],
        zoom_start=14
    )

    # Neighborhood polygon
    if not nta.empty:
        folium.GeoJson(
            nta.__geo_interface__,
            style_function=lambda x: {
                "fillColor": "lightblue",
                "color": "blue",
                "weight": 2,
                "fillOpacity": 0.3
            }
        ).add_to(m)

    # Restaurant locations
    for _, row in restaurants.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=4,
            color="red",
            fill=True,
            popup=f"Restaurant ID: {row['id']}"
        ).add_to(m)

    return m
run_agent("Show restaurants in Chelsea")
run_agent("Show restaurants in Chelsea")
run_agent("Show restaurants in SoHo")
print(pois.head())
print(pois.columns)
for _, row in restaurants.iterrows():

    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=4,
        color="red",
        fill=True,
        fill_opacity=0.8,
        popup=f"OSM ID: {row['id']}"
    ).add_to(m)
import re
from IPython.display import display

def run_agent(query):

    q = query.lower()

    # Count restaurants
    if "how many restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category="restaurant",
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            display(restaurant_map(neighbourhood))

            return (
                f"There are {n} restaurants in {nta_name}."
            )

    # Show restaurants
    elif "show restaurants" in q:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            display(
                restaurant_map(neighbourhood)
            )

            return (
                f"Showing restaurants in "
                f"{neighbourhood}."
            )

    return "I don't yet know how to answer that question."
run_agent("Show restaurants in Chelsea")
run_agent("Show restaurants in SoHo")
run_agent("How many restaurants are there in Harlem?")
run_agent("How many restaurants are there in Harlem?")
VALID_CATEGORIES = set(
    pois_with_nta["amenity"]
    .dropna()
    .unique()
)
sorted(list(VALID_CATEGORIES))[:50]
import folium

def amenity_map(category, neighbourhood):

    nta_name, n = count_pois(
        category=category,
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    nta = manhattan[
        manhattan["ntaname"] == nta_name
    ]

    places = pois_with_nta[
        (pois_with_nta["amenity"] == category) &
        (pois_with_nta["ntaname"] == nta_name)
    ]

    if places.empty:
        print("No locations found.")
        return None

    centre = places.geometry.unary_union.centroid

    m = folium.Map(
        location=[centre.y, centre.x],
        zoom_start=14
    )

    if not nta.empty:

        folium.GeoJson(
            nta.__geo_interface__,
            style_function=lambda x: {
                "fillColor": "lightblue",
                "color": "blue",
                "weight": 2,
                "fillOpacity": 0.3
            }
        ).add_to(m)

    for _, row in places.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=4,
            color="red",
            fill=True,
            popup=f"{category} (ID {row['id']})"
        ).add_to(m)

    return m
def find_category(query):

    q = query.lower()

    for cat in VALID_CATEGORIES:

        if str(cat).lower() in q:
            return cat

    return None
import re
from IPython.display import display

def run_agent(query):

    q = query.lower()

    category = find_category(query)

    #
    # COUNT QUERY
    #
    if "how many" in q and category:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category=category,
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            display(
                amenity_map(
                    category,
                    neighbourhood
                )
            )

            return (
                f"There are {n} "
                f"{category}s in "
                f"{nta_name}."
            )

    #
    # SHOW QUERY
    #
    if "show" in q and category:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            display(
                amenity_map(
                    category,
                    neighbourhood
                )
            )

            return (
                f"Showing {category}s "
                f"in {neighbourhood}."
            )

    #
    # RANKING QUERY
    #
    if "most" in q and category:

        return rank_neighbourhoods(category)

    #
    # SOHO DESCRIPTION
    #
    if "what kind of neighbourhood" in q:

        m = re.search(r"is (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            return summarise_neighbourhood_simple(
                neighbourhood
            )

    #
    # FINANCIAL DISTRICT NEARBY
    #
    if "nearby" in q or "within 1 km" in q:

        return nearby_food(
            40.706,
            -74.011,
            1000
        )

    return (
        "I don't yet know how to "
        "answer that question."
    )
run_agent(
    "How many restaurants are there in Chelsea?"
)
run_agent(
    "How many cafes are there in Harlem?"
)
run_agent(
    "How many bars are there in SoHo?"
)
run_agent(
    "Show restaurants in Chelsea"
)
run_agent(
    "Which neighbourhood has the most restaurants?"
)
run_agent(
    "Which neighbourhood has the most cafes?"
)
run_agent(
    "What kind of neighbourhood is SoHo?"
)
summarise_neighbourhood_simple("SoHo")
import re
from IPython.display import display

def run_agent(query):

    q = query.lower()

    category = find_category(query)

    # COUNT QUERY
    if "how many" in q and category:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            nta_name, n = count_pois(
                category=category,
                neighbourhood=neighbourhood,
                pois_gdf=pois_with_nta
            )

            display(
                amenity_map(
                    category,
                    neighbourhood
                )
            )

            return (
                f"There are {n} {category}s in "
                f"{nta_name}."
            )

    # SHOW QUERY
    elif "show" in q and category:

        m = re.search(r"in (.+?)\??$", query)

        if m:

            neighbourhood = m.group(1).strip()

            display(
                amenity_map(
                    category,
                    neighbourhood
                )
            )

            return (
                f"Showing {category}s in "
                f"{neighbourhood}."
            )

    # RANK QUERY
    elif "most" in q and category:

        return rank_neighbourhoods(category)

    # DESCRIBE NEIGHBOURHOOD
    elif (
        "what kind of neighbourhood" in q
        or "describe" in q
        or "tell me about" in q
    ):

        m = re.search(
            r"(?:is|about)\s+(.+?)\??$",
            query,
            re.IGNORECASE
        )

        if m:

            neighbourhood = m.group(1).strip()

            return summarise_neighbourhood_simple(
                neighbourhood
            )

    # NEARBY FOOD
    elif (
        "nearby" in q
        or "within 1 km" in q
        or "food options" in q
    ):

        return nearby_food(
            40.706,
            -74.011,
            1000
        )

    return "I don't yet know how to answer that question."
run_agent("What kind of neighbourhood is SoHo?")
run_agent("Describe Chelsea")
run_agent("How many cafes are there in Chelsea?")
summarise_neighbourhood_simple("SoHo")
import inspect
print(inspect.getsource(summarise_neighbourhood_simple))
summarise_neighbourhood_simple("SoHo")
import inspect
print(inspect.getsource(summarise_neighbourhood_simple))
def summarise_neighbourhood_simple(neighbourhood):

    subset = pois_with_nta[
        pois_with_nta["ntaname"]
        .str.contains(
            neighbourhood,
            case=False,
            na=False
        )
    ]

    if len(subset) == 0:
        return "Neighbourhood not found."

    top = subset["amenity"].value_counts().head(10)

    summary = (
        f"{neighbourhood} contains "
        f"{len(subset)} mapped amenities. "
        f"The most common amenities are:\n\n"
    )

    for amenity, count in top.items():
        summary += f"• {amenity}: {count}\n"

    return summary
print(
    summarise_neighbourhood_simple("SoHo")
)
def summarise_neighbourhood_simple(neighbourhood):

    subset = pois_with_nta[
        pois_with_nta["ntaname"]
        .str.contains(
            neighbourhood,
            case=False,
            na=False
        )
    ]

    if subset.empty:
        return "Neighbourhood not found."

    total = len(subset)

    restaurants = (
        subset["amenity"] == "restaurant"
    ).sum()

    cafes = (
        subset["amenity"] == "cafe"
    ).sum()

    bars = (
        subset["amenity"] == "bar"
    ).sum()

    top = subset["amenity"].value_counts().head(5)

    text = (
        f"{neighbourhood} contains "
        f"{total} mapped amenities.\n\n"
        f"Restaurants: {restaurants}\n"
        f"Cafes: {cafes}\n"
        f"Bars: {bars}\n\n"
        f"Top amenity categories:\n"
    )

    for amenity, count in top.items():
        text += f"- {amenity}: {count}\n"

    return text
count_pois(
    category="restaurant",
    neighbourhood="Chelsea",
    pois_gdf=pois_with_nta
)
amenity_map(
    category="restaurant",
    neighbourhood="Chelsea"
)
amenity_map(
    category="restaurant",
    neighbourhood="Chelsea"
)
rank_neighbourhoods("restaurant")
summarise_neighbourhood_simple("SoHo")
nearby_food(
    40.706,
    -74.011,
    1000
)
run_agent(
    "How many restaurants are there in Chelsea?"
)
run_agent(
    "Show restaurants in SoHo"
)
run_agent(
    "Which neighbourhood has the most cafes?"
)
run_agent(
    "What kind of neighbourhood is SoHo?"
)
def summarise_neighbourhood_simple(neighbourhood):

    subset = ...

    if len(subset) == 0:
        return "Neighbourhood not found."

    top = subset["amenity"].value_counts().head(10)
def summarise_neighbourhood_simple(neighbourhood):

    subset = pois_with_nta[
        pois_with_nta["ntaname"]
        .str.contains(
            neighbourhood,
            case=False,
            na=False
        )
    ]

    if len(subset) == 0:
        return "Neighbourhood not found."

    top = subset["amenity"].value_counts().head(10)

    text = (
        f"{neighbourhood} contains "
        f"{len(subset)} mapped amenities.\n\n"
        f"Top amenity categories:\n"
    )

    for amenity, count in top.items():
        text += f"- {amenity}: {count}\n"

    return text
print(
    summarise_neighbourhood_simple("SoHo")
)
nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Chelsea",
    pois_gdf=pois_with_nta
)

print(nta_name)
print(n)
m = amenity_map(
    category="restaurant",
    neighbourhood="Chelsea"
)

m
m = amenity_map(
    category="cafe",
    neighbourhood="SoHo"
)

m
rank_neighbourhoods("restaurant")
rank_neighbourhoods("cafe")
print(
    summarise_neighbourhood_simple("SoHo")
)
print(
    summarise_neighbourhood_simple("Chelsea")
)
nearby_food(
    40.706,
    -74.011,
    1000
)
run_agent(
    "How many restaurants are there in Chelsea?"
)
run_agent(
    "Which neighbourhood has the most restaurants?"
)
run_agent(
    "What kind of neighbourhood is SoHo?"
)
run_agent(
    "What food options are near the Financial District?"
)
print("="*60)
print("TEST 1: count_pois")
print(count_pois(
    category="restaurant",
    neighbourhood="Chelsea",
    pois_gdf=pois_with_nta
))

print("="*60)
print("TEST 2: rank_neighbourhoods")
print(rank_neighbourhoods("restaurant"))

print("="*60)
print("TEST 3: summarise_neighbourhood_simple")
print(summarise_neighbourhood_simple("SoHo"))

print("="*60)
print("TEST 4: nearby_food")
print(nearby_food(
    40.706,
    -74.011,
    1000
))
print("="*60)
print("TEST 1: count_pois")
print(
    count_pois(
        category="restaurant",
        neighbourhood="Chelsea",
        pois_gdf=pois_with_nta
    )
)

print("\n" + "="*60)
print("TEST 2: rank_neighbourhoods")
print(
    rank_neighbourhoods("restaurant")
)

print("\n" + "="*60)
print("TEST 3: summarise_neighbourhood_simple")
print(
    summarise_neighbourhood_simple("SoHo")
)

print("\n" + "="*60)
print("TEST 4: nearby_food")
print(
    nearby_food(
        40.706,
        -74.011,
        1000
    )
)

print("\n" + "="*60)
print("TEST 5: restaurant map")

m = restaurant_map("Chelsea")

if m is not None:
    print("✓ Map created successfully")
else:
    print("✗ Map creation failed")
test_queries = [
    "How many restaurants are there in Chelsea?",
    "Show restaurants in SoHo",
    "Which neighbourhood has the most restaurants?",
    "What kind of neighbourhood is SoHo?",
    "What food options are near the Financial District?"
]

for q in test_queries:

    print("\n" + "=" * 80)
    print("QUERY:", q)

    try:
        result = run_agent(q)

        print("RESULT:")
        print(result)

    except Exception as e:
        print("ERROR:")
        print(e)
#Create an interactive nearby-food map
import folium

def nearby_food_map(lat, lon, radius_m):

    restaurants, cafes = nearby_food(
        lat,
        lon,
        radius_m
    )

    m = folium.Map(
        location=[lat, lon],
        zoom_start=15
    )

    # Query location
    folium.Marker(
        [lat, lon],
        popup="Search Location",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Restaurants
    for _, row in restaurants.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=4,
            color="red",
            fill=True,
            popup=f"Restaurant ID: {row['id']}"
        ).add_to(m)

    # Cafes
    for _, row in cafes.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=4,
            color="blue",
            fill=True,
            popup=f"Cafe ID: {row['id']}"
        ).add_to(m)

    return m
import inspect

print(inspect.getsource(count_pois))
elif (
    "near" in q
    or "nearby" in q
    or "food options" in q
):
    
    lat = 40.706
    lon = -74.011
    radius = 1000

    restaurants, cafes = nearby_food(
        lat,
        lon,
        radius
    )

    display(
        nearby_food_map(
            lat,
            lon,
            radius
        )
    )

    return (
        f"There are {len(restaurants)} restaurants "
        f"and {len(cafes)} cafes within "
        f"{radius} metres."
    )
with open("src/analytics.py", "r", encoding="utf-8") as f:
    print(f.read())
from src.analytics import (
    count_pois,
    rank_neighbourhoods,
    summarise_neighbourhood_simple,
    nearby_food
)

print("Analytics module imported successfully!")
nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Chelsea",
    pois_gdf=pois_with_nta
)

print(nta_name)
print(n)
%whos
from src.analytics import (
    count_pois,
    rank_neighbourhoods,
    summarise_neighbourhood_simple,
    nearby_food
)

print("✅ analytics.py imported successfully")
help(count_pois)
from src.analytics import (
    count_pois,
    rank_neighbourhoods,
    summarise_neighbourhood_simple,
    nearby_food
)

print("✅ Analytics module loaded successfully")
from src.mapping import hello_map

m = hello_map()

m
amenity_map
import folium

def nearby_food_map(lat, lon, radius_m):

    restaurants, cafes = nearby_food(
        lat,
        lon,
        radius_m
    )

    m = folium.Map(
        location=[lat, lon],
        zoom_start=15
    )

    # Search location
    folium.Marker(
        [lat, lon],
        popup="Financial District",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Search radius
    folium.Circle(
        location=[lat, lon],
        radius=radius_m,
        color="green",
        fill=False
    ).add_to(m)

    # Restaurants
    for _, row in restaurants.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=4,
            color="red",
            fill=True,
            fill_opacity=0.8,
            popup=f"Restaurant ID: {row['id']}"
        ).add_to(m)

    # Cafes
    for _, row in cafes.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=4,
            color="blue",
            fill=True,
            fill_opacity=0.8,
            popup=f"Cafe ID: {row['id']}"
        ).add_to(m)

    return m
m = nearby_food_map(
    40.706,
    -74.011,
    1000
)

m
restaurants, cafes = nearby_food(
    40.706,
    -74.011,
    1000
)
print("Restaurants:", len(restaurants))
print("Cafes:", len(cafes))
for _, row in restaurants.iterrows():
    print(row.geometry.y, row.geometry.x)
restaurants, cafes = nearby_food(
    40.706,
    -74.011,
    1000
)
print("Restaurants:", len(restaurants))
print("Cafes:", len(cafes))
for _, row in restaurants.iterrows():
    print(row.geometry.y, row.geometry.x)
print(restaurants.crs)
restaurants_ll = restaurants.to_crs(4326)
cafes_ll = cafes.to_crs(4326)
for _, row in restaurants_ll.iterrows():

    folium.CircleMarker(
        location=[
            row.geometry.y,
            row.geometry.x
        ],
        radius=4,
        color="red",
        fill=True
    ).add_to(m)
for _, row in cafes_ll.iterrows():

    folium.CircleMarker(
        location=[
            row.geometry.y,
            row.geometry.x
        ],
        radius=4,
        color="blue",
        fill=True
    ).add_to(m)
count = 0

for _, row in restaurants.iterrows():
    count += 1

print(count)
from folium.plugins import MarkerCluster

cluster = MarkerCluster().add_to(m)

for _, row in restaurants_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup="Restaurant",
        icon=folium.Icon(color="red")
    ).add_to(cluster)

for _, row in cafes_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup="Cafe",
        icon=folium.Icon(color="blue")
    ).add_to(cluster)
print(restaurants.crs)
print(cafes.crs)
restaurants_ll = restaurants.to_crs(4326)
cafes_ll = cafes.to_crs(4326)
for _, row in restaurants_ll.iterrows():

    folium.CircleMarker(
        location=[
            row.geometry.y,
            row.geometry.x
        ],
        radius=4,
        color="red",
        fill=True,
        popup=f"Restaurant ID: {row['id']}"
    ).add_to(m)
for _, row in cafes_ll.iterrows():

    folium.CircleMarker(
        location=[
            row.geometry.y,
            row.geometry.x
        ],
        radius=4,
        color="blue",
        fill=True,
        popup=f"Cafe ID: {row['id']}"
    ).add_to(m)
from folium.plugins import MarkerCluster

cluster = MarkerCluster().add_to(m)
for _, row in restaurants_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Restaurant {row['id']}",
        icon=folium.Icon(color="red")
    ).add_to(cluster)
for _, row in cafes_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Cafe {row['id']}",
        icon=folium.Icon(color="blue")
    ).add_to(cluster)
print(
    restaurants_ll.geometry.iloc[0]
)
m = nearby_food_map(
    40.706,
    -74.011,
    1000
)

m
print(restaurants.crs)
print(cafes.crs)
restaurants_ll = restaurants.to_crs(4326)
print(restaurants_ll.geometry.iloc[0])
print("Restaurant markers:", len(restaurants))
print("Cafe markers:", len(cafes))
from folium.plugins import MarkerCluster

cluster = MarkerCluster().add_to(m)

for _, row in restaurants_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Restaurant ID: {row['id']}",
        icon=folium.Icon(color="red")
    ).add_to(cluster)

for _, row in cafes_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Cafe ID: {row['id']}",
        icon=folium.Icon(color="blue")
    ).add_to(cluster)
restaurants_fg = folium.FeatureGroup(name="Restaurants")
cafes_fg = folium.FeatureGroup(name="Cafes")

# add markers to each group

restaurants_fg.add_to(m)
cafes_fg.add_to(m)

folium.LayerControl().add_to(m)
print(restaurants.crs)

restaurants_ll = restaurants.to_crs(4326)

print(restaurants_ll.geometry.iloc[0])
print(len(restaurants_ll))
for _, row in restaurants_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Restaurant {row['id']}"
    ).add_to(m)
from folium.plugins import MarkerCluster
cluster = MarkerCluster().add_to(m)
for _, row in restaurants_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Restaurant ID: {row['id']}",
        icon=folium.Icon(color="red", icon="cutlery", prefix="fa")
    ).add_to(cluster)
for _, row in cafes_ll.iterrows():

    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Cafe ID: {row['id']}",
        icon=folium.Icon(color="blue", icon="coffee", prefix="fa")
    ).add_to(cluster)
folium.Circle(
    location=[lat, lon],
    radius=1000,
    color="green",
    weight=3,
    fill=False,
    popup="1 km search radius"
).add_to(m)
print("Restaurants:", len(restaurants_ll))
print("Cafes:", len(cafes_ll))
print(f"Restaurant markers added: {len(restaurants_ll)}")
print(f"Cafe markers added: {len(cafes_ll)}")
folium.Circle(
    location=[40.706, -74.011],
    radius=1000,
    color="green",
    weight=3,
    fill=False,
    popup="1 km search radius"
).add_to(m)

m
from folium.plugins import MarkerCluster

m = folium.Map(
    location=[40.706, -74.011],
    zoom_start=15
)

cluster = MarkerCluster().add_to(m)

for _, row in restaurants_ll.iterrows():
    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Restaurant ID: {row['id']}",
        icon=folium.Icon(color="red")
    ).add_to(cluster)

for _, row in cafes_ll.iterrows():
    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Cafe ID: {row['id']}",
        icon=folium.Icon(color="blue")
    ).add_to(cluster)

folium.Circle(
    location=[40.706, -74.011],
    radius=1000,
    color="green",
    weight=3,
    fill=False,
    popup="1 km search radius"
).add_to(m)

m
import os

print(os.getcwd())
import os

print(os.listdir())
print(os.listdir("src"))
import os

os.rename(
    "src/analytics.py.txt",
    "src/analytics.py"
)

print(os.listdir("src"))
print(os.listdir("src"))
from src.analytics import count_pois

print("Import successful")
with open("src/analytics.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    print(f"{i}: {line.rstrip()}")
lat = 40.706
lon = -74.011

folium.Circle(
    location=[lat, lon],
    radius=1000,
    color="green",
    weight=3,
    fill=False,
    popup="1 km search radius"
).add_to(m)

m
from folium.plugins import MarkerCluster

m = folium.Map(
    location=[40.706, -74.011],
    zoom_start=15
)

cluster = MarkerCluster().add_to(m)

for _, row in restaurants_ll.iterrows():
    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"Restaurant {row['id']}"
    ).add_to(cluster)

m
restaurants_ll = restaurants.to_crs(4326)
cafes_ll = cafes.to_crs(4326)
    elif (
        "near" in q
        or "nearby" in q
        or "food options" in q
    ):

        display(
            nearby_food_map(
                40.706,
                -74.011,
                1000
            )
        )

        return (
            "Showing restaurants and cafes "
            "within 1 km of the Financial District."
        )
m = nearby_food_map(
    40.706,
    -74.011,
    1000
)

m
folium.Circle(
    location=[lat, lon],
    radius=radius_m,
    color="green",
    fill=False
).add_to(m)
run_agent(
    "What food options are near the Financial District?"
)
print(
    count_pois(
        category="restaurant",
        neighbourhood="Chelsea",
        pois_gdf=pois_with_nta
    )
)
print(
    rank_neighbourhoods("restaurant")
)
result = summarise_neighbourhood_simple("SoHo")

print(type(result))
print(result)
from src.analytics import count_pois

print("Import successful")
nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Chelsea",
    pois_gdf=pois_with_nta
)

print(nta_name)
print(n)
from src.analytics import count_pois
nta_name, n = count_pois(
    category="restaurant",
    neighbourhood="Chelsea",
    pois_gdf=pois_with_nta
)

print(nta_name)
print(n)
Edit → Find and Replace
Ctrl + F
from src.analytics import rank_neighbourhoods

rank_neighbourhoods("restaurant")
test_queries * [
    "How many restaurants are t*ere in Chelsea?",
    "Show restau*ants in SoHo",
    "Which neighbou*hood has the most restaurants?",
 *  "What kind of neighbourhood is S*Ho?",
    "What food options are near the Financial District?"
]

for q in test_queries:
    print("\n" + "="*80)
    print("QUERY:", q)

    try:
        result = run_agent(q)
        print("RESULT:")
        print(result)

    except Exception as e:
        print("ERROR:")
        print(e)
from IPython.display import display

for q in test_queries:

    print("\n" + "="*80)
    print("QUERY:", q)

    try:

        result = run_agent(q)

        if result is not None:
            print(result)

    except Exception as e:

        print("ERROR:", e)
summarise_neighbourhood_simple("SoHo")
run_agent(
    "I'm staying in the Financial District. What restaurants and cafes are nearby?"
)
print(manhattan.columns)
import matplotlib.pyplot as plt

def show_neighbourhood_map(neighbourhood):

    nta = nta_gdf[
        nta_gdf["NTAName"].str.contains(
            neighbourhood,
            case=False,
            na=False
        )
    ]

    if nta.empty:
        print("Neighbourhood not found.")
        return

    fig, ax = plt.subplots(figsize=(8, 8))

    nta_gdf.boundary.plot(ax=ax, color="lightgrey")
    nta.plot(ax=ax, color="red", alpha=0.6)

    ax.set_title(f"Neighbourhood: {neighbourhood}")
    plt.show()
print(f"There are {n} restaurants in {nta_name}.")
show_neighbourhood_map(neighbourhood)
import matplotlib.pyplot as plt

def show_restaurants_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    restaurants = pois_with_nta[
        (pois_with_nta["category"] == "restaurant")
        & (pois_with_nta["NTAName"] == nta_name)
    ]

    fig, ax = plt.subplots(figsize=(10, 10))

    restaurants.plot(
        ax=ax,
        color="red",
        markersize=10
    )

    ax.set_title(
        f"{n} Restaurants in {nta_name}"
    )

    plt.show()
import folium

def restaurant_map(neighbourhood):

    nta_name, n = count_pois(
        category="restaurant",
        neighbourhood=neighbourhood,
        pois_gdf=pois_with_nta
    )

    restaurants = pois_with_nta[
        (pois_with_nta["category"] == "restaurant")
        & (pois_with_nta["NTAName"] == nta_name)
    ]

    centre = restaurants.geometry.unary_union.centroid

    m = folium.Map(
        location=[centre.y, centre.x],
        zoom_start=14
    )

    for _, row in restaurants.iterrows():

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=3,
            color="red",
            fill=True
        ).add_to(m)

    return m
restaurant_map("SoHo")
run_agent("How many restaurants are there in SoHo?")
q_test = "How many restaurants are there in the Financial District?"
run_agent(q_test)
sorted(
    pois_with_nta["ntaname"]
    .dropna()
    .unique()
)
uws = pois_with_nta[
    (pois_with_nta["amenity"] == "restaurant")
    &
    (
        pois_with_nta["ntaname"]
        .str.contains("Upper West Side", case=False, na=False)
    )
]

uws["ntaname"].value_counts()
lincoln_square = pois_with_nta[
    (pois_with_nta["amenity"] == "restaurant")
    &
    (pois_with_nta["ntaname"] == "Upper West Side-Lincoln Square")
]

n = len(lincoln_square)

print(
    "[1] count_pois(category='restaurant', "
    "neighbourhood='Upper West Side')"
)

print(
    f"→ Upper West Side-Lincoln Square: {n} POIs in category 'restaurant'"
)

print(
    f"Answer: There are {n} restaurants in the Upper West Side."
)
def count_pois(category, neighbourhood, pois_gdf):

    matches = pois_gdf[
        (pois_gdf["amenity"].str.lower() == category.lower())
        &
        (
            pois_gdf["ntaname"]
            .str.lower()
            .str.contains(neighbourhood.lower(), na=False)
        )
    ]

    if len(matches) == 0:
        return "No matching POIs found."

    counts = matches["ntaname"].value_counts()

    nta_name = counts.index[0]
    count = counts.iloc[0]

    return (
        f"{nta_name}: {count} POIs in category '{category}'"
    )
print(
    count_pois(
        "restaurant",
        "Upper West Side",
        pois_with_nta
    )
)
q2 = "How many restaurants are there in the Upper West Side?"

print(f"Query: {q2}\n")

result = count_pois(
    "restaurant",
    "Upper West Side",
    pois_with_nta
)

print(
    "[1] count_pois(category='restaurant', "
    "neighbourhood='Upper West Side')"
)

print(f"→ {result}")

count = int(result.split(":")[1].split()[0])

print(
    f"Answer: There are {count} restaurants in the Upper West Side."
)
def rank_neighbourhoods(category, pois_gdf):
    """
    Rank Manhattan neighbourhoods by number of POIs in a category.
    """

    result = pois_gdf[
        pois_gdf["amenity"].str.lower() == category.lower()
    ]

    ranking = (
        result.groupby("ntaname")
        .size()
        .sort_values(ascending=False)
    )

    return ranking
q3 = "Which neighbourhood has the highest number of bars?"

print(f"Query: {q3}\n")

ranking = rank_neighbourhoods(
    category="bar",
    pois_gdf=pois_with_nta
)

print(
    "[1] count_pois(category='bar', neighbourhood=None)"
)
print("→ Ranking of Manhattan NTAs by 'bar' count:\n")

for nta, count in ranking.head(10).items():
    print(f"{nta} {count}")

top_nta = ranking.index[0]
top_count = ranking.iloc[0]

print(
    f"\nAnswer: {top_nta} has the highest number of bars ({top_count})."
)
def summarise_neighbourhood(neighbourhood, pois_gdf):

    subset = pois_gdf[
        pois_gdf["ntaname"]
        .str.contains(neighbourhood, case=False, na=False)
    ]

    total = len(subset)

    top_categories = (
        subset["amenity"]
        .value_counts()
        .head(5)
    )

    summary = (
        f"{subset['ntaname'].iloc[0]} — "
        f"{total} total POIs\n\n"
        f"Top categories:\n"
    )

    for category, count in top_categories.items():
        summary += f"{category}: {count}\n"

    return summary
q4 = "What kind of neighbourhood is SoHo?"

print(f"Query: {q4}\n")

result = summarise_neighbourhood(
    neighbourhood="SoHo",
    pois_gdf=pois_with_nta
)

print(
    "[1] summarise_neighbourhood(neighbourhood='SoHo')"
)

print("→", result)
subset = pois_with_nta[
    pois_with_nta["ntaname"]
    .str.contains("SoHo", case=False, na=False)
]

top = subset["amenity"].value_counts().head(5)

print("\nAnswer:")

print(
    "SoHo appears to be a dense mixed-use neighbourhood with a strong "
    "commercial and visitor-oriented character. The area contains many "
    "restaurants, public amenities and street infrastructure, indicating "
    "a highly active urban environment that supports shopping, dining and "
    "pedestrian activity."
)
q4 = "What kind of neighbourhood is SoHo?"

print(f"Query: {q4}\n")

answer4 = summarise_neighbourhood(
    "SoHo",
    pois_with_nta
)

print(answer4)
import inspect
print(inspect.getsource(summarise_neighbourhood))
#ln 33

def find_pois_near(lat, lon, radius_m, category, pois_gdf):

    pt = gpd.GeoSeries(
        [Point(lon, lat)],
        crs="EPSG:4326"
    )

    pt_2263 = pt.to_crs(2263)

    pois_2263 = pois_gdf.to_crs(2263)

    nearby = pois_2263[
        pois_2263.distance(pt_2263.iloc[0]) <= radius_m
    ]

    nearby = nearby[
        nearby["amenity"].str.lower() == category.lower()
    ]

    return nearby
lat = 40.706
lon = -74.011
radius_m = 1000
restaurants = find_pois_near(
    lat=40.706,
    lon=-74.011,
    radius_m=1000,
    category="restaurant",
    pois_gdf=pois_with_nta
)

print(
    "[1] find_pois_near(lat=40.706, lon=-74.011, radius_m=1000, category='restaurant')"
)

print(
    f"\n→ {len(restaurants)} POIs within 1000m (category: restaurant)"
)
cafes = find_pois_near(
    lat=40.706,
    lon=-74.011,
    radius_m=1000,
    category="cafe",
    pois_gdf=pois_with_nta
)

print(
    "\n[2] find_pois_near(lat=40.706, lon=-74.011, radius_m=1000, category='cafe')"
)

print(
    f"\n→ {len(cafes)} POIs within 1000m (category: cafe)"
)
print(
    f"\nAnswer: There are {len(restaurants)} restaurants "
    f"and {len(cafes)} cafes within a 1 km radius of the "
    f"Financial District. You have a wide range of sit-down "
    f"dining and cafe options nearby."
)
q5 = (
    "I'm staying at a hotel in the Financial District and I'm "
    "a picky eater. No fast food, only proper sit-down restaurants "
    "and cafes. I'd rather not travel more than about a kilometre. "
    "What's the best food around me?"
)

print(f"Query: {q5}\n")

lat = 40.706
lon = -74.011
radius_m = 1000

restaurants = find_pois_near(
    lat, lon, radius_m,
    "restaurant",
    pois_with_nta
)

cafes = find_pois_near(
    lat, lon, radius_m,
    "cafe",
    pois_with_nta
)

print(
    "[1] find_pois_near(lat=40.706, lon=-74.011, "
    "radius_m=1000, category='restaurant')"
)
print(
    f"→ {len(restaurants)} POIs within 1000m "
    "(category: restaurant)\n"
)

print(
    "[2] find_pois_near(lat=40.706, lon=-74.011, "
    "radius_m=1000, category='cafe')"
)
print(
    f"→ {len(cafes)} POIs within 1000m "
    "(category: cafe)\n"
)

print(
    f"Answer: There are {len(restaurants)} restaurants "
    f"and {len(cafes)} cafes within a 1 km radius of the "
    f"Financial District."
)
run_agent()
count_pois()
summarise_neighbourhood()
find_pois_near()
find_nta()
call_llm()
pois_with_nta
import inspect

print(inspect.getsource(run_agent))
def run_agent(query):
    ...
GLOBAL_POIS = pois_with_nta

def run_agent(query):
    return do_work(query, GLOBAL_POIS)
q3 = "Which neighbourhood has the highest number of bars?"

answer3 = run_agent(
    q3,
    pois_with_nta
)

print(answer3)
q4 = "What kind of neighbourhood is SoHo?"

answer4 = run_agent(
    q4,
    pois_with_nta
)

print(answer4)
def run_agent(query):
    global pois_with_nta

    ...
q2 = "How many restaurants are there in the Upper West Side?"
print(run_agent(q2))

q3 = "Which neighbourhood has the highest number of bars?"
print(run_agent(q3))

q4 = "What kind of neighbourhood is SoHo?"
print(run_agent(q4))
import inspect
print(inspect.getsource(run_agent))
def run_agent(query):
    global pois_with_nta

    ...
q2 = "How many restaurants are there in the Upper West Side?"

print(f"Query: {q2}\n")

answer2 = run_agent(q2, pois_gdf)

print(answer2)
q2 = "How many restaurants are there in the Upper West Side?"

print(f"Query: {q2}\n")

answer2 = run_agent(q2)

print(answer2)
import inspect

print(inspect.signature(run_agent))
import inspect
print(inspect.getsource(run_agent))
import inspect

print(inspect.signature(run_agent))
print(inspect.getsource(run_agent))
run_agent("hello")
%history -f notebook_history.py
