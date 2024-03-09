import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from src.exportar_imagen import mostrar_formato_exportacion


def control_graficos(chart_type, df, dropdown_options, template):
    """
    Función que muestra los diferentes parámetros aceptados según el tipo de gráfico elegido
    :param chart_type: str, nombre del gráfico
    :param df: set de datos importado
    :param dropdown_options: lista con los nombres de las columnas
    :param template: str, representación del tema elegido
    :return:
    """
    length_of_options = len(dropdown_options)
    length_of_options -= 1

    plot = px.scatter()

    if chart_type == 'Grafico de dispersion':
        st.sidebar.subheader("Gráfico de dispersión")

        try:
            x_values = st.sidebar.selectbox('Eje X', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Eje Y',index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            symbol_value = st.sidebar.selectbox("Forma del punto",index=length_of_options, options=dropdown_options)
            marginaly = st.sidebar.selectbox("Gráfico marginal", index=0,options=[ None, 'box',
                                                                         'violin', 'histogram'])
            #log_x = st.sidebar.selectbox('Escala log. en x', options=[False, True])
            #log_y = st.sidebar.selectbox('Escala log. en y', options=[False, True])
            title = st.sidebar.text_input(label='Título de gráfico')

            plot = px.scatter(data_frame=df,
                              x=x_values,
                              y=y_values,
                              color=color_value,
                              symbol=symbol_value,
                              marginal_y=marginaly, 
                              #log_x=log_x, log_y=log_y,
                              template=template, title=title)
            
        except Exception as e:
            print(e)

    if chart_type == 'Histograma':
        st.sidebar.subheader("Histograma")

        try:
            x_values = st.sidebar.selectbox('Eje X', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Eje y',index=length_of_options, options=dropdown_options)
            nbins = st.sidebar.number_input(label='Número de contenedores', min_value=2, value=5)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            barmode = st.sidebar.selectbox('Modo de barra', options=['stack', 'group', 'overlay','relative'], index=1)
            hist_func = st.sidebar.selectbox('Función de agregación del histograma', index=0,
                                             options=['count','sum', 'avg', 'min', 'max'])
            title = st.sidebar.text_input(label='Título del gráfico')

            plot = px.histogram(data_frame=df,
                                x=x_values, y=y_values,
                                nbins=nbins,
                                color=color_value,
                                histfunc=hist_func,
                                barmode='group',
                                template=template, title=title)

            # Configurar los títulos de los ejes
            plot.update_layout(xaxis_title=x_values, yaxis_title=y_values)

        except Exception as e:
            print(e)

    if chart_type == 'Grafico por sectores':
        st.sidebar.subheader('Gráfico por sectores')

        try:
            name_value = st.sidebar.selectbox(label='Nombre (La columna alegida debería ser categórica)', index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox(label='Color (La columna alegida debería ser categórica)', index=length_of_options, options=dropdown_options)
            value = st.sidebar.selectbox("Valor", index=length_of_options, options=dropdown_options)
            labels = st.sidebar.selectbox('Mostrar nombre en el gráfico', options=[True, False])
            title = st.sidebar.text_input(label='Título del gráfico')

            plot = px.pie(data_frame=df,names=name_value,
                          values=value,color=color_value, title=title)

            if labels:
                plot.update_traces(textposition='inside', textinfo='percent+label')

        except Exception as e:
            print(e)

    if chart_type == 'Grafico de lineas':
        st.sidebar.subheader("Gráfico de lineas")

        try:
            x_values = st.sidebar.selectbox('Eje X', index=length_of_options, options=dropdown_options)
            y_values = st.sidebar.selectbox('Eje Y', options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options, options=dropdown_options)
            title = st.sidebar.text_input(label='Título del gráfico')

            plot = px.line(data_frame=df,
                           #line_group=line_group,
                           #line_dash=line_dash,
                           x=x_values,y=y_values,
                           color=color_value,
                           #log_x=log_x,
                           #log_y=log_y,
                           template=template,
                           title=title)
            
        except Exception as e:
            print(e)

    if chart_type == 'Grafico de barras':
        st.sidebar.subheader('Gráfico de barras')

        try:
            x_values = st.sidebar.selectbox('Eje X', index=length_of_options, options=dropdown_options)
            y_values = st.sidebar.selectbox('Ejec Y', index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options, options=dropdown_options)
            hover_name_value = st.sidebar.selectbox("Nombre superpuesto", index=length_of_options, options=dropdown_options)
            barmode = st.sidebar.selectbox('Modo de barra', options=['stack', 'group', 'overlay','relative'], index=3)
            title = st.sidebar.text_input(label='Título del gráfico')

            plot = px.bar(data_frame=df, 
                            x=x_values, y=y_values, 
                            color=color_value, 
                            template=template,
                            hover_name=hover_name_value, 
                            barmode=barmode,
                            title=title)

        except Exception as e:
            print(e)
    
    if chart_type == 'Grafico de violin':
        st.sidebar.subheader('Gráfico de Violín')
    
        try:
            x_values = st.sidebar.selectbox('Eje x', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Eje y',index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            violinmode = st.sidebar.selectbox('Modo de violín', options=['group', 'overlay'])
            box = st.sidebar.selectbox("Mostrar caja", options=[False, True])
            outliers = st.sidebar.selectbox('Mostrar puntos', options=[False, 'all', 'outliers', 'suspectedoutliers'])
            title = st.sidebar.text_input(label='Título del gráfico')

            plot = px.violin(data_frame=df,x=x_values,
                             y=y_values,color=color_value,
                             box=box,
                             #log_x=log_x, log_y=log_y,
                             violinmode=violinmode,points=outliers,
                             template=template, title=title)

        except Exception as e:
            print(e)
    
    if chart_type == 'Grafico de cajas':
        st.sidebar.subheader('Gráfico de cajas')
    
        try:
            x_values = st.sidebar.selectbox('Eje x', index=length_of_options, options=dropdown_options)
            y_values = st.sidebar.selectbox('Eje y', index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options, options=dropdown_options)
            boxmode = st.sidebar.selectbox('Modo de caja', options=['group', 'overlay'])
            outliers = st.sidebar.selectbox('Mostrar puntos', options=[False, 'all', 'outliers', 'suspectedoutliers'])
            notched = st.sidebar.selectbox('Mostrar muescas', options=[False, True])
            title = st.sidebar.text_input(label='Título del gráfico')

            plot = px.box(data_frame=df, x=x_values,
                          y=y_values, color=color_value,
                          notched=notched,
                          #log_x=log_x, log_y=log_y, 
                          boxmode=boxmode, points=outliers,
                          template=template, title=title)
        
    
        except Exception as e:
            print(e)

    if chart_type == 'Mapa de calor':
        st.sidebar.subheader('Mapa de calor')

        st.warning('El mapa de calor solo funciona para las columnas con valores numéricos.')

        try:
            import numpy as np
            # Filtrar columnas numéricas
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            selected_columns = st.sidebar.multiselect('Selecciona las columnas para el mapa de calor', options=numeric_columns)
            abs_value = st.sidebar.checkbox(label='Mapa en valor absoluto')
            title = st.sidebar.text_input(label='Título del mapa de calor')

            if selected_columns:
                selected_data = df[selected_columns]
                correlation_matrix = selected_data.corr()
                plot = px.imshow(abs(correlation_matrix) if abs_value else correlation_matrix, 
                                 template=template, 
                                 title=title,
                                 zmin=0 if abs_value else -1,  # Límite inferior de la escala
                                 zmax=1    # Límite superior de la escala
                                )

        except Exception as e:
            print(e)

    if chart_type not in ('Mapa de calor','Grafico por sectores'):
        st.sidebar.subheader('Ajustes Generales')
        # Agregar control deslizante para ajustar el tamaño de la fuente de los ejes
        axis_value_size = st.sidebar.slider("Tamaño del valor de los ejes", min_value=10, max_value=50, value=15)
        axis_font_size = st.sidebar.slider("Tamaño de los títulos de los ejes", min_value=10, max_value=50, value=15)
        legend_font_size = st.sidebar.slider("Tamaño de la leyenda", min_value=10, max_value=50, value=15)
        # Actualizar el tamaño de las fuentes
        plot.update_xaxes(tickfont=dict(size=axis_value_size, color='black'), title_font=dict(size=axis_font_size, color='black'))
        plot.update_yaxes(tickfont=dict(size=axis_value_size, color='black'), title_font=dict(size=axis_font_size, color='black'))
        plot.update_layout(legend=dict(font=dict(size=legend_font_size),title_font=dict(size=legend_font_size, color='black')))

    st.subheader("Gráfico")
    st.plotly_chart(plot)
    mostrar_formato_exportacion(plot, template)

