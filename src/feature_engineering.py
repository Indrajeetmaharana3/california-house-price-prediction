
import pandas as pd


def add_engineered_features(X):
    X = X.copy()

    X["BedroomsPerRoom"] = (
        X["AveBedrms"] / X["AveRooms"].replace(0, float("nan"))
    )

    return X
