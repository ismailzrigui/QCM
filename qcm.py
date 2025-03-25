import streamlit as st
import random

# ------------------
# Questions et réponses (47 questions avec support de choix multiples)
# ------------------
questions = [
    {"question": "James utilise des ACL pour sécuriser les accès. Sur quelle couche de la défense travaille-t-il ?", "options": ["Application Layer", "Host Layer", "Internal Network Layer", "Perimeter Layer"], "answer": "Perimeter Layer", "multi": False},
    {"question": "Quel type d'attaque consiste à écouter le trafic réseau ?", "options": ["Network Sniffing", "Password Attack", "Social Engineering Attack", "Man-in-the-Middle Attack"], "answer": "Network Sniffing", "multi": False},
    {"question": "Quel dispositif permet de bloquer l'accès à certains sites web ?", "options": ["Firewall", "Internet Content Filter", "IDS", "Network Protocol Analyzer"], "answer": "Internet Content Filter", "multi": False},
    {"question": "Une communication bancaire est détournée et modifiée. Quelle est l'attaque ?", "options": ["Privilege Escalation", "DNS Poisoning", "Man-in-the-Middle Attack", "DNS Cache Poisoning"], "answer": "Man-in-the-Middle Attack", "multi": False},
    {"question": "Quels outils peuvent intercepter le trafic réseau ?", "options": ["Wireless sniffer", "Spectrum analyzer", "Protocol analyzer", "Performance Monitor"], "answer": ["Wireless sniffer", "Protocol analyzer"], "multi": True},
    {"question": "_____ est une tentative d'obtenir un accès à un réseau non autorisé.", "options": ["Network reconnaissance"], "answer": "Network reconnaissance", "multi": False},
    {"question": "Quel processus gère les incidents de sécurité ?", "options": ["Incident response", "Incident handling", "Incident management", "Incident planning"], "answer": "Incident response", "multi": False},
    {"question": "Quel système détecte un incendie ?", "options": ["Extincteurs automatiques d'incendie", "Système d'extinction d'incendie", "Système d'alarme incendie", "Extinction des incendies par gaz"], "answer": "Système d'alarme incendie", "multi": False},
    {"question": "Quel IDS analyse un hôte plutôt que le réseau ?", "options": ["IPS", "HIDS", "DMZ", "NIDS"], "answer": "HIDS", "multi": False},
    {"question": "Quelle solution attire les hackers pour les piéger ?", "options": ["Implement a strong password policy", "Implement a strong firewall", "Implement a honeypot", "Implement network based antivirus"], "answer": "Implement a honeypot", "multi": False},
    {"question": "Quel plan est destiné aux incidents cyber ?", "options": ["Cyber Incident Response Plan", "Crisis Communication Plan", "Disaster Recovery Plan", "Occupant Emergency Plan"], "answer": "Cyber Incident Response Plan", "multi": False},
    {"question": "Quelle politique concerne les mots de passe ?", "options": ["Information protection policy", "Remote access policy", "Group policy", "Password policy"], "answer": "Password policy", "multi": False},
    {"question": "L’exploitation d’une session valide est appelée ?", "options": ["Spoofing", "Smurf", "Session hijacking", "Phishing"], "answer": "Session hijacking", "multi": False},
    {"question": "Quelle politique clarifie les mesures spécifiques ?", "options": ["User policy", "IT policy", "Issue-Specific Security Policy", "Group policy"], "answer": "Issue-Specific Security Policy", "multi": False},
    {"question": "Le site __________ est une signature numérique.", "options": ["signature"], "answer": "signature", "multi": False},
    {"question": "Quel système lit les paquets et identifie les signatures ?", "options": ["HIDS", "IPS", "DMZ", "NIDS"], "answer": "NIDS", "multi": False},
    {"question": "Le responsable de la sécurité info est le __________.", "options": ["CISO"], "answer": "CISO", "multi": False},
    {"question": "Quel pare-feu garde l'état des connexions ?", "options": ["Stateful firewall", "Stateless packet filter firewall", "Circuit-level proxy firewall", "Application gateway firewall"], "answer": "Stateful firewall", "multi": False},
    {"question": "Le chiffrement __________ utilise deux clés.", "options": ["Asymmetric"], "answer": "Asymmetric", "multi": False},
    {"question": "Protocole pour synchroniser l’heure ?", "options": ["NTP"], "answer": "NTP", "multi": False},
    {"question": "Quels pare-feux suivent l’état des connexions ?", "options": ["Circuit-level gateway", "Stateful", "Proxy server", "Dynamic packet-filtering"], "answer": ["Stateful", "Dynamic packet-filtering"], "multi": True},
    {"question": "Système de détection open source ?", "options": ["Dsniff", "KisMAC", "Snort", "Kismet"], "answer": "Snort", "multi": False},
    {"question": "Pourquoi la sécurité réseau est-elle essentielle ?", "options": ["A", "B", "C", "D"], "answer": ["A", "B", "C", "D"], "multi": True},
    {"question": "Quelle politique régit l'utilisation du réseau ?", "options": ["General policy", "Remote access policy", "IT policy", "User policy"], "answer": "User policy", "multi": False},
    {"question": "Attaque par essais multiples ?", "options": ["Buffer overflow", "Brute force attack", "Zero-day attack", "Smurf attack"], "answer": "Brute force attack", "multi": False},
    {"question": "Carte de sécurité avec PIN ?", "options": ["Proximity card", "Java card", "SD card", "Smart card"], "answer": "Smart card", "multi": False},
    {"question": "Filtre Wireshark pour Hotmail ?", "options": ["(http contains 'email') && (http contains 'hotmail')"], "answer": "(http contains 'email') && (http contains 'hotmail')", "multi": False},
    {"question": "Contrôle d’acheminement de mail ?", "options": ["Email tracking"], "answer": "Email tracking", "multi": False},
    {"question": "Cyberharcèlement via faux sites ?", "options": ["La fausse accusation", "Collecte d’infos", "Encourager le harcèlement", "Fausse victimisation"], "answer": "La fausse accusation", "multi": False},
    {"question": "Organisation des noms de domaine ?", "options": ["ISO", "ICANN", "W3C", "ANSI"], "answer": "ICANN", "multi": False},
    {"question": "Analyse comportementale du trafic ?", "options": ["Network Behavior Analysis", "Network-based Intrusion Prevention", "Wireless Intrusion Prevention System", "Host-based Intrusion Prevention"], "answer": "Network Behavior Analysis", "multi": False},
    {"question": "Un site web ______ est un cookie.", "options": ["cookie"], "answer": "cookie", "multi": False},
    {"question": "Un serveur leurre les hackers. C’est ?", "options": ["Polymorphic Virus", "Virus", "Reactive IDS", "Honey Pot"], "answer": "Honey Pot", "multi": False},
    {"question": "Une politique ______ décrit la portée sécurité.", "options": ["security"], "answer": "security", "multi": False},
    {"question": "Protocole VPN le plus sûr ?", "options": ["L2TP", "IP", "PPP", "IPSec"], "answer": "IPSec", "multi": False},
    {"question": "Outil passif pour capturer le trafic ?", "options": ["Sniffer", "IDS", "IPS", "Warchalking"], "answer": "Sniffer", "multi": False},
    {"question": "Une zone DMZ est un ______.", "options": ["demilitarized zone"], "answer": "demilitarized zone", "multi": False},
    {"question": "Étape OPSEC qui identifie les indicateurs ?", "options": ["Analysis of Threats", "Analysis of Vulnerabilities", "Assessment of Risk", "Identification of Critical Information"], "answer": "Analysis of Vulnerabilities", "multi": False},
    {"question": "Attaque avec zombies ?", "options": ["Smurf attack", "Buffer-overflow attack", "DDoS attack", "Bonk attack"], "answer": "DDoS attack", "multi": False},
    {"question": "Quel mécanisme garantit la confidentialité ?", "options": ["Integrity", "Data availability", "Confidentiality", "Authentication"], "answer": "Confidentiality", "multi": False},
    {"question": "Analyse coût-bénéfice ?", "options": ["Business Continuity Planning", "Benefit-Cost Analysis", "Disaster recovery", "Cost-benefit analysis"], "answer": ["Benefit-Cost Analysis", "Cost-benefit analysis"], "multi": True},
    {"question": "Quelle approche mobile autorise le téléphone perso ?", "options": ["BYOD", "COPE", "COBO", "CYOD"], "answer": "BYOD", "multi": False},
    {"question": "Source de renseignement humain ?", "options": ["dark web and honeypots", "blogs and forums", "malware processing", "network monitoring"], "answer": "dark web and honeypots", "multi": False},
    {"question": "Empêcher exécution de code non fiable ?", "options": ["Application sandboxing", "Application whitelisting", "Application blacklisting", "Deployment of WAFS"], "answer": "Application sandboxing", "multi": False},
    {"question": "À quelle couche OSI fonctionne IPsec ?", "options": ["Session", "Application et physique", "Réseau", "Liaison de données"], "answer": "Réseau", "multi": False}
]

# Initialisation sécurisée de session_state
if 'shuffled_questions' not in st.session_state or 'user_answers' not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.user_answers = [None] * len(st.session_state.shuffled_questions)

# Application Streamlit
st.title("🛡️ QCM Cybersécurité - Choix Unique & Multiple")
st.write("Répondez aux questions ci-dessous. Certaines peuvent avoir plusieurs bonnes réponses.")

for i, q in enumerate(st.session_state.shuffled_questions):
    st.subheader(f"Question {i+1}")
    if q.get("multi", False):
        user_choice = st.multiselect(q["question"], q["options"], key=f"question_{i}")
    else:
        user_choice = st.radio(q["question"], q["options"], key=f"question_{i}")
    st.session_state.user_answers[i] = (q["question"], user_choice, q["answer"])

if st.button("Afficher le score"):
    correct = 0
    for (_, user_ans, correct_ans) in st.session_state.user_answers:
        if isinstance(correct_ans, list):
            if sorted(user_ans) == sorted(correct_ans):
                correct += 1
        else:
            if user_ans == correct_ans:
                correct += 1

    total = len(st.session_state.user_answers)
    st.success(f"🎉 Vous avez obtenu {correct} / {total} bonnes réponses.")

    with st.expander("Voir les corrections"):
        for q_text, user_ans, correct_ans in st.session_state.user_answers:
            if isinstance(correct_ans, list):
                if sorted(user_ans) == sorted(correct_ans):
                    st.write(f"✅ **{q_text}**\nVotre réponse : {user_ans}")
                else:
                    st.write(f"❌ **{q_text}**\nVotre réponse : {user_ans} | Réponse correcte : {correct_ans}")
            else:
                if user_ans == correct_ans:
                    st.write(f"✅ **{q_text}**\nVotre réponse : {user_ans}")
                else:
                    st.write(f"❌ **{q_text}**\nVotre réponse : {user_ans} | Réponse correcte : {correct_ans}")

st.info("💡 Certaines questions peuvent avoir plusieurs bonnes réponses. Lisez bien les instructions.")