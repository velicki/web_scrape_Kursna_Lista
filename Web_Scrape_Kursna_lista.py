import requests
import pandas as pd
from tkinter import *
from bs4 import BeautifulSoup
from tkhtmlview import HTMLLabel

def fetch_data():
    try:
        response = requests.get('https://www.kursna-lista.info/')
        response.raise_for_status()  # Raise exception for unsuccessful HTTP response
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('table', id='kursna-lista')
        rows = table.find_all('tr')[1:]

        headers = ['Šifra Valute', 'Zemlja', 'Valuta', 'Količina', 'Kupovni Kurs', 'Srednji Kurs', 'Prodajni Kurs']
        data = [[td.text for td in row.find_all('td')[1:8]] for row in rows[:6]]

        df = pd.DataFrame(data, columns=headers)
        return df
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching data: {e}")
        return None

def windows_configuration():
    K_Lista.geometry("530x250")
    K_Lista.title("KURSNA LISTA")
    K_Lista.resizable(False, False)
    icon = PhotoImage(file="icon.png")
    K_Lista.iconphoto(True, icon)
    K_Lista.config(bg="white")

def headline():
    headline_text = fetch_data()
    if headline_text is not None:
        headline = Label(K_Lista, text=headline_text, font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
        return headline
    else:
        return None

def display_data():
    data = fetch_data()
    if data is not None:
        df = pd.DataFrame(data)
        styled_df = df.style.set_table_styles([{'selector': 'tr', 'props': [('border', 'solid 1px')]}, {'selector': 'th', 'props': [('border', 'solid 1px')]}, {'selector': 'td', 'props': [('border', 'solid 1px')]}]).set_table_attributes("border=1").set_properties(**{'border-collapse': 'collapse', 'border': 'solid'})
        html_table = styled_df.to_html(index=False).replace('<table', '<table style="border-collapse:collapse;border:solid"')
        maintext = HTMLLabel(K_Lista, html=html_table)
        maintext.grid(row=2, column=0, columnspan=7, pady=2, padx=2)
    else:
        return None

K_Lista = Tk()
windows_configuration()

headline_label = headline()
if headline_label is not None:
    headline_label.grid(row=0, column=0, pady=2, padx=2, columnspan=7)

labels = ['Šifra Valute', 'Zemlja', 'Valuta', 'Količina', 'Kupovni Kurs', 'Srednji Kurs', 'Prodajni Kurs']
for i, label in enumerate(labels):
    lbl = Label(K_Lista, text=label, font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
    lbl.grid(row=1, column=i, pady=2, padx=2)

display_data()

K_Lista.mainloop()
