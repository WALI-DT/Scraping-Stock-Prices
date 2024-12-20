import requests 
from bs4 import BeautifulSoup
import pandas
import random


mystocksdata = []
mystocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "BRK-B", 
    "NVDA", "TSLA", "UNH", "JNJ", "XOM", "JPM", "V", 
    "PG", "MA", "HD", "CVX", "MRK","AVGO", "KO", "PEP",
    "COST", "TMO", "PFE", "DIS", "ADBE","CMCSA",
    "CRM", "ACN", "ABT", "INTC", "LIN","TGT",
    "AMD", "HON", "NFLX", "TXN", "VZ", "AMGN", "TMUS"
]


def getdata(symbol):

    url = f'https://finance.yahoo.com/quote/{symbol}/'
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:110.0) Gecko/20100101 Firefox/110.0",
        "Mozilla/5.0 (Linux; Android 11; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1"
    ]

    random_user_agent = random.choice(user_agents)
    
    headers = {
        "User-Agent": random_user_agent
    }

    
    r = requests.get(url, headers=headers)
    # print(r.status_code)

    soup = BeautifulSoup(r.content, 'lxml')
    # print(soup.title.text)
    
    stock = {
        "name" : soup.find("h1", class_="yf-xxbei9").text, 
        "closing_price" : soup.find("fin-streamer", class_="livePrice yf-1tejb6").text,
        "move" : soup.find("fin-streamer", class_="priceChange yf-1tejb6").text,
        "percentage_move" : soup.find_all("fin-streamer", class_="priceChange yf-1tejb6")[1].text,
    }
    
    return(stock)

print("completed")

for item in mystocks:
    mystocksdata.append(getdata(item))

df = pandas.DataFrame(mystocksdata)
# print(df)

df.to_csv(r"C:\Users\VICKY COMPUTERS\Desktop\web scraping projects\stock_price_and_move.csv")
