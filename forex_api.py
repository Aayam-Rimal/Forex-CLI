## forex api using frankfurter api 

import requests
import logging

log_path="forex.log"

logging.basicConfig(
   filename=log_path,
   level= logging.INFO,
   format="%(asctime)s - %(levelname)s - %(message)s"


)


def safe_get(url, params=None, timeout=5):
   try:
      response=requests.get(url, params=params, timeout=timeout)
      response.raise_for_status()
      data=response.json()
      return data
   except requests.exceptions.HTTPError as e:
      logging.error("HTTP error:", e)
   except requests.exceptions.ConnectionError as e:
      logging.error("connection error:", e)
   except requests.exceptions.Timeout as e:
      logging.error("timeout error:", e)
   except requests.exceptions.RequestException as e:
      logging.error("request failed:", e)
   except ValueError as e:
      logging.error("failed to parse json:", e)
   return None
      
      
   
def convert(fromcu, to, amount):
  latest_url= f"https://api.frankfurter.dev/v1/latest?base={fromcu}&symbols={to}"
  data= safe_get(latest_url)
  if data and to in data['rates']:
   converted_amount= amount * data['rates'][to]
   print(f" {amount} {fromcu}: {converted_amount} {to}")
  else:
     logging.error("conversion failed!!")


def historical(fromcu, to, date):
  historical_url=f"https://api.frankfurter.dev/v1/{date}?base={fromcu}&symbols={to}"
  data= safe_get(historical_url)
  if to in data['rates']:
   print(data['rates'])
  else:
     logging.error("data fetch failed!!")
  

def timeseries(fromcu, to, start_date, end_date):
  timeseries_url= f"https://api.frankfurter.dev/v1/{start_date}..{end_date}?base={fromcu}&symbols={to}"
  data= safe_get(timeseries_url)
  full_days= data['rates']
  for days,values in full_days.items():
    print(f"{days}: 1 {fromcu}: {values[to]} {to}")

  
def main():
    while True:
        choice= int(input("enter 1 to convert, 2 to see historical rate , 3 to see time series data and 4 to end : "))
        if choice==1:
            from_amt= input("Enter a valid base currency in symbols: ").upper()
            to= input("enter currency you want to convert to in symbols: ").upper()
            try:
             amount= float(input("enter amount of currency you want to convert: "))
             convert(from_amt, to, amount)
            except ValueError:
               logging.warning("invalid amount! enter correct one!")
               continue
            

        elif choice==2:
            from_curr= input("enter base currency in symbols: ").upper()
            to_curr= input("enter currency you want to convert to: ").upper()
            date= input("enter date in yyyy-mm-dd format: ")
            historical(from_curr, to_curr, date)

        elif choice==3:
            from_cur= input("enter base currency in symbols: ").upper()
            to_cur= input("enter currency you want to convert to: ").upper()
            start_date= input("enter start date in yyyy-mm-dd format: ")
            end_date= input("enter end date in yyyy-mm-dd format: ")
            timeseries(from_cur, to_cur, start_date, end_date)

        elif choice==4:
            break


main()






  

