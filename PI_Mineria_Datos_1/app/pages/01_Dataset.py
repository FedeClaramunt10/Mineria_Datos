import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset - Streaming", page_icon="📊", layout="wide")

st.title("📊 Inspección y Calidad del Dataset")

# Carga de datos procesados
df = pd.read_csv('data/processed/dataset_final.csv')

st.markdown("""
### 📝 Descripción General
El conjunto de datos original contenía información sobre **8,160 usuarios** de una plataforma de streaming, incluyendo variables demográficas (edad, país) y de comportamiento (minutos de consumo, tickets de soporte) [5].
""")

# Ficha técnica
st.info(f"**Volumen final:** {df.shape[0]} filas y {df.shape[1]} columnas.")

st.subheader("🔍 Vista previa de los datos limpios")
st.dataframe(df.head(10))

st.markdown("""
### ✨ Transformaciones Principales
Para asegurar la integridad del análisis, se aplicaron las siguientes correcciones en la **Notebook 02** [7, 8]:
1. **Estandarización de texto:** Se unificaron nombres de países (ej. 'ARG' a 'Argentina') y géneros favoritos [9].
2. **Tratamiento de nulos:** Los valores faltantes en visualización se imputaron usando la **mediana por plan** [GeminiChat].
3. **Filtro de valores imposibles:** Se eliminaron registros con edades de 150 años y minutos de visualización negativos [8].
""")