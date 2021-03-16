import matplotlib.pyplot as plt
import numpy as np

possibleCounties = ['mayo', 'cork', 'galway', 'waterford', 'kerry']
counties = np.random.choice(
    possibleCounties ,
    p=[0.1,0.3,0.2,0.12,0.28],
    size=(100)

)

unique, counts = np.unique(counties, return_counts=True)

plt.bar(unique, counts)
plt.show()