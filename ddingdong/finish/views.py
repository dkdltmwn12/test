from django.shortcuts import render
from django.http import HttpResponse
from .crawling import danggn
from .crawling import hellomarket

# from .crawling import sellit


def form_test(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        search = request.POST["search"]
        dgdic, dgdic2 = danggn(search)
        hdic, hdic2 = hellomarket(search)
        # sdic, sdic2 = sellit(search)

        return render(
            request,
            "index.html",
            context={
                "dgdic": dgdic,
                "dgdic2": dgdic2,
                "hdic": hdic,
                "hdic2": hdic2,
                # "sdic": sdic,
                # "sdic2": sdic2,
            },
        )


def login(request):
    context = {}
    return render(request, "login.html", context=context)
