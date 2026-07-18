import os
import kaggle
import pandas as pd
# sanity check the env var is visible
data_path='./data'
if not os.path.exists(data_path) or not os.listdir(data_path):
    key = os.getenv('KAGGLE_API_TOKEN')
    if key is None:
        print("API key not found! Did you restart VS Code after setting it?")
        exit()
    api = kaggle.KaggleApi()
    api.authenticate()
    # download a dataset
    api.dataset_download_files('laveshjadon/ai-impact-on-students', path=data_path, unzip=True)
    print("Data downloaded successfully")
else:
    print("Data already downloaded , skiping download")


data=pd.read_csv('./data/ai_impact_on_students.csv')

# Data filtering 
f1=data[data['Weekly_GenAI_Hours']>= 20]
f2=data[data['Paid_Subscription']==True]
print(f"Number of students using GenAI for more than 20 hours per week: {len(f1)}")
print(f"Number of students with paid subscription: {len(f2)}")
print(f"Number of students using GenAI for more than 20 hours per week and have paid subscription: {len(f1[f1['Paid_Subscription']==True])}")

# Use of Group By to analyze the data
grouped_data = data.groupby('Paid_Subscription').agg({'Weekly_GenAI_Hours': 'mean'})
grouped_avg=data.groupby('Major_Category').agg({'Post_Semester_GPA': 'mean'})
grouped_geAi=data.groupby('Major_Category').agg({'Weekly_GenAI_Hours': 'mean'})
print("Average Weekly GenAI Hours by Major Category:")
print(grouped_geAi)
print("Average Post Semester GPA by Major Category:")
print(grouped_avg)
print("Average Weekly GenAI Hours by Paid Subscription:")
print(grouped_data)