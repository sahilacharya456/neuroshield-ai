from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv(Path(__file__).resolve().parents[1] / 'sample-data' / 'ai_training_data.csv')
features = ['failed_logins','unusual_hour','source_reputation','endpoint_risk','malware_indicator']
X = data[features]
y = data['severity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.34, random_state=42, stratify=y)
clf = RandomForestClassifier(n_estimators=120, random_state=42).fit(X_train, y_train)
anomaly = IsolationForest(contamination=.18, random_state=42).fit(X)
Path('models').mkdir(exist_ok=True)
joblib.dump(clf, 'models/severity_model.joblib')
joblib.dump(anomaly, 'models/anomaly_model.joblib')
print(classification_report(y_test, clf.predict(X_test)))
