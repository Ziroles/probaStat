import pandas as pd
import folium
from folium.plugins import HeatMap


def test(dataManager):
    # Charger les fichiers de données
    customers_df = dataManager.get_dataframe("Customers")
    orders_df = dataManager.get_dataframe("Orders")

    # Coordonnées moyennes des États brésiliens
    state_coords = {
        "AC": [-9.02, -70.81],
        "AL": [-9.57, -36.53],
        "AP": [1.41, -51.77],
        "AM": [-3.47, -65.10],
        "BA": [-12.97, -41.48],
        "CE": [-5.20, -39.53],
        "DF": [-15.78, -47.93],
        "ES": [-19.19, -40.34],
        "GO": [-15.93, -50.14],
        "MA": [-5.42, -45.44],
        "MT": [-12.64, -55.42],
        "MS": [-20.51, -54.54],
        "MG": [-18.10, -44.38],
        "PA": [-3.79, -52.48],
        "PB": [-7.28, -36.72],
        "PR": [-24.89, -51.55],
        "PE": [-8.38, -37.86],
        "PI": [-6.60, -42.28],
        "RJ": [-22.91, -43.19],
        "RN": [-5.81, -36.59],
        "RS": [-30.03, -51.22],
        "RO": [-10.83, -63.34],
        "RR": [2.82, -61.32],
        "SC": [-27.45, -50.95],
        "SP": [-23.55, -46.63],
        "SE": [-10.57, -37.45],
        "TO": [-10.25, -48.25],
    }

    # Nombre de ventes par état
    sales_by_state = customers_df.merge(orders_df, on="customer_id")
    sales_by_state = (
        sales_by_state.groupby("customer_state").size().reset_index(name="num_sales")
    )

    # Ajouter les coordonnées des états
    sales_by_state["lat"] = sales_by_state["customer_state"].map(
        lambda x: state_coords.get(x, [None, None])[0]
    )
    sales_by_state["lon"] = sales_by_state["customer_state"].map(
        lambda x: state_coords.get(x, [None, None])[1]
    )

    # Créer la carte centrée sur le Brésil
    brasil_map = folium.Map(location=[-14.23, -51.92], zoom_start=4)

    # Ajouter les ventes sous forme de heatmap
    heat_data = sales_by_state.dropna()[["lat", "lon", "num_sales"]].values.tolist()
    HeatMap(heat_data, radius=25, blur=15).add_to(brasil_map)

    # Sauvegarder la carte en HTML
    brasil_map.save("heatmap_ventes_bresil.html")

    # Affichage de la carte (uniquement en environnement Jupyter)
    brasil_map
