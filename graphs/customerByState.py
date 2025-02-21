from utils.DataManager import DataManager


def customer_by_state(dataManager: DataManager):
    customers = dataManager.get_dataframe("Customers")
    print(customers.groupby('customer_state')['customer_id'])
