# 🌪️ Prototype d'Audit Énergétique Agentique

## 📌 Présentation du Projet
Ce projet est un prototype d'intelligence artificielle conçu pour automatiser l'analyse de performance énergétique (PUE) à grande échelle.
Il démontre comment des agents autonomes peuvent traiter des volumes de données techniques pour en extraire une vision stratégique.

Objectif : Automatiser l'audit énergétique de 25 centres de données (data centers) à partir de rapports PDF bruts.
Fonctionnement : Une équipe d'IA (Agents) extrait les indicateurs de performance, principalement le PUE (Power Usage Effectiveness) et la localisation.
Analyse d'Écart (Gap Analysis) : Le système identifie le "Champion" (meilleur site) et l'"Alerte" (pire site) pour les comparer aux standards mondiaux prévus pour 2026.
Valeur ajoutée : Transformer une pile de documents techniques indigestes en un rapport stratégique clair qui identifie immédiatement où les investissements d'optimisation sont nécessaires pour rester compétitif.

## 🚀 Technologies utilisées
- **Framework :** CrewAI (Orchestration d'agents)
- **Modèle :** Llama 3.1 via Ollama (Inférence locale)
- **Hardware :** GPU RTX 3070 & CPU Ryzen 9 9950X. 128gig DDR5.
- **Langage :** Python (Outils sur mesure pour le parsing et le reporting)


🛠️ Prérequis et Installation
1. Environnement
Python : version 3.12+

Modèle local : Ollama installé et configuré.

Recherche Web : Clé d'API gratuite sur Serper.dev.

2. Configuration de l'environnement
Exécutez les commandes suivantes dans votre terminal :

Bash
# Création et activation de l'environnement virtuel
python -m venv venv
.\venv\Scripts\activate

# Installation du modèle Llama 3.1 (8b)
ollama pull llama3.1

# Installation des bibliothèques CrewAI et outils de génération
pip install crewai crewai-tools fpdf

# Installation des outils de communication et de recherche
pip install langchain-community litellm google-search-results

# Installation des outils de traitement PDF (RAG)
pip install PyPDF2 pypdf
📂 Préparation des données
Avant de lancer les analyses, assurez-vous d'avoir vos fichiers sources :

Créez un dossier nommé donnees_serveurs/ à la racine du projet.

Placez vos 25 fichiers PDF de tests à l'intérieur.

🚀 Utilisation (Lignes de commande)
Étape 0 : Initialisation des données
Générez les rapports pour les données de tests (si nécessaire) :

Bash
python generer_rapports.py
Étape 1 : Analyse simple (Trouver le pire PUE)
Exécutez le premier test pour identifier le site le moins performant énergétiquement :

Bash
python agent_expert.py
Étape 2 : Analyse d'écart (Gap Analysis) et Benchmark 2026
Ce test identifie le meilleur et le pire site, effectue une recherche en ligne pour trouver les standards de 2026, et génère un rapport comparatif :

Note : Assurez-vous d'avoir inséré votre clé Serper dans le script.

Bash
python agent_expert_Comparaison.py
📊 Résultats attendus
À la fin de l'exécution du Test 2, le système génère un fichier :

Rapport_Analyse_Ecart.txt : Un rapport narratif en français détaillant l'écart de performance entre vos infrastructures locales et le marché mondial.
