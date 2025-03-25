import streamlit as st
import random

# ------------------
# Questions et réponses (47 questions)
# ------------------
questions = [
    {"question": "James utilise des ACL pour sécuriser les accès. Sur quelle couche de la défense travaille-t-il ?", "options": ["Application Layer", "Host Layer", "Internal Network Layer", "Perimeter Layer"], "answer": "Perimeter Layer"},
    {"question": "Quel type d'attaque consiste à écouter le trafic réseau ?", "options": ["Network Sniffing", "Password Attack", "Social Engineering Attack", "Man-in-the-Middle Attack"], "answer": "Network Sniffing"},
    {"question": "Quel dispositif permet de bloquer l'accès à certains sites web ?", "options": ["Firewall", "Internet Content Filter", "IDS", "Network Protocol Analyzer"], "answer": "Internet Content Filter"},
    {"question": "Une communication bancaire est détournée et modifiée. Quelle est l'attaque ?", "options": ["Privilege Escalation", "DNS Poisoning", "Man-in-the-Middle Attack", "DNS Cache Poisoning"], "answer": "Man-in-the-Middle Attack"},
    {"question": "Quel outil peut intercepter et enregistrer le trafic réseau ?", "options": ["Wireless sniffer", "Spectrum analyzer", "Protocol analyzer", "Performance Monitor"], "answer": "Wireless sniffer"},
    {"question": "_____ est une tentative d'obtenir un accès à un réseau non autorisé.", "options": ["Network reconnaissance"], "answer": "Network reconnaissance"},
    {"question": "Quel processus gère les incidents de sécurité ?", "options": ["Incident response", "Incident handling", "Incident management", "Incident planning"], "answer": "Incident response"},
    {"question": "Quel système détecte un incendie ?", "options": ["Extincteurs automatiques d'incendie", "Système d'extinction d'incendie", "Système d'alarme incendie", "Extinction des incendies par gaz"], "answer": "Système d'alarme incendie"},
    {"question": "Quel IDS analyse un hôte plutôt que le réseau ?", "options": ["IPS", "HIDS", "DMZ", "NIDS"], "answer": "HIDS"},
    {"question": "Quelle solution attire les hackers pour les piéger ?", "options": ["Implement a strong password policy", "Implement a strong firewall", "Implement a honeypot", "Implement network based antivirus"], "answer": "Implement a honeypot"},
    {"question": "Quel plan est destiné aux incidents cyber ?", "options": ["Cyber Incident Response Plan", "Crisis Communication Plan", "Disaster Recovery Plan", "Occupant Emergency Plan"], "answer": "Cyber Incident Response Plan"},
    {"question": "Quelle politique concerne les mots de passe ?", "options": ["Information protection policy", "Remote access policy", "Group policy", "Password policy"], "answer": "Password policy"},
    {"question": "L’exploitation d’une session valide est appelée ?", "options": ["Spoofing", "Smurf", "Session hijacking", "Phishing"], "answer": "Session hijacking"},
    {"question": "Qu’utilisera George pour protéger son réseau sous Vista ?", "options": ["Firewall", "Antivirus", "Anti-spyware", "Windows Updates"], "answer": "Firewall"},
    {"question": "Quelle politique clarifie les mesures spécifiques ?", "options": ["User policy", "IT policy", "Issue-Specific Security Policy", "Group policy"], "answer": "Issue-Specific Security Policy"},
    {"question": "Le site __________ est une signature numérique.", "options": ["signature"], "answer": "signature"},
    {"question": "Quel système lit les paquets et identifie les signatures ?", "options": ["HIDS", "IPS", "DMZ", "NIDS"], "answer": "NIDS"},
    {"question": "Le responsable de la sécurité info est le __________.", "options": ["CISO"], "answer": "CISO"},
    {"question": "Quel pare-feu garde l'état des connexions ?", "options": ["Stateful firewall", "Stateless packet filter firewall", "Circuit-level proxy firewall", "Application gateway firewall"], "answer": "Stateful firewall"},
    {"question": "Le chiffrement __________ utilise deux clés.", "options": ["Asymmetric"], "answer": "Asymmetric"},
    {"question": "Protocole pour synchroniser l’heure ?", "options": ["NTP"], "answer": "NTP"},
    {"question": "Quels pare-feux suivent l’état des connexions ?", "options": ["Circuit-level gateway", "Stateful", "Proxy server", "Dynamic packet-filtering"], "answer": "Stateful"},
    {"question": "Système de détection open source ?", "options": ["Dsniff", "KisMAC", "Snort", "Kismet"], "answer": "Snort"},
    {"question": "Pourquoi la sécurité réseau est-elle essentielle ?", "options": ["A", "B", "C", "D"], "answer": "A"},
    {"question": "Quelle politique régit l'utilisation du réseau ?", "options": ["General policy", "Remote access policy", "IT policy", "User policy"], "answer": "User policy"},
    {"question": "Attaque par essais multiples ?", "options": ["Buffer overflow", "Brute force attack", "Zero-day attack", "Smurf attack"], "answer": "Brute force attack"},
    {"question": "Carte de sécurité avec PIN ?", "options": ["Proximity card", "Java card", "SD card", "Smart card"], "answer": "Smart card"},
    {"question": "Filtre Wireshark pour Hotmail ?", "options": ["(http contains 'email') && (http contains 'hotmail')"], "answer": "(http contains 'email') && (http contains 'hotmail')"},
    {"question": "Contrôle d’acheminement de mail ?", "options": ["Email tracking"], "answer": "Email tracking"},
    {"question": "Cyberharcèlement via faux sites ?", "options": ["La fausse accusation", "Collecte d’infos", "Encourager le harcèlement", "Fausse victimisation"], "answer": "La fausse accusation"},
    {"question": "Organisation des noms de domaine ?", "options": ["ISO", "ICANN", "W3C", "ANSI"], "answer": "ICANN"},
    {"question": "Analyse comportementale du trafic ?", "options": ["Network Behavior Analysis", "Network-based Intrusion Prevention", "Wireless Intrusion Prevention System", "Host-based Intrusion Prevention"], "answer": "Network Behavior Analysis"},
    {"question": "Un site web ______ est un cookie.", "options": ["cookie"], "answer": "cookie"},
    {"question": "Un serveur leurre les hackers. C’est ?", "options": ["Polymorphic Virus", "Virus", "Reactive IDS", "Honey Pot"], "answer": "Honey Pot"},
    {"question": "Une politique ______ décrit la portée sécurité.", "options": ["security"], "answer": "security"},
    {"question": "Protocole VPN le plus sûr ?", "options": ["L2TP", "IP", "PPP", "IPSec"], "answer": "IPSec"},
    {"question": "Outil passif pour capturer le trafic ?", "options": ["Sniffer", "IDS", "IPS", "Warchalking"], "answer": "Sniffer"},
    {"question": "Une zone DMZ est un ______.", "options": ["demilitarized zone"], "answer": "demilitarized zone"},
    {"question": "Étape OPSEC qui identifie les indicateurs ?", "options": ["Analysis of Threats", "Analysis of Vulnerabilities", "Assessment of Risk", "Identification of Critical Information"], "answer": "Analysis of Vulnerabilities"},
    {"question": "Attaque avec zombies ?", "options": ["Smurf attack", "Buffer-overflow attack", "DDoS attack", "Bonk attack"], "answer": "DDoS attack"},
    {"question": "Quel mécanisme garantit la confidentialité ?", "options": ["Integrity", "Data availability", "Confidentiality", "Authentication"], "answer": "Confidentiality"},
    {"question": "Analyse coût-bénéfice ?", "options": ["Business Continuity Planning", "Benefit-Cost Analysis", "Disaster recovery", "Cost-benefit analysis"], "answer": "Cost-benefit analysis"},
    {"question": "Quelle approche mobile autorise le téléphone perso ?", "options": ["BYOD", "COPE", "COBO", "CYOD"], "answer": "BYOD"},
    {"question": "Source de renseignement humain ?", "options": ["dark web and honeypots"], "answer": "dark web and honeypots"},
    {"question": "Empêcher exécution de code non fiable ?", "options": ["Application sandboxing", "Application whitelisting", "Application blacklisting", "Deployment of WAFS"], "answer": "Application sandboxing"},
    {"question": "À quelle couche OSI fonctionne IPsec ?", "options": ["Session", "Application et physique", "Réseau", "Liaison de données"], "answer": "Réseau"}
]

# Initialisation sécurisée
if 'shuffled_questions' not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.user_answers = [None] * len(questions)

# Application Streamlit
st.title("🛡️ QCM Sécurité réseaux")
st.write("Répondez aux questions ci-dessous :")

for i, q in enumerate(st.session_state.shuffled_questions):
    st.subheader(f"Question {i+1}")
    user_choice = st.radio(q["question"], q["options"], key=f"question_{i}")
    st.session_state.user_answers[i] = (q["question"], user_choice, q["answer"])

if st.button("Afficher le score"):
    correct = sum(1 for (_, user_ans, correct_ans) in st.session_state.user_answers if user_ans == correct_ans)
    total = len(st.session_state.user_answers)
    st.success(f"🎉 Vous avez obtenu {correct} / {total} bonnes réponses.")

    with st.expander("Voir les corrections"):
        for q, user_ans, correct_ans in st.session_state.user_answers:
            if user_ans == correct_ans:
                st.write(f"✅ **{q}**\nVotre réponse : {user_ans}")
            else:
                st.write(f"❌ **{q}**\nVotre réponse : {user_ans} | Réponse correcte : {correct_ans}")

st.info("💡 Vous pouvez relancer la page pour refaire un test avec un nouvel ordre aléatoire.")