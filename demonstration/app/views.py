from django.shortcuts import render, HttpResponse
import json
import requests

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')
    
def test(request):
    return HttpResponse('my second  view')
    
def profile(request):
    jsonlist = []
    req = requests.get('https://api.github.com/users/jblloyd14')
    jsonlist.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonlist:
        userData['name'] = data['name']
        userData['email']=data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)
    #content = req.text
    return HttpResponse(parsedData)
    
    
