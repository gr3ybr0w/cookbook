## Elbow Method

When you have no idea how many clusters exist in your dataset, a common strategy for determining `k` is the elbow method.
In the elbow method, you create a plot of the number of clusters (on the x-axis) vs. the average distance of the center
of the cluster to each point (on the y-axis). This plot is called a scree plot

The average distance will always decrease with each additional cluster center. However, with fewer clusters, those decreases
will be more substantial. At some point, adding new clusters will no longer create a substantial decrease in the average distance.
This point is known as the elbow.
