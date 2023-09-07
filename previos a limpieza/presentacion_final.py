#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

austria_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\austria_auto_exported.csv")
belgium_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\belgium_auto_exported.csv")
france_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\france_auto_exported.csv")
germany_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\germany_auto_exported.csv")
italy_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\italy_auto_exported.csv")
luxembourg_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\luxembourg_auto_exported.csv")
netherlands_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\netherlands_auto_exported.csv")


# In[8]:


import streamlit as st
import pandas as pd

# Cargar los archivos CSV
austria_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\austria_auto_exported.csv")
belgium_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\belgium_auto_exported.csv")
france_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\france_auto_exported.csv")
germany_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\germany_auto_exported.csv")
italy_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\italy_auto_exported.csv")
luxembourg_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\luxembourg_auto_exported.csv")
netherlands_df = pd.read_csv(r"C:\Users\VANT\iron\proyectos\PROYECTO_FINAL\bmw_options_2\netherlands_auto_exported.csv")

# Estilo CSS básico
st.markdown(
    """
    <style>
    .title {
        font-size: 32px;
        text-align: center;
        padding: 16px;
    }
    .sidebar {
        background-color: #f0f0f0;
        padding: 16px;
        border-radius: 8px;
        margin: 8px;
    }
    .button {
        background-color: #008CBA;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
    }
    .button:hover {
        background-color: #005F79;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Car Finder App")
    st.sidebar.header("Opciones de Filtro")
    st.sidebar.markdown("¡Personaliza tu búsqueda de autos!")

    # Filtrado de Streamlit
    make_input = st.sidebar.text_input("Marca (Make)")
    model_input = st.sidebar.text_input("Modelo (Model)")
    option_P = st.sidebar.radio("Unidad de Potencia", ["hp", "kw"], index=0)
    power_min_input = st.sidebar.number_input("Potencia Mínima", value=100)
    power_max_input = st.sidebar.number_input("Potencia Máxima", value=200)
    option_gear = st.sidebar.radio("Tipo de Transmisión", ["Manual", "Automático", "Semi"], index=0)
    option_mileage = st.sidebar.selectbox("Kilometraje", ["5.000", "10.000", "30.000", "50.000", "80.000", "100.000"], index=2)
    option_fuel = st.sidebar.selectbox("Tipo de Combustible", ["gasolina", "diésel", "eléctrico", "híbrido"], index=0)
    option_price = st.sidebar.selectbox("Precio", ["500", "10.000", "20.000", "30.000", "40.000", "50.000", "75.000", "100.000"], index=3)

    if st.sidebar.button("Aplicar Filtros", key="apply_filters"):
        # Resto de tu código para aplicar filtros aquí...

        # Muestra los resultados EN tabla en Streamlit
        for country, df in country_data_frames.items():
            st.header(f"Resultados para {country}:")
            st.write(df)  # Utiliza st.write para mostrar los DataFrames

if __name__ == "__main__":
    main()


# In[ ]:




