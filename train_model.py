import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.multiclass import OneVsRestClassifier
from ast import literal_eval
import re
import warnings
from sklearn.exceptions import DataConversionWarning
import joblib

warnings.filterwarnings("ignore", category=DataConversionWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Load the data
data = pd.read_csv('assets/sourcestack-data.csv')

# Preprocessing: convert 'job_name', 'seniority', 'department', and 'remote' into a single text feature
data['text'] = data['job_name'].astype(str) + ' ' + data['seniority'].astype(
    str) + ' ' + data['department'].astype(str) + ' ' + data['remote'].astype(str)

# Preprocessing: 'tags_matched' is a string representation of a list
data['tags_matched'] = data['tags_matched'].fillna('[]').apply(
    lambda x: re.findall(r'[a-zA-Z0-9_]+', x) if x else ['no tags'])

# Convert 'tags_matched' into a binary matrix
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(data['tags_matched'])

# Vectorize 'text' into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['text'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
model = OneVsRestClassifier(RandomForestClassifier(
    n_estimators=100, random_state=42))
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)

with open("model_classification_output.txt", "w") as f:
    # Write the classification report to the file
    report = classification_report(y_test, y_pred, target_names=mlb.classes_)
    f.write(report)

print(classification_report(y_test, y_pred, target_names=mlb.classes_))

joblib.dump(model, 'model/model.joblib')

# Save the vectorizer to a file
joblib.dump(vectorizer, 'model/vectorizer.joblib')

# Save the MultiLabelBinarizer to a file
joblib.dump(mlb, 'model/mlb.joblib')
