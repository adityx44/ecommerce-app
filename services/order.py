import pandas as pd

def place_order(user_id,products):

    try:
        orders = pd.read_csv("orders.csv")
    except:
        orders = pd.DataFrame(
            columns=[
                "order_id",
                "user_id",
                "product_id",
                "quantity"
            ]
        )

    next_id = len(orders)+1

    data = []

    for p in products:

        data.append({
            "order_id":next_id,
            "user_id":user_id,
            "product_id":p,
            "quantity":1
        })

    orders = pd.concat(
        [orders,pd.DataFrame(data)],
        ignore_index=True
    )

    orders.to_csv("orders.csv",index=False)
