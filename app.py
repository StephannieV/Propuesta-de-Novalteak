import streamlit as st
import pandas as pd
import os

# Ruta donde están almacenados los CSVs generados
DATA_DIR = "/mnt/data/csv_datos_canada"

# Lista de archivos y sus nombres visibles
archivos = {
    "Inclusión del sector verde en construcción": "inclusion_sector_verde.csv",
    "Importación de madera a Canadá": "importacion_madera.csv",
    "Valoración de la industria del mueble (2020-2025)": "industria_mueble_valor.csv",
    "Crecimiento de muebles de lujo y sostenibles": "muebles_lujo_sostenibles.csv",
    "E-commerce de muebles personalizados (2020-2025)": "ecommerce_muebles_personalizados.csv",
    "Proyección de ventas de muebles con madera tropical": "ventas_madera_tropical.csv",
    "Penetración proyectada por zonas de Canadá": "penetracion_zonas.csv",
    "Penetración por aplicación final": "penetracion_aplicacion_final.csv",
    "Proyección de ventas según necesidad del cliente": "ventas_por_necesidad_cliente.csv"
}

# Título general
st.title("Dashboard de Datos - Industria Mueblera y Construcción Verde en Canadá")

# Mostrar cada sección del dashboard
for titulo, archivo in archivos.items():
    st.subheader(titulo)

    filepath = os.path.join(DATA_DIR, archivo)

    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        st.dataframe(df, use_container_width=True)
        
        # Descargar CSV
        with open(filepath, "rb") as f:
            st.download_button(
                label="📥 Descargar CSV",
                data=f,
                file_name=archivo,
                mime="text/csv"
            )
    else:
        st.warning(f"Archivo no encontrado: {archivo}")


