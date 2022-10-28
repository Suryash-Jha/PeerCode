import json

lst= []
f= open('Contest/questionWithQuestionTags.json','r')
data = json.load(f)
f.close()
for i in data:
    if i['questionCount'] > 4:
        obj={}
        obj['name']= i['name']
        obj['slug'] = i['slug']
        lst.append(obj)
f= open('Contest/questionWithQuestionTags.json','w')

json.dump(lst,f)
f.close()
print(lst)