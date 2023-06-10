import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('assets/sourcestack-data.csv')

# Function to plot the top N categories of a column

def plot_top_categories(column, n=20):
    top_categories = data[column].value_counts().head(n)
    top_categories.plot(kind='bar')
    plt.title(f'Top {n} {column}')
    plt.tight_layout()
    plt.savefig(f'plots/{column}_plot.png')
    plt.clf()

plot_top_categories('job_name')
plot_top_categories('department')
plot_top_categories('remote')
plot_top_categories('company_name')
plot_top_categories('city')