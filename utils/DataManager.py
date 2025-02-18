import pandas as pd


class DataManager:
    def __init__(self):
        self.dataFrames = {}
        self.__fileName = {"Customers": "./data/olist_customers_dataset.csv",
                           "Geolocation": "./data/olist_geolocation_dataset.csv",
                           "OrderItems": "./data/olist_order_items_dataset.csv",
                           "OrderPayments": "./data/olist_order_payments_dataset.csv",
                           "OrderReviews": "./data/olist_order_reviews_dataset.csv",
                           "Orders": "./data/olist_orders_dataset.csv",
                           "Products": "./data/olist_products_dataset.csv",
                           "Sellers": "./data/olist_sellers_dataset.csv",
                           "ProductCategoryNameTranslation": "./data/product_category_name_translation.csv"}
        self.load_data()

    def get_dataframe(self, key: str) -> pd.DataFrame:
        return self.dataFrames[key]

    def load_data(self):
        for csvFileKey in self.__fileName:
            self.dataFrames[csvFileKey] = pd.read_csv(self.__fileName[csvFileKey],
                                                      delimiter=',',
                                                      header=0)
