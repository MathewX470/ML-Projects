# Iris Dataset Clustering

## Project Overview
This project demonstrates unsupervised learning techniques using K-Means clustering on the famous Iris dataset. The analysis includes exploratory data analysis, optimal cluster determination, and visualization of clustering results.

## Dataset
- **Source**: Scikit-learn's built-in Iris dataset
- **Features**: 4 numerical features
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
- **Samples**: 150 observations

## Technologies Used
- **Python 3.x**
- **Libraries**:
  - NumPy - Numerical computing
  - Pandas - Data manipulation and analysis
  - Matplotlib - Data visualization
  - Scikit-learn - Machine learning algorithms

## Analysis Workflow

### 1. Data Loading and Preparation
- Load Iris dataset from scikit-learn
- Create pandas DataFrame for easier manipulation
- Display initial data exploration

### 2. Feature Scaling
- Apply StandardScaler to normalize features
- Ensures all features contribute equally to clustering
- Important for distance-based algorithms like K-Means

### 3. Optimal Cluster Determination

#### Elbow Method
- Tests K values from 1 to 10
- Calculates Within-Cluster Sum of Squares (WCSS)
- Plots WCSS vs number of clusters
- Identifies the "elbow point" where adding more clusters provides diminishing returns

#### Silhouette Analysis
- Evaluates clustering quality for K = 2 to 10
- Silhouette score ranges from -1 to 1
- Higher scores indicate better-defined clusters
- Results show highest score at K=2, but K=3 chosen for more meaningful grouping

### 4. K-Means Clustering
- **Configuration**:
  - Number of clusters: 3
  - Random state: 42 (for reproducibility)
  - n_init: 10 (number of times algorithm runs with different centroid seeds)
- Assigns each sample to one of three clusters
- Adds cluster labels to the original DataFrame

### 5. Visualization
- 2D scatter plot using sepal length and sepal width
- Different colors represent different clusters
- Red 'X' markers show cluster centroids
- Legend for easy interpretation

### 6. Cluster Analysis
- Displays cluster centers (centroids) for all four features
- Centers are inverse-transformed back to original scale
- Allows interpretation of cluster characteristics

## Key Findings
- The dataset naturally forms 3 distinct clusters
- Silhouette analysis suggested K=2 has the highest score, but K=3 provides more meaningful biological grouping
- Cluster centroids show clear separation in feature space
- Visualization demonstrates the effectiveness of K-Means clustering

## Installation

1. Clone this repository
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage
Open and run the Jupyter notebook:
```bash
jupyter notebook iris.ipynb
```

Run cells sequentially to reproduce the analysis.

## Project Structure
```
.
├── iris.ipynb          # Main Jupyter notebook with analysis
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

## Results Interpretation
The K-Means algorithm successfully clusters the Iris dataset into three groups that likely correspond to the three Iris species (setosa, versicolor, and virginica), demonstrating the power of unsupervised learning to discover natural groupings in data without labeled training examples.

## Future Improvements
- Compare with other clustering algorithms (DBSCAN, Hierarchical clustering)
- Add 3D visualizations using all features
- Perform PCA for dimensionality reduction
- Include confusion matrix comparison with true species labels
- Experiment with different distance metrics

## License
This project is for educational purposes.

## Author
ML Projects Repository

## Acknowledgments
- Iris dataset: Fisher, R.A. (1936)
- Scikit-learn library documentation
