import requests
from tkinter import *
from bs4 import BeautifulSoup
import pandas as pd





response = requests.get('https://www.kursna-lista.info/')
#print (response)
html = response.text
soup = BeautifulSoup(html, 'lxml')
table1 = soup.find('table', id='kursna-lista') #text.strip()
date1 = soup.find('div', id='maint-table-header2')
for i in date1.find_all('h2'):
    headline_text = i.text.strip()
headers = []
# for i in table1.find_all('th'):
#     title = i.text
#     headers.append(title)
# mydata = pd.DataFrame(columns = headers[1:])
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = []
    row.append(row_data[1].text)
    row.append(row_data[2].text)
    row.append(row_data[3].text)
    row.append(row_data[4].text)
    row.append(row_data[5].text)
    row.append(row_data[6].text)
    row.append(row_data[7].text)
    headers.append(row)

#print (headers[1][1])

df = pd.DataFrame(headers[0:6])
maintext_list = df.to_string(index=False)

#------------------------------------------

def windows_configuration():
        K_Lista.geometry("530x250")
        K_Lista.title("KURSNA LISTA")
        K_Lista.resizable(False, False)
        icon = PhotoImage(file="icon.png")
        K_Lista.iconphoto(True, icon)
        K_Lista.config(bg="white")

def headline():
    headline = Label(K_Lista, 
                text=headline_text, 
                font=("Arial", 10), 
                fg="BLACK", borderwidth=1, relief="solid")
    return headline

def maintext():
    maintext = Label(K_Lista, 
                text=maintext_list, 
                font=("Arial", 10), 
                fg="BLACK",
                bg="white", borderwidth=1, relief="solid")
    return maintext

#------------------------------------------

K_Lista = Tk()
l1 = Label(K_Lista, text = "Šifra Valute", font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
l2 = Label(K_Lista, text = "Zemlja", font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
l3 = Label(K_Lista, text = "Valuta", font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
l4 = Label(K_Lista, text = "Količina", font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
l5 = Label(K_Lista, text = "Kupovni Kurs", font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
l6 = Label(K_Lista, text = "Srednji Kurs", font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
l7 = Label(K_Lista, text = "Prodajni Kurs", font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")


canvas = Canvas(K_Lista, width=530, height=250, bg="gray")

windows_configuration()

#------------------------------------------

headline().grid(row = 0, column = 0, pady = 2, padx = 2, columnspan = 7)
l1.grid(row = 1, column = 0, pady = 2, padx = 2)
l2.grid(row = 1, column = 1, pady = 2, padx = 2)
l3.grid(row = 1, column = 2, pady = 2, padx = 2)
l4.grid(row = 1, column = 3, pady = 2, padx = 2)
l5.grid(row = 1, column = 4, pady = 2, padx = 2)
l6.grid(row = 1, column = 5, pady = 2, padx = 2)
l7.grid(row = 1, column = 6, pady = 2, padx = 2)

for i in range(0,7):
    for j in range(0,7):
        field=("field{}{}".format(i, j))
        globals()[field] = Label(K_Lista, text = headers[i][j], font=("Arial", 10), fg="BLACK", borderwidth=1, relief="solid")
        globals()[field].grid(row = i+2, column = j, pady = 2, padx = 2)
#maintext().pack(side="top", pady=10)


K_Lista.mainloop()