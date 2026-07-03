import streamlit as st

st.set_page_config(page_title="Conclusiones - Streaming", page_icon="🏁")

st.title("🏁 Conclusiones y Hallazgos")

st.markdown("""
### 💡 Hallazgos Principales
* **Segmentación:** Existe una correlación positiva entre el costo del plan y el compromiso visual, lo que justifica la estructura de precios actual.
* **Calidad:** La estandarización de variables geográficas permitió descubrir que el mercado con mayor potencial de crecimiento es **[País X]**.

### ⚠️ Limitaciones
* El dataset no cuenta con variables de ingresos económicos del usuario, lo que restringe el análisis de elasticidad de precio.

### 🚀 Próximos Pasos
* Aplicar algoritmos de **Clustering** sobre los componentes principales obtenidos en el PCA para automatizar la personalización de contenidos.
""")