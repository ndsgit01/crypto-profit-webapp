# crypto-profit-webapp

Web applicatiion to
- take in input of crypto tickers, 
- generate comparison plot of profit % changes recorded since 31 days ago for the entered cryptocurrencies 

Data for crypto currency: Web scraping historical data from https://finance.yahoo.com

Webapp endpoints
- /
  <br>
  ![image](https://github.com/ndsgit01/crypto-profit-webapp/assets/51270897/3db279bf-2327-4d27-ac10-d8219f1cae00)

- /show_plot
  <br>
  ![image](https://github.com/ndsgit01/crypto-profit-webapp/assets/51270897/fb376a66-8fe5-4562-83c0-f2968009b129)

Future work:
- allow input for time frame (remove hardcoded value of 31 days)
- speed up (using asyncio?)
- change input field from text to list of choices
