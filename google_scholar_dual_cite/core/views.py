from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
from scholar import SearchScholarQuery, ScholarQuerier

# Create your views here.


def home(request):
    if request.method == 'GET':
        return HttpResponse('<html>get</html>')
    elif request.method == 'POST':
        return


def articles_by_query_api(request):
    if request.method == 'GET':
        phrase = request.GET.get('phrase', '')
        if not phrase:
            return HttpResponseBadRequest()
        query = SearchScholarQuery()
        query.set_phrase(phrase)
        querier = ScholarQuerier()
        querier.send_query(query)
        articles = querier.articles
        if not articles:
            result = {'articles:'[{'title': '', id: 0}]}
        else:
            result = {'articles': [{'title': articles[0]['title'], 'id': articles[0]['cluster_id']}]}
        return JsonResponse(result)
    else:
        return HttpResponseBadRequest()

