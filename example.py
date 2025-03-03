from valr import Valr
from dotenv import load_dotenv
from os import getenv

load_dotenv()

if __name__ == '__main__':
    valr = Valr(key=getenv('VALR_KEY', ''), secret=getenv('VALR_SECRET', ''))

    # Example usage:
    response = valr.account.balances()
    print(response.content)
