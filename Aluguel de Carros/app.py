import streamlit as st
st.title('RP cars - aluguel de carros')
lista_de_carros = ['logo','jeep','fox','toro','uno','corolla','Kombi','bmw','ferrari','lamborghini','koenigsegg','Mercedes-Benz','Land Rover','Fusca','porche']
st.sidebar.image('logo.png')
opcao = st.sidebar.selectbox("escolha seu carro: ", lista_de_carros)

if opcao == 'logo':
    st.image(f'{opcao}.png')
else:
    st.image(f'{opcao}.png')
    st.markdown(f'## você alugou o modelo: {opcao}')
    st.markdown('---')

    dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
    km = st.text_input(f'quantos Km você rodou com o {opcao}?')
