def get_metrics(expected, predicted):
    mse = mean_squared_error(expected, predicted, squared=True)
    mae = mean_absolute_error(expected, predicted)
    r2 = r2_score(expected, predicted)

    return mse, mae, r2
