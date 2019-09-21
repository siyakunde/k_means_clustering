----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
K-means Clustering
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
TO RUN:
Copy the folder k_means_algorithm. 
Type cd k_means_algorithm to enter the forlder.
To run the program type a command as follows with inputs dataset, k, epsilon, iterations:
python3 main.py test_data.csv 2 0.001 500 

The output will be in the file kmc_run_data.csv
NOTE: Make sure the test data file name does not contain the word "preprocessed", 
since that is how the code determines if the file data is normalized (ours) or not (yours).
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
PROGRAM DESCRIPTION:
For the K-Means Clustering Algorithm the following functions are used:

1) main(dataset, k, epsilon, iterations)
This method accepts the dataset, the number of clusters k, the epsilon value for SSE comparison, and the maximum number of iterations the algorithm should perform.
It first randomly picks out k centroids. 
Then in a loop, the records in the dataset are considered one at a time, and based on the minimum distance to one of the k centroids, the record is added to cluster of one of the centroids. Next the centroid is recalculated based on members of the cluster.
At each level of the iteration the SSE is computed and if less than epsilon value then the method returns, otherwise the computations will continue until maximum number of iterations are completed.
The method returns the clusters generated, the final centroids, the start and end timestamps, the SSE calculated and the difference from previous iteration, and the iteration at which computation was terminated.

2) get_closest_centroid(item, centroids)
This method accepts a dataset row as item and the k centroids. 
It computes the euclidean distance from this item to each centroid.
The function finally returns the index of the centroid to which the least distance was computed, the distances to all centroids, and the min distance.

3) euclidean_distance(item, centroid, columns)
This method accepts a dataset record, a centroid and the list of attributes.
It computes the euclidean distance from the record to the centroid with respect to each attribute,
and it returns this distance.
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------