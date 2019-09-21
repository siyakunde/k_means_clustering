----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
# K-means Clustering
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
## TO RUN:

Copy the folder k_means_algorithm. <br />
Type `cd k_means_algorithm` to enter the forlder.<br />
To run the program type a command as follows with inputs dataset, k, epsilon, iterations:<br />
`python3 main.py test_data.csv 2 0.001 500` <br />
The output will be in the file kmc_run_data.csv<br />
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
# PROGRAM DESCRIPTION:
## For the K-Means Clustering Algorithm the following functions are used:

1) main(dataset, k, epsilon, iterations)<br />
This method accepts the dataset, the number of clusters k, the epsilon value for SSE comparison, and the maximum number of iterations the algorithm should perform.<br />
It first randomly picks out k centroids. <br />
Then in a loop, the records in the dataset are considered one at a time, and based on the minimum distance to one of the k centroids, the record is added to cluster of one of the centroids. Next the centroid is recalculated based on members of the cluster.<br />
At each level of the iteration the SSE is computed and if less than epsilon value then the method returns, otherwise the computations will continue until maximum number of iterations are completed.<br />
The method returns the clusters generated, the final centroids, the start and end timestamps, the SSE calculated and the difference from previous iteration, and the iteration at which computation was terminated.<br />

2) get_closest_centroid(item, centroids)<br />
This method accepts a dataset row as item and the k centroids. <br />
It computes the euclidean distance from this item to each centroid.<br />
The function finally returns the index of the centroid to which the least distance was computed, the distances to all centroids, and the min distance.<br />

3) euclidean_distance(item, centroid, columns)<br />
This method accepts a dataset record, a centroid and the list of attributes.<br />
It computes the euclidean distance from the record to the centroid with respect to each attribute,
and it returns this distance.<br />
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------