from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CreatedContest
import requests
import random
import time

def difficultyQuestions(tag, diffi):
    headers = {
    'authority': 'leetcode.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://leetcode.com',
    'referer': 'https://leetcode.com/tag/string/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
    'x-csrftoken': 'sQ8L7NVt84PJfSpPnyGz2HhulIXM28kms50Qnt9fx51v3n7dlEb2NHuHP5Cqw1FJ',
    'x-newrelic-id': 'UAQDVFVRGwEAXVlbBAg=',
    }

    json_data = {
        'operationName': 'getTopicTag',
        'variables': {
            'slug': tag,
        },
        'query': 'query getTopicTag($slug: String!) {\n  topicTag(slug: $slug) {\n    name\n    slug\n    questions {\n      status\n      questionId\n      questionFrontendId\n      title\n      titleSlug\n      stats\n      difficulty\n      isPaidOnly\n      topicTags {\n        name\n        slug\n        __typename\n      }\n      companyTags {\n        name\n        slug\n        __typename\n      }\n      __typename\n    }\n    frequencies\n    __typename\n  }\n  favoritesLists {\n    publicFavorites {\n      ...favoriteFields\n      __typename\n    }\n    privateFavorites {\n      ...favoriteFields\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment favoriteFields on FavoriteNode {\n  idHash\n  id\n  name\n  isPublicFavorite\n  viewCount\n  creator\n  isWatched\n  questions {\n    questionId\n    title\n    titleSlug\n    __typename\n  }\n  __typename\n}\n',
    }
    response = requests.post('https://leetcode.com/graphql', headers=headers, json=json_data).json()
    # print(response)
    final= []
    for i in response['data']['topicTag']['questions']:
        if i['difficulty']== diffi:
            final.append(i['titleSlug'])
    return final


def contestIdGenerator():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))

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
    s= contestIdGenerator()
    if request.method == 'POST':
        resp= request.POST
        if(int(resp['easy'])+ int(resp['medium']) + int(resp['hard']) != 4):
            return render(request, 'Contest/contest_create.html', {'questions': questions, 'msg': f'Number of questions should be 4, You have selected {int(resp["easy"])+ int(resp["medium"]) + int(resp["hard"])} questions'})
        contest= CreatedContest()
        contest.contest_id= contestIdGenerator()
        # questionlist= difficultyQuestions(resp['topic'], 'EASY')
        lst=[]
        for i in range(int(resp['easy'])):
            lst.append('Easy')
        for i in range(int(resp['medium'])):
            lst.append('Medium')
        for i in range(int(resp['hard'])):
            lst.append('Hard')
        print(lst)
        questionForContest= []

        for i in lst:
            questionlist= difficultyQuestions(resp['topic'], i)
            questionForContest.append(random.choice(questionlist))
        contest.first= questionForContest[0]
        contest.second= questionForContest[1]
        contest.third= questionForContest[2]
        contest.forth= questionForContest[3]
        contest.save()

        # print(questionForContest)
    else:
        return render(request, 'Contest/contest_create.html', {'questions': questions, 'name': "suryash", 'msg': "Please fill the form to create a contest"})
        
    return render(request, 'Contest/contest_create.html', {'questions': questions, 'name': "suryash", 'msg': questionForContest})

def caesar(request):
    return render(request, 'Contest/caesar.html')
    
def index(request):
    return render(request, "Contest/main.html")
