import streamlit as st

st.set_page_config(page_title="Recherche intelligente de CV", layout="wide")
st.title("Recherche intelligente de CV")

# === 1. Upload du cahier des charges ===
st.header("1. Cahier des charges client")
uploaded_file = st.file_uploader("Déposez ici le fichier PDF ou Word", type=["pdf", "docx"])
if uploaded_file:
    st.success("Fichier chargé : " + uploaded_file.name)

# === 2. Filtres manuels ===
st.header("2. Filtres manuels")

# -- Spécialité (métier d’ingénierie en industrie)
specialites = [
    "Ingénieur méthodes", "Ingénieur qualité", "Ingénieur industrialisation", "Ingénieur production",
    "Chef de projet industriel", "Automaticien", "Ingénieur maintenance", "Ingénieur logistique",
    "Ingénieur électronique", "Ingénieur mécanique", "Ingénieur génie électrique", "Ingénieur sûreté",
    "Responsable HSE", "Ingénieur R&D", "Technicien supérieur", "Data engineer industriel"
]
selected_specialites = st.multiselect("Spécialités industrielles recherchées", options=specialites)

# -- Localisations / Mobilité
villes = [
    "Strasbourg", "Mulhouse", "Colmar", "Metz", "Nancy", "Epinal",
    "Belfort", "Besançon", "Montbéliard", "Haguenau", "Saint-Louis", "Saverne"
]
selected_villes = st.multiselect("Zones géographiques ciblées (mobilité)", options=villes)

# -- Expérience
experience = st.slider("Expérience minimale (en années)", 0, 20, 3)

# -- Compétences clés + logique
skills_input = st.text_input("Compétences clés (mots-clés séparés par des virgules)", "Python, API, SQL")
logic = st.radio("Mode de filtrage des mots-clés", ["AND", "OR"])

# === 3. Lancer la recherche (simulation pour l’instant) ===
if st.button("Lancer la recherche de CV"):
    st.info("Recherche lancée... (simulation)")
    st.write("**Filtres sélectionnés :**")
    st.write(f"Spécialités : {', '.join(selected_specialites)}")
    st.write(f"Zones : {', '.join(selected_villes)}")
    st.write(f"Expérience minimale : {experience} ans")
    st.write(f"Compétences clés : {skills_input} (logique : {logic})")
    
    st.subheader("Résultats simulés")
    fake_results = [
        {"nom": "Dupont J.", "exp": 5, "ville": "Strasbourg", "skills": "Python, SQL"},
        {"nom": "Martin A.", "exp": 7, "ville": "Colmar", "skills": "Python, API REST"},
    ]
    for cv in fake_results:
        st.write(f"**{cv['nom']}** - {cv['exp']} ans - {cv['ville']}")
        st.write(f"Compétences : {cv['skills']}")
        st.markdown("---")
