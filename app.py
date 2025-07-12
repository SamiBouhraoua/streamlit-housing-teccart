import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Analyse des facteurs influençant les prix des logements en Californie")

@st.cache_data
def importer_donnees():
    data = pd.read_csv("housing.csv")
    return data

data = importer_donnees()

if st.checkbox("Voir les premières lignes du jeu de données"):
    st.dataframe(data.head())

if st.checkbox("Afficher les statistiques descriptives"):
    st.header("Statistiques descriptives")
    st.write(data.describe())

if st.checkbox("Visualiser la distribution des prix des logements"):
    st.subheader("Histogramme des prix")
    fig_hist, ax_hist = plt.subplots()
    sns.histplot(data['median_house_value'], bins=30, kde=True, ax=ax_hist)
    st.pyplot(fig_hist)

if st.checkbox("Comparer les prix selon l'âge médian des logements"):
    st.subheader("Boxplot des prix par âge médian")
    fig_box, ax_box = plt.subplots()
    sns.boxplot(x=data['housing_median_age'], y=data['median_house_value'], ax=ax_box)
    st.pyplot(fig_box)

if st.checkbox("Voir la matrice de corrélation des variables numériques"):
    corr = data.corr(numeric_only=True)
    fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax_corr)
    st.pyplot(fig_corr)

colonne_choisie = st.selectbox("Sélectionnez une variable pour étudier sa corrélation avec le prix", data.columns)

if colonne_choisie != "median_house_value":
    fig_scatter, ax_scatter = plt.subplots()
    sns.scatterplot(data=data, x=colonne_choisie, y="median_house_value", alpha=0.5, ax=ax_scatter)
    ax_scatter.set_ylabel("Valeur médiane des logements")
    st.pyplot(fig_scatter)

st.header("Conclusion")
st.write("Pour plus de détails sur les facteurs influençant les prix, veuillez consulter le rapport final.")
