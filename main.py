# Projeto desenvolvido para o Bootcamp Gen AI E2.
#
# Durante o desenvolvimento deste projeto foi utilizado o ChatGPT como apoio para:
# - estruturação da solução;
# - geração e revisão de código Python;
# - criação da interface em Streamlit;
# - documentação do projeto;
# - otimização da lógica da aplicação.

import streamlit as st

import time

st.set_page_config(

    page_title="SAP MM Support Copilot",

    page_icon="🤖",

    layout="wide"

)

with st.sidebar:

    st.title("🤖 SAP MM Copilot")

    st.markdown("---")

    st.write("👩 *Desenvolvido por:* Lara Rocha")

    st.write("🎓 *Workshop:* GenAI E2")

    st.write("💼 *Projeto:* Copiloto de Suporte SAP MM")

    st.write("🐍 *Tecnologia:* Python + Streamlit")

    st.write("📋 *Tipo de análise:* Regras SAP")

    st.write("📧 *Saída:* Resposta em inglês")

    st.markdown("---")

    st.info("Aplicação para triagem inicial de incidentes SAP MM usando regras e Engenharia de Prompt.")

    st.warning("Utilize apenas dados fictícios.")

def analisar_incidente(texto):

    texto = texto.lower()

    if "estoque" in texto or "910" in texto or "déficit" in texto or "deficit" in texto:

        return {

            "diagnostico": "Possível déficit de estoque disponível.",

            "modulo": "MM / WM",

            "transacoes": "MMBE, MB52, MB51, MIGO",

            "equipe": "Suporte SAP MM/WM",

            "acao": "Validar estoque disponível no material, centro e local de armazenamento.",

        }

    if "miro" in texto or "invoice" in texto or "diferença de preço" in texto:

        return {

            "diagnostico": "Possível erro na MIRO automática ou divergência de preço/quantidade.",

            "modulo": "MM / FI",

            "transacoes": "MIRO, MIR4, ME23N, MIGO, MRBR",

            "equipe": "Suporte SAP MM/FI",

            "acao": "Validar pedido, entrada de mercadoria, nota fiscal e diferenças de preço ou quantidade.",

        }

    if "nota fiscal" in texto or "monitor" in texto or "nfe" in texto or "status 2" in texto or "engrenagem" in texto:

        return {

            "diagnostico": "Possível inconsistência no monitor fiscal ou documento NF-e pendente.",

            "modulo": "MM / Fiscal",

            "transacoes": "J1BNFE, MIGO, MIRO, WE02, SLG1",

            "equipe": "Suporte SAP MM/Fiscal",

            "acao": "Validar status da NF-e, logs de integração e documentos relacionados.",

        }

    if "sto" in texto or "pgi" in texto or "delivery" in texto:

        return {

            "diagnostico": "Possível pendência no fluxo de transferência STO ou status de entrega.",

            "modulo": "MM / SD / WM",

            "transacoes": "ME23N, VL03N, VL09, MIGO, LT03, LT12",

            "equipe": "Suporte SAP MM/SD/WM",

            "acao": "Validar fluxo da STO, delivery, PGI, documentos subsequentes e movimentações de estoque.",

        }

    return {

        "diagnostico": "Tipo de incidente não identificado automaticamente.",

        "modulo": "A validar",

        "transacoes": "A validar",

        "equipe": "SAP Support",

        "acao": "Informar mais detalhes, como transação SAP, mensagem de erro, material, centro ou documento envolvido.",

    }

def gerar_resposta_ingles(analise):

    return f"""Hello,

Based on the initial analysis, this issue appears to be related to the following scenario:

Diagnosis: {analise["diagnostico"]}

Probable module: {analise["modulo"]}

Suggested transactions: {analise["transacoes"]}

Suggested support team: {analise["equipe"]}

Next action: {analise["acao"]}

Please validate the suggested points and let us know if the issue persists after the checks.

Best regards,

"""

st.markdown("""

# 🤖 Copiloto de Suporte SAP MM

### Assistente inteligente para análise inicial de incidentes SAP MM

Este projeto utiliza regras de análise e conceitos de Prompt Engineering para apoiar consultores SAP na triagem de incidentes, sugerindo diagnóstico, módulo provável, transações SAP, equipe responsável e resposta em inglês.

""")

st.warning(

    "⚠️ Utilize somente dados fictícios. Não insira dados reais de clientes, usuários, notas fiscais, entregas ou tickets."

)

st.divider()

st.subheader("📥 Entrada do incidente")

incidente = st.text_area(

    "Descreva o incidente SAP:",

    placeholder="Exemplo: Déficit de estoque utilização livre no local de armazenamento 910",

    height=150,

)

col_botao1, col_botao2 = st.columns([1, 3])

with col_botao1:

    analisar = st.button("🔍 Analisar incidente", use_container_width=True)

if analisar:

    with st.spinner("🔎 Analisando incidente SAP..."):

        time.sleep(2)

        analise = analisar_incidente(incidente)

    st.divider()

    st.subheader("📊 Resultado da análise")

    col1, col2, col3 = st.columns([1.2, 2.0, 0.8])

    with col1:

        st.metric("Módulo provável", analise["modulo"])

    with col2:

        st.metric("Equipe sugerida", analise["equipe"])

    with col3:

        st.metric("Nível de Confiança", "Alta")

    st.divider()

    col4, col5 = st.columns(2)

    with col4:

        st.info("🧠 Diagnóstico inicial")

        st.write(analise["diagnostico"])

        st.success("👥 Equipe sugerida")

        st.write(analise["equipe"])

    with col5:

        st.info("🧾 Transações sugeridas")

        st.write(analise["transacoes"])

        st.warning("➡️ Prox. Ação")

        st.write(analise["acao"])

    st.divider()

    st.subheader("📧 Resposta sugerida em inglês")

    resposta = gerar_resposta_ingles(analise)

    st.code(resposta, language="text")

    st.divider()

    st.markdown("""

    <div style="background:#F5F7FA; padding:18px; border-radius:10px; text-align:center; color:#555; font-size:14px;">

    <b>🤖 SAP MM Support Copilot</b><br>

    Workshop GenAI E2<br>

    Desenvolvido por <b>Lara Rocha</b><br><br>

    Python • Streamlit • Engenharia de Prompt

    </div>

    """, unsafe_allow_html=True)