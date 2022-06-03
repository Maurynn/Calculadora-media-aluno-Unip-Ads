from tkinter import *

janela = Tk()
janela.title('By: Mauro Alves Developer')
janela.geometry("350x200")
janela.configure(background="#303030",
borderwidth="3",
highlightbackground="orange",
highlightthickness="2",
relief="groove")
janela.resizable(False, False)

#Cálculo Média:
def calcular():
	prova = prova_entry.get()
	pim = pim_entry.get()
	ava = ava_entry.get()
	media = float(prova)*0.7 + float(pim)*0.2 + float(ava)*0.1
    
	if media >= 5.70:
		media = (f'Sua Média é: {media:.2f}\n\nPARABÉNS!')
	else:
		media =(f'Sua Média é: {media:.2f}\n\nATENÇÃO!\nVocê terá que realizar\nEXAME!')
	resultado_label['text']=media

# build ui
label = Label(janela,)
label.configure(
            background="orange",
            borderwidth="3",
            font="{Nirmala UI} 11 {bold}",
            foreground="black")
label.configure(
            justify="center",
            relief="sunken",
            text="CALCULADORA DE MÉDIA - GESTÃO UNIP",
            width="100")
label.pack(padx="5", pady="5", side="top")
prova_label = Label(janela)
prova_label.configure(
            background="#303030",
            font="{Arial Baltic} 11 {bold}",
            foreground="#ffffff",
            text="Nota Prova")
prova_label.pack(anchor="n", padx="5", pady="11", side="left")
prova_entry = Entry(janela)
prova_entry.configure(
            background="#ffffff",
            borderwidth="3",
            font="{Ebrima} 10 {}",
            highlightbackground="black")
prova_entry.configure(
            highlightthickness="1",
            insertborderwidth="0",
            insertwidth="0",
            relief="sunken")
prova_entry.configure(selectborderwidth="0", width="8")
prova_entry.pack(anchor="w", pady="10", side="top")
pim_label = Label(janela)
pim_label.configure(
            background="#303030",
            font="{Arial Baltic} 11 {bold}",
            foreground="#ffffff",
            text="Nota PIM")
pim_label.place(anchor="nw", relx="0.0", rely="0.45", x="5")
pim_entry = Entry(janela)
pim_entry.configure(
            background="#ffffff",
            borderwidth="3",
            font="{Ebrima} 10 {}",
            highlightbackground="black")
pim_entry.configure(highlightthickness="1", width="8")
pim_entry.pack(anchor="w", side="top")
ava_label = Label(janela)
ava_label.configure(
            background="#303030",
            font="{Arial Baltic} 11 {bold}",
            foreground="#ffffff",
            text="Nota AVA")
ava_label.place(anchor="nw", rely="0.64", x="5", y="1")
ava_entry = Entry(janela)
ava_entry.configure(
            background="#ffffff",
            borderwidth="3",
            font="{Ebrima} 10 {}",
            highlightbackground="black")
ava_entry.configure(highlightthickness="1", width="8")
ava_entry.pack(anchor="nw", pady="10", side="top")
calcular = Button(janela, command=calcular)
calcular.configure(
            background="orange",
            borderwidth="3",
            font="{Arial CE} 10 {bold}",
            relief="ridge")
calcular.configure(text="Calcular ")
calcular.place(anchor="nw", height="25", rely="0.83", width="156", x="5", y="1")
resultado_label = Label(janela, text='')
resultado_label.configure(
            background="#ffffff",
            borderwidth="3",
            height="10",
            highlightbackground="orange", 
            font='Arial 10 bold', 
            highlightthickness="1", 
            justify="center", 
            padx="1", 
            pady="1", 
            relief="sunken", 
            width="1")
resultado_label.place(relheight="0.71", relwidth="0.48", relx="0.50", rely="0.08", x="0", y="33")

janela.mainloop()

