import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # drop duplicates
    df.drop_duplicates(inplace=True)

    # handle missing values
    df.dropna(how="all", inplace=True)

    # date parsing
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        df['year'] = df['order_date'].dt.year
        df['month'] = df['order_date'].dt.month

    # total sales
    if {'quantity', 'price'}.issubset(df.columns):
        df['total_sales'] = df['quantity'] * df['price']

    return df


if __name__ == '__main__':
    df = load_data('data/ecommerce_sales.csv')
    df_clean = clean_data(df)
    df_clean.to_csv('data/ecommerce_sales_clean.csv', index=False)