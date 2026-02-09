import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração visual do App (Layout)
st.set_page_config(page_title="EduAdapt", page_icon="🎓", layout="wide")

# 2. Pega a chave que você colocou no Google Cloud
api_key = os.getenv("API_KEY")

st.title("🎓 EduAdapt Pro")
st.write("Ferramenta de inclusão para alunos com Deficiência Intelectual.")

if api_key:
    try:
        # Configura a conexão com a IA
        genai.configure(api_key=api_key)
        
        # --- ESSA É A PARTE 2 QUE MUDAMOS ---
        # Testaremos sem o "models/". Se der erro, tentaremos 'gemini-1.5-flash-latest'
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Conteúdo Original")
            texto_aula = st.text_area("Cole a aula aqui:", height=300)

        with col2:
            st.subheader("Adaptação")
            if st.button("✨ ADAPTAR AGORA"):
                if texto_aula:
                    with st.spinner('A IA está simplificando o texto...'):
                        prompt = f"Adapte o seguinte conteúdo para um aluno com DI (6º ano), use frases curtas e tópicos: {texto_aula}"
                        response = model.generate_content(prompt)
                        st.markdown(f"<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>{response.text}</div>", unsafe_allow_html=True)
                else:
                    st.warning("Por favor, insira o conteúdo da aula.")

    except Exception as e:
        st.error(f"Ocorreu um erro técnico: {e}")
else:
    st.error("Chave API não configurada no Google Cloud.")
