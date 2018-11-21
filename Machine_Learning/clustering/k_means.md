## K-Means
The K-Means algorithm is used to cluster all sorts of data.

It can group together
1. Books of similar genres or  written by the same authors.
2. similar movies.
3. Similar music.
4. Similar groups of customers.

The K in K-means relates to how many clusters you wnat to split your data into.
Finding how many clusters there are in a dataset can be more of an art than a science, but there are tools that can help ie 'Elbow Method'

### How does K-Means work

We start by randomly setting K points on our data, each one representing a centroid for the number of clusters that we are looking to find.
We then assign each point in our dataset to the closest centroid.
Now we know which point is in which group we assign our new centroid to the center of these groups.
We know repeat a previous step of assigning each point in our dataset to the clostest centroid. This will now probably included points that were not in the previous grouping.
Again we move the centorid to the middle of the group.
This is repeated untill the centroid no longer move.

Due to the random nature of the inital centroids we can end up with different selected clusters if we were to run the method again. If this is the case then you have to go with the groupings that are the best. The best ones are those that have the lowest average distances between the centroids and their points.
