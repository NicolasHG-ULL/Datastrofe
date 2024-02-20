import streamlit as st

from ydata_profiling import ProfileReport

def mostrar_informe(df):
    try:
        # Generar informe de perfil
        profile = ProfileReport(df, title="Profiling Report")

        # Convertir el informe de perfil en HTML
        html_report = profile.to_html()

        # Mostrar el informe en Streamlit
        st.title("Informe")
        st.components.v1.html(html_report, width=800, height=600, scrolling=True)
    except Exception as e:
        st.error("Se produjo el siguiente error:")    
        st.error(e)