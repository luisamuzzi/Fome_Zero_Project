import streamlit as st
from PIL import Image

#==============================================
# Configuração da largura da página
#==============================================
st.set_page_config(page_title='Home', page_icon='🏠', layout='wide')

#==============================================
# Barra Lateral
#==============================================
# Logo:
image = Image.open('logo.png')

# Colunas para logo e nome da empresa:
with st.sidebar:

    col1, col2 = st.columns(2)

    with col1:

        st.image(image=image, use_column_width=True)

    with col2:

        st.markdown('')
        st.markdown('')
        st.markdown('# Fome Zero')

    st.markdown("""___""")
    
#==============================================
# Texto da página
#==============================================
st.write('# Fome Zero Dashboard')

st.markdown(
    """
    Este dashboard foi construído para acompanhar as métricas da empresa Fome Zero.
    ### Como utilizar esse Dashboard?
    - Main Page: Métricas gerais e mapa de restaurantes.
    - Visão Países: Métricas por país.
    - Visão Cidades: Métricas por cidade.
    - Visão Tipos de Culinária: Métricas por tipo de culinária.
""")