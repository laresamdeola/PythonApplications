from tkinter import *
import requests


def get_zen_quote():
    url = "https://buddha-api.com/api/random"
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    zen_quote = data['text']
    canvas.itemconfig(quote_text, text=zen_quote, fill='black')


window = Tk()
window.title('ZENQUOTES')
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=400)
quote_text = canvas.create_text(150,
                                207,
                                text="Zen Quotes",
                                width=250,
                                font=('Times New Roman', 25, 'bold'),
                                fill="black"
                                )
canvas.grid(row=0, column=0)

button = Button(width=20,
                height=2,
                highlightthickness=0,
                command=get_zen_quote,
                bg="black",
                text='FETCH',
                fg='white',
                font=('Times New Roman', 15, 'bold'))
button.grid(row=1, column=0)


window.mainloop()