import streamlit as st
import random

# ------------------
# Questions et réponses (47 questions avec support de choix multiples)
# ------------------
questions = [
    {"question": "James, administrateur de réseau dans une grande entreprise informatique basée aux États-Unis, a été chargé d'auditer et de mettre en œuvre des contrôles de sécurité sur toutes les couches du réseau. Il a mis en place des listes noires et des listes blanches d'ACL. Sur quelle couche de l'architecture de défense en profondeur travaille-t-il ?", "options": ["Application Layer", "Host Layer", "Internal Network Layer", "Perimeter Layer"], "answer": "Perimeter Layer", "multi": False},
    {"question": "Un employé s'est connecté à un port ouvert du réseau d'une entreprise et a capturé des e-mails confidentiels. Quelle attaque a-t-il effectuée ?", "options": ["Network Sniffing", "Password Attack", "Social Engineering Attack", "Man-in-the-Middle Attack"], "answer": "Network Sniffing", "multi": False},
    {"question": "Quel dispositif de sécurité réseau permet de bloquer certains sites web comme les réseaux sociaux et les sites de streaming ?", "options": ["Firewall", "Internet Content Filter", "IDS", "Network Protocol Analyzer"], "answer": "Internet Content Filter", "multi": False},
    {"question": "Une station malveillante a intercepté une communication bancaire et modifié le numéro de compte. De quelle attaque s'agit-il ?", "options": ["Privilege Escalation", "DNS Poisoning", "Man-in-the-Middle Attack", "DNS Cache Poisoning"], "answer": "Man-in-the-Middle Attack", "multi": False},
    {"question": "Quels outils peuvent analyser le trafic réseau pour retracer des transactions spécifiques et enregistrer le trafic ?", "options": ["Wireless sniffer", "Spectrum analyzer", "Protocol analyzer", "Performance Monitor"], "answer": ["Wireless sniffer", "Protocol analyzer"], "multi": True},
    {"question": "_____ est généralement le fait d'un attaquant distant qui tente d'obtenir des informations ou d'accéder à un réseau sur lequel il n'est pas autorisé.", "options": ["Network reconnaissance"], "answer": "Network reconnaissance", "multi": False},
    {"question": "Quel processus permet de détecter, analyser et résoudre les incidents de sécurité ?", "options": ["Incident response", "Incident handling", "Incident management", "Incident planning"], "answer": "Incident response", "multi": False},
    {"question": "Quel système est conçu pour détecter la présence d'un incendie en surveillant les changements environnementaux ?", "options": ["Extincteurs automatiques d'incendie", "Système d'extinction d'incendie", "Système d'alarme incendie", "Extinction des incendies par gaz"], "answer": "Système d'alarme incendie", "multi": False},
    {"question": "Quel système de détection d'intrusion analyse les éléments internes d’un hôte ?", "options": ["IPS", "HIDS", "DMZ", "NIDS"], "answer": "HIDS", "multi": False},
    {"question": "Quelle solution attire les pirates pour les piéger ?", "options": ["Implement a strong password policy", "Implement a strong firewall", "Implement a honeypot", "Implement network based antivirus"], "answer": "Implement a honeypot", "multi": False},
    {"question": "Quel plan traite les incidents de cybersécurité comme l'accès non autorisé ou les attaques DoS ?", "options": ["Cyber Incident Response Plan", "Crisis Communication Plan", "Disaster Recovery Plan", "Occupant Emergency Plan"], "answer": "Cyber Incident Response Plan", "multi": False},
    {"question": "Quelle politique impose l'utilisation de mots de passe forts et sécurisés ?", "options": ["Information protection policy", "Remote access policy", "Group policy", "Password policy"], "answer": "Password policy", "multi": False},
    {"question": "Exploiter une session informatique valide pour un accès non autorisé est appelé ?", "options": ["Spoofing", "Smurf", "Session hijacking", "Phishing"], "answer": "Session hijacking", "multi": False},
    {"question": "Quelle politique sert à détailler les mesures spécifiques de sécurité ?", "options": ["User policy", "IT policy", "Issue-Specific Security Policy", "Group policy"], "answer": "Issue-Specific Security Policy", "multi": False},
    {"question": "Le site _____________ est une technique d'authentification de documents numériques utilisant la cryptographie informatique.", "options": ["signature"], "answer": "signature", "multi": False},
    {"question": "Quel système lit les paquets entrants et identifie les signatures ou règles suspectes ?", "options": ["HIDS", "IPS", "DMZ", "NIDS"], "answer": "NIDS", "multi": False},
    {"question": "Le responsable principal de la sécurité de l'information dans une organisation est le ____________.", "options": ["CISO"], "answer": "CISO", "multi": False},
    {"question": "Quel pare-feu garde la trace de l'état des connexions réseau ?", "options": ["Stateful firewall", "Stateless packet filter firewall", "Circuit-level proxy firewall", "Application gateway firewall"], "answer": "Stateful firewall", "multi": False},
    {"question": "Le chiffrement _____________ utilise deux clés (publique et privée).", "options": ["Asymmetric"], "answer": "Asymmetric", "multi": False},
    {"question": "Quel protocole est utilisé pour synchroniser l'heure sur un réseau ?", "options": ["NTP"], "answer": "NTP", "multi": False}
]

questions += [
    {"question": "Quels pare-feux suivent l’état des connexions actives et déterminent les paquets autorisés à entrer ?", "options": ["Circuit-level gateway", "Stateful", "Proxy server", "Dynamic packet-filtering"], "answer": ["Stateful", "Dynamic packet-filtering"], "multi": True},
    {"question": "Quel outil open source fonctionne comme un renifleur de réseau et détecte les intrusions par signature ?", "options": ["Dsniff", "KisMAC", "Snort", "Kismet"], "answer": "Snort", "multi": False},
    {"question": "Pourquoi la sécurité réseau est-elle nécessaire ?", "options": ["To protect information from loss and deliver it to its destination properly", "To protect information from unwanted editing, accidentally or intentionally by unauthorized users", "To protect private information on the Internet", "To prevent a user from sending a message to another user with the name of a third person"], "answer": ["To protect information from loss and deliver it to its destination properly", "To protect information from unwanted editing, accidentally or intentionally by unauthorized users", "To protect private information on the Internet", "To prevent a user from sending a message to another user with the name of a third person"], "multi": True},
    {"question": "Quelle politique définit ce que les utilisateurs peuvent et doivent faire pour utiliser les ressources informatiques de l'organisation ?", "options": ["General policy", "Remote access policy", "IT policy", "User policy"], "answer": "User policy", "multi": False},
    {"question": "Quelle attaque utilise un logiciel pour tester de nombreuses combinaisons de mots de passe ?", "options": ["Buffer overflow", "Brute force attack", "Zero-day attack", "Smurf attack"], "answer": "Brute force attack", "multi": False},
    {"question": "Quel dispositif, de la taille d'une carte de crédit, stocke des informations personnelles et s'utilise avec un code PIN ?", "options": ["Proximity card", "Java card", "SD card", "Smart card"], "answer": "Smart card", "multi": False},
    {"question": "Quel filtre Wireshark permet de voir les paquets contenant des e-mails Hotmail ?", "options": ["(http = \"login.pass.com\") && (http contains \"SMTP\")", "(http contains \"email\") && (http contains \"hotmail\")", "(http contains \"hotmail\") && (http contains \"Reply-To\")", "(http = \"login.passport.com\") && (http contains \"POP3\")"], "answer": "(http contains \"email\") && (http contains \"hotmail\")", "multi": False},
    {"question": "__________ est une méthode permettant de contrôler l'acheminement du courrier électronique.", "options": ["Email tracking"], "answer": "Email tracking", "multi": False},
    {"question": "Quel type de cyberharcèlement implique la création de faux sites web ou blogs contre une personne ?", "options": ["La fausse accusation", "Tentatives de collecte d'informations sur la victime", "Encourager d'autres personnes à harceler la victime", "Fausse victimisation"], "answer": "La fausse accusation", "multi": False},
    {"question": "Quelle organisation gère l’attribution des noms de domaine et adresses IP ?", "options": ["ISO", "ICANN", "W3C", "ANSI"], "answer": "ICANN", "multi": False},
    {"question": "Quelle technologie détecte les anomalies dans les flux de trafic réseau, telles que les attaques DDoS ?", "options": ["Network Behavior Analysis", "Network-based Intrusion Prevention", "Wireless Intrusion Prevention System", "Host-based Intrusion Prevention"], "answer": "Network Behavior Analysis", "multi": False},
    {"question": "Un site web __________ est un bloc de données stocké sur le client par un serveur web.", "options": ["cookie"], "answer": "cookie", "multi": False},
    {"question": "Une machine non utilisée simule un serveur de base de données pour piéger les pirates. De quoi s'agit-il ?", "options": ["A Polymorphic Virus", "A Virus", "A reactive IDS", "A Honey Pot"], "answer": "A Honey Pot", "multi": False},
    {"question": "Une politique __________ décrit la portée des exigences de sécurité d'une organisation.", "options": ["security"], "answer": "security", "multi": False},
    {"question": "Quel protocole offre le plus haut niveau de sécurité VPN ?", "options": ["L2TP", "IP", "PPP", "IPSec"], "answer": "IPSec", "multi": False},
    {"question": "Quel logiciel est utilisé dans les attaques passives pour capturer le trafic réseau ?", "options": ["Sniffer", "Intrusion detection system", "Intrusion prevention system", "Warchalking"], "answer": "Sniffer", "multi": False},
    {"question": "Un site __________ est un sous-réseau logique ou physique ajoutant une couche de sécurité au LAN.", "options": ["demilitarized zone"], "answer": "demilitarized zone", "multi": False},
    {"question": "Quelle étape du processus OPSEC analyse les indicateurs qui pourraient révéler des informations critiques ?", "options": ["Analysis of Threats", "Analysis of Vulnerabilities", "Assessment of Risk", "Identification of Critical Information", "Application of Appropriate OPSEC Measures"], "answer": "Analysis of Vulnerabilities", "multi": False},
    {"question": "Quelle attaque utilise des zombies pour envoyer du trafic malveillant ?", "options": ["Smurf attack", "Buffer-overflow attack", "DDoS attack", "Bonk attack"], "answer": "DDoS attack", "multi": False},
    {"question": "Quel mécanisme garantit que seuls les destinataires autorisés peuvent lire les données ?", "options": ["Integrity", "Data availability", "Confidentiality", "Authentication"], "answer": "Confidentiality", "multi": False},
    {"question": "Quelles méthodes permettent d’évaluer si un projet vaut la peine selon le rapport coût/bénéfice ?", "options": ["Business Continuity Planning", "Benefit-Cost Analysis", "Disaster recovery", "Cost-benefit analysis"], "answer": ["Benefit-Cost Analysis", "Cost-benefit analysis"], "multi": True},
    {"question": "Quelle politique mobile permet aux employés d'utiliser leurs appareils personnels pour le travail ?", "options": ["BYOD", "COPE", "COBO", "CYOD"], "answer": "BYOD", "multi": False},
    {"question": "Comment obtenir des informations sur les menaces via le renseignement humain ?", "options": ["By extracting information from security blogs and forums", "By discovering vulnerabilities through exploration, understanding malware behavior through malware processing, etc.", "From the data of past incidents and network monitoring", "From attackers through the dark web and honeypots"], "answer": "From attackers through the dark web and honeypots", "multi": False},
    {"question": "Quel mécanisme empêche l’exécution de code non fiable ou non vérifié ?", "options": ["Application sandboxing", "Application whitelisting", "Application blacklisting", "Deployment of WAFS"], "answer": "Application sandboxing", "multi": False},
    {"question": "Sur quelle couche OSI fonctionne IPsec ?", "options": ["The session layer", "The application and physical layers", "The network layer", "The data link layer"], "answer": "The network layer", "multi": False},
    {"question": "Quel dispositif peut être utilisé pour bloquer les sites web indésirables sur le réseau ?", "options": ["Firewall", "Network Protocol Analyzer", "Internet Content Filter", "Proxy server"], "answer": "Internet Content Filter", "multi": False},
    {"question": "Quel mode de déploiement d’IDS/IDPS permet de détecter ET bloquer le trafic malveillant ?", "options": ["promiscuous mode", "passive mode", "firewall mode", "inline mode"], "answer": "inline mode", "multi": False}
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