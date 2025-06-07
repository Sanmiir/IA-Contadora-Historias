import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBuYuMf4v0dZGceJQB4fYtLYCqGKkO-4vk")

model = genai.GenerativeModel("gemini-1.5-flash")


st.set_page_config(page_title="Criador de Histórias Interativas")

st.title("Criador de Histórias Interativas com IA")
st.markdown("Preencha os campos abaixo e gere uma história com ajuda da IA gemini 1.5 flash!")

personagem = st.text_input("Nome do personagem principal:")
ambiente = st.text_input("Ambiente onde a história se passa:")
genero = st.selectbox("Gênero da história:", ["Aventura", "Fantasia", "Terror", "Comédia", "Mistério", "Romance"])
idade = st.slider("Idade do personagem:", 5, 100, 25)
moral = st.text_area("Mensagem ou moral da história (opcional):")


if st.button("Gerar História"):
    if personagem and ambiente and genero:
        prompt = f"""
        Crie uma história no gênero {genero} com um personagem chamado {personagem}, de {idade} anos.
        A história deve se passar em {ambiente}. 
        {f"Inclua uma moral no final: {moral}" if moral else ""}
        A história deve ser cativante, envolvente e criativa.
        """
        with st.spinner("Gerando história..."):
            try:
                resposta = model.generate_content(prompt)
                st.subheader("📖 História Gerada:")
                st.write(resposta.text)
            except Exception as e:
                st.error(f"Erro ao gerar história: {str(e)}")
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios!")
st.markdown("---")  # linha horizontal para separar

st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>"
    "Desenvolvido por Sanmir Gabriel | © 2025 | Contato: sanmir@email.com"
    "</p>", 
    unsafe_allow_html=True
)