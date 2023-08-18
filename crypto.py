import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

def get_profits(crypto_ticker, time_period=31):
  # query for response
  def to_unix_timestamp(timestamp):
    return (timestamp - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
  end = pd.Timestamp.now()
  start = end - pd.Timedelta(time_period, 'D')
  period2 = to_unix_timestamp(end)
  period1 = to_unix_timestamp(start)
  url = (f'https://finance.yahoo.com/quote/{crypto_ticker}/history'
         f'?period1={period1}&period2={period2}'
          '&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true')
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
              AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.102 \
              Safari/537.36'}
  response = requests.get(url, headers=headers)
  assert response.status_code == 200

  # process response
  soup = BeautifulSoup(response.text)
  table = soup.find('table', attrs={'data-test':'historical-prices'})
  rows = table.find_all('tr')[1:]
  prices = []
  for row in rows:
    try:
      price = float(row.find_all('td')[1].text.replace(',', ''))
      prices.append(price)
    except:
      pass
  prices = np.array(prices[::-1])

  # compute profits percentage
  profits = ((prices/prices[0]) - 1)*100

  return profits