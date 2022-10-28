import requests

# #EASY, MEDIUM, HARD
# diffi= input()
# n= int(input())

# #Slugs of tags
# tag= []
# for i in range(0,n):
#     x= input()
#     tag.append(x)

# filter= {}
# filter['difficulty']= diffi
# # filter['tags']= tag

# #'array', 'depth-first-search'

# json_data = {
#     'query': '\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ',
#     'variables': {
#         'categorySlug': '',
#         'skip': 0,
#         'limit': 100,
#         'filters': filter,
#     },
# }

# response = requests.post('https://leetcode.com/graphql/', json=json_data).json()
# print(response)



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
tag= 'array'
json_data = {
    'operationName': 'getTopicTag',
    'variables': {
        'slug': tag,
    },
    'query': 'query getTopicTag($slug: String!) {\n  topicTag(slug: $slug) {\n    name\n    slug\n    questions {\n      status\n      questionId\n      questionFrontendId\n      title\n      titleSlug\n      stats\n      difficulty\n      isPaidOnly\n      topicTags {\n        name\n        slug\n        __typename\n      }\n      companyTags {\n        name\n        slug\n        __typename\n      }\n      __typename\n    }\n    frequencies\n    __typename\n  }\n  favoritesLists {\n    publicFavorites {\n      ...favoriteFields\n      __typename\n    }\n    privateFavorites {\n      ...favoriteFields\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment favoriteFields on FavoriteNode {\n  idHash\n  id\n  name\n  isPublicFavorite\n  viewCount\n  creator\n  isWatched\n  questions {\n    questionId\n    title\n    titleSlug\n    __typename\n  }\n  __typename\n}\n',
}
diffi= 'Easy'
response = requests.post('https://leetcode.com/graphql', headers=headers, json=json_data).json()
# print(response)
final= []
for i in response['data']['topicTag']['questions']:
    if i['difficulty']== diffi:
        final.append(i)
print(final)