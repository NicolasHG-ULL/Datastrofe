import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

def mostrar_informe(df):
    try:
        st.header("Informe")

        # Seguridad antes DF de garn tamaño
        if len(df) > 20000:
            st.info("El dataset es grande, se genera un informe resumido.")
            df = df.sample(n=20000, random_state=42)

        profile = ProfileReport(
            df,
            title="Profiling Report",
            minimal=True,          
            explorative=False,
            correlations=None,
            interactions=None,
            missing_diagrams=None
        )

        st_profile_report(profile)

    except Exception as e:
        st.error("Se produjo un error al generar el informe")
        st.exception(e)