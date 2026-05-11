from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Movie
from . translate import translate_en_to_ko
import requests
import json

apiKey = "58df9d61"

def movie_search(request):
    sendData = {
        "searchKeyword" : "spider"
    }
    return render(request, "webcrawl/movie_search.html", sendData)

############################################################################
# 영화 전체 검색
############################################################################

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

############################################################################
# 영화 제목 검색
############################################################################

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

def movie_save(request, imdbId):
    print("movie_save")
    print("imdbId = ", imdbId)

    # API에서 상세정보 가져오기.
    url = f"http://www.omdbapi.com/?apikey={apiKey}&i={imdbId}"

    response = requests.get(url)

    # 딕셔너리 변경 response.text
    data = json.loads(response.text)
    print(data)

    # DB에 저장
    saveData = Movie()

    saveData.title      = data['Title']
    
    # 한국어 번역
    saveData.ko_title   = translate_en_to_ko(data['Title'])

    saveData.year       = data['Year']
    saveData.rated      = data['Rated']
    saveData.released   = data['Released']
    saveData.runtime    = data['Runtime']
    saveData.genre      = data['Genre']
    saveData.director   = data['Director']
    saveData.writer     = data['Writer']
    saveData.actors     = data['Actors']
    saveData.plot       = data['Plot']
    saveData.language   = data['Language']
    saveData.country    = data['Country']
    saveData.awards     = data['Awards']
    saveData.poster     = data['Poster']

    # Ratings
    try:
        saveData.ratings1_source     = data['Ratings'][0]['Source']
        saveData.ratings1_value      = data['Ratings'][0]['Value']
    except:
        saveData.ratings1_source     = ''
        saveData.ratings1_value      = ''
    try:
        saveData.ratings2_source     = data['Ratings'][1]['Source']
        saveData.ratings2_value      = data['Ratings'][1]['Value']
    except:
        saveData.ratings2_source     = ''
        saveData.ratings2_value      = ''

    # Score fields
    saveData.metascore      = data['Metascore']
    saveData.imdb_rating    = data['imdbRating']
    saveData.imdb_votes     = data['imdbVotes']
    saveData.imdb_id        = data['imdbID']

    # Metadata
    saveData.type       = data['Type']
    saveData.dvd        = data['DVD']
    saveData.box_office = data['BoxOffice']
    saveData.production = data['Production']
    saveData.website    = data['Website']
    saveData.response   = data['Response']

    # 저장
    try:
        saveData.save()
    except:
        return HttpResponse("중복된 데이터 입니다.")

    return redirect('/webcrawl/')