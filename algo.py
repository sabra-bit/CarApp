import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import pickle
data = pd.read_csv("car.data")
print(data.head())

le = preprocessing.LabelEncoder()
Age = data.Age.to_list()
Job = le.fit_transform(list(data["Job"]))
print(Job)
Qualification = le.fit_transform(list(data["Qualification"]))
Hstatus = le.fit_transform(list(data["Hstatus"]))
ManufacturingYear = data.ManufacturingYear.to_list()
Cc = data.Cc.to_list()
Vage = data.Vage.to_list()
Use = le.fit_transform(list(data["Use"]))
Mileage = data.Mileage.to_list()
Premium = data.Premium.to_list()
Tclaim = le.fit_transform(list(data["Tclaim"]))
InsuranceVal = data.InsuranceVal.to_list()
Decision = le.fit_transform(list(data["Decision"]))
 
X = list(zip(Age, Job, Qualification, Hstatus, ManufacturingYear, Cc ,Vage ,Use,Mileage,Premium,Tclaim,InsuranceVal))
y = list(Decision)

best = 0
for _ in range(20):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

    model = KNeighborsClassifier(n_neighbors=9)

    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    
    print("Accuracy: " + str(acc))

    if acc > best:
        best = acc
        with open("CarData.pickle", "wb") as f:
            pickle.dump(model, f)

print("best : " +str(best))
predicted = model.predict(x_test)
names = ["rejection", "acception"]




# for x in range(len(predicted)):
#     print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
#     n = model.kneighbors([x_test[x]], 9, True)
#     print("N: ", n)
# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
