''' Egy példa egy egyszerű Python program megoldásra, döntési fát építünk Jupyter Notebook-ban.
Először telepíteni kell a megfelelő csomagokat a Jupyter Notebook-kal való munkához. Az alábbi terminál parancsokkal:
'''
```
pip install jupyter
pip install scikit-learn
pip install pandas
```

'''Készítsünk egy új Jupyter Notebook file-t, majd írjuk meg a következő kódrészletet:'''

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# adat betöltése
data = pd.read_csv("iris.csv", delimiter=",")

# adatok előkészítése
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# döntési fa létrehozása és tanítása
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# teszt és pontosság számítása
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Tesztpontosság:", accuracy)

# döntési fa kirajzolása
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

dot_data = export_graphviz(model, out_file=None, 
                         feature_names=X.columns.tolist(),  
                         class_names=y.unique().tolist(),  
                         filled=True, rounded=True,  
                         special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png())  
```
