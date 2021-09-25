# K-Nearest-Neighbors-Machine-Learning

Using KNN Algorithm to return k nearest neighbors of the provided features. These features are the result of dimentionality reduction by PCA on some OS data related to processes and their intrusivity in some network. We have a dictionary EXAMPLES, mapping each process id (p_id) to a respective dictionary containing its associated features as well as labels representing whether the relevant process was intrusive to the network.Label 0 indicates that the process was not intrusive and label 1 indicates otherwise.

To find the k nearest neighbors, iterate through all the features in dataset and find the diatance between each feature and the provided feature.

I have used Euclidean distance as the distance metric.To find Euclideam distance between 2 features, start by iterating through each element in both features, subtract one value from the other and square the result.Store them in a list containing the squared differences, one for each item in the features. Finally we take the sum of each element in the list and take the square root. 

After calculating the distance between each feature in the dataset and each of the provided features,sort them and take the top k elements so as to obtain the k nearest neighbors.

To perform the prediction we need to get the labels of the k nearest neighbors and return the most frequent among them. 

Note : No libraries were used to implement KNN.
