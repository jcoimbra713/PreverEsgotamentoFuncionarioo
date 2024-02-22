import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva_esgotamento.pkl', 'rb') 
maquina_preditiva_esgotamento = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PROJETO PARA PREVER ESGOTAMENTO DE FUNCIONARIO</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA PARA PREVER ESGOTAMENTO DE FUNCIONARIO - by João Coimbra </h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da pessoa que deseja prever o diabetes
    Sexo = st.selectbox('Sexo', ("Feminino", "Masculino"))
    TipoEmpresa =st.selectbox('Tipo De Empresa', ("Produto", "Serviço"))
    Configuração = st.selectbox('Configuração', ("Não", "Sim"))
    NivelAntiguidade =st.number_input("Nivel de Antiguidade")
    HorasAlocadas = st.number_input("Horas Alocadas")
    AvaliaçãoEstresse = st.number_input("Avaliação De Estresses") 

      
    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result = prediction(Sexo, TipoEmpresa, Configuração, NivelAntiguidade, HorasAlocadas, AvaliaçãoEstresse) 
        st.success(f'Resultado: {result}')


# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(Sexo, TipoEmpresa, Configuração, NivelAntiguidade, HorasAlocadas, AvaliaçãoEstresse):   
    # Pre-processando a entrada do Usuário    
    if Sexo == "Feminino":
        Sexo = 0
    else:
        Sexo = 1
 
    if TipoEmpresa == "Produto":
        TipoEmpresa = 0
    else:
        TipoEmpresa = 1  
    

    if Configuração == "Não":
        Configuração = 0

    else:
        Configuração = 1


    # Fazendo a Predição
    parametro = np.array([[Sexo, TipoEmpresa, Configuração, NivelAntiguidade, HorasAlocadas, AvaliaçãoEstresse]])
    fazendo_previsao = maquina_preditiva_esgotamento.predict(parametro)
   
    return fazendo_previsao[0]

if __name__ == '__main__':
    main()
