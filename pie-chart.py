import matplotlib.pyplot as plt

labels = ['U.S', 'India', 'China', 'Russia']
sizes = [20, 56, 10, 14]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
plt.show()