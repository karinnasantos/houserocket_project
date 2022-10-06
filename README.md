 <h1 align="center">House Rocket Project </h1>

![Getting Started](./houserocket.png)


Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações [link da comunidade](https://comunidadeds.com/)

[link para app no Heroku](https://analytics-hr-kc.herokuapp.com/)

		*A logo criada é ficticia.* 


# 1. Descrição 
A *House Rocket* é uma empresa fictícia que utiliza a tecnologia para tomar decisões de compra e venda de imóveis. Este projeto de Ciência de Dados tem como objetivo encontrar as melhores oportunidades de negócio para maximizar o faturamento da empresa. A melhor estratégia é a compra de casas em ótimas condições por baixos preços e a venda desses imóveis por um preço superior. Nesse projeto o cientista de dados deve obter insights através da manipulação de dados para auxiliar as melhores decisões da equipe de negócios. As questões a serem respondidas são:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2.** Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

# 2. Atributos 

Os dados para este projeto podem ser encontrados em: https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885 . Abaixo segue a definição para cada um dos 21 atributos:


|    Atributos    |                         Significado                          |
| :-------------: | :----------------------------------------------------------: |
|       id        |       Numeração única de identificação de cada imóvel        |
|      date       |                    Data da venda da casa                     |
|      price      |    Preço que a casa está sendo vendida pelo proprietário     |
|    bedrooms     |                      Número de quartos                       |
|    bathrooms    | Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro) |
|   sqft_living   | Medida (em pés quadrado) do espaço interior dos apartamentos |
|    sqft_lot     |     Medida (em pés quadrado)quadrada do espaço terrestre     |
|     floors      |                 Número de andares do imóvel                  |
|   waterfront    | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) |
|      view       | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa  4 = alta |
|    condition    | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde: 1 = baixo \|-\| 5 = alta |
|      grade      | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta |
|  sqft_basement  | A metragem quadrada do espaço habitacional interior acima do nível do solo |
|    yr_built     |               Ano de construção de cada imóvel               |
|  yr_renovated   |                Ano de reforma de cada imóvel                 |
|     zipcode     |                         CEP da casa                          |
|       lat       |                           Latitude                           |
|      long       |                          Longitude                           |
| sqft_livining15 | Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo |
|   sqft_lot15    | Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo |


# 3. Premissas do Negócio
- Para o desenvolvimento desse projeto, seguimos as seguintes premissas:
1. Valores iguais a zero corresponde a casas nunca reformadas em **yr_renovated**.
2. Na coluna **bathroom** o valor 33 foi considerado como um erro de digitação e foi substituído por 3 nas análises.
3. Para valores de ID duplicados, apenas os mais recentes foram considerados.
4. As localidades e estação do ano foram decisivas para compra ou venda dos imóveis.

# 4. Planejamento e estratégia de solução:
- Etapas para solucionar o problema de negócio:
1. Coleta de dados via Kaggle
2. Entendimento de negócio
3. Tratamento de dados 

- Tranformação de variaveis
- Limpeza
- Entendimento

5. Responder problemas do negócio
6. Resultados para o negócio
7. Conclusão

# 5. Ferramentas

* Python 3.10

* VSCode

* Streamlit

* Heroku

# 6. Insights e análise das hipóteses (H) de negócio

H1 -         Verdadeira | Imóveis com vista para água são mais caros

H2 -         Falsa      | Imóveis com data de construção não afeta o preço

H3 -         Verdadeira | Imóveis sem porão possuem maior área total e são mais caros

H4 -         Verdadeira | Imóveis sem reforma são mais baratos

H5 -         Falsa      | Imóveis com más condições e com vista ruim são mais caros

H6 -         Verdadeira | Imóveis com menos andares são mais baratos

H7 -         Verdadeira | Imóveis que não foram reformados são mais baratos

H8 -         Verdadeira | Imóveis com melhores vistas são mais caroa

H9 -         Falsa      | Os imóveis  com menos de três quartos não são mais baratos

H10-         Verdadeira | Imóveis com mais de três quartos tem área total maior

# 7. Conclusão

Imóveis foram agrupados por região (**zipcode**) e foi calculada a mediana do preço dos imóveis. Um total de 151 impoveis apresentaram o preço abaixo da mediana e foram sugeridos para a compra. Além disso, atributos como localidade e estação do ano foram importantes para a grupar os imóveis e as melhores condições para executar o negócio. Assim, o momento ideal para vender os 151 imóveis é durante a primavera, onde os preços são mais altos.

# 8. Próximos passos
O presente projeto em ciência de dados foi capaz de solucionar problemas de negócio e gerar insights capazes de otmizar o lucro da empresa. Entretanto, o prejeto ainda pode ser melhorado através de técnicas robustas e precisas em resolver o problema de negócio. Os próximos passos são:

- Observar o tipo de distribuição dos dados para saber se é necessário realizar alguma transformação (e.g., log), seguido de análises de relações dos atributos, como modelos lineares ou correlações.
- Utilizar testes de média como intuito de validar as hipóteses. Testes paramétricos (e.g., Anova) e não paramétricos (e.g., Kruskal-Wallis) podem ser aplicados nesse caso.
- Direcionar a venda dos imóveis conforme o interesse dos clientes, conforme os atributos dos imóveis.
