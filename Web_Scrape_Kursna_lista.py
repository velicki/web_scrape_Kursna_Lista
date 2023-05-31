import requests
from tkinter import *
from bs4 import BeautifulSoup
import pandas as pd


def windows_configuration():
    K_Lista.geometry("530x250")
    K_Lista.title("KURSNA LISTA")
    K_Lista.resizable(False, False)
    icon = PhotoImage(file="icon.png")
    K_Lista.iconphoto(True, icon)
    K_Lista.config(bg="white")


def fetch_data():
    try:
        response = requests.get('https://www.kursna-lista.info/')
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        return soup
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching data: {e}")
        return None


def get_headline_text():
    date1 = fetch_data().find('div', id='maint-table-header2')
    for i in date1.find_all('h2'):
        headline_text = i.text.strip()
    return headline_text


def get_rows_data():
    table1 = fetch_data().find('table', id='kursna-lista')
    rows = table1.find_all('tr')[1:]
    data = [[td.text for td in row.find_all('td')[1:8]] for row in rows]
    return data


def display_data():
    headline_text = get_headline_text()
    headline_label = ["Šifra Valute", "Zemlja", "Valuta", "Količina", "Kupovni Kurs", "Srednji Kurs", "Prodajni Kurs"]

    headline = Label(K_Lista, text=headline_text, font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
    headline.grid(row=0, column=0, pady=15, padx=2, columnspan=7)

    for i, label in enumerate(headline_label):
        field1 = Label(K_Lista, text=label, font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
        field1.grid(row=1, column=i, pady=2, padx=2)

    for i in range(0, 6):
        for j in range(0, 7):
            field = Label(K_Lista, text=get_rows_data()[i][j], font=("Arial", 10), fg="BLACK", borderwidth=1,
                          relief="solid")
            field.grid(row=i + 2, column=j, pady=2, padx=2)


# ------------------------------------------

K_Lista = Tk()

canvas = Canvas(K_Lista, width=530, height=250, bg="gray")

windows_configuration()

display_data()

K_Lista.mainloop()
