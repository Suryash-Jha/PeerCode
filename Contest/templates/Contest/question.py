import requests

#EASY, MEDIUM, HARD
diffi= input()
n= int(input())

#Slugs of tags
tag= []
for i in range(0,n):
    x= input()
    tag.append(x)

filter= {}
filter['difficulty']= diffi
filter['tags']= tag

#'array', 'depth-first-search'

json_data = {
    'query': '\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ',
    'variables': {
        'categorySlug': '',
        'skip': 0,
        'limit': 100,
        'filters': filter,
    },
}

response = requests.post('https://leetcode.com/graphql/', json=json_data).json()
print(response)
