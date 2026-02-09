import streamlit as st
import google.generativeai as genai
import os

# Pega a chave que você configurou no Google Cloud
api_key = os.getenv("API_KEY")

st.set_page_config(page_title="EduAdapt", page_icon="🎓")

st.title("🎓 EduAdapt")
st.subheader("Inclusão Pedagógica com IA")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.write("---")
    materia = st.text_input("Disciplina (Ex: Artes, Filosofia):")
    conteudo_original = st.text_area("Cole o conteúdo da aula aqui:", height=250)

    if st.button("✨ Adaptar Material"):
        if conteudo_original:
            with st.spinner('Simplificando para o aluno...'):
                prompt = f"Adapte para um aluno com deficiência intelectual (6º ano), usando linguagem simples e direta. Matéria: {materia}. Conteúdo: {conteudo_original}"
                response = model.generate_content(prompt)
                st.success("Material pronto!")
                st.markdown(response.text)
        else:
            st.warning("Por favor, cole um conteúdo primeiro.")
else:
    st.error("Erro: Chave API não encontrada. Verifique as variáveis no Google Cloud.")
