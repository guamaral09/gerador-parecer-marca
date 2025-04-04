from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Gerador de Parecer de Marca - Berggren", layout="centered")

st.title("🔍 Gerador de Parecer de Viabilidade de Registro de Marca")
st.write("Preencha os campos abaixo para gerar automaticamente o parecer técnico-jurídico.")

# Inputs do usuário
nome_marca = st.text_input("Nome da marca")
classe = st.text_input("Classe Nice (ex: 35, 41, 43)")
parecer = st.selectbox("Parecer de Viabilidade", ["parece ser VIÁVEL", "parece ser INVIÁVEL"])
justificativa = st.text_area("Justificativa Técnica", height=200)
cidade = st.text_input("Cidade", value="São Paulo")

data_hoje = datetime.today().strftime('%d/%m/%Y')

if st.button("Gerar Parecer") and nome_marca and classe and justificativa:
    parecer_formatado = f"""
{cidade}, {data_hoje}

BERGGREN MARCAS E PATENTES
CNPJ: 30.151.525/0001-99
E-mail: contato@berggrenmarcasepatentes.com.br
Site: www.berggrenmarcasepatentes.com.br

---

PARECER TÉCNICO-JURÍDICO DE VIABILIDADE DE REGISTRO DE MARCA

Após pesquisas nos bancos de dados oficiais do INPI e análise preliminar, considerando a legislação vigente e a jurisprudência administrativa, informamos que o pedido de registro da marca “{nome_marca}”, na classe {classe}, {parecer.upper()} no momento.

{justificativa}

Ressaltamos que a decisão final sobre o deferimento do pedido cabe exclusivamente ao Instituto Nacional da Propriedade Industrial – INPI, nos termos da Lei nº 9.279/96.

Permanecemos à disposição para prestar os esclarecimentos adicionais e, sendo do interesse do cliente, seguir com o protocolo ou estudar estratégias alternativas.

Atenciosamente,

**Ezequiel Berggren**
OAB/SP 113274
"""

    st.markdown("---")
    st.subheader("📄 Parecer Gerado:")
    st.code(parecer_formatado, language='markdown')
    st.download_button("📥 Baixar parecer em .txt", data=parecer_formatado, file_name=f"parecer_{nome_marca}.txt")
else:
    st.warning("Preencha todos os campos obrigatórios para gerar o parecer.")
