from datetime import date
import pandas as pd
import seaborn as sns
import streamlit as st
import folium
import numpy as np
from streamlit_folium import folium_static
import plotly.express as px
from folium.plugins import MarkerCluster
from matplotlib import pyplot as plt
import plotly.figure_factory as ff

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    return data

def features_n (data):
    data['date'] = pd.to_datetime( data['date'] )
    data = data.drop_duplicates(subset = ['id'], keep = 'last')
    data.loc[data['bedrooms'] == 33, 'bedrooms'] = 3
    return data

def  descritivas (data):
    num_atributos = data.select_dtypes(include = ['int64', 'float64'])
    #deletando a coluna 'ID'
    num_atributos = num_atributos.iloc[:, 1: ]
    # Medidas de tendência central:
    data_mean =  pd.DataFrame(num_atributos.apply(np.mean)).T
    data_median = pd.DataFrame(num_atributos.apply(np.median)).T
    # Medidas de dispersão
    std = pd.DataFrame( num_atributos.apply( np.std ) ).T
    max_ = pd.DataFrame( num_atributos.apply( np.max ) ).T
    min_ = pd.DataFrame( num_atributos.apply( np.min ) ).T
    # Concatenando as medidas geradas
    df = pd.concat( [data_mean, data_median, std, max_, min_ ]).T.reset_index()
    # Alterando o nome das colunas
    df.columns = [ 'atributos','media', 'mediana', 'std', 'min', 'max']
    return data

# Header Image
col1, col2, col3 = st.columns(3)
col2.image('houserocket.png')

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.1, 2, 0.2, 1, 0.1)
)

    
row0_1.title("Bem vindo ao House Rocket Project")
with row0_2:
        st.write("")
row0_2.subheader(
        "Para mais informações sobre o projeto acessar [aqui](https://github.com/karinnasantos?tab=repositories)"
    )


st.write('')
st.write("A  House Rocket é uma empresa fictícia que utiliza a tecnologia para tomar decisões de compra e venda de imóveis. Este projeto de Ciência de Dados tem como objetivo encontrar as melhores oportunidades de negócio para maximizar o faturamento da empresa. A melhor estratégia é a compra de casas em ótimas condições por baixos preços e a venda desses imóveis por um preço superior. Neses projeto o cientista de dados deve obter insights através da manipulação de dados para auxiliar as melhores decisões da equipe de negócios.")

def  home (data):
        # Show dataset
    st.header('Dataset')
    b_dataset = st.checkbox('Exibir o conjunto de dados')
    if b_dataset:
        st.dataframe(data)
    return None
    
def  hipoteses (data):
        st.write("<h1 style='text-align: center; color: black;'>Testando Hipóteses de Negócio</h1>", unsafe_allow_html=True)

        c1,c2 = st.columns(2)

        c1.subheader('Hipótese 1:  Imóveis com vista para a água são em média 30% mais caros')
        h1 = data[['price', 'waterfront',  'sqft_lot']].groupby('waterfront').mean().reset_index()
        h1['waterfront'] = h1['waterfront'].astype(str)
        fig = px.bar(h1, x='waterfront', y = 'price', color='waterfront', color_discrete_map ={'0':'green', '1':'darkred'},  labels={"waterfront": "Visão das casas para água",
                                                                                    "price": "Preço"},
                                                                                    template= 'simple_white',
                                                                                    title="Hipótese verdadeira: Imóveis com vista para água são mais caros")
        fig.update_layout(showlegend = False)
        c1.plotly_chart(fig, use_container_width= True)
        #---------------------- h2
        c2.subheader('Hipótese 2: Imóveis com data de construção menor que 1955 são em média 50% mais baratos')
        data['construcao'] = data['yr_built'].apply(lambda x: '> 1955' if x > 1955
                                                                        else '< 1955')
   
        h2 = data[['construcao', 'price',  'sqft_lot']].groupby('construcao').mean().reset_index()

        fig2 = px.bar(h2, x='construcao', y = 'price', color = 'construcao', color_discrete_map ={'>1955':'black', '<1955':'purple'}, labels = {"construcao":"Ano da Construção",
                                                                                        'price': 'Preço'},
                                                                                            template='simple_white',
                                                                                            title="Hipótese falsa: A data de construção dos imóveis não afeta o preço")
        fig2.update_layout(showlegend = False)
        c2.plotly_chart(fig2, use_container_width= True)
    #---------------------- h3
        c3,c4 = st.columns(2)

        c3.subheader('Hipótese 3: Imóveis sem porão com maior área total são 40% mais caros do que imóveis com porão')
        data['basement'] = data['sqft_basement'].apply(lambda x: "Imóveis com porão" if x > 0 else "Imóveis sem porão")     
        
        h3 = data[['basement', 'sqft_lot', 'price']].groupby('basement').sum().reset_index()
        fig3 = px.bar(h3, x='basement', y = 'price', color = 'basement', color_discrete_map ={'Imóveis com porão':'green', 'Imóveis sem porão':'darkred'}, labels = {'price': 'Preço',
                                                                                'basement': ' ',
                                                                                'sqft_lot': 'Área Total'},
                                                                                template= 'simple_white',
                                                                                title="Hipótese verdadeira:Imóveis sem porão possuem maiores preços e área total")
        fig3.update_layout(showlegend = False)
        c3.plotly_chart(fig3, use_container_width= True)

    #---------------------- h4
        c4.subheader('Hipótese 4: Imóveis que nunca foram reformadas são em média 20% mais baratos')
        data['renovacao'] = data['yr_renovated'].apply(lambda x: 'sim' if x > 0 else
                                                            'nao'   )
        
        h4 = data[['price', 'renovacao', 'sqft_lot']].groupby('renovacao').mean().reset_index()
        fig4 = px.bar(h4, x='renovacao', y = 'price', color = 'renovacao', color_discrete_map ={'sim':'green', 'não':'darkred'},labels = {'renovacao':'Renovação',
                                                'price': 'Preço'}, template = 'simple_white',
                                                title="Hipótese verdadeira: Imóveis sem reforma são mais baratos.")
        fig4.update_layout(showlegend = False)
        c4.plotly_chart(fig4, use_container_width= True)

    #---------------------- h5
        c5, c6 = st.columns(2)
        c5.subheader('Hipótese 5: Imóveis com 3 banheiros tem um crescimento de MoM de 15%')
        data['mes'] = data['date'].dt.month
        data['ano'] = data['date'].dt.year

        h5 = data.loc[data['bathrooms'] == 3].copy()
        h5['mes'] = h5['date'].dt.strftime('%Y-%m')
        h5 = h5[['mes', 'price']].groupby('mes').mean().reset_index()
        h5['porcentagem'] = h5['price'].pct_change()*100
        h5['pct'] = h5['porcentagem'].apply(lambda x: 'Verdadeira' if x > 0 else 'Falsa')
    
        fig5 = px.line(h5, x = "mes", y = "price", labels = {'mes':'Mês','price':'Preço'}, title=' ')
        fig5.update_layout(coloraxis_showscale=False)
        c5.plotly_chart(fig5, use_container_width= True)

    #---------------------- h6
        c6.subheader('Hipótese 6: Imóveis com dois andares ou menos, são 40% mais baratos')
        data['andares'] = data['floors'] .apply(lambda x: '2 ou <' if x <= 2 else '> 3')
        h6 = data[['andares', 'price']].groupby('andares').mean().reset_index()
        h6['porcetagem'] = h6['price'].pct_change()*100
        
        fig6 = px.bar(h6, x ='andares', y = 'price', color = 'andares', color_discrete_map ={'2 ou <':'green', '> 3':'darkred'},
        labels = {'price':'Preço','andares': 'Número de andares'} ,
                                                                                        template= 'simple_white',
                                                                                        title="Hipótese verdadeira: Imóveis com menos andares são mais baratos.")
        fig6.update_layout(showlegend = False)
        c6.plotly_chart(fig6, use_container_width= True)   
    #---------------------- h7
        c7, c8 = st.columns(2)
        c7.subheader('Hipótese 7: Imóveis não reformados são 35% mais baratos')

        data['renovacao'] = data['yr_renovated'].apply(lambda x: 'sim' if x > 0 else
                                                            'nao'   )

        h7 = data[data['condition'] == 1]
        h7 = data[['price', 'renovacao']].groupby('renovacao').sum().reset_index()
        h7['porcetagem'] = h7['price'].pct_change()*100

        fig7 = px.bar(h7, x ='renovacao', y = 'price', color = 'renovacao', color_discrete_map ={'sim <':'darkred', '> não':'magenta'},
        labels = {'price':'Preço','renovacao': 'Reformados'} ,
                                                                                        template= 'simple_white',
                                                                                        title="Hipótese verdadeira: Imóveis que não foram reformados são mais baratos.")

        fig7.update_layout(showlegend = False)
        c7.plotly_chart(fig7, use_container_width= True)

    #---------------------- h8
        c8.subheader('Hipótese 8: Imóveis com melhores vistas são 25% mais caros')
        data['boa_vista'] = data['view'].apply(lambda x: 'Boa' if x == 3 else 
                                                    'Boa para ruim')
        h8 = data[['boa_vista', 'price']].groupby('boa_vista').mean().reset_index()
        h8['porcentagem'] = h8['price'].pct_change()*-100

        fig8 = px.bar(h8, x ='boa_vista', y = 'price', color = 'boa_vista', color_discrete_map ={'Boa <':'m', '> Boa para ruim':'c'},
        labels = {'price':'Preço','boa_vista': 'Vista da casa'} ,
                                                                                        template= 'simple_white',
                                                                                        title="Hipótese verdadeira: Imóveis com melhores vistas são mais caros.")

        fig8.update_layout(showlegend = False)
        c8.plotly_chart(fig8, use_container_width= True)

    #---------------------- h9
        c9, c10 = st.columns(2)
        c9.subheader('Hipótese 9: Imóveis com menos de três quartos são 15% mais baratos')
        data['quartos'] = data['bedrooms'].apply(lambda x: 'sim' if x <= 3
                                                    else 'não')  

        h9 = data[['quartos', 'price']].groupby('quartos').mean().reset_index()
        h9['porcentagem'] = h8['price'].pct_change()*-100

        
        fig9 = px.bar(h9, x='quartos', y = 'price', color_discrete_map ={'sim <':'green', '> não':'darkred'}, template = 'simple_white',
                    labels={'quarto':'Número de quartos', 'price': 'Preço'},
                    title="Hipótese falsa: Os imóveis  com menos de três quartos não são mais baratos.")

        fig9.update_layout(showlegend = False)
        c9.plotly_chart(fig9, use_container_width= True)

    #---------------------- h10
        c10.subheader('Hipótese 10: Imóveis com mais de três quatros tem área total 15% maior que os imóveis com menos de três quatros')
        data['quarto'] = data['bedrooms'].apply(lambda x: "Mais de 3 quartos" if x > 3 else "Menos de três quartos") 
        h10 = data[['quarto', 'sqft_lot']].groupby('quarto').mean().reset_index()
        h10['porcentagem'] = h10['sqft_lot'].pct_change()*-100

        fig10 = px.bar(h10, x ='quarto', y = 'sqft_lot', color = 'quarto', color_discrete_map ={'Mais de três quartos <':'#00CC96', '> Menos de três quartos':'brown'},
        labels = {'sqft_lot':'Área total','quartos': ' '} ,
                                                                                        template= 'simple_white',
                                                                                        title="Hipótese verdadeira: Imóveis com mais de três quartos tem área total maior.")

        fig10.update_layout(showlegend = False)
        c10.plotly_chart(fig10, use_container_width= True)

        return None
#--------------------------------------------------------------------------
def conclusion(data):
            st.write("<h1 style='text-align: center; color: black;'>Questão de negócios</h1>", unsafe_allow_html=True)
            st.write("1 - Quais são os negócios que a House Rocket deveria comprar e por qual preço?")
            
            data['season'] = data['mes'].apply(lambda x: 'summer' if (x > 5) & (x < 8) else
                                                'spring' if (x > 2) & (x < 5) else
                                                'fall' if (x > 8) & (x < 12) else
                                                'winter') 

           
            a = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
            date2 = pd.merge(a, data, on='zipcode', how = 'inner')
            date2 = date2.rename(columns = {'price_y' : 'price', 'price_x' : 'price_median'} ) #alterando nome das colunas
                #criando coluna
            for i, row in date2.iterrows():
                if (row['price_median'] >= row['price']) & (row['condition'] < 3):
                    date2.loc[i,'pay'] =  'sim'
                else:
                    date2.loc[i, 'pay'] = 'nao'

                #criar coluna com cor
            for i, row in date2.iterrows():
                if (row['pay'] == 'sim'):
                    date2.loc[i,'marker_color'] = 'green'
                else:
                    date2.loc[i, 'marker_color'] = 'red'
                    # Assumptions
            st.markdown('Mapa - Quais imóveis devem ser comprados?')
            st.markdown('Em verde os imóveis indicados ')

            mapa = folium.Map(width = 600, height = 300,
                        location = [data['lat'].mean(),data[ 'long'].mean()],
                        default_zoom_start=30)
            features = {}
            for row in pd.unique(date2['marker_color']):
                features[row] = folium.FeatureGroup(name=row)

            for index, row in date2.head(10000).iterrows():
                circ = folium.Circle([row['lat'], row['long']],
                    radius=150, color=row['marker_color'], fill_color=row['marker_color'],
                    fill_opacity = 1, popup= 'Compra: {0}, Preço: {1}'.format(row['pay'],
                                    row['price']))
                circ.add_to(features[row['marker_color']])

            #for row in pd.unique(date2["marker_color"]):
               # features[row].add_to(mapa)

                folium.LayerControl().add_to(mapa)
                folium_static(mapa)

       #===================================================================================
            st.write('2- Uma vez comprado, qual é o melhor momento para vendê-lo e por qual preço?')
            
            date3 = date2[date2['pay'] == 'sim']
            date4 = date3[['season', 'zipcode', 'price']].groupby(['zipcode', 'season']).median().reset_index()
            date5 = date4.rename(columns = {'price' : 'price_medi_season', 'season': 'season_median'} ) 
            date6 = pd.merge(date4, date5, on='zipcode', how = 'inner')
            for i, row in date6.iterrows():
                if (row['price_medi_season'] > row['price']):
                    date6.loc[i, 'sale'] =  row['price'] * 1.1
                else:
                    date6.loc[i, 'sale'] = row['price'] * 1.3
            # Plotando a figura
            
            fig11 = px.bar(date6, x = 'season', y = 'sale', color_discrete_sequence= ['teal'],labels={'season':'Estação do Ano', 'sale': 'Preço'},
                                                                                template = 'simple_white')
            fig11.update_layout(showlegend = False)
            st.plotly_chart(fig11, x='season', y='sale', use_container_width= True)
            return None

if __name__ == "__main__":
    path = 'kc_house_data.csv'
    data = get_data(path)
    data = data.sample(10000)
    features_n(data)
    descritivas(data)
    home (data)
    hipoteses (data)
    conclusion(data)