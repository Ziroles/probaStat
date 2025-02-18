import pandas as pd

class DataManager:


    
    def __init__(self):
        self.data = {}
        self.fileName = {"olistCustomersDataset":"olist_customers_dataset.csv", "olistGeolocationDataset":"olist_geolocation_dataset.csv", "olistOrderItemsDataset":"olist_order_items_dataset.csv", "olistOrderPaymentsDataset":"olist_order_payments_dataset.csv","olistOrderReviewsDataset": "olist_order_reviews_dataset.csv","olistOrdersDataset": "olist_orders_dataset.csv","olistProductsDataset": "olist_products_dataset.csv", "olistSellersDataset":"olist_sellers_dataset.csv", "productCategoryNameTranslation":"product_category_name_translation.csv"}
        self.load_data()
        

    def data(self,key):
        return self.data[key]
    
    

    def load_data(self):
        for i in self.fileName:
            self.data[i] = pd.read_csv(self.fileName[i])