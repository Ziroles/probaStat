import pandas as pd

class DataManager:
    def __init__(self):
        self.dataFrames = {}
        self.fileName = {"Customers": "olist_customers_dataset.csv",
                         "Geolocation": "olist_geolocation_dataset.csv",
                         "OrderItems": "olist_order_items_dataset.csv",
                         "OrderPayments": "olist_order_payments_dataset.csv",
                         "OrderReviews": "olist_order_reviews_dataset.csv",
                         "Orders": "olist_orders_dataset.csv",
                         "Products": "olist_products_dataset.csv",
                         "Sellers": "olist_sellers_dataset.csv",
                         "ProductCategoryNameTranslation": "product_category_name_translation.csv"}
        self.load_data()

    def get_data(self, key):
        return self.dataFrames[key]

    def load_data(self):
        for csvFileKey in self.fileName:
            self.dataFrames[csvFileKey] = pd.read_csv(self.fileName[csvFileKey])
