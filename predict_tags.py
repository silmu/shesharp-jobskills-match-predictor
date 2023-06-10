import joblib

# Load the saved model from file
model = joblib.load('model/model.joblib')
vectorizer = joblib.load('model/vectorizer.joblib')
mlb = joblib.load('model/mlb.joblib')

# Define a jobseeker's skills
jobseeker_skills = ['Python', 'JavaScript', 'HTML', 'CSS']

# Define a job text
job_text = "We are looking for a senior web developer with experience Python in JavaScript."

print("Jobseeker's skills:", jobseeker_skills)
print("Job text:", job_text)

# Transform job text using the fitted vectorizer
job_text_features = vectorizer.transform([job_text])

# Predict the tags for the job
predicted_tags = mlb.inverse_transform(model.predict(job_text_features))

# Check if any of the jobseeker's skills match the predicted tags
matching_skills = set(jobseeker_skills).intersection(predicted_tags[0])

print(
    f"The jobseeker matches the following skills for the job: {matching_skills}")
