import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def analyze_statistics(dfm):

    order_items_df = dfm.get_dataframe("OrderItems")
    order_reviews_df = dfm.get_dataframe("OrderReviews")
    orders_df = dfm.get_dataframe("Orders")

    orders_df["order_purchase_timestamp"] = pd.to_datetime(
        orders_df["order_purchase_timestamp"]
    )
    orders_df["order_delivered_customer_date"] = pd.to_datetime(
        orders_df["order_delivered_customer_date"]
    )

    orders_df["delivery_time"] = (
        orders_df["order_delivered_customer_date"]
        - orders_df["order_purchase_timestamp"]
    ).dt.days

    reviews_df = (
        order_reviews_df.groupby("order_id")["review_score"].mean().reset_index()
    )
    data = order_items_df.merge(orders_df, on="order_id").merge(
        reviews_df, on="order_id", how="left"
    )

    variables = ["price", "freight_value", "delivery_time", "review_score"]

    def remove_outliers(df, column):
        Q1 = df[column].quantile(0.01)
        Q3 = df[column].quantile(0.99)
        return df[(df[column] >= Q1) & (df[column] <= Q3)]

    data_filtered = data.copy()
    for col in variables:
        data_filtered = remove_outliers(data_filtered, col)

    stats_desc = data_filtered[variables].describe()
    print(stats_desc)

    colors = {
        "price": "lightblue",
        "freight_value": "lightgreen",
        "delivery_time": "lightcoral",
        "review_score": "gold",
    }

    for col in variables:
        plt.figure(figsize=(6, 4))
        plt.hist(
            data_filtered[col].dropna(),
            bins=30,
            edgecolor="black",
            alpha=0.7,
            color=colors[col],
        )
        plt.title(f"Histogramme de {col}", fontsize=12)
        plt.xlabel(col, fontsize=10)
        plt.ylabel("Fréquence", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.savefig(f"img/{col}_histogram.png")
        plt.close()

        plt.figure(figsize=(6, 4))
        plt.boxplot(
            data_filtered[col].dropna(),
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor=colors[col]),
        )
        plt.title(f"Boxplot de {col}", fontsize=12)
        plt.ylabel(col, fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.savefig(f"img/{col}_boxplot.png")
        plt.close()

    def confidence_interval(data, confidence=0.95):
        n = len(data)
        mean = np.mean(data)
        std_err = stats.sem(data)
        margin = std_err * stats.t.ppf((1 + confidence) / 2.0, n - 1)
        return mean - margin, mean + margin

    confidence_levels = [0.90, 0.95]
    confidence_results = {}

    for col in variables:
        if col != "review_score":
            for conf in confidence_levels:
                ci = confidence_interval(data_filtered[col].dropna(), confidence=conf)
                confidence_results[f"{col}_{int(conf*100)}%"] = ci
                print(f"Intervalle de confiance à {int(conf*100)}% pour {col}: {ci}")

    return confidence_results
