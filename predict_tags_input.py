import joblib

# Load the saved model from file
model = joblib.load('model/model.joblib')
vectorizer = joblib.load('model/vectorizer.joblib')
mlb = joblib.load('model/mlb.joblib')

# Get user input for jobseeker's skills
jobseeker_skills = input(
    "Enter jobseeker's skills (comma-separated): ").split(',')

# Get user input for job text
job_text = input("Enter the job text: ")

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
