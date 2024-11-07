import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn import tree
#import lime
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt
#dataset load and clean
data = pd.read_csv('nimbu.csv')
data = data.dropna()


X = data.iloc[:, 2:] 
y = data.iloc[:, 1]   

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred)*100)
print("Classification Report:")
print(classification_report(y_test, y_pred))

plt.figure(figsize=(10, 8))
tree.plot_tree(clf, feature_names=X.columns, class_names=['M', 'B'], filled=True)
plt.show()

explainer = LimeTabularExplainer(X_train.values, feature_names=X.columns, class_names=['B', 'M'], discretize_continuous=True)

def predict_proba_wrapper(data):
    return clf.predict_proba(pd.DataFrame(data, columns=X.columns))

idx = 7 
exp = explainer.explain_instance(X_test.values[idx], predict_proba_wrapper, num_features=len(X.columns))  # Show all features

exp.show_in_notebook(show_table=True, show_all=False)

exp_map = exp.as_map()[1]
feature_names = [X.columns[i] for i, _ in exp_map]
weights = [weight for _, weight in exp_map]

plt.figure(figsize=(10, 8))
plt.barh(feature_names, weights, color='skyblue')
plt.xlabel('Weight')
plt.ylabel('Feature')
plt.title('LIME Analysis for Local Sample Class Benign{}'.format(idx))
plt.show()
