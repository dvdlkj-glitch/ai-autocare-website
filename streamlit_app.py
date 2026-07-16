"""AI AutoCare — Streamlit wrapper.

Serves the static single-page site (index.html) full-screen inside Streamlit,
so the same repo can be deployed on Streamlit Cloud as well as GitHub Pages.
The car photo is inlined as a base64 data URI because relative asset paths
don't resolve inside the Streamlit component iframe.
"""

import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="AI AutoCare — Smart Service. Better Rides.",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent


@st.cache_data
def load_site() -> str:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    car = ROOT / "assets" / "car-side.webp"
    b64 = base64.b64encode(car.read_bytes()).decode()
    return html.replace(
        "assets/car-side.webp", f"data:image/webp;base64,{b64}"
    )


# Strip Streamlit chrome and let the embedded site fill the viewport.
st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {display: none;}
    [data-testid="stAppViewContainer"] {padding: 0;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    .stApp iframe {height: 100vh !important; width: 100% !important; border: none; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.iframe(load_site(), height="stretch")
