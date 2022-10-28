import requests
import json


questions= [{"name": "Array", "slug": "array"}, {"name": "String", "slug": "string"}, {"name": "Hash Table", "slug": "hash-table"}, {"name": "Dynamic Programming", "slug": "dynamic-programming"}, {"name": "Math", "slug": "math"}, {"name": "Sorting", "slug": "sorting"}, {"name": "Greedy", "slug": "greedy"}, {"name": "Depth-First Search", "slug": "depth-first-search"}, {"name": "Database", "slug": "database"}, {"name": "Breadth-First Search", "slug": "breadth-first-search"}, {"name": "Tree", "slug": "tree"}, {"name": "Binary Search", "slug": "binary-search"}, {"name": "Matrix", "slug": "matrix"}, {"name": "Binary Tree", "slug": "binary-tree"}, {"name": "Two Pointers", "slug": "two-pointers"}, {"name": "Bit Manipulation", "slug": "bit-manipulation"}, {"name": "Stack", "slug": "stack"}, {"name": "Heap (Priority Queue)", "slug": "heap-priority-queue"}, {"name": "Design", "slug": "design"}, {"name": "Graph", "slug": "graph"}, {"name": "Simulation", "slug": "simulation"}, {"name": "Prefix Sum", "slug": "prefix-sum"}, {"name": "Backtracking", "slug": "backtracking"}, {"name": "Counting", "slug": "counting"}, {"name": "Sliding Window", "slug": "sliding-window"}, {"name": "Union Find", "slug": "union-find"}, {"name": "Linked List", "slug": "linked-list"}, {"name": "Ordered Set", "slug": "ordered-set"}, {"name": "Monotonic Stack", "slug": "monotonic-stack"}, {"name": "Recursion", "slug": "recursion"}, {"name": "Enumeration", "slug": "enumeration"}, {"name": "Trie", "slug": "trie"}, {"name": "Divide and Conquer", "slug": "divide-and-conquer"}, {"name": "Binary Search Tree", "slug": "binary-search-tree"}, {"name": "Bitmask", "slug": "bitmask"}, {"name": "Queue", "slug": "queue"}, {"name": "Memoization", "slug": "memoization"}, {"name": "Topological Sort", "slug": "topological-sort"}, {"name": "Geometry", "slug": "geometry"}, {"name": "Segment Tree", "slug": "segment-tree"}, {"name": "Hash Function", "slug": "hash-function"}, {"name": "Game Theory", "slug": "game-theory"}, {"name": "Binary Indexed Tree", "slug": "binary-indexed-tree"}, {"name": "Number Theory", "slug": "number-theory"}, {"name": "Interactive", "slug": "interactive"}, {"name": "String Matching", "slug": "string-matching"}, {"name": "Rolling Hash", "slug": "rolling-hash"}, {"name": "Data Stream", "slug": "data-stream"}, {"name": "Shortest Path", "slug": "shortest-path"}, {"name": "Combinatorics", "slug": "combinatorics"}, {"name": "Randomized", "slug": "randomized"}, {"name": "Brainteaser", "slug": "brainteaser"}, {"name": "Monotonic Queue", "slug": "monotonic-queue"}, {"name": "Merge Sort", "slug": "merge-sort"}, {"name": "Iterator", "slug": "iterator"}, {"name": "Concurrency", "slug": "concurrency"}, {"name": "Doubly-Linked List", "slug": "doubly-linked-list"}, {"name": "Probability and Statistics", "slug": "probability-and-statistics"}, {"name": "Quickselect", "slug": "quickselect"}, {"name": "Bucket Sort", "slug": "bucket-sort"}, {"name": "Suffix Array", "slug": "suffix-array"}, {"name": "Minimum Spanning Tree", "slug": "minimum-spanning-tree"}, {"name": "Counting Sort", "slug": "counting-sort"}]

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
dict ={}
for i in questions:
    json_data = {
        'operationName': 'getTopicTag',
        'variables': {
            'slug': i['slug'],
        },
        'query': 'query getTopicTag($slug: String!) {\n  topicTag(slug: $slug) {\n    name\n    slug\n    questions {\n      status\n      questionId\n      questionFrontendId\n      title\n      titleSlug\n      stats\n      difficulty\n      isPaidOnly\n      topicTags {\n        name\n        slug\n        __typename\n      }\n      companyTags {\n        name\n        slug\n        __typename\n      }\n      __typename\n    }\n    frequencies\n    __typename\n  }\n  favoritesLists {\n    publicFavorites {\n      ...favoriteFields\n      __typename\n    }\n    privateFavorites {\n      ...favoriteFields\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment favoriteFields on FavoriteNode {\n  idHash\n  id\n  name\n  isPublicFavorite\n  viewCount\n  creator\n  isWatched\n  questions {\n    questionId\n    title\n    titleSlug\n    __typename\n  }\n  __typename\n}\n',
    }
    response = requests.post('https://leetcode.com/graphql', headers=headers, json=json_data).json()
    temp={}
    temp['Easy']= []
    temp['Medium']= []
    temp['Hard']= []
    for obj in response['data']['topicTag']['questions']:
        temp[obj['difficulty']].append(obj['titleSlug'])
    dict[i['slug']]= temp
with open("questionsTagDiffi.json", "w") as write_file:
    json.dump(dict, write_file, indent=4)
print("Success")
# print(response)
# final= []
# for i in response['data']['topicTag']['questions']:
#     if i['difficulty']== diffi:
#         final.append(i['titleSlug'])
