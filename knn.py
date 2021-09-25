import math
def predict_label(examples,features,k,label_key = "is_intrusive"):
  k_n_n = find_k_n_n(examples,features,k)
  k_n_n_labels = [examples[pid][label_key] for pid in k_n_n]
  return round(sum(k_n_n_labels) / k)
  
def find_k_n_n(examples,features,k):
  distances ={}
  for pid,features_label_map in examples.items():
    distance = get_euclidean_distance(features,features_label_map["feature"])
    distance[pid]=distance
   return sorted(distances, key=distances.get)[:k]
   
def get_euclidean_distance(features,other_features):
  squared_diff =[]
  for i in rang(len(features)):
    squared_diff.append((other_features[i] - features[i]) ** 2)
   return math.sqrt(sum(squared_diff))
