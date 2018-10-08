from sklearn.datasets.samples_generator import make_blobs


xdata, y = make_blobs(n_samples=10, centers=4)

x = []
for count in range(len(xdata)):
    x.append(xdata[count][0])

for element in range(len(x)):
    x[element] = int(x[element] * 10)

for element in range(len(y)):
    y[element] = int(y[element] * 10)
print(x)
print(y)