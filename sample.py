def zad1():
    # Proste okno
    import tkinter as tk

    window = tk.Tk()
    window.title("Zadanie 1")
    window.geometry("300x300")
    window.mainloop()
# zad1()
def zad2():
    # 2. Dodaj etykietę i przycisk
    import tkinter as TKTK
    window = TKTK.Tk()
    window.title("Zadanie 2")
    window.geometry("300x300")

    text = TKTK.Label(window,text="Hello World")
    text.pack()
    button = TKTK.Button(window,text="Kliknij mnie",command=lambda:print("Kliknięto"))
    button.pack()
    window.mainloop()
# zad2()


def zad3():
    # 3. Pole tekstowe i przycisk
    import tkinter as tk 
    window = tk.Tk()
    window.geometry("300x300")
    window.title("Zadanie 3")
    label1 = tk.Label(window,text="Zadanie 3",font="Sans")
    label1.pack()

    # Input = tk.
    def wys():
        x = entry.get()
        print(x)
    x = 0

    entry = tk.Entry(window)
    entry.pack()
    button = tk.Button(window,text="Wyślij",command=lambda:wys())
    button.pack()
    window.mainloop()
# zad3()

def zad4():
    # 4. Kalkulator dodawania
    import tkinter as tk
    master = tk.Tk()
    master.geometry("300x600")
    master.title("Zadanie 4 Kalkulator dodawnia")

    title = tk.Label(master,text="Kalkulator Dodawania",font="Sans")
    title.pack()
    entry1, entry2 = tk.Entry(master), tk.Entry(master)
    entry1.pack()
    entry2.pack()

    def suma():
        a = int(entry1.get())+ int(entry2.get())
        sumalabel = tk.Label(master,text=str(a),background="white",font="Sans")
        sumalabel.pack()

    button = tk.Button(master,text="Oblicz sume",command=lambda:suma())
    button.pack()

    master.mainloop()
# zad4()

def zad5():
    # 5. Kalkulator działań (dodawanie, odejmowanie, mnożenie, dzielenie)
    import tkinter as tk
    from tkinter import ttk

    master = tk.Tk()
    master.geometry("300x450")
    master.title("Zadanie 5")


    label = tk.Label(master,text="Zadanie 5 \n Kalkulator: \ndodawanie odejmowanie mnożenie dzielenie")
    label.pack()

    opcje = ["Dodawanie","Odejmowanie","Mnożenie","Dzielenie"]
    combo = ttk.Combobox(master,values=opcje)
    combo.pack(pady=15)
    enter1 , enter2 = tk.Entry(master) , tk.Entry(master)

    enter1.pack()
    enter2.pack()

    def wynik():
        a = int(enter1.get())
        b = int(enter2.get())
        if combo.get() == "Dodawanie":
            c = a + b
        elif combo.get() == "Odejmowanie":
            c = a - b
        elif combo.get() == "Mnożenie":
            c = a * b
        elif combo.get() == "Dzielenie":
            c = a / b

        finalo = tk.Label(master,text=c)
        finalo.pack()

    button = tk.Button(master,text="Oblicz",command=lambda:wynik())
    button.pack()
    



    master.mainloop()

# zad5()

def zad6():
    # Jeszcze raz ale z gridem
    import tkinter as tk
    from tkinter import ttk

    master = tk.Tk()
    master.geometry("220x400")
    master.title("Zadanie 6")

    title = tk.Label(master,text="Zadanie 6 \n Kalkulator: \ndodawanie odejmowanie\n mnożenie dzielenie  ale z gridem")
    title.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    option = ["Dodawanie","Odejmowanie","Mnożenie","Dzielenie"]
    combo = ttk.Combobox(master,values=option)
    combo.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    enter1, enter2 = tk.Entry(master,width=8),tk.Entry(master,width=8)
    enter1.grid(row=4,column=0)
    enter2.grid(row=4,column=1)

    def finalo():
        
        a = int(enter1.get())
        b = int(enter2.get())
        if combo.get() == "Dodawanie":
            c = a + b
        elif combo.get() == "Odejmowanie":
            c = a - b
        elif combo.get() == "Mnożenie":
            c = a * b
        elif combo.get() == "Dzielenie":
            c = a / b

        odp = tk.Label(master,text=c,bg="gray",font=30,padx=5,pady=5)
        odp.grid(row=6,column=0,columnspan=2)

    button = tk.Button(master,text="Oblicz",command=lambda:finalo())
    button.grid(row=5,column=0,columnspan=2)
    master.mainloop()
# zad6()


def dzialanie_grida(): # by AI
    import tkinter as tk

    root = tk.Tk()
    root.title("Łączenie komórek w grid()")
    root.geometry("300x200")

    # Etykieta zajmująca dwie kolumny
    label1 = tk.Label(root, text="To zajmuje 2 kolumny", bg="lightblue")
    label1.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # Etykieta zajmująca dwa wiersze
    label2 = tk.Label(root, text="To zajmuje 2 wiersze", bg="lightgreen")
    label2.grid(row=1, column=0, rowspan=2, padx=10, pady=5)

    # Dodatkowe etykiety do wypełnienia siatki
    label3 = tk.Label(root, text="Kolumna 2, Wiersz 1", bg="lightgray")
    label3.grid(row=1, column=1, padx=10, pady=5)

    label4 = tk.Label(root, text="Kolumna 2, Wiersz 2", bg="lightgray")
    label4.grid(row=2, column=1, padx=10, pady=5)

    root.mainloop()
# dzialanie_grida()


ciag = ""



def zad7_kal():
    import tkinter as tk
    # Full kalkulator

    master = tk.Tk()
    master.geometry("295x463")  # 300 px po 100 px na jedną columne
    master.title("Kalkulator by Fistaszeq")


    def liczymy(x):
        global ciag
        ciag += x
        output = tk.Label(master,text=ciag,bg="white",font=20,width=30)
        output.grid(row=0,column=0,columnspan=3)
    
    def finalito():
        global ciag
        x = eval(ciag)

        output = tk.Label(master,text=x,bg="white",font=20,width=30)
        output.grid(row=0,column=0,columnspan=3)
        ciag = ""

    btn = [tk.Button(master,text="9",width=9,height=4,command=lambda: liczymy("9")),
           tk.Button(master,text="8",width=9,height=4,command=lambda: liczymy("8")),
           tk.Button(master,text="7",width=9,height=4,command=lambda: liczymy("7")),

           tk.Button(master,text="6",width=9,height=4,command=lambda: liczymy("6")),
           tk.Button(master,text="5",width=9,height=4,command=lambda: liczymy("5")),
           tk.Button(master,text="4",width=9,height=4,command=lambda: liczymy("4")),

           tk.Button(master,text="3",width=9,height=4,command=lambda: liczymy("3")),
           tk.Button(master,text="2",width=9,height=4,command=lambda: liczymy("2")),
           tk.Button(master,text="1",width=9,height=4,command=lambda: liczymy("1")),

           tk.Button(master,text="0",width=9,height=4,command=lambda: liczymy("0")),
           tk.Button(master,text="+",width=9,height=4,command=lambda: liczymy("+")),
           tk.Button(master,text="-",width=9,height=4,command=lambda: liczymy("-")),

           tk.Button(master,text="*",width=9,height=4,command=lambda: liczymy("*")),
           tk.Button(master,text=":",width=9,height=4,command=lambda: liczymy("/")),
           tk.Button(master,text="=",width=9,height=4,command=lambda: finalito())
           ]
    

    wynik = "Sample"
    output = tk.Label(master,text=wynik,bg="white",font=20,width=30)
    output.grid(row=0,column=0,columnspan=3)


    btn[0].grid(row=1,column=0)
    btn[1].grid(row=1,column=1)
    btn[2].grid(row=1,column=2)

    btn[3].grid(row=2,column=0)
    btn[4].grid(row=2,column=1)
    btn[5].grid(row=2,column=2)

    btn[6].grid(row=3,column=0)
    btn[7].grid(row=3,column=1)
    btn[8].grid(row=3,column=2)
    
    btn[9].grid(row=4,column=0)
    btn[10].grid(row=4,column=1)
    btn[11].grid(row=4,column=2)

    btn[12].grid(row=5,column=0)
    btn[13].grid(row=5,column=1)
    btn[14].grid(row=5,column=2)




    master.mainloop()

zad7_kal()