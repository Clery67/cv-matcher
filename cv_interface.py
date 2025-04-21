import streamlit as st

st.title("Recherche intelligente de CV")

# === 1. Upload du cahier des charges ===
st.header("Cahier des charges client")
uploaded_file = st.file_uploader("Déposez ici le fichier PDF ou Word", type=["pdf", "docx"])
if uploaded_file:
    st.success("Fichier chargé : " + uploaded_file.name)

# === 2. Filtres manuels ===
st.header("Filtres manuels")
col1, col2 = st.columns(2)
with col1:
    location = st.text_input("Localisation souhaitée", "Strasbourg")
    mobility = st.selectbox("Mobilité du candidat", ["Peu mobile", "Mobile en région", "Nationalement mobile"])
with col2:
    experience = st.slider("Expérience minimale (en années)", 0, 20, 3)
    domain = st.text_input("Domaine d'activité", "Informatique / Développement")
skills = st.text_input("Compétences clés (séparées par des virgules)", "Python, API, SQL")

# === 3. Lancer la recherche (simulation) ===
if st.button("Lancer la recherche de CV"):
    st.info("Recherche lancée... (simulation)")
    fake_results = [
        {"nom": "Dupont J.", "exp": 5, "ville": "Strasbourg", "skills": "Python, SQL"},
        {"nom": "Martin A.", "exp": 7, "ville": "Colmar", "skills": "Python, API REST"},
    ]
    st.subheader("Résultats trouvés")
    for cv in fake_results:
        st.write(f"**{cv['nom']}** - {cv['exp']} ans - {cv['ville']}")
        st.write(f"Compétences : {cv['skills']}")
        st.markdown("---")
