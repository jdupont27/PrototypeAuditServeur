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

## 📊 Méthodologie & Tests d'Itération
Le développement a été structuré en deux phases de tests critiques :

### **Test 1 : Analyse de masse (Traitement par lots) Local**
- **Objectif :** Valider la capacité de l'agent à scanner et extraire les métriques de **25 fichiers PDF** simultanément.
- **Résultat :** Extraction réussie des indicateurs clés (PUE, consommation, localisation) malgré la charge de données, démontrant la stabilité du pipeline local.

### **Test 2 : Recherche Contextuelle & Reporting Stratégique**
- **Objectif :** Enrichir les données internes par une analyse comparative avec les standards du marché
- **Action de l'IA :** L'agent a effectué une **recherche en temps réel sur Internet** pour identifier les standards de PUE (Power Usage Effectiveness) en vigueur en **2026**.
- **Résultat :** Génération d'un rapport comparatif

## 🛠️ Architecture des Agents
1. **L'Analyste Technique :** Responsable du scan massif des 25 fichiers et de la validation des données.
2. **Le Consultant Stratégique :** Responsable de la rédaction en français, assurant la transition entre la donnée brute et la recommandation d'affaires.

#############################################################
Outils à installer

-Python 3.12
-Google Search API. Peut utiliser gratuitement une clé sur https://serper.dev/

### Exécuter en lignes de commande ###
#Créer environnement virtuel
py -m venv venv
.\venv\Scripts\activate

#Installer le modèle Ollama
ollama pull llama3.1:8b

#Installer crewai et outil pour générer fpdf
py -m pip install crewai crewai-tools fpdf

#Installer langchain-community (Outils pour crewAI)
pip install langchain-community

#Bibliothèque d'outils pour crewai
py -m pip install "crewai[tools]"

#Installer PyPDF2 pour lire du texte/pdf. (RAG en mode texte)
py -m pip install PyPDF2

#Traducteur pour que CrewAI puisse parler à LLAMA (Moteur communication)
py -m pip install litellm

#Recherche en ligne (2500 recherches gratuites)
py -m pip install google-search-results

#Outil pour Pdf
pip install crewai crewai-tools pypdf

#############################################################
#Générer des rapports pour données tests (25 fichiers tests dans le répertoire "donnees_serveurs")
python generer_rapports.py

#Test 1 : Trouver le pire Indice d'Efficacite Energetique dans les 25 rapports de serveur.
python agent_expert.py

#Test 2 : Trouver le pire et meilleur Indice d'Efficacite Energetique dans les 25 rapports de serveur
#Chercher sur internet pour le standard en 2026 et comparer avec les données locales. Afficher et crée un fichier Rapport_Analyse_Ecart.txt
#Il faut copier la clé dans le script à la première étape
python agent_expert_Comparaison.py
