import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

target = train.pop('price')

train = pd.get_dummies(train)
test = pd.get_dummies(test)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(random_state=0)
model.fit(X_train, y_train)

# pred_val = model.predict(X_val)

# from sklearn.metrics import root_mean_squared_error
# rmse = root_mean_squared_error(y_val, pred_val)
# print("rmse: ", rmse)

pred = model.predict(test)
submit = pd.DataFrame({'pred': pred})
submit.to_csv("result.csv", index=False)

print(pd.read_csv("result.csv").head())