import pandas as pd

def register(username,password):

    users = pd.read_csv("users.csv")

    if username in users["username"].values:
        return False

    new_user = pd.DataFrame({
        "user_id":[len(users)+1],
        "username":[username],
        "password":[password]
    })

    users = pd.concat([users,new_user],ignore_index=True)
    users.to_csv("users.csv",index=False)

    return True


def login(username,password):

    users = pd.read_csv("users.csv")

    user = users[
        (users["username"]==username) &
        (users["password"]==password)
    ]

    if len(user)>0:
        return int(user.iloc[0]["user_id"])

    return None