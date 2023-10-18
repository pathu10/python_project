import qrcode
from tkinter import*

cp=Tk()
cp.title('Pratham Ajeru')
cp.geometry('700x250')
cp.config(bg='#e52165')

def generate():
	img=qrcode.make(msg.get())
	type(img)
	img.save(f'{save_name.get()}.png')
	Label(cp,text='File Saved!',bg='#e52165',fg='black',font=('Arial Black',8)).pack()

def show():
	img=qrcode.make(msg.get())
	type(img)
	img.show()

frame=Frame(cp,bg='#e52165')
frame.pack(expand=True)

#----------------------------Enter the Text Or Url--------------

Label(frame,text='Enter the Text Or Url: ',font=('Arial Black',18),bg='#e52165').grid(row=0,column=0,sticky='w')

msg=Entry(frame)
msg.grid(row=0,column=1)

#----------------------------Enter the file name--------------

Label(frame,text='Enter the file name(Save As): ',font=('Arial Black',18),bg='#e52165').grid(row=0,column=0,sticky='w')

save_name=Entry(frame)
save_name.grid(row=0,column=1)

#----------------------------Buttons To show or save Qrcode--------------

btn=Button(cp,text='Show QR Code',bd='5',command=show,width=15)
btn.pack()
btn=Button(cp,text='Save QR Code',command=generate,bd='5',width=15)
btn.pack()

cp.mainloop()


