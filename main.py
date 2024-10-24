"""
Problem Statement: Finding Optimal Paths for GenAI Summary Using DFS
You are working on a GenAI-based summarization system that processes customer reviews for various products. The reviews are stored as nodes in a graph, where each node represents a review, and an edge between two nodes indicates that the reviews are related based on sentiment similarity or topic similarity.

Your task is to implement a DFS-based algorithm to find optimal paths in this graph, where each path corresponds to a group of reviews that should be summarized together by the GenAI model. Each review node has a sentiment score and a topic. The quality of a path is determined by the consistency of sentiment and topic across the path, as well as the length of the path.

Graph Representation:
Each node in the graph represents a review and has the following attributes:
review_id: Unique identifier for the review.
sentiment_score: A sentiment score between -1 (negative) and 1 (positive).
topic: The primary topic of the review (e.g., "Delivery", "Quality", "Price").
An edge exists between two reviews if:
Their sentiment scores are within a threshold of ±0.3.
Their topics are the same.

"""
from reviewPath import review_sort_path
from reviewInfo import data



# Example graph
if __name__ == "__main__":
    all_paths = review_sort_path(data)
    print(all_paths)