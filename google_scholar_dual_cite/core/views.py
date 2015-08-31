from django.shortcuts import render_to_response
from django.http.response import JsonResponse, HttpResponseBadRequest
from google_scholar_dual_cite.core.scholar_x import CitesScholarQuery
from scholar import SearchScholarQuery, ScholarQuerier


def home(request):
    if request.method == 'GET':
        return render_to_response('home.html')


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
            result = {'articles:'[{'title': '', id: 0, 'url': ''}]}
        else:
            result = {'articles': [{'title': articles[0]['title'],
                                    'id': articles[0]['cluster_id'],
                                    'url': articles[0]['url']}]}
        return JsonResponse(result)
    else:
        return HttpResponseBadRequest()


def cites_api(request):
    if request.method == 'GET':
        article_id = request.GET.get('article_id', 0)
        page = request.GET.get('page', None)
        if not article_id or page is None:
            return HttpResponseBadRequest()

        query = CitesScholarQuery(article_id, page)
        querier = ScholarQuerier()
        querier.send_query(query)
        articles = querier.articles

        cites = []
        for article in articles:
            cites.append({'title': article['title'],
                          'id': article['cluster_id'],
                          'url': article['url']})

        return JsonResponse({'cites': cites})
    else:
        return HttpResponseBadRequest()

