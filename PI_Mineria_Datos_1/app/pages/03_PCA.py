import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="PCA - Streaming", page_icon="🧬", layout="wide")

st.title("🧬 Análisis de Componentes Principales (PCA)")

st.markdown("""
### 🛠️ Proceso Técnico
Para reducir la complejidad del dataset, se seleccionaron las variables numéricas: `age`, `monthly_watch_time_mins` y `customer_support_tickets`.
**Nota Crítica:** Se aplicó `StandardScaler` antes del análisis para evitar sesgos por magnitud de escala [12, 13].
""")

# Ejemplo de métricas de varianza (reemplazá con tus valores reales)
st.subheader("📉 Varianza Explicada Acumulada")
# Aquí graficarías el Scree Plot que hicimos en la Notebook 04 [14]
st.info("Con los primeros 2 componentes se logra retener más del **80% de la varianza total**, permitiendo una reducción eficiente sin pérdida crítica de información [Notebook 04].")