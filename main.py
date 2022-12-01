from tkinter import *
from tkinter import messagebox
from tkinter import ttk
master = Tk()
master.title(&#39;tk&#39;)
master.geometry(&#39;600x800&#39;)
Label(master,font=(&quot;Arial&quot;, 15), text= &#39;Job
Application&#39;).place(x=5+120,y= 0)
Label(master, text= &#39;Personal Information&#39;).place(x=5,y= 5+ 10)
Label(master, text= &#39;Name &#39;).place(x=5+0,y= 25+ 15+10)
Label(master, text=&#39;Email &#39;).place(x=5+0,y= 25+ 15+50)
Label(master, text=&#39;Education &#39;).place(x=5+0,y= 25+ 15+90)
Label(master, text=&#39;Resume &#39;).place(x=5+0,y= 25+ 15+130)
Label(master, text=&#39;Address&#39;).place(x=5+0,y= 25+ 15+170)
Label(master, text=&#39;Phone Number &#39;).place(x=5+0,y= 25+ 15+290)

Label(master, text=&#39;What are your hobbies?&#39;).place(x=5+0,y= 25+
15+310)
Label(master,text=&#39;PREVIOUS/CURRENT EMPLOYMENT
DETAILS&#39;).place(x=5+0,y= 25+ 15+350)
Label(master, text=&#39;Comapany Name &#39;).place(x=5+0,y= 25+ 15+370)
Label(master, text=&#39;Job Title &#39;).place(x=5+0,y= 25+ 15+410)
Label(master, text=&#39;How long were you&#39;).place(x=5+0,y= 25+ 15+430)
Label(master, text=&#39;here? &#39;).place(x=5+0,y= 25+ 15+450)
Label(master, text=&#39;REFERENCE #1&#39;).place(x=5+0,y= 25+ 15+470)
Label(master, text=&#39;Name &#39;).place(x=5+0,y= 25+ 15+490)
Label(master, text=&#39;Phone &#39;).place(x=5+0,y= 25+ 15+530)
Label(master, text=&#39;REFERENCE #2 &#39;).place(x=5+0,y= 25+ 15+550)
Label(master, text=&#39;Name &#39;).place(x=5+0,y= 25+ 15+570)
Label(master, text=&#39;Phone &#39;).place(x=5+0,y= 25+ 15+610)
e1 = Entry(master,width=20).place(x=5+120,y= 25+ 15+10)
e18=Entry(master,width=20).place(x=5+260,y= 25+ 15+10)
e2 = Entry(master,width=40).place(x=5+120,y= 25+ 15+50)
e4 = Entry(master,width=40).place(x=5+120,y= 25+ 15+130)
e5=Entry(master,width=40).place(x=5+120,y= 25+ 15+170)
e6=Entry(master,width=18).place(x=5+120,y= 25+ 15+250)
e19=Entry(master,width=5).place(x=5+240,y= 25+ 15+250)
e20=Entry(master,width=10).place(x=5+280,y= 25+ 15+250)
e8=Entry(master,width=30).place(x=5+160,y= 25+ 15+290)
e21=Entry(master,width=5).place(x=5+120,y= 25+ 15+290)
e9 =Entry(master,width=60).place(x=5+0,y= 25+ 15+330)
e10=Entry(master,width=40).place(x=5+120,y= 25+ 15+370)
e11=Entry(master,width=40).place(x=5+120,y= 25+ 15+410)
e12=Entry(master,width=40).place(x=5+120,y= 25+ 15+450)
e13=Entry(master,width=40).place(x=5+120,y= 25+ 15+490)
e14=Entry(master,width=40).place(x=5+120,y= 25+ 15+530)
e15=Entry(master,width=40).place(x=5+120,y= 25+ 15+570)
e16=Entry(master,width=40).place(x=5+120,y= 25+ 15+410)
e17=Entry(master,width=40).place(x=5+120,y= 25+ 15+610)
n = StringVar()
monthchoosen = ttk.Combobox(master, text=&#39;Please Choose&#39;,width = 35,
textvariable = n)
monthchoosen[&#39;values&#39;] = (&#39; X&#39;,
&#39; XII&#39;,
&#39;BTech&#39;,
&#39; BSc&#39;,
&#39; MBBS&#39;,
&#39; LLB&#39;,
&#39; MSc&#39;,
&#39; MTech&#39;)
monthchoosen.place(x=5+120,y= 25+ 15+90)
monthchoosen.set(&#39;Please Choose&#39;)
p = StringVar()
countrychoosen= ttk.Combobox(master, text=&#39;Please Choose&#39;,width =
35,
textvariable = p)
countrychoosen[&#39;values&#39;] = (&#39; India&#39;,
&#39; USA&#39;,
&#39;Australia&#39;,
&#39; Canada&#39;,
&#39; Denmark&#39;,
&#39; Nepal&#39;,

&#39; Srilanka&#39;,
&#39; Brazil&#39;)
countrychoosen.place(x=5+120,y= 25+ 15+210)
countrychoosen.set(&#39;Select a Country&#39;)
btn = Button(master, text=&#39;Apply&#39;).place(x=5+160,y= 25+ 15+650)
master.mainloop()