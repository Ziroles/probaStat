import matplotlib.pyplot as plt
import pandas as pd
from utils.DataManager import DataManager

if __name__ == "__main__":
    dataManager = DataManager()
    customers = dataManager.get_dataframe("Customers")

    print(customers.groupby('customer_state')['customer_id'])
