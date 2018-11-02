# Import package
import matplotlib.pyplot as plt

# clas = "banner"
clas = "tree"
x = [10,50,100,150,200]
if clas == "banner":
    recall = [0.48,0.37,0.69,0.79,0.84]
    precision = [0.78,0.93,0.92,0.85,0.79]
else:
    recall = [0.21, 0.60, 0.50, 0.59, 0.63]
    precision = [1.0, 1.0, 0.98, 0.99, 1.0]

fig, ax = plt.subplots()
for a, b in zip(x, recall):
    ax.text(a - 5, b + 0.01, str(b), color='black')

for a, b in zip(x, precision):
    ax.text(a - 5, b + 0.01, str(b), color='black')

ax.plot(x, recall, label='recall')
ax.plot(x, precision, label='precision')
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, loc='lower right')

# Strings
xlab = 'Number of training images'
ylab = 'Precision-recall (%)'
title = 'The results of precision-recall in {} class'.format(clas)

# Add axis labels　＆　title
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [0,10,50,100,150,200,210]
tick_lab = ['0','10','50','100','150','200','']

tick_val2 = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
tick_lab2 = ['0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)
plt.yticks(tick_val2,tick_lab2)

# After customizing, display the plot
# plt.legend()
plt.show()