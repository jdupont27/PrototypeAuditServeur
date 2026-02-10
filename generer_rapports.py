import os
from fpdf import FPDF
import random

# 1. Configuration et création du dossier
output_dir = "donnees_serveurs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

villes = ["Montreal", "Quebec", "Laval", "Sherbrooke", "Gatineau", "Trois-Rivieres"]
# Note : J'ai remplacé "Nœud" par "Unite" pour éviter l'erreur Unicode
types_serveurs = ["Lame de calcul Haute-Densite", "Stockage NVMe Array", "Unite d'inference IA"]
technologies = ["Refroidissement liquide", "Ventilation forcee", "Immersion thermique"]

print(f"🚀 Debut de la generation de 25 rapports dans '{output_dir}'...")

# 2. Boucle de génération
for i in range(1, 26):
    pdf = FPDF()
    pdf.add_page()
    
    # En-tête (Arial standard supporte mal les caractères spéciaux sans config)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Rapport d'Audit Technique #2026-X{i:03d}", ln=True, align='C')
    pdf.ln(10)
    
    ville = random.choice(villes)
    serveur = random.choice(types_serveurs)
    tech = random.choice(technologies)
    pue = round(random.uniform(1.1, 1.9), 2)
    uptime = round(random.uniform(99.1, 99.99), 2)
    charge_cpu = random.randint(40, 95)

    # Corps du rapport
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, txt="1. Informations Generales", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 10, txt=f"Localisation : {ville}", ln=True)
    pdf.cell(0, 10, txt=f"Infrastructure : {serveur}", ln=True)
    pdf.cell(0, 10, txt=f"Refroidissement : {tech}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, txt="2. Metriques de Performance", ln=True)
    pdf.set_font("Arial", size=11)
    
    # On évite les caractères spéciaux comme "œ" ou "—" ici
    content = (
        f"- Indice d'Efficacite Energetique (PUE) : {pue}\n"
        f"- Taux de disponibilite (Uptime) : {uptime}%\n"
        f"- Charge moyenne des processeurs : {charge_cpu}%\n"
        "- Latence reseau inter-unites : 2.4ms"
    )
    pdf.multi_cell(0, 10, txt=content)
    pdf.ln(5)

    # Conclusion
    pdf.set_font("Arial", 'I', 10)
    observation = "Performance optimale." if pue < 1.4 else "Avertissement : Consommation elevee."
    pdf.multi_cell(0, 10, txt=f"Observation : {observation} Document interne.")

    # Sauvegarde
    pdf.output(f"{output_dir}/audit_{i}.pdf")

print(f"✅ Termine ! 25 fichiers PDF generes avec succes.")