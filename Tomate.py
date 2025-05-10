import streamlit as st
import numpy as np
import pandas as pd
import datetime

st.set_page_config(page_title="Aviator1 - Previsão Inteligente", layout="centered")

st.title("Aviator1 - Análise e Previsão Inteligente")

# Histórico de entradas
if "valores" not in st.session_state:
    st.session_state.valores = []

st.subheader("Inserir novo valor")
novo_valor = st.number_input("Digite o valor da rodada (ex: 2.15)", min_value=0.0, step=0.01, format="%.2f")
if st.button("Adicionar valor"):
    st.session_state.valores.append(novo_valor)
    st.success("Valor adicionado com sucesso!")

# Exibir histórico
st.subheader("Histórico")
if st.session_state.valores:
    st.dataframe(pd.DataFrame(st.session_state.valores, columns=["Valores"]).reset_index(drop=True))
else:
    st.info("Nenhum valor inserido ainda.")

# Análise Inteligente
def calcular_estatisticas(valores):
    media = np.mean(valores)
    mediana = np.median(valores)
    minimo = np.min(valores)
    maximo = np.max(valores)
    variancia = np.var(valores)
    return media, mediana, minimo, maximo, variancia

if st.session_state.valores:
    st.subheader("Análise Inteligente")

    media, mediana, minimo, maximo, variancia = calcular_estatisticas(st.session_state.valores)

    st.markdown(f"- **Média Geral:** {media:.2f}")
    st.markdown(f"- **Mediana:** {mediana:.2f}")
    st.markdown(f"- **Mínimo:** {minimo:.2f}")
    st.markdown(f"- **Máximo:** {maximo:.2f}")
    st.markdown(f"- **Variância:** {variancia:.2f}")

    # Estimativas Futuras
    st.subheader("Previsão Estimada")

    estimativa_min = round(max(1.00, media - 0.45), 2)
    estimativa_med = round(media + 0.35, 2)

    st.success(f"**Valor Mínimo Provável:** {estimativa_min}x")
    st.info(f"**Valor Médio Estimado:** {estimativa_med}x")

    # Estratégia automática
    st.subheader("Conselho Inteligente")

    if maximo > 10 or any(v > 20 for v in st.session_state.valores):
        st.warning("Alerta: Sequência com picos altos detectada. Possível queda iminente.")
    elif all(v < 2 for v in st.session_state.valores[-5:]):
        st.warning("Queda contínua detectada. Possível recuperação em breve.")
    elif np.mean(st.session_state.valores[-3:]) > 3:
        st.info("Sequência quente! Boa probabilidade de manter valores altos.")
    else:
        st.info("Padrão normal. Sem tendência forte no momento.")
