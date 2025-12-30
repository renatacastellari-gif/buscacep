import streamlit as st

import requests

st.title("Sistema de busca de CEP")

def busca_cep(cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    return resposta

st.set_page_config('Busca CEP',
                   page_icon='📫')

st.divider()

menu = st.sidebar
cep = menu.text_input("Digite o seu CEP")
botao = menu.button('Pesquisar')

if botao:
    #st.write('Clicou no botão!')
    #st.write(f'Você digitou o {cep}')
    resposta = busca_cep(cep)
    
    if resposta.status_code == 200:
        st.success('CEP encontrado com sucesso!', icon='✅')
        dados = resposta.json()
        
        col1, col2 = st.columns(2)
        
        col1.markdown(f'**CEP:** {dados['cep']}')
        col1.markdown(f"**Logradouro:** {dados['logradouro']}")
        col1.markdown(f"**Complemento:** {dados['complemento']}")
        col1.markdown(f"**Unidade:** {dados['unidade']}")
        col1.markdown(f"**Bairro:** {dados['bairro']}")
        col1.markdown(f"**Localidade:** {dados['localidade']}")
        col2.markdown(f"**UF:** {dados['uf']}")
        col2.markdown(f"**IBGE:** {dados['ibge']}")
        col2.markdown(f"**GIA:** {dados['gia']}")
        col2.write(f"**DDD:** {dados['ddd']}")
        st.write(f"**SIAFI:** {dados['siafi']}")
        st.snow()
     
    else:
        st.error("O CEP informado esta incorreto!", icon='❌')
    
    #st.write(resposta.status_code)
    
    #st.write(resposta.json())
    


st.divider()
#st.date_input('Data')