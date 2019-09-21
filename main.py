import os
import numpy as np  
from collections import OrderedDict
import sys
import matplotlib.pyplot as plt  
import pandas as pd
import random
import kmc

def normalize():
	for c in dataset.columns: 
		dataset[c]=(dataset[c]-dataset[c].min())/(dataset[c].max()-dataset[c].min())

# Verify correct input arguments: 1 or 2
if (len(sys.argv) < 5 or len(sys.argv) > 5):
	print("Invalid number of arguments:   " + str(len(sys.argv)))
	print("Try: 'python3 main.py data_file.arff min_sup min_conf'")
	sys.exit(1)
elif (len(sys.argv) == 5):
	data_file_name = str(sys.argv[1])
	k = int(sys.argv[2])
	epsilon = float(sys.argv[3])
	iterations = int(sys.argv[4])
	print("processing data now......")
else:
	print("bad argument(s): " + str(sys.argv))	#shouldnt really come up
	sys.exit(1)

# ---------------------------------------------------------------------------------------------
# --------------------------------Start Data Pre-processing Section----------------------------
# ---------------------------------------------------------------------------------------------

# Import data
dataset = pd.read_csv(data_file_name) 

if("_preprocessed" not in data_file_name):
	#normalize all the columns
	normalize()

# ---------------------------------------------------------------------------------------------
# --------------------------------End Data Pre-processing Section------------------------------
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# ---------------------------------------Start KMC Section-------------------------------------
# ---------------------------------------------------------------------------------------------

# Choose k random centroids from given dataset
# For each item in dataset, calculate distance to each centroid and add to cluster of the centroid to which it has least distance
# update the centroid values while adding a new member to the cluster. End result should be k clusters and k centroids.
# Compare each item from database to the new k centroids and add......

outputData = OrderedDict()

clusters, centroids, start_time, end_time, sse, ssed, iterations_completed = kmc.main(dataset, k, epsilon, iterations)
run_time = end_time - start_time
outputData[str(k)] = [k, start_time, end_time, run_time, sse, ssed, epsilon, iterations, iterations_completed, centroids, clusters]

dfOutputData = pd.DataFrame.from_dict(outputData, orient='index')
dfOutputData.columns = ['NumClusters', 'StartTime', 'EndTime', 'RunTime', 'SSE', 'SSED', 'Epsilon', 'Iterations', 'IterationsCompleted', 'Centroids', 'Clusters']
dfOutputData.to_csv(os.getcwd()+'/kmc_run_data.csv')

# ---------------------------------------------------------------------------------------------
# ----------------------------------------End KMC Section--------------------------------------
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# ----------------------------------------Start Output Section---------------------------------
# ---------------------------------------------------------------------------------------------

print('Number of iterations : ' + str(iterations_completed))
print('Within cluster sum of squared errors : ' + str(sse))
print('Initial starting points (random) : ')
print(centroids)
print('Total Runtime (seconds): ' + str(end_time - start_time))
for i in range(0, k):
	print('Cluster' + str(i) + ' size : ' + str(len(clusters[i])))

# ---------------------------------------------------------------------------------------------
# -----------------------------------------End Output Section----------------------------------
# ---------------------------------------------------------------------------------------------