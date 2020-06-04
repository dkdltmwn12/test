from bs4 import BeautifulSoup
from selenium import webdriver
import time
from urllib.request import urlopen


def danggn(search):
    query_txt = search

    path = "C:\\Users\\dydtj\\Desktop\\test\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.daangn.com/search/" + query_txt)

    i = 0
    while i < 1:
        driver.find_element_by_class_name("more-btn").click()
        i = i + 1

    time.sleep(1)

    full_html = driver.page_source

    soup = BeautifulSoup(full_html, "html.parser")

    data = []
    n = 1
    for item in soup.select("a[href*=articles]"):
        data.append("https://www.daangn.com" + item.get("href", "/"))
        n += 1
        if n > 6:
            break

    imgurl = []
    n = 1
    for i in soup.find_all(class_="card-photo"):
        imgurl.append(i.find("img")["src"])
        n += 1
        if n > 6:
            break

    title = []
    n = 1
    for i in soup.find_all("span", {"class": "article-title"}):
        title.append(str(i.text))
        n += 1
        if n > 6:
            break

    cost = []
    n = 1
    for i in soup.find_all("p", {"class": "article-price"}):
        cost.append(str(i.text))
        n += 1
        if n > 6:
            break

    dic = {}
    n = 0
    while n < 6:
        dic.setdefault(data[n])
        dic[data[n]] = title[n]
        n += 1

    dic2 = {}
    m = 0
    while m < 6:
        dic2.setdefault(imgurl[m])
        dic2[imgurl[m]] = cost[m]
        m += 1

    return dic, dic2


def hellomarket(search):
    query_txt = search

    path = "C:\\Users\\dydtj\\Desktop\\test\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.hellomarket.com/search?q=" + query_txt)

    full_html = driver.page_source
    soup = BeautifulSoup(full_html, "html.parser")

    hdata = []
    n = 1
    for item in soup.select("a[href*=item]"):
        hdata.append("https://www.hellomarket.com" + item.get("href", "/"))
        n += 1
        if n > 6:
            break

    himgurl = []
    n = 1
    for i in soup.find_all(class_="image_centerbox"):
        himgurl.append(i.find("img")["src"])
        n += 1
        if n > 6:
            break

    htitle = []
    n = 1
    for i in soup.find_all("div", {"class": "item_title"}):
        htitle.append(str(i.text))
        n += 1
        if n > 6:
            break

    hcost = []
    n = 1
    for i in soup.find_all("div", {"class": "item_price"}):
        hcost.append(i.text)
        n += 1
        if n > 6:
            break

    hdic = {}
    n = 0
    while n < 6:
        hdic.setdefault(hdata[n])  # url
        hdic[hdata[n]] = htitle[n]
        n += 1

    hdic2 = {}
    m = 0

    while m < 6:
        hdic2.setdefault(himgurl[m])
        hdic2[himgurl[m]] = hcost[m]
        m += 1

    return hdic, hdic2


# def sellit(search):
#     query_txt = search

#     path = "C:\\Users\\dydtj\\Desktop\\test\\chromedriver.exe"
#     driver = webdriver.Chrome(path)
#     driver.get("https://www.withsellit.com/search?query=" + query_txt)

#     full_html = driver.page_source
#     soup = BeautifulSoup(full_html, "html.parser")

#     sdata = []
#     n = 0
#     for item in soup.select("a[href*=products]"):
#         sdata.append("https://www.withsellit.com" + item.get("ng-href", "/"))
#         if sdata[n] == "https://www.withsellit.com/":
#             del sdata[n]
#             n = n - 1
#         n = n + 1
#         if n > 5:
#             break

#     simgurl = []
#     n = 1
#     for i in soup.find_all(class_="gdidx-img"):
#         simgurl.append(i.find("img")["src"])
#         n += 1
#         if n > 6:
#             break

#     stitle = []
#     n = 1
#     for i in soup.find_all("div", {"class": "gdidx-name ng-binding"}):
#         stitle.append(str(i.text))
#         n += 1
#         if n > 6:
#             break

#     scost = []
#     n = 1
#     for i in soup.find_all("span", {"class": "gdidx-price-unit.ng-hide"}):
#         scost.append(i.text)
#         n += 1
#         if n > 6:
#             break

#     sdic = {}
#     n = 0
#     while n < 6:
#         sdic.setdefault(sdata[n])
#         sdic[sdata[n]] = stitle[n]
#         n += 1

#     sdic2 = {}
#     m = 0

#     while m < 6:
#         sdic2.setdefault(simgurl[m])
#         sdic2[simgurl[m]] = scost[m]
#         m += 1

#     return sdic, sdic2
