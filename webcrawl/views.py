from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

apiKey = "58df9d61"

def movie_search(request):
    sendData = {
        "searchKeyword" : "spider"
    }
    return render(request, "webcrawl/movie_search.html", sendData)

def movie_all_search(request):
    print("func movie_all_search")
    url = f"http://www.omdbapi.com/?s=movie&y=2026&apikey={apiKey}&page=1"
    response = requests.get(url)

    # 딕셔너리 변경 response.text
    data = json.loads(response.text)
    print(data)

    sendData = {
        "searchKeyword" : "",
        "qryData" : data
    }

    # all search로 이동
    return render(request, "webcrawl/movie_search.html", sendData)

def movie_qry_search(request):
    print("func movie_qry_search")
    qry = request.GET.get('qry', '')
    print('qry = ',qry)

    # AI 프로그램, 데이터베이스 처리 되는 루틴
    # url = f"http://www.omdbapi.com/?s=movie&y=2026&apikey={apiKey}&page=1"
    url = f"http://www.omdbapi.com/?apikey={apiKey}&s={qry}"

    response = requests.get(url)

    # 딕셔너리 변경 response.text
    data = json.loads(response.text)
    print(data)

    sendData = {
        "searchKeyword" : qry,
        "qryData" : data
    }

    # all search로 이동
    return render(request, "webcrawl/movie_search.html", sendData)

    return HttpResponse("func movie_qry_search")