import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn.decomposition import PCA

mnist = fetch_mldata('MNIST original')
x = mnist["data"]
y = mnist["target"]

pca = PCA()
pca.fit(x)

cumsum = np.cumsum(pca.explained_variance_ratio_)
d = np.argmax(cumsum >= 0.9) + 1

plt.plot(cumsum)
plt.ylim(0,1.1)
plt.xlabel('no.of principal',fontsize=16)
plt.ylabel('explained variance ratio',fontsize=16)
plt.show()

Xr = []
for n in [5,15,35,85]:
    pca = PCA(n_components=n)
    X_reduced = pca.fit_transform(x)
    X_recovered = pca.inverse_transform(X_reduced)
    Xr.append(X_recovered)

instances = []
for i in range(10):
    instances.append(x[y==i][0])
    for j in range(1,5):
        instances.append(Xr[j-1][y==i][0])

def plot_digits(instances):
    images = [instance.reshape(28,28)
              for instance in instances]
    row_images = []
    for row in range(5):
        rimages = images[row*5:(row+1)*5]
        row_images.append(np.concatenate(rimages,axis=1))
    image = np.concatenate(row_images,axis=0)
    plt.imshow(image,cmap=matplotlib.cm.binary)
    plt.axis("off")

plt.figure(figsize=(7,4))
plt.subplot(121)
plot_digits(instances[:25])
plt.subplot(122)
plot_digits(instances[25:])
plt.show()