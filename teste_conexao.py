import streamlit as st
import psycopg2

st.title("🔌 Teste de Conexão com Neon PostgreSQL")

try:
    # Lê a URL do secrets.toml
    db_url = st.secrets["general"]["database_url"]

    st.write("📡 Conectando ao banco...")

    # Conecta no Neon
    conn = psycopg2.connect(db_url, sslmode="require")
    cur = conn.cursor()

    # Teste simples: versão do banco
    cur.execute("SELECT version();")
    versao = cur.fetchone()[0]

    st.success("✅ Conexão bem-sucedida!")
    st.code(versao)

    cur.close()
    conn.close()

except Exception as e:
    st.error("❌ Erro ao conectar ao banco!")
    st.exception(e)
