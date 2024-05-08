import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):

  try:
    return pd.read_excel(filepath)
  except FileNotFoundError:
    print(f"Error: File '{filepath}' not found.")
    return None

def analyze_world_data(world_data):

  total_meditation_by_year = world_data.groupby('year')['meditation population'].sum()
  highest_meditation_year = total_meditation_by_year.idxmax()
  highest_meditation_population = total_meditation_by_year.max()

  print(f"Year with Highest Total Meditation Population: {highest_meditation_year} ({highest_meditation_population})")

  meditation_by_country = world_data.sort_values(by='meditation population', ascending=False)

  plt.figure(figsize=(10, 6))
  plt.bar(meditation_by_country['country'], meditation_by_country['meditation population'])
  plt.xlabel("Country")
  plt.ylabel("Meditation Population")
  plt.title("Distribution of Meditation Population Across Countries")
  plt.xticks(rotation=45, ha="right")
  plt.tight_layout()
  plt.show()


def analyze_patient_demographics(meditation_data):
  gender_counts = meditation_data['GENDER'].value_counts()
  print(gender_counts.describe())  

  city_counts = meditation_data['CITY'].value_counts()
  if len(city_counts) > 10:  
    print(city_counts.nlargest(10))  
  else:
    print(city_counts.describe()) 

  marital_status_counts = meditation_data['MARITAL_STATUS'].value_counts()
  plt.figure(figsize=(6, 6))
  plt.pie(marital_status_counts.values, labels=marital_status_counts.index, autopct="%1.1f%%")
  plt.title("Distribution of Patients by Marital Status")
  plt.show() 



if __name__ == "__main__":
  world_data = load_data("world_statistics.xlsx")
  meditation_data = load_data("meditation.xlsx")

  if world_data is not None:
    analyze_world_data(world_data)
  else:
    print("Analysis for world_statistics.xlsx could not be completed due to errors loading data.")

  if meditation_data is not None:
    analyze_patient_demographics(meditation_data)  
  else:
    print("Analysis for meditation.xlsx could not be completed due to errors loading data.")

