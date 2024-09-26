import joblib

class Model:
    def __init__(self):
        self.model = joblib.load('model/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)

# Add in this code chunk temporarily (delete it after this run)
# beneficiary_example = {
#     "age": 30,
#     "sex": "female",
#     "bmi": 20,
#     "children": 1,
#     "smoker": "yes",
#     "region": "southwest"
# }
# model_inputs = list(beneficiary_example.values())

# print(model_inputs)                  # [30, 'female', 20, 1, 'yes', 'southwest']
# print(Model().predict(model_inputs)) # 17353.51581464062