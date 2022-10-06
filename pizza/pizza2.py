import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
toppings = ('Mushroom', 'Red Peppers', 'Black Olives', 'Pepperoni', 'Sausage')
y_pos = np.arange(len(toppings))
rankings = 3 + 10 * np.random.rand(len(toppings))
error = np.random.rand(len(toppings))

ax.barh(y_pos, rankings, xerr=error, align='center')
ax.set_yticks(y_pos, labels=toppings)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Rankings')
ax.set_title('Toppings')

plt.savefig("/home/student/static/perfectPizza2.png")
