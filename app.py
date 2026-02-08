import streamlit as st
import google.generativeai as genai

# Configuração visual
st.set_page_config(page_title="EduAdapt", page_icon="🎓")

st.title("🎓 EduAdapt")
st.markdown("### Ferramenta de Inclusão Pedagógica")
st.info("Bem-vindo, Professor! Use esta ferramenta para adaptar seus materiais.")

# Barra lateral para configurações
with st.sidebar:
    st.header("Configuração")
    api_key = st.text_input("Insira sua Chave API:", type="password")
    modelo = st.selectbox("Modelo de IA:", ["gemini-1.5-flash"])

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(modelo)

        # Interface Principal
        st.write("---")
        materia = st.text_input("Qual a matéria? (Ex: Filosofia, Artes, Sociologia)")
        conteudo = st.text_area("Cole aqui o conteúdo original da aula:", height=250)

        if st.button("✨ Adaptar Material"):
            if conteudo:
                with st.spinner('A IA está simplificando o material...'):
                    prompt = f"Adapte o seguinte conteúdo de {materia} para um aluno com deficiência intelectual. Use linguagem clara, tópicos e foque nos pontos centrais: {conteudo}"
                    response = model.generate_content(prompt)
                    st.success("Material Adaptado com Sucesso!")
                    st.markdown(response.text)
            else:
                st.warning("Por favor, insira o conteúdo da aula.")
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
else:
    st.warning("👈 Por favor, insira sua Chave API na barra lateral para começar.")
