import streamlit as st
import random

# ------------------
# Questions et réponses
# ------------------
questions = [
    {
        "question": "James utilise des ACL pour sécuriser les accès. Sur quelle couche de la défense travaille-t-il ?",
        "options": ["Application Layer", "Host Layer", "Internal Network Layer", "Perimeter Layer"],
        "answer": "Perimeter Layer"
    },
    {
        "question": "Quel type d'attaque consiste à écouter le trafic réseau ?",
        "options": ["Network Sniffing", "Password Attack", "Social Engineering", "Man-in-the-Middle"],
        "answer": "Network Sniffing"
    },
    {
        "question": "Quel dispositif permet de bloquer l'accès à certains sites web ?",
        "options": ["Firewall", "Internet Content Filter", "IDS", "Protocol Analyzer"],
        "answer": "Internet Content Filter"
    },
    {
        "question": "Quelle attaque modifie la communication entre deux parties à leur insu ?",
        "options": ["Privilege Escalation", "DNS Poisoning", "Man-in-the-Middle Attack", "DNS Cache Poisoning"],
        "answer": "Man-in-the-Middle Attack"
    },
    {
        "question": "Quel système détecte les attaques à l'intérieur d’un hôte ?",
        "options": ["IPS", "HIDS", "DMZ", "NIDS"],
        "answer": "HIDS"
    },
    {
        "question": "Quel protocole VPN offre le plus haut niveau de sécurité ?",
        "options": ["L2TP", "IP", "PPP", "IPSec"],
        "answer": "IPSec"
    },
    {
        "question": "Quelle politique encourage l’usage de mots de passe forts ?",
        "options": ["Information protection policy", "Remote access policy", "Group policy", "Password policy"],
        "answer": "Password policy"
    },
    {
        "question": "Qu’est-ce qu’un cookie ?",
        "options": ["Une attaque", "Un malware", "Un bloc de données", "Un antivirus"],
        "answer": "Un bloc de données"
    },
    {
        "question": "Quelle carte est utilisée pour authentifier un utilisateur ?",
        "options": ["Proximity card", "Java card", "SD card", "Smart card"],
        "answer": "Smart card"
    },
    {
        "question": "Qui gère les noms de domaine et adresses IP ?",
        "options": ["ISO", "ICANN", "W3C", "ANSI"],
        "answer": "ICANN"
    }
]

random.shuffle(questions)

# ------------------
# Application Streamlit
# ------------------
st.title("🛡️ QCM Cybersécurité")
st.write("Répondez aux questions ci-dessous :")

score = 0
user_answers = []

for i, q in enumerate(questions):
    st.subheader(f"Question {i+1}")
    user_choice = st.radio(q["question"], q["options"], key=i)
    user_answers.append((q["question"], user_choice, q["answer"]))

if st.button("Afficher le score"):
    correct = sum(1 for (_, user_ans, correct_ans) in user_answers if user_ans == correct_ans)
    total = len(user_answers)
    st.success(f"🎉 Vous avez obtenu {correct} / {total} bonnes réponses.")

    with st.expander("Voir les corrections"):
        for q, user_ans, correct_ans in user_answers:
            if user_ans == correct_ans:
                st.write(f"✅ **{q}**\nVotre réponse : {user_ans}")
            else:
                st.write(f"❌ **{q}**\nVotre réponse : {user_ans} | Réponse correcte : {correct_ans}")

st.info("Créez votre propre quiz ou ajoutez plus de questions pour vous entraîner davantage !")
