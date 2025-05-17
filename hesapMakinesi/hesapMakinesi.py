from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    
    def __init__(self,master): #GUI arayüzü kullanildi #bu satir yapici methottur(constructor) bu sinif cagirilidiginda calisan ilk fonskiyondur
        master.title("Calculator") # Başlık
        master.geometry('357x420+0+0') #Genişlik ve yükseklik, 0+0 ise ekranın sol üst köşesine 0,0 koordinatlarina yerleştirir
        master.config(bg='gray') # pencere arka plani gri yapar
        master.resizable(False,False) #pencere yeniden boyutlandirilmamasini sağlar

        self.equation = StringVar() #hesap makinesinin giriş kismindaki görünecek işlemleri tutar
        self.entry_value='' #hesaplamada kullanilacak işlemin metinsel halini tutar(başlangiçta boştur)
        Entry(width=17,bg='#fff',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0) #kullanicidan giriş alamk için bir giriş kutusu oluşturur

        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='white', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=350)
    def show(self,value): #bir butona basıldığında o butonun degerini ekrana yazdırmaya yarayan fonskiyon
        self.entry_value+=str(value) #degeri string olarak alir ve bunu soldaki degiskene ekler
        self.equation.set(self.entry_value) #StringVar() değişkenini günceller

    def clear(self): #Sonuç ekranini temizlemek için kullanilir
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)
    
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set("syntx err!")
            self.entry_value = ''



Root=Tk()
calculator=Calculator(Root)
Root.mainloop()