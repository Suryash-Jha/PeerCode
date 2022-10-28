import requests

tag= 'array'
diffi= 'Medium'
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
print(response)
# final= []
# for i in response['data']['topicTag']['questions']:
#     if i['difficulty']== diffi:
#         final.append(i)
# return final