import pandas as pd

def get_products():
    return pd.read_csv("products.csv")


def add_product(name,price):

    products = pd.read_csv("products.csv")

    pid = len(products)+1

    new_product = pd.DataFrame({
        "product_id":[pid],
        "name":[name],
        "price":[price]
    })

    products = pd.concat([products,new_product])
    products.to_csv("products.csv",index=False)


def delete_product(product_id):

    products = pd.read_csv("products.csv")

    products = products[
        products["product_id"]!=product_id
    ]

    products.to_csv("products.csv",index=False)