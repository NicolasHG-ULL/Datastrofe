from base64 import b64encode
from PIL import Image
import io
import streamlit as st
import plotly.io as pio

@st.cache_data
def descargar_grafica(plot, output_format, width=None, height=None):
    """

    :param plot: gráfico a exportar
    :param output_format: str, el formato de imagen a exportar
    :return:
    """

    file_name_with_extension = 'plot.'+output_format

    if output_format == 'html':
        buffer = io.StringIO()
        plot.write_html(buffer)
        html_bytes = buffer.getvalue().encode()
        encoding = b64encode(html_bytes).decode()

        href = f'<a download={file_name_with_extension} href="data:file/html;base64,{encoding}" >Download</a>'

    if output_format in ('json', 'svg', 'pdf'):
        img_bytes = plot.to_image(format=output_format)
        encoding = b64encode(img_bytes).decode()

        href = f'<a download={file_name_with_extension} href="data:file/{output_format};base64,{encoding}" >Download</a>'

    if output_format in ('png', 'jpeg'):
        img_bytes = plot.to_image(format=output_format, width=width, height=height)
        encoding = b64encode(img_bytes).decode()

        href = f'<a download={file_name_with_extension} href="data:image/{output_format};base64,{encoding}" >Download</a>'
    return href


def mostrar_formato_exportacion(plot, template):
    try:
        st.subheader('Exportar imagen')
        output_format = st.selectbox(label='Seleccione formato de descarga', options=['png', 'jpeg', 'pdf', 'svg',
                                                                              'html', 'json'])
        if output_format in ('png', 'jpeg'):
            resolution = st.radio("Resolución de la imagen", options=["Baja", "Media", "Alta"], index=1)

            if resolution == "Baja":
                width, height = 800, 600
            elif resolution == "Media":
                width, height = 1200, 800
            elif resolution == "Alta":
                width, height = 1920, 1080

            href = descargar_grafica(plot, output_format=output_format, width=width, height=height)
        else:
            href = descargar_grafica(plot, output_format=output_format)
        st.markdown(href, unsafe_allow_html=True)
    except Exception as e:
        print(e)

