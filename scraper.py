from bs4 import BeautifulSoup
import requests,openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated Movies"
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMBD Rating'])
try:

    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    #print(source.text)
    soup = BeautifulSoup(source.text, 'html.parser')
    
    movies = soup.find('tbody',class_="lister-list").find_all('tr')
    for movie in movies:
        
        name = movie.find('td',class_="titleColumn").find('a').text
        rank = movie.find('td',class_="titleColumn").get_text(strip=True).split(".")[0]
        year = movie.find('td',class_="titleColumn").span.text.strip('()')
        rating = movie.find('td',class_="ratingColumn imdbRating").strong.text
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating])
        
except Exception as e:
    print(e)

excel.save("IMBD Movie Ratings.xlsx")

