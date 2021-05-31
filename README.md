# wiki_text_analysis

A Django based web application to determine the count of each word of a wikipedia page and display top ten frequent words.<br>

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

```bash
pip install django
pip install bs4
pip install numpy
pip install re
```

TECHNOLOGIES USED :

1) On the frontend side technologies used are HTML, CSS (which is stored in static folder)<br>
2) For web scrapping technology used is bs4 (BeautifulSoup)<br>
3) To validate the input phython package used is re<br>
4) To operate on list/array numpy is used <br>

## Steps to execute project
- Download zip file or clone the project.<br>
- Execute installations.<br>
- Open command prompt of that directory.<br>
- Execute command :
```bash
python manage.py runserver
```
- A prompt will be generated stating "Starting development server at http://127.0.0.1:8000/" (Depends on your localhost)<br>
- Paste the link to any web browser and append "wiki_Freq" (Example : http://127.0.0.1:8000/wiki_Freq)

## Screenshots
![](images/Screenshot%20(147).png)
![](images/Screenshot%20(148).png)
### <br>Including stop words <br><br>
![](images/Screenshot%20(149).png)
![](images/Screenshot%20(150).png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
