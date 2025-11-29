# Forex CLI Tool

A command-line interface (CLI) tool to fetch and convert forex data using the **Frankfurter API**.  
This project demonstrates API integration, JSON handling, user input validation, and error-safe programming in Python.

---

## Features

1. **Currency Conversion**  
   Convert an amount from one currency to another using the latest rates.

2. **Historical Rates**  
   Fetch historical exchange rates for a specific date.

3. **Time Series Data**  
   Get exchange rates for a currency pair over a date range.

4. **Error Handling**  
   Handles invalid currency codes, bad inputs, network errors, and API failures .

---

## Requirements

- Python 3.x  
- `requests` library  

## Install dependencies via pip:

- pip install -r requirements.txt

## Notes

- The program uses a helper function to safely handle API requests.
- All outputs are printed in the CLI for easy reading.
- You can expand this project to save results in JSON or integrate more APIs.
