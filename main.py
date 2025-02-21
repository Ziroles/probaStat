import matplotlib.pyplot as plt
import pandas as pd

from utils.DataManager import DataManager
from graphs.customerByState import customer_by_state
from graphs.reviewByAccuracyDeliveryData import reviewByAccuracyDeliveryData

if __name__ == "__main__":
    dataManager = DataManager()

    # reviewByAccuracyDeliveryData(dataManager)
    customer_by_state(dataManager)
