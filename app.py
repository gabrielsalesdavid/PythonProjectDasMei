import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# --- CONFIGURAÇÃO DA INTERFACE WEB ---
st.set_page_config(
    page_title="Facilitador de Orientação MEI",
    page_icon="📖",
    layout="wide"
)


def gerar_pdf_manual():
    """Gera o manual passo a passo em formato PDF para o usuário baixar"""
    nome_pdf = "Roteiro_Passo_a_Passo_MEI.pdf"
    c = canvas.Canvas(nome_pdf, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, altura - 50, "GUIA PRÁTICO: EMISSÃO DE PARCELAS MEI")
    c.setFont("Helvetica", 10)
    c.drawString(50, altura - 65,
                 "Link Oficial do Sistema: https://www8.receita.fazenda.gov.br/SimplesNacional/Servicos/Grupo.aspx?grp=19")
    c.drawString(50, altura - 75,
                 "--------------------------------------------------------------------------------------------------------------------------------")

    y = altura - 110
    linhas = [
        "Siga este roteiro seguro para emitir a guia do seu acordo:",
        "",
        "1. ACESSO EXTERNO:",
        "   Abra o seu navegador de internet e acesse o link oficial.",
        "",
        "2. PREENCHIMENTO DOS DADOS DE LOGIN:",
        "   Insira o CNPJ da empresa, o CPF do responsável e o seu Código de Acesso.",
        "",
        "3. VALIDAÇÃO DE SEGURANÇA (CAPTCHA):",
        "   Marque a caixinha 'Sou humano' e resolva o desafio visual. Clique em 'Continuar'.",
        "",
        "4. DENTRO DO PORTAL (EMISSÃO):",
        "   No menu do painel inicial, clique na opção 'Emissão de Parcela'.",
        "",
        "5. SELEÇÃO E IMPRESSÃO:",
        "   Marque a caixinha da parcela do mês atual e clique em 'Imprimir' ou 'Emitir DAS'."
    ]

    for linha in linhas:
        if "1. " in linha or "2. " in linha or "3. " in linha or "4. " in linha or "5. " in linha:
            c.setFont("Helvetica-Bold", 11)
        else:
            c.setFont("Helvetica", 10)
        c.drawString(50, y, linha)
        y -= 18

    c.save()
    return nome_pdf


# --- FUNÇÃO DO POP-UP (DIÁLOGO FLUTUANTE) ---
@st.dialog("🚨 Atenção: Direcionamento Seguro")
def abrir_popup_direcionamento():
    st.markdown("""
    Você está prestes a ser direcionado para o site oficial da **Receita Federal**.

    **Lembre-se das instruções fundamentais:**
    1. Preencha seus dados cadastrais com atenção.
    2. O teste **'Sou humano' (CAPTCHA)** deve ser resolvido por você diretamente na nova janela.
    3. Após entrar no painel, clique em **'Emissão de Parcela'**.
    """)
    st.warning("Deixamos este painel do Streamlit aberto aqui ao lado para servir de mapa durante o seu processo!")

    # O botão de link real fica dentro do pop-up para o clique de saída
    st.link_button(
        "🔗 Entendi, ir para o site do Governo",
        "https://www8.receita.fazenda.gov.br/SimplesNacional/Servicos/Grupo.aspx?grp=19",
        use_container_width=True
    )


# --- INTERFACE VISUAL DO STREAMLIT ---
st.title("📖 Facilitador e Guia de Emissão DAS - MEI")
st.markdown("""
Este aplicativo foi desenhado para ajudar usuários leigos a emitir a guia do acordo MEI de forma rápida e com **100% de segurança**.
""")

st.markdown("---")

col_link, col_roteiro = st.columns([1, 1.3])

with col_link:
    st.subheader("🌐 Acesso ao Sistema")
    st.info("Clique no botão abaixo para abrir o alerta de direcionamento e acessar o sistema oficial.")

    # Este botão aciona a função que desenha o pop-up na tela
    if st.button("🚀 Iniciar Acesso Seguro", use_container_width=True, type="primary"):
        abrir_popup_direcionamento()

    st.markdown("---")
    st.subheader("📥 Guardar para Depois")
    st.write("Quer baixar esse roteiro no seu computador ou celular?")

    pdf_pronto = gerar_pdf_manual()
    with open(pdf_pronto, "rb") as f:
        st.download_button(
            label="⬇️ Baixar Roteiro em PDF",
            data=f,
            file_name="Guia_Passo_a_Passo_MEI.pdf",
            mime="application/pdf",
            use_container_width=True
        )

with col_roteiro:
    st.subheader("🗺️ Mapa do Caminho (Siga estes passos)")

    with st.expander("🔑 Passo 1: Preenchendo os Dados de Acesso", expanded=True):
        st.markdown("""
        Assim que a página da Receita Federal abrir, você verá três campos em branco. Preencha-os:
        * **CNPJ:** Os 14 números da sua empresa (sem pontos ou barras).
        * **CPF:** O CPF do proprietário/responsável pelo MEI.
        * **Código de Acesso:** O seu código de segurança do Simples Nacional.
        """)

    with st.expander("🛡️ Passo 2: O Teste de Segurança (CAPTCHA)", expanded=True):
        st.markdown("""
        Logo abaixo dos campos, haverá uma caixinha dizendo **"Sou humano"**.
        1. Clique nessa caixinha.
        2. Se o site exibir um teste com imagens, selecione as figuras corretas.
        3. Quando aparecer o sinal de verificado verde (✔️), clique no botão **"Continuar"**.
        """)

    with st.expander("📄 Passo 3: Emitindo o Boleto (DAS)", expanded=True):
        st.markdown("""
        Ao entrar no sistema do governo:
        1. Procure e clique no link escrito **"Emissão de Parcela"**.
        2. Uma tabela com as parcelas do seu acordo vai aparecer na tela.
        3. Marque o quadradinho de seleção da parcela que vence este mês.
        4. Vá até o final da página e clique no botão **"Imprimir"** ou **"Emitir DAS"**.
        """)