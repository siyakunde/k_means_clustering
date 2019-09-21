import scipy
import pandas as pd
import math
import time
import numpy as np 

def main(dataset, k, epsilon, iterations):
	start_time = time.time()

	centroids = dataset.sample(k)

	columns = centroids.columns
	
	sse = 0
	for i in range(0,iterations):
		clusters = []
		for index, row in centroids.iterrows():
			clusters.append([list(row.tolist())])
		old_sse = sse
		sse = 0
		for index, row in dataset.iterrows():
			closest_centroid, dist_all, dist = get_closest_centroid(row, centroids)
			sse = sse + dist
			old_length = len(clusters[closest_centroid])
			clusters[closest_centroid].append(list(row.values))
			new_length = len(clusters[closest_centroid])
			for c in columns:
				centroids.loc[centroids.index[closest_centroid], c] = ((centroids.iloc[closest_centroid][c] * old_length) + row[c]) / new_length
		
		ssed = abs(old_sse-sse)
		if(ssed < epsilon):
			end_time = time.time()
			return clusters, centroids, start_time, end_time, sse, ssed, i
		# print(ssed)

		# print(len(clusters[0]), len(clusters[1]))

	end_time = time.time()

	return clusters, centroids, start_time, end_time, sse, ssed, i

def get_closest_centroid(item, centroids):
	columns = centroids.columns
	dist_all = []
	for i in range(0,len(centroids)):
		dist_all.append(euclidean_distance(item, centroids.iloc[i], columns))
	return dist_all.index(min(dist_all)), dist_all, min(dist_all)

def euclidean_distance(item, centroid, columns):
	inner_value = 0
	for c in columns:
		inner_value += (item[c] - centroid[c]) ** 2
	return math.sqrt(inner_value)