import streamlit as st
from rsc.extraction import load_data

st.set_page_config(layout='wide')

def create_dataframe_SECTION(df):
    st.title("Database")
    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """"
                        """

    col_2.markdown(data_description)

    return None

# Lendo o dataset de fabricantes
companies = pd.read_csv('../data/raw/companies.csv', index_col=0)

# Método novo
companies_tuple = create_sorted_companies_tuple(companies)

# Criando a coluna `company` no DataFrame
df_raw['company'] = df_raw.apply(lambda line: create_company_name(companies_tuple, line), axis=1)

df_raw.head()


def main():
    df_raw = load_data()
    st.dataframe(df_raw)

if __name__ == '__main__':
    main()




