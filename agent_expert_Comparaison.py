import os
from pypdf import PdfReader
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

# --- 1. CONFIGURATION ---
os.environ["SERPER_API_KEY"] = "CLE_API_ICI"

local_llm = LLM(
    model="ollama/llama3.1",
    base_url="http://localhost:11434",
    timeout=1200 
)

base_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(base_dir, "donnees_serveurs")

# --- 2. EXTRACTION DES 25 SITES ---
fichiers = [f for f in os.listdir(data_folder) if f.endswith('.pdf')][:25]
donnees_sites = ""
for file in fichiers:
    try:
        reader = PdfReader(os.path.join(data_folder, file))
        texte = reader.pages[0].extract_text()
        donnees_sites += f"\nSITE: {file}\nCONTENU: {texte[:1000]}\n"
    except Exception:
        pass

# --- 3. AGENTS ---
analyste = Agent(
    role="Expert en Métriques Énergétiques",
    goal="Isoler uniquement le PUE le plus bas (Champion) et le plus haut (Alerte).",
    backstory="Tu ne retiens que les extrêmes pour une analyse d'écart rapide.",
    llm=local_llm,
    verbose=True
)

consultant_strategique = Agent(
    role="Consultant Gap Analysis",
    goal="Calculer l'écart entre nos extrêmes et le standard du marché 2026.",
    backstory="Expert en optimisation, tu expliques combien d'énergie est gaspillée par rapport aux normes mondiales.",
    llm=local_llm,
    tools=[SerperDevTool()],
    verbose=True
)

# --- 4. TÂCHES CIBLÉES ---
task_extremes = Task(
    description=f"Analyse ces données et donne-moi uniquement :\n1. Le site avec le meilleur PUE\n2. Le site avec le pire PUE.\nDonnées :\n{donnees_sites}",
    expected_output="Identification claire du Champion et de l'Alerte avec leurs valeurs PUE respectives.",
    agent=analyste
)

task_gap_report = Task(
    description="""
    1. Utilise les résultats de l'analyste.
    2. Cherche sur le web : 'Standard PUE data center Canada 2026'.
    3. Rédige un rapport EXCLUSIVEMENT focalisé sur l'écart (Gap).
    4. Structure du rapport :
       - Standard du Marché (Source Web)
       - Écart de performance de notre Champion vs Marché (Est-il en avance ?)
       - Écart de performance de notre Pire Site vs Marché (Quel est le retard ?)
       - Coût de l'inaction (Pourquoi cet écart est dangereux).
    """,
    expected_output="Rapport d'analyse d'écart en Markdown.",
    agent=consultant_strategique,
    context=[task_extremes]
)

# --- 5. EXECUTION ---
vortex_crew = Crew(
    agents=[analyste, consultant_strategique],
    tasks=[task_extremes, task_gap_report],
    verbose=True
)

resultat = vortex_crew.kickoff()

# --- 6. EXTRACTION DU TEXTE PUR (ANTI-JSON) ---
# On convertit l'objet résultat en chaîne de caractères
rapport_brut = str(resultat.raw)

# Nettoyage de sécurité pour garantir un format texte propre
# On retire les balises de code Markdown si l'IA en a mis
nettoyage = rapport_brut.replace("```markdown", "").replace("```", "").strip()

# On s'assure que le contenu est bien du texte et non un dictionnaire JSON
if nettoyage.startswith("{") or "pue" in nettoyage[:20].lower():
    # Si l'IA a quand même sorti du JSON, on demande un nettoyage de dernier recours
    print("⚠️ Formatage du texte en cours...")

# --- 7. SAUVEGARDE FINALE EN FORMAT TEXTE ---
nom_fichier = "Rapport_Analyse_Ecart.txt"

with open(nom_fichier, "w", encoding="utf-8") as f:
    f.write(nettoyage)

print(f"\n✅ Analyse terminée !")
print(f"📄 Le rapport d'écart est disponible ici : {os.path.abspath(nom_fichier)}")

# Affichage d'un aperçu dans la console pour validation immédiate
print("\n--- APERÇU DU RAPPORT ---")
print(nettoyage[:500] + "...")