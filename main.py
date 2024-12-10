from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow 
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        #variables
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()




        #Product Categories
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
        #SubCatClothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spykar=8000

        self.T_shirt=['Polo','Roadster','Jack&Jones']
        self.price_polo=1500 
        self.price_Roadster=1800 
        self.price_JackJones=1700 

        self.Shirt=['Peter England','Louis Phillipe','Park Avenue']
        self.price_Peter=2100 
        self.price_Louis=2700
        self.price_Park=1740 



        #SubcatLifeStyle
        self.SubCatLifeStyle=["Bath Soap","Face Creame","Hair Oil"]
        self.Bath_soap=['LifeBuy','Lux','Santoor','Pearl']
        self.price_life=20
        self.price_lux=20
        self.price_santoor=20
        self.price_pearl=30

        self.Face_creame=['Fair&Lovely','Ponds','Olay','Garnier']
        self.price_fair=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=30

        self.Hair_oil=['Parachute','Jashmin','Bajaj']
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30
        #SubCatMobiles
        self.SubCatMobiles=["Iphone","Samsung","Xiome","Realme","One+"]
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']
        self.price_ix=40000
        self.price_il1=60000
        self.price_il2=85000

        self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.Xiome=['Red11','Redme-12','RedmePro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.Realme=['Realme 12','Realme 13','Realme Pro']
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.OnePlus=['OnePlus 1','OnePlus 2','OnePlus 3']
        self.price_one1=45000
        self.price_one2=60000
        self.price_one3=45800

        


        

        #image1
        img=Image.open("image/OIP.jpg")
        img=img.resize((500,130),Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)

        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)
        #image2
        img_1=Image.open("image/download (1).jpg")
        img_1=img_1.resize((500,130),Image.BILINEAR)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lb1_img_1=Label(self.root,image=self.photoimg_1)
        lb1_img_1.place(x=500,y=0,width=500,height=130)
        #image3 
        img_2=Image.open("image/OIP (1).jpg")
        img_2=img_2.resize((520,130),Image.BILINEAR)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lb1_img_2=Label(self.root,image=self.photoimg_2)
        lb1_img_2.place(x=900,y=0,width=500,height=130)
        lb1_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lb1_title.place(x=0,y=130,width=1300,height=45)

        def time():
             string=strftime('%H:%M:%S %p')
             lb1.config(text=string)
             lb1.after(1000,time)

        lb1=Label(lb1_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        lb1.place(x=0,y=0,width=175,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1300,height=620)

        #Customer LabelFrame 
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lb1_mob=Label(Cust_Frame,text="Mobile No",font=("times new roman",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lb1CustName=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lb1CustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lb1Email=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",bd=4)
        self.lb1Email.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        #Product LabelFrame 
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        #category
        self.lb1Category=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories",bd=4)
        
        self.lb1Category.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #subcategory
        self.lb1SubCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="SubCategory",bd=4)
        self.lb1SubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product Name
        self.lb1product=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lb1product.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lb1Price=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
        self.lb1Price.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,font=("arial",10,"bold"),width=24,state="readonly",textvariable=self.prices)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #qty
        self.lb1Qty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
        self.lb1Qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Middle Frame 
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)
        #image1
        img12=Image.open("image/good.jpg")
        img12=img12.resize((490,340),Image.BILINEAR)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lb1_img12=Label(MiddleFrame,image=self.photoimg12)
        lb1_img12.place(x=0,y=0,width=490,height=340)
        #image2
        
        img_13=Image.open("image/download.jpg")
        img_13=img_13.resize((470,340),Image.BILINEAR)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lb1_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lb1_img_13.place(x=490,y=0,width=490,height=340)

        #search 
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=990,y=1,width=400,height=40)
        self.lb1Bill=Label(Search_Frame,font=("arial",7,"bold"),bg="red",fg="white",text="Bill Number")
        self.lb1Bill.grid(row=0,column=0,sticky=W,padx=1)
        self.Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',8,'bold'),width=24)
        self.Entry_Search.grid(row=0,column=1,sticky=W,padx=2)
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=5,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)





        #RightFrame Bill Aria
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=250,height=300)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",8,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=335,width=1520,height=125)
        self.lb1SubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lb1SubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('arial',10,'bold'),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lb1_tax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Gov Tax",bd=4)
        self.lb1_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arial',10,'bold'),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lb1AmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
        self.lb1AmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',10,'bold'),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frame 
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add to Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)

        self.welcome()
        self.l=[]
         #Function Declaretion
    def welcome(self):
         self.textarea.delete(1.0,END)
         self.textarea.insert(END,"\t Welcome to Mini Mall")
         self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
         self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
         self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
         self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")
         self.textarea.insert(END,"\n=====================================")
         self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
         self.textarea.insert(END,"\n=====================================\n")
           

    
    def AddItem(self):
         Tax=1
         self.n=self.prices.get()
         self.m=self.qty.get()*self.n
         self.l.append(self.m)
         if self.product.get()=="":
              messagebox.showerror("Error","Please Select the Product Name")
         else:
              self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
              self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
              self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
              self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
         if self.product.get()=="":
              messagebox.showerror("Error","Please Add To Cart Product")
         else:
              text=self.textarea.get(10.0,(10.0+float(len(self.l))))
              self.welcome()
              self.textarea.insert(END,text)
              self.textarea.insert(END,"\n=====================================")
              self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
              self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
              self.textarea.insert(END,f"\n Total amount:\t\t\t{self.total.get()}")
              self.textarea.insert(END,"\n=====================================")

    def save_bill(self):
         op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
         if op>0:
              self.bill_data=self.textarea.get(1.0,END)
              f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
              f1.write(self.bill_data)
              op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()}saved successfully")
              f1.close()
    def iprint(self):
         q=self.textarea.get(1.0,"end-1c")
         filename=tempfile.mktemp('.txt')
         open(filename,'w').write(q)
         os.startfile(filename,"print")
    def find_bill(self):
         found="no"
         for i in os.listdir("bills/"):
              if i.split('.')[0]==self.search_bill.get():
               f1=open(f'bills/{i}','r')
               self.textarea.delete(1.0,END)
               for d in f1:
                    self.textarea.insert(END,d)
               f1.close()
               found="yes"
         if found=="no":
               messagebox.showerror("Error","Invalid BillNumber")
          
    def clear(self):
         self.textarea.delete(1.0,END)
         self.c_name.set("")
         self.c_phon.set("")
         self.c_email.set("")
         x=random.randint(1000,9000)
         self.bill_no.set(str(x))
         self.search_bill.set("")
         self.product.set("")
         self.prices.set(0)
         self.qty.set(0)
         self.l=[0]
         self.total.set("")
         self.sub_total.set("")
         self.tax_input.set('')
         self.welcome()

               
              
         
             
         
         
         




    

         

         


    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
            if self.ComboSubCategory.get()=="Pant":
                 self.ComboProduct.config(value=self.pant)
                 self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="T-Shirt":
                 self.ComboProduct.config(value=self.T_shirt)
                 self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Shirt":
                 self.ComboProduct.config(value=self.Shirt)
                 self.ComboProduct.current(0)

            #LifeStyle 
            if self.ComboSubCategory.get()=="Bath Soap":
                 self.ComboProduct.config(value=self.Bath_soap)
                 self.ComboProduct.current(0)
            
            if self.ComboSubCategory.get()=="Face Creame":
                 self.ComboProduct.config(value=self.Face_creame)
                 self.ComboProduct.current(0)
            
            if self.ComboSubCategory.get()=="Hair Oil":
                 self.ComboProduct.config(value=self.Hair_oil)
                 self.ComboProduct.current(0)

            #Mobile 
            if self.ComboSubCategory.get()=="Iphone":
                 self.ComboProduct.config(value=self.Iphone)
                 self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Samsung":
                 self.ComboProduct.config(value=self.Samsung)
                 self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Xiome":
                 self.ComboProduct.config(value=self.Xiome)
                 self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Realme":
                 self.ComboProduct.config(value=self.Realme)
                 self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="One+":
                 self.ComboProduct.config(value=self.OnePlus)
                 self.ComboProduct.current(0)
    def price(self,event=""):
         #Pant
         if self.ComboProduct.get()=="Levis":
              self.ComboPrice.config(value=self.price_levis)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Mufti":
              self.ComboPrice.config(value=self.price_mufti)
              self.ComboPrice.current(0)
              self.qty.set(1)
        
         if self.ComboProduct.get()=="Spykar":
              self.ComboPrice.config(value=self.price_spykar)
              self.ComboPrice.current(0)
              self.qty.set(1)

            #T-shirt 
         if self.ComboProduct.get()=="Polo":
              self.ComboPrice.config(value=self.price_polo)
              self.ComboPrice.current(0)
              self.qty.set(1)
                 
         if self.ComboProduct.get()=="Roadster":
              self.ComboPrice.config(value=self.price_Roadster)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Jack&Jones":
              self.ComboPrice.config(value=self.price_JackJones)
              self.ComboPrice.current(0)
              self.qty.set(1)

            #shirt 
         if self.ComboProduct.get()=="Peter England":
              self.ComboPrice.config(value=self.price_Peter)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Louis Phillipe":
              self.ComboPrice.config(value=self.price_Louis)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Park Avenue":
              self.ComboPrice.config(value=self.price_Park)
              self.ComboPrice.current(0)
              self.qty.set(1)

            #Bath soap
         if self.ComboProduct.get()=="LifeBuy":
              self.ComboPrice.config(value=self.price_life)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Lux":
              self.ComboPrice.config(value=self.price_lux)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Santoor":
              self.ComboPrice.config(value=self.price_santoor)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Pearl":
              self.ComboPrice.config(value=self.price_pearl)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Fair&Lovely":
              self.ComboPrice.config(value=self.price_fair)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Ponds":
              self.ComboPrice.config(value=self.price_ponds)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Olay":
              self.ComboPrice.config(value=self.price_olay)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Garnier":
              self.ComboPrice.config(value=self.price_garnier)
              self.ComboPrice.current(0)
              self.qty.set(1)
        
         if self.ComboProduct.get()=="Parachute":
              self.ComboPrice.config(value=self.price_para)
              self.ComboPrice.current(0)
              self.qty.set(1)
            
         if self.ComboProduct.get()=="Jashmin":
              self.ComboPrice.config(value=self.price_jashmin)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Bajaj":
              self.ComboPrice.config(value=self.price_bajaj)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Iphone_X":
              self.ComboPrice.config(value=self.price_ix)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Iphone_11":
              self.ComboPrice.config(value=self.price_il1)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Iphone_12":
              self.ComboPrice.config(value=self.price_il2)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Samsung M16":
              self.ComboPrice.config(value=self.price_sm16)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Samsung M12":
              self.ComboPrice.config(value=self.price_sm12)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Samsung M21":
              self.ComboPrice.config(value=self.price_sm21)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Red11":
              self.ComboPrice.config(value=self.price_r11)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Redme-12":
              self.ComboPrice.config(value=self.price_r12)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="RedmePro":
              self.ComboPrice.config(value=self.price_rpro)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Realme 12":
              self.ComboPrice.config(value=self.price_rel12)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Realme 13":
              self.ComboPrice.config(value=self.price_rel13)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="Realme Pro":
              self.ComboPrice.config(value=self.price_relpro)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="OnePlus 1":
              self.ComboPrice.config(value=self.price_one1)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="OnePlus 2":
              self.ComboPrice.config(value=self.price_one2)
              self.ComboPrice.current(0)
              self.qty.set(1)
         if self.ComboProduct.get()=="OnePlus 3":
              self.ComboPrice.config(value=self.price_one3)
              self.ComboPrice.current(0)
              self.qty.set(1)










 


        












if  __name__== '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
