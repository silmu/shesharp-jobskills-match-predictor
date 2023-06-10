# Job skills match predictor 👩‍⚕️👩‍⚕️💼📊

This project is made for SheSharp Hackathon 2023.
It provides a data analysis of the dataset provided by the organizers.
The dataset is a list of job posts worldwide for engineering and software developing positions.
It contains 500 job posts for May 2023.

`Important!`: this is my first project in any way connected with Machine Learning.
The model created is very weak, as the dataset is too small.
Nevertheless, it conveys the general idea. With a bigger dataset it can be improved significantly.

## ✨ Idea ✨

Firstly, historical data analysis is provided below that shows top 20 leaders by frequency in each category.
For example, we can see that engineering is the leading department in provided dataset, Bangalore is the leading city, software engineer is the top looked after profession, a bit more jobs are offered in non-remote that in remote positions.

Secondly, a simple machine learning model is provided for predicting what tags would match to a job seeker skills.
For example, if I am an engineer with skills in Python, JavaScript, HTML, CSS and the job description is "We are looking for a senior web developer with experience Python in JavaScript.", it would predict that a tag "Python" would fit in this case.

The project aims to help job seekers find suitable job opportunities that match their skills and experience.

## Requirements

- Installed `pip` and `python3`

## How to use

1. Run `pip install pandas matplotlib sklearn`
2. Import .csv file: `python3 import_job_posting_data.py`

## Features

- Data analysis: top 20 in each category. You can find data plotted for the provided dataset in `data_plots` folder.
  To plot your own data, run `python3 data_analysis.py`.

  ![Top 20 cities](/data_plots/city_plot.png)
  ![Top 20 companies](/data_plots/company_name_plot.png)
  ![Top 20 departments](/data_plots/department_plot.png)
  ![Top 20 job names](/data_plots/job_name_plot.png)
  ![Remote vs non-remote jobs](/data_plots/remote_plot.png)

- ML model already trained is in `model` folder. To train model on your owb data run `python3 train_model.py`. Put data in .csv format into `assets` folder with name `sourcestack-data.csv`. Or edit source link in `import_job_posting_data.py` and import with `python3 import_job_posting_data.py`.
- Predictions based on trained ML model: to get a prediction example run `python3 predict_tags.py`.
  To use your own input run `python3 predict_tags_input.py`. `Important!`: the model is very weak and might not give any reliable answer.

## Classification report:

Full report is in `model_classification_output.txt`

                precision    recall  f1-score   support

            10       0.00      0.00      0.00         0
             2       0.00      0.00      0.00         0
             3       0.00      0.00      0.00         0
           365       0.00      0.00      0.00         2
             8       0.00      0.00      0.00         0
           ARM       0.00      0.00      0.00         0
           ASA       0.00      0.00      0.00         1
           ASP       0.00      0.00      0.00         0
           AWS       0.67      0.22      0.33         9
     Accenture       0.00      0.00      0.00         0

     micro avg       0.38      0.08      0.14       337
     macro avg       0.03      0.01      0.01       337
    weighted avg     0.25      0.08      0.12       337
    samples avg      0.10      0.03      0.04       337
