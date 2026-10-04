# Shri Ice Cream — Revenue Intelligence

A premium, responsive presentation and prediction interface derived from `Icecream_Revenue_Prediction.ipynb`.

## Project analysis

The notebook reads `https://github.com/ybifoundation/Dataset/raw/main/Ice%20Cream.csv`. It has two columns: `Temperature` and `Revenue`. `Revenue` is the target (`y`); the only feature (`X`) is `Temperature`. The notebook output reports 500 records, split into 350 training and 150 test records. No missing-value handling, duplicate removal, encoding, feature engineering, scaling, or categorical variables are present in the notebook.

The model is `sklearn.linear_model.LinearRegression()` with default parameters. The split is `train_test_split(X, y, train_size=0.7, random_state=2529)`. The fitted notebook outputs are:

- intercept: `42.444772590839705`
- coefficient: `21.54587147`
- MAE: `19.138687444270737`
- MAPE: `0.042214848219420134` (4.22%)
- MSE: `583.7362763558341`

The notebook does not calculate R² or RMSE, does not define a currency/unit, and does not contain authentication, persistence, a deployable model file, or an admin workflow. The UI therefore does not invent those items. The repository does not contain a copy of the remote CSV, so the relationship visualization is explicitly labelled as a fitted-equation view rather than a fabricated point chart.

## Implemented architecture

- **Overview** — brand, notebook scope, CTA, and restrained 3D CSS ice-cream treatment.
- **Prediction Studio** — temperature input + synchronized slider, validation bounds, live notebook-equation result.
- **Model Snapshot** — only the metrics present in the notebook.
- **Relationship View** — fitted equation visualization with an explicit note about unavailable raw CSV.
- **Method** — feature, split, model and evaluation steps.
- **Operations note** — makes the missing authentication/persistence layer visible rather than pretending a fake admin exists.

## Stack

Semantic HTML, CSS, vanilla JavaScript, CSS 3D transforms/animation, and a dependency-free Python standard-library HTTP service. This keeps the demo light and deployable while preserving the notebook logic.

## Run locally

```bash
python3 server.py
# open http://localhost:8000
```

The server binds to `0.0.0.0` for hosted previews. API endpoints:

- `GET /api/health` — model availability check.
- `POST /api/predict` — accepts `{ "temperature": 25 }`; returns the notebook-equivalent prediction and model metadata.

Example:

```bash
curl -X POST http://localhost:8000/api/predict \
  -H 'Content-Type: application/json' -d '{"temperature":25}'
```

## Validation

For a temperature `t`, both the browser and API calculate `42.444772590839705 + (21.54587147 * t)`. This is the fitted notebook relationship. The notebook itself depends on a remote dataset; the service uses its recorded fitted parameters and does not silently retrain.

## Security and production limitations

This checkout contains no authentication, database, secret configuration, or model artifact. Consequently an admin panel, prediction history, uploads, and retraining are not claimed as implemented. Before production use, add server-side authentication with password hashing, secure sessions/CSRF protection, persistent storage, rate limiting, and a versioned serialized pipeline. Keep dataset replacement and retraining explicit and audited. Do not expose credentials in the frontend.

The GitHub project link shown in the UI is the supplied repository: https://github.com/rajyogi9070/icecreampriceprediction
