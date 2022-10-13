import requests
url= "https://leetcode.com/graphql"
dict= {}
question_list_query="""
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      topicTags {
        name
        id
        slug
      }
      hasSolution
      hasVideoSolution
    }
  }
} 
"""
c=0;
for i in range(0, 2): 
  print(i)
  r= requests.post(url, json={"query": question_list_query,"variables": {"categorySlug": "", "skip": i*100, "limit": 100, "filters": {}}}).json()
  question= r["data"]["problemsetQuestionList"]["questions"]
  for j in question:
    c+=1;
    dict[c]= j
print(dict)
# for i in dict:
#   print(i)