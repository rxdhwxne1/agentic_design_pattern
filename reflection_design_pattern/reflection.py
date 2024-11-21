import streamlit as st
import ollama

def ask_llama(text, question, history):
    messages = [{"role": "user", "content": f"Voici le texte : \n{text}\n\nQuestion : {question}"}]

    for entry in history:
        messages.append({"role": "user", "content": entry['question']})
        messages.append({"role": "assistant", "content": entry['response']})

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=messages
        )

        return response.get("message").get("content")
    
    except Exception as e:
        return f"Une erreur s'est produite lors de la génération de la réponse : {str(e)}"
    
def reflect_on_response(response, text, history):
    reflection_prompt = f"Voici le texte original : {text}. Réévalue la réponse suivante : {response} et corrige la si des améliorations sont nécessaires ?"
    
    messages = [{"role": "user", "content": reflection_prompt}]
    
    for entry in history:
        messages.append({"role": "user", "content": entry['question']})
        messages.append({"role": "assistant", "content": entry['reflection']})
    
    try:
        reflection = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": reflection_prompt}]
        )
        return reflection.get("message").get("content")
    
    except Exception as e:
        return f"Erreur lors de la réflexion : {str(e)}"

st.title("Interaction avec Ollama sur un Texte")

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

text_input = st.text_area("Entrez le texte :", height=150)

question_input = st.text_input("Posez votre question :")

if st.button("Poser la question"):
    with st.spinner("Génération de la réponse..."):
        if question_input:
            # Demande la réponse d'Ollama
            response = ask_llama(text_input, question_input, st.session_state.conversation_history)
            
            st.session_state.conversation_history.append({
                "question": question_input, 
                "response": response,
            })

            # Affiche les résultats
            st.subheader("Réponse d'Ollama :")
            st.write(response)
            
            if st.button("Réflexion sur la réponse"):
                reflection = reflect_on_response(response, text_input, st.session_state.conversation_history)
                
                st.session_state.conversation_history.append({
                    "reflection": reflection
                })
                st.subheader("Réflexion sur la réponse :")
                st.write(reflection)

        else:
            st.warning("Veuillez entrer une question.")

if st.session_state.conversation_history:
    st.subheader("Historique des questions et réponses :")
    for entry in st.session_state.conversation_history:
        st.write(f"**Vous :** {entry['question']}")
        st.write(f"**Ollama :** {entry['response']}")
        if 'reflection' in entry:
            st.write(f"**Réflexion :** {entry['reflection']}")
