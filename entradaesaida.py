from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk


#FORMULARIO PRINCIPAL
root = Tk()

#TITULO DO SISTEMA
root.title("ESTRELA LIMAS")

#TAMANHO DO FORMULARIO
width = 1000
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable (0, 0)
root.config(bg="Purple")

#VAR CADASTRO PRODUTOS
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()


#CRIANDO CONEXAO COM BD SQLITE3
def Database():
    global conn, cursor
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES ('admin', 'admin')")
        conn.commit()
          
#CRIANDO O METEDO DO BOTAO SAIR
def Exit():
    result=tkMessageBox.askquestion('ESTRELA LIMAS','SAIR', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

        
#FORM LOGIN
def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("SISTEMA DE LOGIN")
    width=700
    height=370
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

#FORMULARIO DE LOGIN
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=50, height=50, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=2)
    lbl_text = Label (TopLoginForm, text="SEJA BEM VINDO", fg="black", font=('arial', 10, 'bold'), width=100)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)

    lbl_username = Label(MidLoginForm, text="USUARIO:", font=('arial', 15, 'bold'), fg="black", bd=18)
    lbl_username.grid(row=0)

    lbl_password = Label(MidLoginForm, text="SENHA:", font=('arial', 15, 'bold'),fg="black", bd=18)
    lbl_password.grid(row=1)

    lbl_result = Label(MidLoginForm,text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)

    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 15), width=30)
    username.grid(row=0, column=1)

    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 15), width=30, show="*")
    password.grid(row=1, column=1)

    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

#FORM DE PROD E HOME PRINCIPAL
def Home():
    global Home
    Home= Tk()
    Home.title("CADASTRO DE PRODUTOS")
    width=1024
    height=500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)

    lbl_display= Label(Title, text="CADASTRO DE PRODUTOS",bg=('SlateGray1'), font=('arial',45))
    lbl_display.pack()


    menubar= Menu(Home)
    filemenu=Menu(menubar, tearoff=0)
    filemenu2=Menu(menubar, tearoff=0)                    
    filemenu.add_command(label="LOGOUT", command=Logout)
    filemenu.add_command(label="SAIR", command=Exit)
    filemenu2.add_command(label="NOVO CADASTRO", command=ShowAddNew)
    filemenu2.add_command(label="VISUALIZAR", command=ShowView)
    filemenu2.add_command(label="BAIXA DE ESTOQUE", command=ShowViewe)
    menubar.add_cascade(label="CONTA", menu=filemenu)
    menubar.add_cascade(label="CADASTROS", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="purple")

#CRIANDO OS PRODUTOS
def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("ADICIONAR PRODUTOS")
    width=600
    height=400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

#METODO DO NOVO CADASTRO DE PRODUTOS
def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="CADASTRAR NOVO PRODUTO", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="PRODUTO:", font=('arial', 15), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNew, text="QUANTIDADE:", font=('arial', 15), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    lbl_price = Label(MidAddNew, text="PRECO:", font=('arial', 15), bd=10)
    lbl_price.grid(row=2, sticky=W)
    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial',25), width=15)
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial',25), width=15)
    productqty.grid(row=1, column=1)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial',25), width=15)
    productprice.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="SALVAR", font=('arial', 18), width=30, bg="gray63", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=50)

def AddNewForme():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="DAR BAIXA EM SEU PRODUTO", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)

#CRIANDO A CONEXAO DO NOVO DASTARDO DO BANDO DE DADOS

def AddNew():
    Database()
    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    cursor.close()
    conn.close()

#CAMPO DE FORMULARIO DE CADASTRO DE PRODUTOS
def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Produtos", font=('arial', 18), width= 600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Pesquisar", font=('arial',15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial',15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Pesquisar", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Atualizar", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Deletar", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Produto ID", "Nome Produto", "Qtidade", "Preco"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Produto ID', text="Produto ID",anchor=W)
    tree.heading('Nome Produto', text="Nome Produto",anchor=W)
    tree.heading('Qtidade', text="Qtidade",anchor=W)
    tree.heading('Preco', text="Preco",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def ViewForme():
    global tree
    TopViewForm = Frame(viewforme, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewforme, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewforme, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="BAIXA EM PRODUTOS", font=('arial', 18), width= 600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="QUANTIDADE VENDIDA", font=('arial',15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial',15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_baixa = Button(LeftViewForm, text="Dar Baixa", command="")
    btn_baixa.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Produto ID", "Nome Produto", "Qtidade", "Preco"), selectmode="extended", height=120, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Produto ID', text="Produto ID",anchor=W)
    tree.heading('Nome Produto', text="Nome Produto",anchor=W)
    tree.heading('Qtidade', text="Qtidade",anchor=W)
    tree.heading('Preco', text="Preco",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

    #METODO PARA ATUALIZAR CADASTROS
def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
      

#METODO DE ATUARLIZAR CADASTRO DE PRODUTOS
def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('','end', values=(data))
        cursor.close()
        conn.close()

#METODO PARA DELETAR
def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('CADASTRO DE PRODUTOS', 'TEM CERTEZA QUE DESEJA DELETAR O PRODUTO?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents ['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close


#DEFININDO O TAMNO DO FORMULARIO
def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("CADASTRO DE PRODUTOS/VISUALIZAR PRODUTOS")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable (0, 0)
    ViewForm()

def ShowViewe():
    global viewforme
    viewforme = Toplevel()
    viewforme.title("BAIXA DE PRODUTOS")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewforme.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewforme.resizable (0, 0)
    ViewForme() 
    

            
#FORMULARIO SAIR
def Logout():
    result = tkMessageBox.askquestion('CADASTRO DE PRODUTOS', 'TEM CERTEZA? LOGOUT', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()




#FORMULARIO DE LOGIN
def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="FAVOR ENTRAR COM OS CAMPOS VALIDOS, TENTE NOVAMENTE!", fg="red", font=('arial', 10))
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",(USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",(USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="USUARIO OU SENHA INVALIDAS", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()

#MENU DROPDOWN
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="ENTRAR", command=ShowLoginForm)
filemenu.add_command(label="SAIR", command=Exit)
menubar.add_cascade(label="ARQUIVOS", menu=filemenu)
root.configure(menu=menubar)

#BEM VINDO AO SISTEMA
Title= Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#CRIANDO LABEL DE PRODUTOS
lbl_display = Label(Title, text="CONTROLE DE ESTOQUE ESTRELA LIMAS", bg="SlateGray1",font=('arial', 30))
lbl_display.pack()

        
#ROOT END
if __name__ == '__main__':
    root.mainloop()
        

        
