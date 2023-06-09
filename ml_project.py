# -*- coding: utf-8 -*-
"""ML Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ptKpO-AFV9Jk94Q5ZIoSdxckVON0fY1C
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.cluster import KMeans
from sklearn import preprocessing
import sklearn.cluster as cluster
import sklearn.metrics as metrics
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
from matplotlib import pyplot as plt
# %matplotlib inline

import zipfile
import pandas as pd

# Open the ZIP archive
with zipfile.ZipFile('/content/archive (5).zip', 'r') as zip_file:
    
    # Extract the CSV file you want to read
    with zip_file.open('Features.csv') as file:
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)
        
# Print the first 21 rows of the DataFrame
df.head(5)

scaler = MinMaxScaler()
scale = scaler.fit_transform(df[['liveness','tempo']])
df_scale = pd.DataFrame(scale, columns = ['liveness','tempo']);
df_scale.head(21)

df.dropna(inplace=True)
km = KMeans(n_clusters=2)
y_predicted = km.fit_predict(df[['liveness','tempo']])
y_predicted

km.cluster_centers_

df['Clusters'] = km.labels_
sns.scatterplot(x="tempo", y="liveness",hue = 'Clusters',  data=df,palette='viridis')

df_scale.dropna(inplace=True)
K=range(2,12)
wss = []

for k in K:
    kmeans=cluster.KMeans(n_clusters=k)
    kmeans=kmeans.fit(df_scale)
    wss_iter = kmeans.inertia_
    wss.append(wss_iter)

plt.xlabel('K')
plt.ylabel('Within-Cluster-Sum of Squared Errors (WSS)')
plt.plot(K,wss)