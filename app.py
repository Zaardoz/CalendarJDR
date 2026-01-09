import streamlit as st
import pandas as pd
import os

# Configuration de la page
st.set_page_config(page_title="Dispos JDR", layout="wide")
st.image("https://i.redd.it/dungeons-dragons-honor-among-thieves-3840-x-2160-v0-x5mw9i1aeyza1.jpg?width=3840&format=pjpg&auto=webp&s=d4f3740f9b570488a687247533305411817c17df", use_container_width=True)
st.title("🧙‍♂️Donjon & Dragons Session🧙‍♂️")
st.subheader("Disponibilités du samedi 10 au dimanche 18 (20h - 00h+)")

# Paramètres
jours = [
    "Samedi 10", "Dimanche 11", "Lundi 12", "Mardi 13", 
    "Mercredi 14", "Jeudi 15", "Vendredi 16", "Samedi 17", "Dimanche 18"
]
joueurs = ["MJ", "Elisa", "Rody", "Pierre", "Jenn"]
heures_fin = ["22h00", "22h30", "23h00", "23h30", "00h00", "00h30+", "Pas de limite"]

# Interface de saisie
nom_joueur = st.selectbox("Qui es-tu ?", joueurs)

st.write("Coche tes dispos et ton heure max de fin :")
data_input = []

for jour in jours:
    col1, col2, col3 = st.columns([2, 2, 4])
    with col1:
        dispo = st.checkbox(f"{jour}", key=f"check_{jour}")
    with col2:
        heure = st.selectbox("Heure max", heures_fin, key=f"h_{jour}", disabled=not dispo)
    with col3:
        note = st.text_input("Commentaire (optionnel)", key=f"n_{jour}", disabled=not dispo)
    
    if dispo:
        data_input.append({"Joueur": nom_joueur, "Jour": jour, "Fin": heure, "Note": note})

if st.button("Enregistrer mes dispos"):
    if data_input:
        df = pd.DataFrame(data_input)
        # Sauvegarde dans un CSV (ajoute à la suite)
        file_exists = os.path.isfile('dispos_jdr.csv')
        df.to_csv('dispos_jdr.csv', mode='a', index=False, header=not file_exists)
        st.success("Tes dispos ont été enregistrées !")
    else:
        st.warning("Tu n'as coché aucun jour.")

# Affichage des résultats
if st.checkbox("Voir le récapitulatif global"):
    if os.path.isfile('dispos_jdr.csv'):
        res = pd.read_csv('dispos_jdr.csv')
        st.dataframe(res)
    else:
        st.info("Aucune donnée enregistrée pour le moment.")
