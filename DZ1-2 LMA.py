import requests
import json
from pprint import pprint
import wikipedia


a = wikipedia.summary("Bill Gates's house")
b = wikipedia.page("Bill Gates's house").content
c = wikipedia.page("Bill Gates's house").url
d = wikipedia.page("Bill Gates's house").references
e = wikipedia.page("C").title
f = wikipedia.page("Bill Gates's house").categories
g = wikipedia.page("Bill Gates's house").links
h = wikipedia.page("Bill Gates's house").images[0]
i = wikipedia.page("Bill Gates's house").html()

data = {}
data['wiki'] = []
json.dumps(data, indent=4)
data['wiki'].append({
    'Resume' : a
})
pprint(a)
pprint("-"*150)

data['wiki'].append({
    'Text' : b
})
pprint(b)
pprint("-"*150)

data['wiki'].append({
    'URL' : c
})
print(c)
pprint("-"*150)

data['wiki'].append({
    'Links' : d
})
pprint(d)
pprint("-"*150)

data['wiki'].append({
    'Title' : e
})
print(e)
pprint("-"*150)

data['wiki'].append({
    'Categories' : f
})
pprint(f)
pprint("-"*150)

data['wiki'].append({
    'Pages title' : g
})
pprint(g)
pprint("-"*150)

data['wiki'].append({
    'Img links' : h
})
print(h)
pprint("-"*150)

data['wiki'].append({
    'Total page' : i
})
pprint(i)
pprint("-"*150)

json.dumps(data, indent=4)

with open('data.json', 'w') as out:
    json_data = json.dump(data, out)