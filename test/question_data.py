import requests
url= 

curl 'https://leetcode.com/graphql/' \
  -H 'authority: leetcode.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: ' \
  -H 'content-type: application/json' \
  -H 'cookie: gr_user_id=872a6a7e-7002-424a-92d7-fa177a74bd82; _gcl_au=1.1.702471025.1657551245; intercom-id-pq9rak4o=496871a5-860d-4df8-a5b4-66b4e739cfbd; _ga_DKXQ03QCVK=GS1.1.1657551245.1.1.1657551440.60; _ga=GA1.2.1195630836.1657035522; __stripe_mid=0ce82c4b-cf05-4c4f-8968-00c96120b99686ba46; csrftoken=zIu3Q4DQ45N5Rm4AKnAWXmBYNDE5wuCs5AJwE8UQGEkoEEHgWA8M8T5LmDaMXMH6; 87b5a3c3f1a55520_gr_last_sent_cs1=godofcode99; _gid=GA1.2.446147206.1660400005; NEW_PROBLEMLIST_PAGE=1; __atuvc=25%7C33%2C8%7C34%2C31%7C35%2C16%7C36%2C12%7C37; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNjg2MzgwMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjAzODgxNjZjZDFmMzY2NjMwM2Q2OTEyN2M5M2JlNzAxM2FiNDFkMzkiLCJpZCI6Njg2MzgwMiwiZW1haWwiOiJnb2RvZmNvZGU5OUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImdvZG9mY29kZTk5IiwidXNlcl9zbHVnIjoiZ29kb2Zjb2RlOTkiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2MjM1NDc2Ni5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NjM0NzQ5MjUsImlwIjoiMjQwOTo0MDUwOjJkNGM6NWI1Mjo4Y2Q1OmRiMTg6NjlmNTpjNmQ1IiwiaWRlbnRpdHkiOiJhMDkwOTgxMGE2ZDEzMjgzMmUyOGVmNmRhMThlYzc3YyIsInNlc3Npb25faWQiOjI1MDc5Njc4fQ.ShbtS1nDuLA8ZEkxucFLjBWpx-ADPGcKaGQyx5NBGyk; _gat=1; 87b5a3c3f1a55520_gr_session_id=b7b29921-3bab-4eee-a597-f55ff19613ce; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=b7b29921-3bab-4eee-a597-f55ff19613ce; 87b5a3c3f1a55520_gr_session_id_b7b29921-3bab-4eee-a597-f55ff19613ce=true; c_a_u="Z29kb2Zjb2RlOTk=:1oZn8F:e5QDf4Sn3B7NvgWCyMUUc9Fv1YM"; 87b5a3c3f1a55520_gr_cs1=godofcode99' \
  -H 'origin: https://leetcode.com' \
  -H 'referer: https://leetcode.com/problemset/all/' \
  -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  -H 'x-csrftoken: zIu3Q4DQ45N5Rm4AKnAWXmBYNDE5wuCs5AJwE8UQGEkoEEHgWA8M8T5LmDaMXMH6' \
  --data-raw '{"query":"\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ","variables":{"categorySlug":"","skip":0,"limit":100,"filters":{}}}' \
  --compressed