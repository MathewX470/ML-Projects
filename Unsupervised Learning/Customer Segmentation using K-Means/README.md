# Customer Segmentation using K-Means Clustering

## Project Overview
This project implements **K-Means clustering** to segment customers based on their purchasing behavior. The analysis uses mall customer data to identify distinct customer groups, enabling targeted marketing strategies.

## Dataset
**File:** `Mall_Customers.csv`

The dataset contains customer information including:
- Customer ID
- Annual Income (k$)
- Spending Score (1-100)
- Additional demographic information


## Methodology

### 1. Data Loading and Exploration
- Load the Mall Customers dataset using pandas
- Explore the data structure and features
- Select relevant features for clustering

### 2. Feature Selection
Features used for clustering:
- **Annual Income (k$)**: Customer's yearly income
- **Spending Score (1-100)**: Score assigned based on customer spending behavior

### 3. Feature Scaling
- Applied **StandardScaler** to normalize features
- Ensures all features contribute equally to distance calculations
- Critical for K-Means performance

### 4. Optimal Cluster Selection (Elbow Method)
- Tested cluster numbers from 1 to 10
- Calculated **Within-Cluster Sum of Squares (WCSS)** for each K
- Plotted WCSS vs. number of clusters
- Identified optimal K = **5** clusters based on the elbow point

### 5. K-Means Clustering
- Applied K-Means algorithm with **5 clusters**
- Set `random_state=42` for reproducibility
- Assigned each customer to a cluster

### 6. Visualization
- Created scatter plot showing customer segments
- Color-coded clusters using viridis colormap
- Displayed cluster centroids (marked with red X)
- Visualized relationship between Annual Income and Spending Score

## Technologies Used
- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Data visualization
- **scikit-learn**: Machine learning algorithms
  - `KMeans`: Clustering algorithm
  - `StandardScaler`: Feature scaling

## Results
The analysis identifies **5 distinct customer segments** based on income and spending patterns, enabling businesses to:
- Develop targeted marketing campaigns
- Customize product offerings
- Optimize customer engagement strategies
- Improve resource allocation

## How to Run
1. Ensure all dependencies are installed:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook customer_segmentation.ipynb
   ```

3. Run all cells sequentially to reproduce the analysis

## Key Insights
The customer segments can be interpreted as:
- **High Income, High Spending**: Premium customers
- **High Income, Low Spending**: Potential targets for engagement
- **Medium Income, Medium Spending**: Average customers
- **Low Income, High Spending**: Price-sensitive but engaged
- **Low Income, Low Spending**: Requiring special attention
