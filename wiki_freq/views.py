from wiki_text_analysis.settings import TEMPLATES
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import numpy as np
from re import search


# Create your views here.


def home(request):
    return render(request, 'home.html')


def wikiprocess(request):
    url = request.POST.get('url_link')
    wiki_url = "https://en.wikipedia.org/wiki/"
    if search(wiki_url, url):
        url = request.POST.get('url_link')
        chk_btn = request.POST.get('chk_btn')
        print(chk_btn)
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')

        content = soup.get_text()

        with open("file.txt", "w+", encoding="utf-8") as f:
            f.write(content)

        with open("file.txt", "r", encoding="utf-8") as file_read:
            file_count = file_read.read()

        file_count_lower = file_count.lower()
        unique_word = {}
        words = file_count_lower.split()
        # checking stopwords for better results
        # Program will also work if we remove check_stopwords
        if chk_btn=="on":
            check_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
                        'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        else:
            check_stopwords=[]
        for word in words:
            if word not in unique_word and word not in check_stopwords:
                if len(word) == 1 and ((ord(word) >= 33 and ord(word) <= 64) or (ord(word) >= 91 and ord(word) <= 96)):
                    # print(ord(word))
                    continue
                unique_word[word] = 0
            else:
                pass

        for i in unique_word:
            word_frequency = words.count(i)
            unique_word[i] = word_frequency
            # print(i, ":", word_frequency)

        sort_orders = sorted(unique_word.items(), key=lambda x: x[1], reverse=True)
        temp = 0
        srno = 1
        res = []
        for i in sort_orders:
            print(i[0], ":", i[1])
            temp = temp + 1
            if temp == 10:
                break
            for e in sort_orders:
                res.append((srno, e[0], np.round(e[1], 3)))
                srno = srno+1
         
            res = res[:10]
            return render(request, 'result.html', {'res': res})

    else:
        error_msg="Please enter any Wikipedia URL"
        # print(error_msg)
    return render(request, 'home.html',{'error':error_msg})
    
   