import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from utils.optimalNumberOfClasses import nombre_de_classes  # Fonction pour calculer k


def reviewByAccuracyDeliveryData(dm):
    customers = dm.get_dataframe("Customers")
    orders = dm.get_dataframe("Orders")
    orderReviews = dm.get_dataframe("OrderReviews")

    reviewsByOrder = pd.merge(orders, orderReviews, how="inner", on="order_id")

    reviewsByOrder = reviewsByOrder[reviewsByOrder["order_status"] == "delivered"]

    reviewsByOrder["order_delivered_customer_date"] = pd.to_datetime(
        reviewsByOrder["order_delivered_customer_date"]
    )
    reviewsByOrder["order_estimated_delivery_date"] = pd.to_datetime(
        reviewsByOrder["order_estimated_delivery_date"]
    )

    reviewsByOrder["delivery_delay"] = (
        reviewsByOrder["order_delivered_customer_date"]
        - reviewsByOrder["order_estimated_delivery_date"]
    ).dt.days

    reviewsByOrder = reviewsByOrder.sort_values(by=["delivery_delay"])

    nb_valeurs = reviewsByOrder["delivery_delay"].dropna().shape[0]
    nb_classes = nombre_de_classes(nb_valeurs)

    bin_edges = np.linspace(
        reviewsByOrder["delivery_delay"].min(),
        reviewsByOrder["delivery_delay"].max(),
        nb_classes + 1,
    )

    reviewsByOrder["delay_class"] = pd.cut(
        reviewsByOrder["delivery_delay"], bins=bin_edges
    )

    average_review_by_class = (
        reviewsByOrder.groupby("delay_class")["review_score"].mean().reset_index()
    )

    average_review_by_class["class_center"] = [
        (interval.left + interval.right) / 2
        for interval in average_review_by_class["delay_class"]
    ]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        average_review_by_class["class_center"],
        average_review_by_class["review_score"],
        marker="o",
        linestyle="-",
        label="Satisfaction moyenne",
    )

    ax.set_xlabel("Retart de livraison (en jours)")
    ax.set_ylabel("Note moyenne de satisfaction (review_score)")
    ax.set_title("Impact du retard de livraison sur la satisfaction client (lissé)")

    plt.axvline(
        0, color="red", linestyle="dashed", linewidth=2, label="Livraison à l'heure"
    )

    plt.legend()

    plt.show()
