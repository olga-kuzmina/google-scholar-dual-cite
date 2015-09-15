from django.shortcuts import render_to_response
from django.http.response import JsonResponse, HttpResponseBadRequest
import time
from google_scholar_dual_cite.core.scholar_x import CitesScholarQuery
from scholar import SearchScholarQuery, ScholarQuerier


def home(request):
    if request.method == 'GET':
        return render_to_response('home.html')


def papers_by_query_api(request):
    if request.method == 'GET':
        phrase = request.GET.get('phrase', '')
        if not phrase:
            return HttpResponseBadRequest()

        query = SearchScholarQuery()
        query.set_phrase(phrase)
        querier = ScholarQuerier()
        querier.send_query(query)
        papers = querier.articles

        if not papers:
            result = {'papers': [{'title': '', 'id': 0, 'url': '', 'excerpt': ''}]}
        else:
            result = {'papers': [{'title': papers[0]['title'],
                                  'id': papers[0]['cluster_id'],
                                  'url': papers[0]['url'],
                                  'excerpt': papers[0]['excerpt']}]}
        return JsonResponse(result)
    else:
        return HttpResponseBadRequest()


def cites_api(request):
    if request.method == 'GET':
        paper_id = request.GET.get('paper_id', 0)
        page = request.GET.get('page', None)
        if not paper_id or page is None:
            return HttpResponseBadRequest()
        query = CitesScholarQuery(paper_id, page)
        querier = ScholarQuerier()
        querier.send_query(query)
        papers = querier.articles

        cites = []
        for paper in papers:
            cites.append({'title': paper['title'],
                          'id': paper['cluster_id'],
                          'url': paper['url']})

        return JsonResponse({'paper_id': paper_id, 'cites': cites})
    else:
        return HttpResponseBadRequest()

