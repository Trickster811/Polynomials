###############################################################
###	    Ngaoundere, Feb, 9 2022 | Nedaouka Joachim	        ###
###	    Project talking about Operations on Polynomials		  ###
###	    ............ **************** ............	        ###
###	                 ****************             	        ###
###	    Here is the project's interface already 	          ###
###		            connected with the functions		          ###
###		...... Started on Feb, 9 2022 at 05:41 am ......	    ###
###		.... Last Modified on Mar, 07 2022 at 04:40 pm ....	  ###
###		...... Ended on Mar, 7 2022 at 05:41 pm ......		    ###
###############################################################


from textwrap import wrap
from tkinter import *
import tkinter.font as font
from function import *

#========================================Camtel:620 09 75 75

class FunnyButton(Button):
  "Bouton de fantaisie : vert virant au rouge quand on l'actionne"
  def __init__(self, boss, **Arguments):
    Button.__init__(self, boss, bg ="dark green", fg ="white", bd =5, activebackground ="red", activeforeground ="yellow", font =('Helvetica', 12, 'bold'), **Arguments)


class RoundedButton(Canvas):
  def __init__(self, parent, border_radius,font_size, width, padding, color, outlinecolor, text='', command=None):
    Canvas.__init__(self, parent, borderwidth=0,
                       relief="flat", highlightthickness=0, bg=parent["bg"])
    self.command = command
    #font_size = 16
    self.font = font.Font(size=font_size, family='space grotesk', weight="bold")
    self.id = None
    height = font_size+(2*padding)
    #width = self.font.measure(text)+(4*padding)
    #width = width if width >= 80 else 80
    width = width

    if border_radius > 0.5*width:
      print("Error: border_radius is greater than width.")
      return None

    if border_radius > 0.5*height:
      print("Error: border_radius is greater than height.")
      return None

    rad = 2*border_radius

    def shape():
      self.create_arc((0, rad, rad, 0), start=90, extent=90, fill=color)
      self.create_arc((width-rad, 0, width, rad), start=0, extent=90, fill=color)
      self.create_arc((width, height-rad, width-rad, height), start=270, extent=90, fill=color)
      self.create_arc((0, height-rad, rad, height), start=180, extent=90, fill=color)
      return self.create_polygon((0, height-border_radius, 0, border_radius, border_radius, 0, width-border_radius, 0, width, border_radius, width, height-border_radius, width-border_radius, height, border_radius, height), fill=color, outline = outlinecolor)

    id = shape()
    (x0, y0, x1, y1) = self.bbox("all")
    width = (x1-x0)
    height = (y1-y0)
    self.configure(width=width, height=height)
    self.create_text(width/2, height/2,text=text, fill='white', font= self.font)
    self.bind("<ButtonPress-1>", self._on_press)
    self.bind("<ButtonRelease-1>", self._on_release)

  def _on_press(self, event):

    """ None -> None """

    self.configure(relief="sunken")
    #color = "#b4bfdf"

  def _on_release(self, event):

    """ None -> None """

    self.configure(relief="raised")
    #color = "#102129"
    if self.command is not None:
      self.command()


class Page():
  def __init__(self):
    """self.master.geometry("900x500+250+100")
    self.master.resizable(width =0, height =0)
    self.master.config(bg ="#b4bfdf")"""

    # Header _start_

    self.frame1 = Frame(bg= '#102129', height= 40, width= 900)
    self.frame1.place(relx= 0, rely= 0)
    self.text = Label(self.frame1,text='Operations On Polynomials', bg= '#102129', fg= 'white', font =('space grotesk', 14, 'bold'))
    self.text.place(relx=0.5, rely=0.1)

    # Header _end_

    # Side bar _start_

    self.frame2 = Frame(bg ="#102129", height= 400, width= 279)
    self.frame2.place(relx= 0, rely= 0)
    self.bou1 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf", font_size= 11, width = 278, padding=8, color="#102129",text= 'Home', command= Start_page)
    self.bou1.place(relx= 0, rely= 0.1)
    self.bou2 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf",font_size= 11, width = 278, padding=8, color="#102129",text= 'Create and Print a polynomial', command= self.Canvas_zone1)
    self.bou2.place(relx= 0, rely= 0.36)
    self.bou3 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf",font_size= 11, width = 278, padding=8, color="#102129",text= 'Sum of polynomials', command= self.Canvas_zone2)
    self.bou3.place(relx= 0, rely= 0.43)
    self.bou4 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf",font_size= 11, width = 278, padding=8, color="#102129",text= 'Substraction of polynomials', command= self.Canvas_zone3)
    self.bou4.place(relx= 0, rely= 0.5)
    self.bou5 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf",font_size= 11, width = 278, padding=8, color="#102129",text= 'Product of polynomials', command= self.Canvas_zone4)
    self.bou5.place(relx= 0, rely= 0.57)
    self.bou6 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf",font_size= 11, width = 278, padding=8, color="#102129",text= 'Operations on Equations', command= self.Canvas_zone5)
    self.bou6.place(relx= 0, rely= 0.64)
    self.bou7 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf",font_size= 11, width = 278, padding=8, color="#102129",text= 'Printf a list of polynomials', command= self.Canvas_zone6)
    self.bou7.place(relx= 0, rely= 0.71)
    self.bou8 = RoundedButton(self.frame2,border_radius=5,outlinecolor ="#b4bfdf",font_size= 11, width = 278, padding=8, color="#102129",text= 'Quit', command= quit)
    self.bou8.place(relx= 0, rely= 0.88)

    # Side bar _end_

    # image

    self.frame = Canvas(bg= '#102129', height= 340, width= 621)
    self.photo = PhotoImage(file ='/home/macnight/Documents/Polynomial_in_python/images/2.png')
    self.frame.create_image(310.5,170, image =self.photo)
    self.frame.place(relx= 0.31, rely= 0.1)

    # image

    # Footer _start_

    self.frame3 = Frame(bg= '#102129', height= 20, width= 900)
    self.frame3.place(relx= 0, rely= 0.94899)
    self.text = Label(self.frame3,text='by_Sof_Up__NJ', bg= '#102129', fg= 'white', font =('cousine', 10))
    self.text.place(relx=0.588, rely=-0.1)

    # Footer _end_

    # Some variables _start_

    self.string0 = StringVar()  # Entry to store entries
    self.string1 = StringVar()  # Entry to store entries

    self.list_poly = [] # list to store polynimials

    self.key = '' # variable to store operation keys

    # Some variables _end_

  def Open_canvas(self, canvas):

    """ None -> None """

    canvas.destroy()
    self.Canvas_zone1() 
  
  def Transform_to_pol(self, string):
    list_deg_coef = []
    for i in string:
      if i != ' ':
        try:
          a = int(i)
          list_deg_coef.append(a)
        except ValueError:
          list_deg_coef.append(i)

    list_deg_coef.append(' ')
    list_deg_coef.insert(0, 'b')
    i = 0
    print(list_deg_coef)
    #j = len(list_deg_coef)

    while list_deg_coef[i] != ' ':   
      if isinstance(list_deg_coef[i], int) and list_deg_coef[i-1] == '-': # Here we're managing positives and negatives reals
        list_deg_coef[i] = list_deg_coef[i] * (-1)
        if list_deg_coef[i-2] == 'b':
          list_deg_coef.pop(i-1)
          i -= 1
        else:
          list_deg_coef[i-1] = '+'
                                                         
      if isinstance(list_deg_coef[i], int) and isinstance(list_deg_coef[i+1], int):       # Here with the while loop we are associate two intergers
        list_deg_coef[i] = int(str(list_deg_coef[i]) + str(list_deg_coef[i+1]))                   # which follows in a list
        list_deg_coef.pop(i+1)
      # elif list_deg_coef[i] == 'x' and list_deg_coef[i-1] == '+':
      #   list_deg_coef.insert(i, 1)
      #   i += 1
      #   if not isinstance(list_deg_coef[i+1], int):
      #     list_deg_coef.insert(i+1, 1)
      #     list_deg_coef.insert(i+1, '^')
          
      #     i += 2
  
      if list_deg_coef[i] == 'x' and (list_deg_coef[i+1] == '+' or list_deg_coef[i+1] == '-' or list_deg_coef[i+1] == ' '):
        if not isinstance(list_deg_coef[i-1], int):
          list_deg_coef.insert(i, 1)
          i += 1
        
        list_deg_coef.insert(i+1, 1)
        list_deg_coef.insert(i+1, '^')
        i += 2
      else:
        if isinstance(list_deg_coef[i], int) and (list_deg_coef[i+1] == '+' or list_deg_coef[i+1] == '-' or list_deg_coef[i+1] == ' '):
          if list_deg_coef[i-1] != '^': 
            list_deg_coef.insert(i+1, 0)
            list_deg_coef.insert(i+1, '^')
            list_deg_coef.insert(i+1, 'x')
            i += 3
      i += 1
    
    i = 0
    while list_deg_coef[i] != ' ':
      if list_deg_coef[i] == 'x':
        list_deg_coef.pop(i)
      else:
        i += 1

    list_deg_coef.pop(0)
        #print(list_deg_coef[i])

    return list_deg_coef

  def Get_Value(self):
    z = self.key
    x = self.string0.get()
    # x = x[1: : ]
    y = self.string1.get()
    # a,i = '',0

    if z == '1':
      poly1 = self.Transform_to_pol(x)
      p1 = Polynomial(Monomial(poly1[0],poly1[2]),Monomial(poly1[4], poly1[6]),Monomial(poly1[8], poly1[10]))
    
      self.Print_zone.configure(text = "" + str(p1.print_polynomial()))
      print(poly1)

    elif z == '5':
      poly1 = self.Transform_to_pol(x)
      p1 = Polynomial(Monomial(poly1[0],poly1[2]),Monomial(poly1[4], poly1[6]),Monomial(poly1[8], poly1[10]))
      self.Print_zone.configure(text = "" + str(p1.factorize_polynomial()))
      p1.factorize_polynomial()

    else:
      poly1 = self.Transform_to_pol(x)
      p1 = Polynomial(Monomial(poly1[0],poly1[2]),Monomial(poly1[4], poly1[6]),Monomial(poly1[8], poly1[10]))

      poly2 = self.Transform_to_pol(y)
      p2 = Polynomial(Monomial(poly2[0],poly2[2]),Monomial(poly2[4], poly2[6]),Monomial(poly2[8], poly2[10]))

      if z == '2':
        p3 = p1.sum_polynomials(p2)
      elif z == '3':
        p3 = p1.substract_polynomials(p2)
      elif z == '4':
        p3 = p1.multiply_monomials(p2)
      elif z == '6':
        return 0

      self.Print_zone.configure(text = "" + str(p3.print_polynomial()))
      print(p3)
    

    # while list_deg_coef[i] != ' ':
    #   if list_deg_coef[i] == '+' and list_deg_coef[i+1] < 0:
    #     i += 1
    #   a += str(list_deg_coef[i])
    #   i += 1

  def Canvas_zone1(self):

    """ None -> None """

    self.key = '1'
    self.can0 = Canvas(bg= '#b4bfdf', height= 340, width= 621)
    self.can0.place(relx= 0.31, rely= 0.1)
    self.text1 = Label(self.can0,text='Create and Print a Polynomial', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 14, 'bold'))
    self.text1.place(relx=0.25, rely=0.05)
    self.entry1 = Entry(self.can0, textvariable=self.string0, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    #self.entry1.bind("<Return>", evaluate_char)
    self.entry1.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.23)
    self.bou0 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Create', command=self.Get_Value)
    self.bou0.place(relx= 0.55, rely= 0.245)
    self.bou1 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Save')
    self.bou1.place(relx= 0.75, rely= 0.245)

    # image

    self.text2 = Label(self.can0,text='Print_zone Result', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 11))
    self.text2.place(relx=0.40, rely=0.38)
    self.zone = Canvas(bg= '#102129', height= 189, width= 620)
    self.photo = PhotoImage(file ='/home/macnight/Documents/Polynomial_in_python/images/3.png')
    self.zone.create_image(310,94.5, image =self.photo)
    self.zone.place(relx= 0.31, rely= 0.478)
    self.Print_zone = Label(self.zone, height= 9, width= 31)
    self.Print_zone.place(relx= 0.314, rely= 0.08)
    
    # image

  def Canvas_zone2(self):

    """ None -> None """

    self.key = '2'
    self.can0 = Canvas(bg= '#b4bfdf', height= 340, width= 621)
    self.can0.place(relx= 0.31, rely= 0.1)
    self.text1 = Label(self.can0,text='Sum of Polynomials', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 13, 'bold'))
    self.text1.place(relx=0.35, rely=0.002)
    self.text2 = Label(self.can0,text='Polynomial_1', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 8, 'bold'))
    self.text2.place(relx=0.10, rely=0.10)
    self.entry1 = Entry(self.can0, borderwidth= 0, textvariable=self.string0, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    self.entry1.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.13)
    self.text3 = Label(self.can0,text='Polynomial_2', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 8, 'bold'))
    self.text3.place(relx=0.10, rely=0.23)
    self.entry2 = Entry(self.can0, borderwidth= 0, textvariable=self.string1, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    self.entry2.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.29)
    self.bou0 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Sum', command=self.Get_Value)
    self.bou0.place(relx= 0.55, rely= 0.29)
    self.bou1 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Save')
    self.bou1.place(relx= 0.75, rely= 0.29)

    # image

    self.text2 = Label(self.can0,text='Print_zone Result', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 11))
    self.text2.place(relx=0.40, rely=0.38)
    self.zone = Canvas(bg= '#102129', height= 189, width= 620)
    self.photo = PhotoImage(file ='/home/macnight/Documents/Polynomial_in_python/images/3.png')
    self.zone.create_image(310,94.5, image =self.photo)
    self.zone.place(relx= 0.31, rely= 0.478)
    self.Print_zone = Label(self.zone, height= 9, width= 31)
    self.Print_zone.place(relx= 0.314, rely= 0.08)
    
    # image

  def Canvas_zone3(self):

    """ None -> None """

    self.key = '3'
    self.can0 = Canvas(bg= '#b4bfdf', height= 340, width= 621)
    self.can0.place(relx= 0.31, rely= 0.1)
    self.text1 = Label(self.can0,text='Substraction of Polynomials', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 14, 'bold'))
    self.text1.place(relx=0.35, rely=0.03)
    self.text2 = Label(self.can0,text='Polynomial_1', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 8, 'bold'))
    self.text2.place(relx=0.10, rely=0.12)
    self.entry1 = Entry(self.can0, borderwidth= 0, textvariable=self.string0, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    self.entry1.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.17)
    self.text3 = Label(self.can0,text='Polynomial_2', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 8, 'bold'))
    self.text3.place(relx=0.10, rely=0.27)
    self.entry2 = Entry(self.can0, borderwidth= 0, textvariable=self.string1, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    self.entry2.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.32)
    self.bou0 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Substract', command=self.Get_Value)
    self.bou0.place(relx= 0.55, rely= 0.35)
    self.bou1 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Save')
    self.bou1.place(relx= 0.75, rely= 0.35)

    # image

    self.text2 = Label(self.can0,text='Print_zone Result', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 11))
    self.text2.place(relx=0.40, rely=0.38)
    self.zone = Canvas(bg= '#102129', height= 189, width= 620)
    self.photo = PhotoImage(file ='/home/macnight/Documents/Polynomial_in_python/images/3.png')
    self.zone.create_image(310,94.5, image =self.photo)
    self.zone.place(relx= 0.31, rely= 0.478)
    self.Print_zone = Label(self.zone, height= 9, width= 31)
    self.Print_zone.place(relx= 0.314, rely= 0.08)
    
    # image

  def Canvas_zone4(self):

    """ None -> None """

    self.key = '4'
    self.can0 = Canvas(bg= '#b4bfdf', height= 340, width= 621)
    self.can0.place(relx= 0.31, rely= 0.1)
    self.text1 = Label(self.can0,text='Product of Polynomials', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 14, 'bold'))
    self.text1.place(relx=0.35, rely=0.03)
    self.text2 = Label(self.can0,text='Polynomial_1', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 8, 'bold'))
    self.text2.place(relx=0.10, rely=0.12)
    self.entry1 = Entry(self.can0, borderwidth= 0, textvariable=self.string0, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    self.entry1.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.17)
    self.text3 = Label(self.can0,text='Polynomial_2', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 8, 'bold'))
    self.text3.place(relx=0.10, rely=0.27)
    self.entry2 = Entry(self.can0, borderwidth= 0, textvariable=self.string1, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    self.entry2.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.32)
    self.bou0 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Multiply', command=self.Get_Value)
    self.bou0.place(relx= 0.55, rely= 0.35)
    self.bou1 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Save')
    self.bou1.place(relx= 0.75, rely= 0.35)

    # image

    self.text2 = Label(self.can0,text='Print_zone Result', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 11))
    self.text2.place(relx=0.40, rely=0.38)
    self.zone = Canvas(bg= '#102129', height= 189, width= 620)
    self.photo = PhotoImage(file ='/home/macnight/Documents/Polynomial_in_python/images/3.png')
    self.zone.create_image(310,94.5, image =self.photo)
    self.zone.place(relx= 0.31, rely= 0.478)
    self.Print_zone = Label(self.zone, height= 9, width= 31)
    self.Print_zone.place(relx= 0.314, rely= 0.08)
    
    # image

  def Canvas_zone5(self):

    """ None -> None """

    self.key = '5'
    self.can0 = Canvas(bg= '#b4bfdf', height= 340, width= 621)
    self.can0.place(relx= 0.31, rely= 0.1)
    self.text1 = Label(self.can0,text='Operations with Equations', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 14, 'bold'))
    self.text1.place(relx=0.25, rely=0.05)
    self.entry1 = Entry(self.can0, textvariable=self.string0, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    #self.entry1.bind("<Return>", evaluate_char)
    self.entry1.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.23)
    self.bou0 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Make', command=self.Get_Value)
    self.bou0.place(relx= 0.55, rely= 0.245)
    self.bou1 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 100, padding=8, color="#102129",text= 'Save')
    self.bou1.place(relx= 0.75, rely= 0.245)

    # image

    self.text2 = Label(self.can0,text='Print_zone Result', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 11))
    self.text2.place(relx=0.40, rely=0.38)
    self.zone = Canvas(bg= '#102129', height= 189, width= 620)
    self.photo = PhotoImage(file ='/home/macnight/Documents/Polynomial_in_python/images/3.png')
    self.zone.create_image(310,94.5, image =self.photo)
    self.zone.place(relx= 0.31, rely= 0.478)
    self.Print_zone = Label(self.zone, height= 9, width= 31)
    self.Print_zone.place(relx= 0.314, rely= 0.08)
    
    # image


  def Canvas_zone6(self):

    """ None -> None """

    self.key = '6'
    self.can0 = Canvas(bg= '#b4bfdf', height= 340, width= 621)
    self.can0.place(relx= 0.31, rely= 0.1)
    self.text1 = Label(self.can0,text='Print a list of Polynomials', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 14, 'bold'))
    self.text1.place(relx=0.25, rely=0.05)
    #self.entry = Entry(self.can0, borderwidth= 0, bg= "white", foreground= '#102129', font =('cousine', 18, 'bold'))
    #self.entry.place(relheight= 0.1, relwidth=0.4, relx= 0.10, rely= 0.23)
    #self.text = Label(self.can0,text='Print_zone Result', bg= '#b4bfdf', fg= '#102129', font =('space grotesk', 11))
    #self.text.place(relx=0.40, rely=0.38)
    self.Print_zone = Label(self.can0, height= 15, width= 87, wraplength=10, wrap=WORD)
    self.Print_zone.place(relx= 0.006, rely= 0.15)
    self.bou0 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 150, padding=8, color="#102129",text= 'Add Polynomial(s)')
    self.bou0.place(relx= 0.45, rely= 0.90)
    self.bou1 = RoundedButton(self.can0, border_radius=2.5, outlinecolor ="#b4bfdf", font_size= 11, width = 160, padding=8, color="#102129",text= 'Delete Polynomial(s)')
    self.bou1.place(relx= 0.7, rely= 0.90)


class Start_page():
  def __init__(self):
    """self.master.geometry("900x500+250+100")
    self.master.resizable(width = 0, height = 0)
    self.master.config(bg ="#102129")"""
    self.frame = Canvas(bg= '#102129', height= 400, width= 900)
    self.photo = PhotoImage(file ='/home/macnight/Documents/Polynomial_in_python/images/1.png')
    self.frame.create_image(450,200, image =self.photo)
    self.frame.place(relx= 0, rely= 0)
    self.text = Label(self.frame,text='Operations On Polynomials', bg= '#102129', fg= 'white', font =('space grotesk', 26, 'bold'))
    self.text.place(relx=0.25, rely=0.5)
    start_btn = RoundedButton(self.frame, border_radius=2,outlinecolor ="#b4bfdf", font_size= 16, width = 150, padding=8, color="dark green", text='Start', command = self.change_page)
    #self.bou = Button(self.frame,text='Start', background= "dark green", foreground="white", activebackground ="red", activeforeground ="yellow",font =('space grotesk', 12, 'bold'), command = self.change_page)
    start_btn.place(relx=0.39, rely=0.8)

  def change_page(self):

    """ None -> None """

    for widget in self.frame.winfo_children():
        widget.destroy()
    self.frame.destroy()
    Page()
        
     
if __name__ == '__main__':
    window1 = Tk()
    window1.geometry("900x400+250+100")
    window1.resizable(width= 0, height= 0)
    #window1.config(bg="#102129")
    Start_page()
    window1.mainloop()

