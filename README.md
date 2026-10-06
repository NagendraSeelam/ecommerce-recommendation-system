#  E-Commerce Recommendation System

An end-to-end **E-Commerce Product Recommendation System** built using Python and Machine Learning. The system generates personalized product recommendations by combining **Collaborative Filtering** and **Content-Based Filtering** into a hybrid recommendation engine.

The project is deployed as an interactive **Streamlit web application**.

##  Live Demo

**Streamlit App:**
[https://ecommerce-recommendation-system-9lnyyy7wnrnjsnl3pawgc4.streamlit.app/]

---

## Pro ject Overview

E-commerce platforms contain thousands of products, making it difficult for customers to discover products that match their interests.

This project addresses that problem by analyzing customer purchase history and product information to recommend relevant products.

The system supports two types of users:

* **Existing customers** → personalized recommendations based on their previous purchases
* **New customers** → popular-product recommendations when there is no purchase history

The personalized recommendation engine uses a **hybrid approach**:

> **90% Collaborative Filtering + 10% Content-Based Filtering**

---

##  Objectives

* Build a real-world product recommendation system.
* Analyze customer-product purchase interactions.
* Identify products similar to those previously purchased.
* Combine different recommendation techniques.
* Handle the cold-start problem for new customers.
* Deploy the recommendation system as a web application.

---

## 📊 Dataset

The project uses the **Online Retail dataset**, containing transactional records from an e-commerce retailer.

Important columns include:

| Column        | Description                    |
| ------------- | ------------------------------ |
| `Invoice`     | Transaction/invoice identifier |
| `StockCode`   | Product identifier             |
| `Description` | Product description            |
| `Quantity`    | Number of items purchased      |
| `InvoiceDate` | Date and time of transaction   |
| `UnitPrice`   | Price per unit                 |
| `CustomerID`  | Customer identifier            |
| `Country`     | Customer's country             |

After preprocessing, the recommendation system works with approximately:

* **3,896 customers**
* **4,017 products**

---

##  Recommendation Approach

The system combines two recommendation techniques.

### 1. Collaborative Filtering

Collaborative Filtering recommends products based on **customer-product interaction patterns**.

The system creates a user-item interaction matrix:

```text
              Product A  Product B  Product C
Customer 1        1          0          1
Customer 2        1          1          0
Customer 3        0          1          1
```

Products are then recommended based on similarities learned from customer purchase behavior.

The saved Collaborative Filtering model contains approximately **3,947 products**.

---

### 2. Content-Based Filtering

Content-Based Filtering recommends products based on **product similarity**.

Product information, particularly product descriptions, is used to identify products that are similar to one another.

For example:

```text
STRAWBERRY CERAMIC TRINKET BOX
        ↓
Similar product
        ↓
SWEETHEART CERAMIC TRINKET BOX
```

The content-based component contains approximately **4,017 products**.

---

##   Hybrid Recommendation

The two recommendation approaches are combined to create a hybrid system.

```text
Collaborative Filtering
        │
        │ 90%
        ▼
   Hybrid Score
        ▲
        │ 10%
        │
Content-Based Filtering
```

The final recommendation score is calculated using the hybrid weighting:

```text
Hybrid Score =
    0.90 × Collaborative Similarity
    +
    0.10 × Content Similarity
```

Products already purchased by the customer are removed before generating the final recommendations.

The system then returns the **Top 5 products**.

---

##  New Customer Recommendation

A new customer does not have enough purchase history for personalized Collaborative Filtering.

To handle this **cold-start problem**, the application provides popular-product recommendations instead.

```text
New Customer
     ↓
Popular Products
     ↓
Top 5 Recommendations
```

---

##  System Workflow

```text
                Online Retail Dataset
                         │
                         ▼
               Data Cleaning & Processing
                         │
                         ▼
              Customer-Product Interactions
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
   Collaborative Filtering    Content-Based Filtering
             │                       │
             │ 90%                   │ 10%
             └───────────┬───────────┘
                         ▼
                  Hybrid Scoring
                         │
                         ▼
             Remove Purchased Products
                         │
                         ▼
                  Top 5 Products
                         │
                         ▼
                  Streamlit App
```

---

##  Technologies Used

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* Collaborative Filtering
* Content-Based Filtering
* Nearest Neighbors / similarity-based recommendation

### Model Management

* Joblib
* Gzip model compression

### Deployment

* Streamlit
* GitHub
* Streamlit Community Cloud

---

## Application Features

### Customer Selection

Users can select a customer from the available customer list.

### Personalized Recommendations

For existing customers, the application analyzes previously purchased products and generates personalized recommendations.

### New Customer Support

New customers receive popular-product recommendations.

### Recommendation Score

The application displays the calculated hybrid recommendation score for personalized recommendations.

### Interactive Web Interface

The complete recommendation system is accessible through a Streamlit web application.

---

##  Example Recommendation

Example output from the deployed application:

| Rank | StockCode | Product                            |
| ---: | --------- | ---------------------------------- |
|    1 | 85123A    | WHITE HANGING HEART T-LIGHT HOLDER |
|    2 | 22423     | REGENCY CAKESTAND 3 TIER           |
|    3 | 21212     | PACK OF 72 RETRO SPOT CAKE CASES   |
|    4 | 22138     | BAKING SET 9 PIECE RETROSPOT       |
|    5 | 85099B    | JUMBO BAG RED WHITE SPOTTY         |

---

##  Project Structure

```text
ecommerce-recommendation-system/
│
├── app.py
├── ecommerce_recommendation_system.pkl.gz
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit application and recommendation logic.

### `ecommerce_recommendation_system.pkl.gz`

Compressed serialized recommendation-system components used by the deployed application.

### `requirements.txt`

Contains the Python dependencies required to run the application.

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/NagendraSeelam/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit

```bash
streamlit run app.py
```

The application will open in your browser.

---

##  Key Learning Outcomes

Through this project, I worked with:

* Real-world transactional data
* Data preprocessing
* Customer-product interaction matrices
* Similarity-based recommendation
* Collaborative Filtering
* Content-Based Recommendation
* Hybrid Recommendation Systems
* Cold-start handling
* Model serialization
* Model compression
* Streamlit application development
* Cloud deployment

---

##  Future Improvements

Potential improvements include:

* Add product images
* Add product prices
* Improve recommendation ranking
* Add user feedback such as likes/clicks
* Introduce popularity and recency signals
* Experiment with different hybrid weights
* Evaluate recommendations using metrics such as Precision@K and Recall@K
* Add a more advanced recommendation model

---

##  Author

**Nagendra Seelam**

B.Tech | Aspiring Data Analyst / Data Scientist / ML Engineer

GitHub:
https://github.com/NagendraSeelam

---

##  Project Summary

This project demonstrates an end-to-end Machine Learning workflow:

**Data → Processing → Recommendation Models → Hybrid System → Application → Cloud Deployment**

The final system provides personalized product recommendations through an interactive Streamlit application.
