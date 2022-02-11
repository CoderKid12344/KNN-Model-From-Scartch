from collections import Counter
import pandas as pd
import math

Train_Data = pd.read_csv('Train.csv')
Test_Data = pd.read_csv('Test.csv')

Train_Data.gender = Train_Data.gender.map({'m': 0, 'f': 1})
Test_Data.gender = Test_Data.gender.map({'m': 0, 'f': 1})

k = 3
distances = []
for ind in Train_Data.index:
    value = ((Test_Data["age"][0] - Train_Data["age"][ind]) ** 2 + (Test_Data["gender"][0] - Train_Data["gender"][ind]) ** 2)
    distance = math.sqrt(value)
    distances.append(distance)

Train_Data["distance"] = distances

min_distances = Train_Data.nsmallest(k, 'distance')

age_filtered = min_distances["age"].values
gender_filtered = min_distances["gender"].values
sport_filtered = list(min_distances["sport"])

occurence_count = Counter(sport_filtered)
Prediction = occurence_count.most_common(1)[0][0]
print(Prediction)
