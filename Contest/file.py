import json
f= open("questionWithQuestionTags.json")
data= json.load(f)
f.close()
lst= data["items"]
for i in lst:
    print(f'("{i["slug"]}","{i["name"]}"),')

