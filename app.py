
import streamlit as st
import pandas as pd
import joblib
import gzip

st.set_page_config(
    page_title="E-Commerce Recommendation System",
    page_icon="🛍️",
    layout="wide"
)


@st.cache_resource
def load_system():
    with gzip.open("ecommerce_recommendation_system.pkl.gz", "rb") as f:
        return joblib.load(f)


# Load recommendation system
system = load_system()

train_user_item = system["train_user_item"]
cf_distances = system["cf_distances"]
cf_indices = system["cf_indices"]
content_distances = system["content_distances"]
content_indices = system["content_indices"]
product_info = system["product_info"]
popular_products = system["popular_products"]
hybrid_weight = system["hybrid_weight"]


# Product mappings
cf_products = train_user_item.columns.astype(str).tolist()
content_products = product_info["StockCode"].astype(str).tolist()

cf_product_to_index = {
    product: i for i, product in enumerate(cf_products)
}

cf_index_to_product = {
    i: product for i, product in enumerate(cf_products)
}

content_product_to_index = {
    product: i for i, product in enumerate(content_products)
}

content_index_to_product = {
    i: product for i, product in enumerate(content_products)
}


# -----------------------------
# Header
# -----------------------------

st.title("🛍️ E-Commerce Recommendation System")

st.write(
    "Personalized product recommendations using "
    "Collaborative Filtering and Content-Based Filtering."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Products", f"{len(content_products):,}")

with col2:
    st.metric("Customers", f"{len(train_user_item.index):,}")

with col3:
    st.metric(
        "Hybrid Model",
        f"{hybrid_weight:.0%} CF / {(1-hybrid_weight):.0%} Content"
    )

st.divider()


# -----------------------------
# Customer Selection
# -----------------------------

customer_ids = train_user_item.index.tolist()

selected_customer = st.selectbox(
    "Select a Customer",
    ["NEW CUSTOMER"] + customer_ids
)


# -----------------------------
# New Customer
# -----------------------------

if selected_customer == "NEW CUSTOMER":

    st.subheader("🔥 Popular Products")

    st.caption(
        "Recommendations for new customers are based on popular products."
    )

    popular_codes = [str(x) for x in popular_products.index[:5]]

    result = product_info[
        product_info["StockCode"].astype(str).isin(popular_codes)
    ].copy()

    rank = {
        code: i + 1
        for i, code in enumerate(popular_codes)
    }

    result["Rank"] = (
        result["StockCode"]
        .astype(str)
        .map(rank)
    )

    result = result.sort_values("Rank")

    st.dataframe(
        result[["Rank", "StockCode", "Description"]],
        use_container_width=True,
        hide_index=True
    )


# -----------------------------
# Existing Customer
# -----------------------------

else:

    st.subheader("🎯 Personalized Recommendations")

    purchased = train_user_item.loc[selected_customer]

    purchased_products = (
        purchased[purchased > 0]
        .index
        .astype(str)
        .tolist()
    )

    scores = {}

    # Collaborative Filtering + Content-Based Filtering
    for product in purchased_products:

        # Collaborative Filtering
        if product in cf_product_to_index:

            cf_idx = cf_product_to_index[product]

            for distance, neighbor_idx in zip(
                cf_distances[cf_idx],
                cf_indices[cf_idx]
            ):

                neighbor_product = cf_index_to_product[
                    int(neighbor_idx)
                ]

                if neighbor_product == product:
                    continue

                similarity = max(0, 1 - distance)

                scores[neighbor_product] = (
                    scores.get(neighbor_product, 0)
                    + hybrid_weight * similarity
                )

        # Content-Based Filtering
        if product in content_product_to_index:

            content_idx = content_product_to_index[product]

            for distance, neighbor_idx in zip(
                content_distances[content_idx],
                content_indices[content_idx]
            ):

                neighbor_product = content_index_to_product[
                    int(neighbor_idx)
                ]

                if neighbor_product == product:
                    continue

                similarity = max(0, 1 - distance)

                scores[neighbor_product] = (
                    scores.get(neighbor_product, 0)
                    + (1 - hybrid_weight) * similarity
                )

    # Remove products already purchased
    for product in purchased_products:
        scores.pop(product, None)

    # Top 5 recommendations
    recommendations = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    recommendation_codes = [
        product for product, score in recommendations
    ]

    score_dict = dict(recommendations)

    result = product_info[
        product_info["StockCode"]
        .astype(str)
        .isin(recommendation_codes)
    ].copy()

    result["Recommendation Score"] = (
        result["StockCode"]
        .astype(str)
        .map(score_dict)
        .round(2)
    )

    result["Rank"] = (
        result["StockCode"]
        .astype(str)
        .map(
            {
                code: i + 1
                for i, code in enumerate(recommendation_codes)
            }
        )
    )

    result = result.sort_values("Rank")

    st.dataframe(
        result[
            [
                "Rank",
                "StockCode",
                "Description",
                "Recommendation Score"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        f"Recommendations generated from "
        f"{len(purchased_products)} previously purchased products."
    )

    st.info(
        "The recommendation engine combines Collaborative Filtering "
        "and Content-Based Filtering using a 90/10 hybrid weighting."
    )
