from django.shortcuts import render, HttpResponse

# Create your views here.
import requests # Biblioteca  para solicitudes HTTP en formato JSON.
import json      #Biblioteca para dar formato a los datos JSON.

# Create your views here.

def index(request):
	return HttpResponse('<body style="background:black; color:white"><h1 style="color:#4cd137">DJANGO => Hello, World</h1><h3>I am first view</h3></body>')

def test(request):
	return HttpResponse('<body style="background:black; color:white"><h1 style="color:#4cd137">DJANGO => Hello, World</h1><h3>I am second view</h3></body>')

#Respuesta en bruto JSON.
"""def profile(request):
	req = requests.get("https://api.github.com/users/nullx5")
	content = req.text
	return HttpResponse(content)
"""
#respuesta estatica con user denifido previamente.
"""def profile(request):
	jsonList = []
	parsedData = []
	userData = {}
	req = requests.get("http://api.github.com/users/nullx5")
	jsonList.append(json.loads(req.content))

	for data in  jsonList:
		userData["id"] = data["id"]
		userData["name"] = data["name"]
		userData["blog"] = data["blog"]
		userData["email"] = data["email"]
		userData["public_gists"] = data["public_gists"]
		userData["public_repos"] = data["public_repos"]
		userData["avatar_url"] = data["avatar_url"]
		userData["followers"] = data["followers"]
		userData["following"] = data["following"]
		userData["created_at"] = data["created_at"]
		userData["location"] = data["location"]
	parsedData.append(userData)
	#return HttpResponse(parsedData)
	return render(request, "app/profile.html", {"data": parsedData})
"""
#Respuesta dinamica obteniendo el user con POST.
def profile(request):
	jsonList = []
	userData = {}
	parsedData = []
	if request.method == "POST":
		username = request.POST.get("user")
		req = requests.get("http://api.github.com/users/" + username)
		jsonList.append(req.json())
		#jsonList.append(json.loads(req.content))

		for data in  jsonList:
			userData["id"] = data["id"]
			userData["name"] = data["name"]
			userData["blog"] = data["blog"]
			userData["email"] = data["email"]
			userData["public_gists"] = data["public_gists"]
			userData["public_repos"] = data["public_repos"]
			userData["avatar_url"] = data["avatar_url"]
			userData["followers"] = data["followers"]
			userData["following"] = data["following"]
			userData["created_at"] = data["created_at"]
			userData["location"] = data["location"]
		parsedData.append(userData)
	#return HttpResponse(parsedData)
	return render(request, "app/profile.html", {"data": parsedData})
