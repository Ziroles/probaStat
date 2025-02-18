import matplotlib.pyplot as plt
import pandas as pd


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
        reviewsByOrder["order_estimated_delivery_date"]
        - reviewsByOrder["order_delivered_customer_date"]
    ).dt.days

    # plus en avance/retard
    average_review_by_delay = (
        reviewsByOrder.groupby("delivery_delay")["review_score"].mean().reset_index()
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        average_review_by_delay["delivery_delay"],
        average_review_by_delay["review_score"],
        marker="o",
        linestyle="-",
    )

    ax.set_xlabel("Avance de livraison (en jours)")
    ax.set_ylabel("Note moyenne de satisfaction (review_score)")
    ax.set_title("Impact du retard de livraison sur la satisfaction client")

    plt.axvline(0, color="red", linestyle="dashed", label="Livraison à l'heure")
    plt.legend()

    plt.show()
