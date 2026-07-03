import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EDA - Streaming", page_icon="📈", layout="wide")

st.title("📈 Análisis Exploratorio de Datos (EDA)")

df = pd.read_csv('data/processed/dataset_final.csv')

# 1. Gráfico Univariado: Edad
st.subheader("1. Distribución Etaria")
fig_age = px.box(df, y="age", title="Dispersión de la Edad de Usuarios", labels={'age': 'Edad'})
st.plotly_chart(fig_age, use_container_width=True)
st.markdown("> **Interpretación:** La mediana de edad se sitúa en los 33 años, evidenciando que el público objetivo es mayoritariamente adulto joven [Notebook 03].")



# 2. grafico univariado: Minutos de Visualización 
st.subheader("2. Distribución del Tiempo de Visualización")
fig_mins = px.histogram(df, x="monthly_watch_time_mins", 
                       title="Frecuencia de Minutos Consumidos Mensualmente",
                       labels={'monthly_watch_time_mins': 'Minutos mensuales'},
                       marginal="box", # Incluye un boxplot para ver la dispersión
                       template="plotly_white")
st.plotly_chart(fig_mins, use_container_width=True)

st.markdown("""
> **Interpretación:** Este histograma permite observar la forma de la distribución del consumo. Tras la limpieza realizada en la Notebook 02, se evidencia una distribución más natural sin el sesgo del valor técnico '99,999'. La concentración en ciertos rangos ayuda a definir qué se considera un 'usuario promedio' frente a un 'heavy user' [3].
""")





# 3. Gráfico Bivariado: Plan vs Minutos
st.subheader("3. Consumo por Plan de Suscripción")
fig_plan = px.box(df, x="subscription_plan", y="monthly_watch_time_mins", color="subscription_plan",
                 title="Minutos Mensuales según Nivel de Plan")
st.plotly_chart(fig_plan, use_container_width=True)
st.markdown("> **Interpretación:** Se observa que el **Plan Premium** tiene una mediana de consumo superior, validando que los usuarios que pagan más son los más comprometidos [GeminiChat].")

# NOTA: Debés completar los 3 gráficos restantes (1 univariado, 1 bivariado y el multivariado)
# siguiendo esta misma estructura de "Gráfico + Interpretación" [4].




# 4. gráfico multivariado: País vs Género Favorito
st.subheader("4. Preferencias Culturales por Región")
# Creamos la tabla de contingencia
tabla_genero_pais = pd.crosstab(df['country'], df['favorite_genre'])

fig_heat = px.imshow(tabla_genero_pais, 
                    text_auto=True, 
                    aspect="auto",
                    title="Mapa de Calor: Género Favorito vs. País",
                    labels=dict(x="Género", y="País", color="Cantidad de Usuarios"),
                    color_continuous_scale='YlGnBu')
st.plotly_chart(fig_heat, use_container_width=True)

st.markdown("""
> **Interpretación:** Al cruzar el país con el género favorito, este gráfico evidencia si existen nichos de mercado geográficos. Por ejemplo, una alta concentración en un género específico en un país permite tomar decisiones de negocio sobre la adquisición de licencias de contenido local o regionalizado [4, 5].
""")






# 5 grafico multivariado: Edad vs Consumo vs Plan
st.subheader("5. Análisis Multivariado: Edad, Consumo y Plan")
fig_multi = px.scatter(df, 
                       x="age", 
                       y="monthly_watch_time_mins", 
                       color="subscription_plan",
                       title="Relación entre Edad y Consumo según el Plan de Suscripción",
                       labels={'age': 'Edad (años)', 
                               'monthly_watch_time_mins': 'Minutos mensuales',
                               'subscription_plan': 'Tipo de Plan'},
                       opacity=0.6,
                       template="plotly_white")
st.plotly_chart(fig_multi, use_container_width=True)

st.markdown("""
> **Interpretación:** Este gráfico multivariado permite identificar si el comportamiento de alto consumo (eje Y) está vinculado a un rango de edad específico o si es transversal a todos los planes. La superposición de colores (Planes) ayuda a detectar oportunidades de 'upselling': usuarios jóvenes con alto consumo que aún están en planes básicos [7, 8].
""")