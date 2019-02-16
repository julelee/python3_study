import Func.Test as FuncTest
import pandas as pd
import math


def build_list(upper_limit=1, delta=0.1, step=10, cash=10000):
    L = []

    price = round(upper_limit, 3)
    total_amount = 0
    amount = 0
    cost = cash / step
    for _ in range(step+1):
        d = dict(up_lim=price,
                 amount=amount,
                 delta=delta,
                 total_amount=total_amount,
                 cost=cost,
                 cash = cash)

        L.append(d)
        price = round(price - price * delta, 3)
        amount = int((cost//price)//100*100)
        total_amount = total_amount + amount
        cash = cash - price * amount
    return pd.DataFrame(L)
