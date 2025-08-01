import pandas as pd
from sklearn.linear_model import LogisticRegression

def test_model_trains_and_predicts():
    # Simple test dataset
    X = pd.DataFrame({
        "Amount": [100, 50, 300, 10],
        "Amount_log": [4.6, 3.9, 5.7, 2.3]
    })
    y = [0, 0, 1, 0]

    # Train logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    # Make predictions
    preds = model.predict(X)

    # Verify predictions are returned
    assert len(preds) == 4