import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="EduAdapt - Materiais Adaptados", layout="wide")

# Título do seu projeto
st.title("🎨 EduAdapt: Inclusão na Prática")
st.subheader("Gerador de Material Pedagógico Adaptado")

# Área para colocar a sua Chave da API (aquela que começa com AIza)
# DICA: No futuro, podemos esconder isso por segurança, mas para testar agora, cole aqui.
api_key = st.sidebar.text_input("Insira sua Chave API do Gemini:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # Espaço para o professor colar o conteúdo da aula normal
    st.write("### 1. Cole aqui o conteúdo original da aula:")
    conteudo_original = st.text_area("Ex: Capítulo 2: Da Forma à Imagem (6º Ano)", height=200)

    if st.button("Adaptar Aula para Aluno DI"):
        if conteudo_original:
            with st.spinner('Criando material adaptado...'):
                # O "comando" mágico que a IA vai seguir
                prompt = f"""
                Você é um professor especialista em Educação Especial. 
                Adapte o conteúdo abaixo para um aluno com Deficiência Intelectual (DI) do 6º ano.
                Use linguagem simples, frases curtas, metáforas visuais e foque no essencial.
                
                Conteúdo Original:
                {conteudo_original}
                
                Estrutura da resposta:
                1. Título do Capítulo (Simplicado)
                2. Conceitos principais explicados de forma visual.
                3. Uma atividade simples para fazer em casa com a família.
                """
                
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write("### ✨ Aula Adaptada:")
                st.write(response.text)
        else:
            st.warning("Por favor, cole um conteúdo antes de adaptar.")
else:
    st.info("Por favor, insira sua chave API na barra lateral para começar.")
