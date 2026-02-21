import os
from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool # <-- IMPORTANT : On utilise le décorateur de CrewAI, pas LangChain
from PyPDF2 import PdfReader

# 1. Configuration du LLM Local
local_llm = LLM(model="ollama/llama3.1", base_url="http://localhost:11434")

# 2. Création des outils avec le décorateur de CrewAI
@tool("lister_fichiers")
def lister_fichiers(dossier: str):
    """Liste tous les fichiers présents dans un dossier donné."""
    try:
        return os.listdir(dossier)
    except Exception as e:
        return f"Erreur : {str(e)}"

@tool("lire_contenu_pdf")
def lire_contenu_pdf(nom_fichier: str):
    """Lit le texte d'un fichier PDF spécifique dans le dossier donnees_serveurs."""
    # On s'assure que le chemin est correct même si l'IA oublie le nom du dossier
    if not nom_fichier.startswith("donnees_serveurs"):
        chemin = os.path.join("donnees_serveurs", nom_fichier)
    else:
        chemin = nom_fichier
        
    try:
        reader = PdfReader(chemin)
        texte = ""
        for page in reader.pages:
            texte += page.extract_text()
        return texte
    except Exception as e:
        return f"Erreur lors de la lecture du fichier {nom_fichier} : {str(e)}"

# 3. L'Agent
analyste = Agent(
    role='Expert Performance',
    goal='Extraire les scores PUE des rapports et trouver le pire.',
    backstory='Tu es un ingenieur systeme qui analyse des rapports PDF locaux.',
    tools=[lister_fichiers, lire_contenu_pdf],
    llm=local_llm,
    verbose=True,
    allow_delegation=False
)

mission = Task(
    description='''
    INTERDICTION : N'utilise QUE les outils 'lister_fichiers' et 'lire_contenu_pdf'. 
    N'invente aucun autre outil.

    PROCÉDURE STRICTE :
    1. Utilise 'lister_fichiers' sur le dossier 'donnees_serveurs'.
    2. Pour chaque fichier trouvé, utilise 'lire_contenu_pdf'.
    3. Lis le texte retourné, trouve manuellement le chiffre après 'PUE' et le nom de la ville.
    4. Garde en mémoire le pire score.
    ''',
    expected_output="Un rapport final indiquant : 'Le pire PUE est de [X] à [Ville], trouvé dans le fichier [Nom]'.",
    agent=analyste
)

crew = Crew(agents=[analyste], tasks=[mission])
print("\n🚀 Analyse en cours...")
print(crew.kickoff())

