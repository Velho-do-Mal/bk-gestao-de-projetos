import streamlit as st
import psycopg2


st.set_page_config(page_title="Teste Neon", layout="centered")

st.title("🔌 Teste de Conexão com Neon PostgreSQL")

try:
    # Lê a URL do banco a partir do secrets.toml
    db_url = st.secrets["general"]["database_url"]

    st.write("📡 Conectando ao banco...")

    # Conexão usando a URL completa
    conn = psycopg2.connect(db_url)

    cur = conn.cursor()

    # Teste simples: versão do PostgreSQL
    cur.execute("SELECT version();")
    versao = cur.fetchone()[0]

    st.success("✅ Conexão bem-sucedida com o Neon!")
    st.code(versao)

    cur.close()
    conn.close()

except KeyError as e:
    st.error("❌ Não encontrei a chave 'general.database_url' no secrets.")
    st.info("Verifique o arquivo .streamlit/secrets.toml e o nome da seção/campo.")
    st.exception(e)

except Exception as e:
    st.error("❌ Erro ao conectar ao banco!")
    st.exception(e)
