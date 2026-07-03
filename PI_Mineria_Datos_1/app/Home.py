import streamlit as st

# Configuración de la página (esto debe ser lo primero)
st.set_page_config(
    page_title="Dashboard - Plataforma Streaming",
    page_icon="🎬",
    layout="wide"
)

# Título Principal
st.title("🎬 Análisis de Comportamiento de Usuarios de Streaming")

# Introducción Ejecutiva
st.markdown("""
## 👋 Bienvenida
Esta aplicación interactiva presenta los resultados del análisis integral de datos realizado sobre una base de usuarios de una plataforma de streaming. 
A través de este dashboard, podrá navegar por las diferentes etapas del proyecto, desde la limpieza de datos hasta el análisis de componentes principales (PCA).
""")

# Columnas para Objetivos y Equipo
col1, col2 = st.columns(2)

with col1:
    st.info("### 🎯 Objetivos del Proyecto")
    st.markdown("""
    * **Calidad de Datos:** Identificar y corregir errores técnicos en el dataset original.
    * **Perfil del Usuario:** Entender las características demográficas y hábitos de consumo.
    * **Optimización de Negocio:** Evaluar la relación entre los planes de suscripción y el compromiso del usuario.
    """)

with col2:
    st.success("### 👥 Integrantes del Grupo")
    st.markdown("""
    * **Nombre y Apellido 1**
    * **Nombre y Apellido 2**
    """)
    st.caption("Tecnicatura Superior en Ciencia de Datos e IA - ITSE")

# Nota sobre la trazabilidad
st.divider()
st.markdown("""
> **Nota de Trazabilidad:** Este proyecto sigue un riguroso proceso de Minería de Datos, documentado paso a paso para asegurar que cada decisión técnica esté respaldada por evidencia estadística [3].
""")