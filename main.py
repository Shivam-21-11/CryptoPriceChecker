from urllib.request import urlopen
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import date


def get_price():
    '''
    Gets The Current Bitcoin Price From The Website
    '''
    url = "https://www.coindesk.com/price/bitcoin"
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    Html_tag = soup.find_all("div", {"class": "price-large"})
    Tag_String = str(Html_tag)
    BitCoin_Price = Tag_String[55:64]
    print(f"${BitCoin_Price}")
    return BitCoin_Price


window = tk.Tk()
window.geometry("200x100")
window.title("BitCoin Price Checker")
Today_date = date.today()

label = tk.Label(window, text=f"The Bitcoin Price as of {Today_date}").pack()
pricelabel = tk.Label(window, text=f"$ {get_price()}").pack()

window.mainloop()
