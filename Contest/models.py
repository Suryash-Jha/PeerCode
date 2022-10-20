from django.db import models
from django.utils.translation import autoreload_started
from django.contrib.auth.models import User

TOPIC_CHOICE= (
    ("array","Array"),
    ("string","String"),
    ("hash-table","Hash Table"),
    ("dynamic-progrmming","Dynamic Programming"),
    ("math","Math"),
    ("sorting","Sorting"),
    ("greedy","Greedy"),
    ("depth-first-search","Depth-First Search"),
    ("database","Database"),
    ("breadth-first-search","Breadth-First Search"),
    ("tree","Tree"),
    ("binary-search","Binary Search"),
    ("matrix","Matrix"),
    ("binary-tree","Binary Tree"),
    ("two-pointers","Two Pointers"),
    ("bit-manipulation","Bit Manipulation"),
    ("stack","Stack"),
    ("heap-priority-queue","Heap (Priority Queue)"),
    ("design","Design"),
    ("graph","Graph"),
    ("simulation","Simulation"),
    ("prefix-sum","Prefix Sum"),
    ("backtracking","Backtracking"),
    ("counting","Counting"),
    ("sliding-window","Sliding Window"),
    ("union-find","Union Find"),
    ("linked-list","Linked List"),
    ("ordered-set","Ordered Set"),
    ("monotonic-stack","Monotonic Stack"),
    ("recursion","Recursion"),
    ("enumeration","Enumeration"),
    ("trie","Trie"),
    ("divide-and-conquer","Divide and Conquer"),
    ("binary-search-tree","Binary Search Tree"),
    ("bitmask","Bitmask"),
    ("queue","Queue"),
    ("memoization","Memoization"),
    ("topological-sort","Topological Sort"),
    ("geometry","Geometry"),
    ("segment-tree","Segment Tree"),
    ("hash-function","Hash Function"),
    ("game-theory","Game Theory"),
    ("binary-indexed-tree","Binary Indexed Tree"),
    ("number-theory","Number Theory"),
    ("interactive","Interactive"),
    ("string-matching","String Matching"),
    ("rolling-hash","Rolling Hash"),
    ("data-stream","Data Stream"),
    ("shortest-path","Shortest Path"),
    ("combinatorics","Combinatorics"),
    ("randomized","Randomized"),
    ("brainteaser","Brainteaser"),
    ("monotonic-queue","Monotonic Queue"),
    ("merge-sort","Merge Sort"),
    ("iterator","Iterator"),
    ("concurrency","Concurrency"),
    ("doubly-linked-list","Doubly-Linked List"),
    ("probability-and-statistics","Probability and Statistics"),
    ("quickselect","Quickselect"),
    ("bucket-sort","Bucket Sort"),
    ("suffix-array","Suffix Array"),
    ("minimum-spanning-tree","Minimum Spanning Tree"),
    ("counting-sort","Counting Sort")
)
# Create your models here.
class ContestQuestions(models.Model):
    contest_id= models.CharField(max_length=100)
    created_on= models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE)
    easy= models.IntegerField()
    medium= models.IntegerField()
    hard= models.IntegerField()
    topic= models.CharField(max_length=50, 
            choices= TOPIC_CHOICE,
            default='array'
        )
    start_time= models.DateTimeField()
    end_time= models.DateTimeField()
    def __str__(self):
        return self.contest_id
    class Meta:
        ordering = ['created_on']
