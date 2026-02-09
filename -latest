import streamlit as st
import google.generativeai as genai
import os

# Configuração da Página (Título na aba do navegador)
st.set_page_config(page_title="EduAdapt Pro", page_icon="🎓", layout="wide")

# Estilização CSS para parecer com o AI Studio
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #1a73e8; color: white; font-weight: bold; }
    .stTextArea>div>div>textarea { border-radius: 10px; }
    .css-15448i9 { background-color: #ffffff; border-radius: 15px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    h1 { color: #1a73e8; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Pega a chave do Google Cloud
api_key = os.getenv("API_KEY")

# Barra Lateral (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3449/3449625.png", width=100)
    st.title("Configurações")
    st.info("Otimizado para Educação Especial (DI)")
    disciplina = st.selectbox("Selecione a Disciplina:", ["Artes", "Filosofia", "Sociologia", "Ciências", "Outra"])
    if not api_key:
        st.error("⚠️ Chave API não encontrada no Google Cloud!")

# Corpo Principal
st.title("🎓 EduAdapt Pro")
st.write("Transforme conteúdos complexos em materiais acessíveis para alunos com Deficiência Intelectual.")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Conteúdo Original")
    aula_original = st.text_area("Cole aqui o texto do livro ou da aula:", height=300, placeholder="Ex: A Noite Estrelada de Van Gogh...")

with col2:
    st.markdown("### ✨ Adaptação Pedagógica")
    if st.button("GERAR MATERIAL ADAPTADO"):
        if aula_original and api_key:
            try:
                genai.configure(api_key=api_key)
                # O Pulo do Gato: Adicionamos 'models/' antes do nome
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                
                with st.spinner('Processando adaptação...'):
                    prompt = f"""
                    Você é um especialista em Educação Especial. Adapte o conteúdo abaixo para um aluno com Deficiência Intelectual do 6º ano.
                    Regras:
                    1. Use Linguagem Simples e direta.
                    2. Crie tópicos curtos.
                    3. Destaque 1 conceito principal.
                    4. Sugira uma atividade prática para fazer com a família.
                    
                    Disciplina: {disciplina}
                    Conteúdo: {aula_original}
                    """
                    response = model.generate_content(prompt)
                    
                    st.success("Concluído!")
                    st.markdown(f"<div style='background-color: white; padding: 20px; border-radius: 10px; border: 1px solid #ddd;'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro na conexão: {e}")
        else:
            st.warning("Certifique-se de colar o conteúdo e configurar a API.")

st.markdown("---")
st.caption("EduAdapt - Tecnologia Assistiva para Professores")
