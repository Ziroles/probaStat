import matplotlib.pyplot as plt
import pandas as pd
from utils.DataManager import DataManager

if __name__ == "__main__":
    dataManager = DataManager()
    customers = dataManager.get_dataframe("Customers")
    orders = dataManager.get_dataframe("Orders")
    orderReviews = dataManager.get_dataframe("OrderReviews")

    reviewsByOrder = pd.merge(orders, orderReviews, how="inner", on="order_id")

    print(reviewsByOrder)
