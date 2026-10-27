# app.py

import streamlit as st
from streamlit_folium import st_folium

from src.data_loader import load_data
from src.agent import run_agent


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="GeoAI Manhattan Explorer",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🗽 GeoAI Manhattan Explorer")

st.markdown("""
A **Natural Language Spatial Query System**
for Manhattan neighbourhood analysis.

### Example Queries

- How many restaurants are there in Chelsea?
- What kind of neighbourhood is SoHo?
- What food options are near the Financial District?
- Which neighbourhood has the most restaurants?

### Interactive Map Queries

- Show restaurants in Chelsea
- Show cafes in SoHo
- Show bars in Harlem

### Future GeoAI Queries

- Compare Chelsea and SoHo
- Which neighbourhood is best for coffee lovers?
- Which area has the highest concentration of restaurants?
""")

# --------------------------------------------------
# QUERY INPUT
# --------------------------------------------------

query = st.text_input(
    "Ask a spatial question"
)

# --------------------------------------------------
# RUN QUERY
# --------------------------------------------------

if st.button("Run Query"):

    if not query.strip():

        st.warning(
            "Please enter a query."
        )

    else:

        try:

            with st.spinner(
                "Loading spatial datasets..."
            ):
                manhattan, pois_with_nta = (
                    load_data()
                )

            with st.spinner(
                "Running GeoAI analysis..."
            ):
                result = run_agent(
                    query,
                    pois_with_nta,
                    manhattan
                )

            st.success(
                result["message"]
            )

            if (
                result.get("map")
                is not None
            ):

                st.subheader(
                    "🗺️ Interactive Map"
                )

                st_folium(
                    result["map"],
                    width=1200,
                    height=700,
                    returned_objects=[]
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )