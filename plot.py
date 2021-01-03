import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('iterations')
plt.axhline(y=3.14159265, color='r', linestyle='-')
plt.ylabel('value')
plt.title('PI value by number of iteration')
plt.legend()
plt.show()