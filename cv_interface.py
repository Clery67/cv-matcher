import streamlit as st
import pdfplumber
import docx2txt
import openai

# " Colle ici ta clé OpenAI entre guillemets
openai.api_key = "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"

def extraire_texte_fichier(uploaded_file):
    """
    Lit le PDF ou DOCX uploadé et renvoie tout le texte.
    """
    if uploaded_file.name.lower().endswith(".pdf"):
        texte = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_txt = page.extract_text()
                if page_txt:
                    texte += page_txt + "\n"
    elif uploaded_file.name.lower().endswith(".docx"):
        texte = docx2txt.process(uploaded_file)
    else:
        texte = ""
    return texte.strip()

def analyser_cahier_des_charges(texte):
    """
    Envoie le texte à l'API OpenAI pour extraire 
    poste, compétences, expérience et localisation.
    """
    prompt = f"""
    Tu es un assistant RH. Analyse ce cahier des charges et extrait :
    - Le poste ou métier ciblé
    - Les compétences clés
    - L’expérience minimale demandée (en années)
    - Les villes ou régions mentionnées

    Cahier des charges :
    {texte}

    Réponds sous forme de JSON.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content

st.set_page_config(page_title="Recherche intelligente de CV", layout="wide")
st.title("Recherche intelligente de CV")

# === 1. Upload du cahier des charges ===
st.header("1. Cahier des charges client")
uploaded_file = st.file_uploader("Déposez ici le fichier PDF ou Word", type=["pdf", "docx"])

if uploaded_file:
    # 1. Extraction du texte
    texte = extraire_texte_fichier(uploaded_file)
    st.success("Fichier chargé : " + uploaded_file.name)
    st.text_area("📄 Texte extrait", texte, height=200)

    # 2. Bouton d'analyse IA
    if st.button("🧠 Analyser automatiquement avec IA"):
        with st.spinner("Analyse en cours…"):
            resultat_ia = analyser_cahier_des_charges(texte)
        st.subheader("Résultat de l'analyse IA")
        st.code(resultat_ia, language="json")

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
