import pandas as pd
import plotly.express as px
import streamlit as st

df_grouped = df1[['id', 'seller_type']].groupby('seller_type')

df_grouped = df_grouped.count().reset_index()

df_grouped = df_grouped.rename(columns={'id': 'count'})

fig = px.bar(
    df_grouped,
    x="seller_type",
    y="count",
    labels=["seller_type": "Seller type", "count": "Quantity"],
    color="seller_type",
    text="count",
)

fig.update_traces(textposition="outside")
st.plotly_char(fig, user_container_width=True)

return None 


unico_dono = df1[df1['owner'] == '1st owner'].shape[0]
unico_dono

print(f'A base de dados possui {unico_dono} motos de um único dono')
df_grouped = df1.groupby('owner').agg(
    qty = pd.NamedAgg('id', 'count')
).sort_values('qty').reset_index()

ax = sns.barplot(
    data=df_grouped,
    x = 'owner',
    y = 'qty'
)

ax.bar_label(ax.containers[0])

ax.set(
    title = 'Quantidade de Motos por tipo de dono',
    xlabel = 'Tipo de Dono',
    ylabel = 'Quantidade de donos'
);

def rd1_question_9(df):

def rd1_question_13(df):

def rd1_question_14(df):