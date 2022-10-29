from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CreatedContest
from django.views.decorators.cache import never_cache
import requests
import random
import json

def contestIdGenerator():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))

def getQuestionContent(slug):
    headers = {
    'authority': 'leetcode.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://leetcode.com',
    'referer': 'https://leetcode.com/problems/3sum/',
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
        'operationName': 'getQuestionDetail',
        'variables': {
            'titleSlug': slug,
        },
        'query': 'query getQuestionDetail($titleSlug: String!) {\n  isCurrentUserAuthenticated\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    translatedTitle\n    questionTitleSlug\n    content\n    translatedContent\n    difficulty\n    stats\n    allowDiscuss\n    contributors {\n      username\n      profileUrl\n      __typename\n    }\n    similarQuestions\n    mysqlSchemas\n    randomQuestionUrl\n    sessionId\n    categoryTitle\n    submitUrl\n    interpretUrl\n    codeDefinition\n    sampleTestCase\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    judgerAvailable\n    infoVerified\n    envInfo\n    urlManager\n    article\n    questionDetailUrl\n    libraryUrl\n    adminUrl\n    companyTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    __typename\n  }\n  interviewed {\n    interviewedUrl\n    companies {\n      id\n      name\n      slug\n      __typename\n    }\n    timeOptions {\n      id\n      name\n      __typename\n    }\n    stageOptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  subscribeUrl\n  isPremium\n  loginUrl\n}\n',
    }

    response = requests.post('https://leetcode.com/graphql', headers=headers, json=json_data).json()
    return response['data']['question']['content']
# Create your views here.
def contest(request, id, n):
    data= CreatedContest.objects.get(contest_id= id)
    if n==1:
        slug= data.first
    elif n==2:
        slug= data.second
    elif n==3:
        slug= data.third
    elif n==4:
        slug= data.fourth
    print(slug)
    content= getQuestionContent(slug)
    content= content.replace('\n', '<br />')
    return render(request, 'Contest/index.html', {'id': id, 'content': content, 'n': n})

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
        f = open('./static/json/questionsTagDiffi.json')
        data = json.load(f)
        f.close()
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
            questionlist= data[resp['topic']][i]
            try:
                questionForContest.append(random.choice(questionlist))
            except:
                return render(request, 'Contest/contest_create.html', {'questions': questions, 'msg': f'No {i} questions for {resp["topic"]} topic, Total {i} questions for {resp["topic"]} topic are {len(questionlist)}'})
        contest.first= questionForContest[0]
        contest.second= questionForContest[1]
        contest.third= questionForContest[2]
        contest.forth= questionForContest[3]
        contest.save()
    else:
        return render(request, 'Contest/contest_create.html', {'questions': questions, 'name': "suryash", 'msg': "Please fill the form to create a contest"})
        
    return render(request, 'Contest/contest_create.html', {'questions': questions, 'name': "suryash", 'msg': questionForContest})

def caesar(request):
    return render(request, 'Contest/caesar.html')

# Change it
# @never_cache
def listContest(request):
    data= CreatedContest.objects.all()
    return render(request, 'Contest/listContest.html', {'contest_list': data})
    
def index(request):
    return render(request, "Contest/main.html")

def listContestQuestion(request, id):
    data= CreatedContest.objects.get(contest_id= id)
    return render(request, 'Contest/listContestQuestion.html', {'contest': data})