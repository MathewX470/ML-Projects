# House Price Prediction

A clean, minimal Jupyter Notebook workflow to predict house prices using scikit-learn. The notebook loads `data.csv`, splits the dataset, trains a simple `LinearRegression`, evaluates MAE/RMSE/R², and shows how to predict a single new house.

## Project Structure

- `house.ipynb` — Main notebook to run end-to-end
- `data.csv` — Input dataset (numerical features + `House_Price` target)
- `requirements.txt` — Python dependencies


## Quick Start (Windows)

```powershell
# From the project root
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Launch VS Code and open the notebook
code .
```

In VS Code:
- Select the `.venv` Python interpreter for the notebook kernel.
- Open `house.ipynb` and run cells top-to-bottom.

## Notebook Flow

1. Import libraries
2. Load `data.csv` and split train/test
3. Fit `LinearRegression` on training data
4. Evaluate on test (`MAE`, `RMSE`, `R²`)
5. Predict a single new house
