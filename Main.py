from tkinter import *
from Calculate import *

obj=Convert()
def click():
	x=a.get()
	y=b.get()
	k,flag=obj.cal(x,y)
	if(flag==1):
		val, s = (k).split(' ', 1)
		val=str(round(float(val),2))+' '+s
		output.delete(0.0,END)
		output.insert(0.0,val)
	else:
		output.delete(0.0, END)
		output.insert(0.0, k)

def close_window():
	window.destroy()
	exit()


window=Tk()
window.title('Currency Converter')
window.configure(background='black')
pic1=PhotoImage(file='pic.png')

Label(window,image=pic1,bg='black').grid(row=0)
Label(window,text='Currency Code from',bg='black',fg='yellow',
	font='none 12 bold').grid(row=1)

a=Entry(window,width=20,bg='white')
a.grid(row=2)

Label(window,text='To',bg='black',fg='yellow',
	font='none 12 bold').grid(row=3)

b=Entry(window,width=20,bg='white')
b.grid(row=4)

Button(window,text='Check',width=6,command=click).grid(row=5)

output=Text(window,width=50,height=3,fg='yellow',bg='black')
output.grid(row=6,columnspan=1)

Button(window,text='Exit',width=6,command=close_window).grid(row=7)

window.mainloop()