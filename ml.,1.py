# ml.3

X = np.array([
[1, 2],
[1.5, 1.2],
[5, 7],
[8, 8],
[1, 6],
[9, 1],
])
hclust = AgglomerativeClustering(n_clusters = 2)
hclust.fit(X)
Z = linkage(X, method='ward')
print("Cluster Labels:", hclust.labels_)
dendrogram(Z)
plt.scatter(X[:, 0],X[:, 1], c=hclust.labels_) plt.show()
