from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def contest(request, id):
    content= """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
          <br><br>
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        <br><br>
        You can return the answer in any order.
        <br><br>
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        <br><br>
      You may assume that each input would have exactly one solution, and you may not use the same element twice.
      <br><br>
      You can return the answer in any order.
      <br><br>
    """
    return render(request, 'Contest/index.html', {'id': id, 'content': content})

def create(request):
    questions= [{"name": "Array", "slug": "array"}, {"name": "String", "slug": "string"}, {"name": "Hash Table", "slug": "hash-table"}, {"name": "Dynamic Programming", "slug": "dynamic-programming"}, {"name": "Math", "slug": "math"}, {"name": "Sorting", "slug": "sorting"}, {"name": "Greedy", "slug": "greedy"}, {"name": "Depth-First Search", "slug": "depth-first-search"}, {"name": "Database", "slug": "database"}, {"name": "Breadth-First Search", "slug": "breadth-first-search"}, {"name": "Tree", "slug": "tree"}, {"name": "Binary Search", "slug": "binary-search"}, {"name": "Matrix", "slug": "matrix"}, {"name": "Binary Tree", "slug": "binary-tree"}, {"name": "Two Pointers", "slug": "two-pointers"}, {"name": "Bit Manipulation", "slug": "bit-manipulation"}, {"name": "Stack", "slug": "stack"}, {"name": "Heap (Priority Queue)", "slug": "heap-priority-queue"}, {"name": "Design", "slug": "design"}, {"name": "Graph", "slug": "graph"}, {"name": "Simulation", "slug": "simulation"}, {"name": "Prefix Sum", "slug": "prefix-sum"}, {"name": "Backtracking", "slug": "backtracking"}, {"name": "Counting", "slug": "counting"}, {"name": "Sliding Window", "slug": "sliding-window"}, {"name": "Union Find", "slug": "union-find"}, {"name": "Linked List", "slug": "linked-list"}, {"name": "Ordered Set", "slug": "ordered-set"}, {"name": "Monotonic Stack", "slug": "monotonic-stack"}, {"name": "Recursion", "slug": "recursion"}, {"name": "Enumeration", "slug": "enumeration"}, {"name": "Trie", "slug": "trie"}, {"name": "Divide and Conquer", "slug": "divide-and-conquer"}, {"name": "Binary Search Tree", "slug": "binary-search-tree"}, {"name": "Bitmask", "slug": "bitmask"}, {"name": "Queue", "slug": "queue"}, {"name": "Memoization", "slug": "memoization"}, {"name": "Topological Sort", "slug": "topological-sort"}, {"name": "Geometry", "slug": "geometry"}, {"name": "Segment Tree", "slug": "segment-tree"}, {"name": "Hash Function", "slug": "hash-function"}, {"name": "Game Theory", "slug": "game-theory"}, {"name": "Binary Indexed Tree", "slug": "binary-indexed-tree"}, {"name": "Number Theory", "slug": "number-theory"}, {"name": "Interactive", "slug": "interactive"}, {"name": "String Matching", "slug": "string-matching"}, {"name": "Rolling Hash", "slug": "rolling-hash"}, {"name": "Data Stream", "slug": "data-stream"}, {"name": "Shortest Path", "slug": "shortest-path"}, {"name": "Combinatorics", "slug": "combinatorics"}, {"name": "Randomized", "slug": "randomized"}, {"name": "Brainteaser", "slug": "brainteaser"}, {"name": "Monotonic Queue", "slug": "monotonic-queue"}, {"name": "Merge Sort", "slug": "merge-sort"}, {"name": "Iterator", "slug": "iterator"}, {"name": "Concurrency", "slug": "concurrency"}, {"name": "Doubly-Linked List", "slug": "doubly-linked-list"}, {"name": "Probability and Statistics", "slug": "probability-and-statistics"}, {"name": "Quickselect", "slug": "quickselect"}, {"name": "Bucket Sort", "slug": "bucket-sort"}, {"name": "Suffix Array", "slug": "suffix-array"}, {"name": "Minimum Spanning Tree", "slug": "minimum-spanning-tree"}, {"name": "Counting Sort", "slug": "counting-sort"}]
    resp= {}
    if request.method == 'POST':
        resp= request.POST
    return render(request, 'Contest/contest_create.html', {'questions': questions, 'name': "suryash", 'msg': resp})

def caesar(request):
    return render(request, 'Contest/caesar.html')
    
def index(request):
    return render(request, "Contest/main.html")
