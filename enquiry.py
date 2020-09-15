import tkinter as tk
from tkinter import ttk
import os
import json

recCtr=0;fdataInJson={};listofKeys=[]
dataFr=None
btnFr=None

#-------------------------------------------------------------------------------------------

def show_enq():
	global recCtr,fdataInJson,listofKeys,dataFr,btnFr
	if dataFr:
		dataFr.destroy();dataFr=None
		btnFr.destroy();btnFr=None

	def disp_rec(v):
		l1a = ttk.Label(dataFr, text='Name :')
		l1a.grid(column=0, row=0, sticky=tk.E, padx=5, pady=2)
		l1b = ttk.Label(dataFr, text=v['name'], width=20)
		l1b.grid(column=1, row=0, sticky=tk.E, padx=5, pady=2)

		l2a = ttk.Label(dataFr, text='Phone :')
		l2a.grid(column=0, row=1, sticky=tk.E, padx=5, pady=2)
		l2b = ttk.Label(dataFr, text=v['phone'], width=20)
		l2b.grid(column=1, row=1, sticky=tk.E, padx=5, pady=2)

		l3a = ttk.Label(dataFr, text='E-mail :')
		l3a.grid(column=0, row=2, sticky=tk.E, padx=5, pady=2)
		l3b = ttk.Label(dataFr, text=v['email'], width=20)
		l3b.grid(column=1, row=2, sticky=tk.E, padx=5, pady=2)

		l4a = ttk.Label(dataFr, text='Course :')
		l4a.grid(column=0, row=3, sticky=tk.E, padx=5, pady=2)
		l4b = ttk.Label(dataFr, text=v['course'], width=20)
		l4b.grid(column=1, row=3, sticky=tk.E, padx=5, pady=2)

		l5a = ttk.Label(dataFr, text='Background :')
		l5a.grid(column=0, row=4, sticky=tk.E, padx=5, pady=2)
		l5b = ttk.Label(dataFr, text=v['background'], width=20)
		l5b.grid(column=1, row=4, sticky=tk.E, padx=5, pady=2)

		l6a = ttk.Label(dataFr, text='Demo details :')
		l6a.grid(column=0, row=5, sticky=tk.E, padx=5, pady=2)
		l6b = ttk.Label(dataFr, text=v['demo'], width=20)
		l6b.grid(column=1, row=5, sticky=tk.E, padx=5, pady=2)

		l7a = ttk.Label(dataFr, text='Other details :')
		l7a.grid(column=0, row=6, sticky=tk.E, padx=5, pady=2)
		l7b = ttk.Label(dataFr, text=v['other'], width=20)
		l7b.grid(column=1, row=6, sticky=tk.E, padx=5, pady=2)

	def prevBT():
		global recCtr, fdataInJson
		recCtr -= 1
		disp_rec(fdataInJson[listofKeys[recCtr]])
		if nextBtn['state'] == 'disabled':
			nextBtn.configure(state='active')
		if recCtr == 0:
			prevBtn.configure(state='disabled')

	def nextBT():
		global recCtr, fdataInJson
		recCtr += 1
		disp_rec(fdataInJson[listofKeys[recCtr]])
		if prevBtn['state'] == 'disabled':
			prevBtn.configure(state='active')
		if recCtr == len(fdataInJson)-1:
			nextBtn.configure(state='disabled')

	dataFr = tk.LabelFrame(app)
	dataFr['borderwidth'] = 2
	dataFr['text'] = '........DATA........'
	dataFr.grid(row=0, column=5, ipadx=5, ipady=5, padx=10)

	btnFr = tk.LabelFrame(app)
	btnFr['borderwidth'] = 2
	btnFr.grid(row=6, column=5, ipadx=2)

	prevBtn = tk.Button(btnFr, text="Previous", command=prevBT)
	prevBtn.configure(state='disabled')
	prevBtn.grid(column=0, row=0, padx=2, pady=0)
	nextBtn = tk.Button(btnFr, text="next", command=nextBT)
	nextBtn.grid(column=1, row=0, padx=2, pady=0)

	if os.path.exists('enq.json'):
		with open('enq.json','rt') as f:
			fdataInJson = json.load(f)
		listofKeys = list(fdataInJson.keys())
		disp_rec(fdataInJson[listofKeys[recCtr]])

#------------------------------------------------------------------------------------

def create_enq():
	global recCtr,fdataInJson,listofKeys,dataFr,btnFr
	if dataFr:
		dataFr.destroy();dataFr=None
		btnFr.destroy();btnFr=None

	def saveBT():
		if eqname.get() and eqphone.get() and eqemail.get() and eqcourse.get() and eqbg.get() and eqdemo.get() and eqother.get():
			enq={}.fromkeys(['name','phone','email','course','background','demo','other'])
			enq['name']=eqname.get()
			enq['phone']=eqphone.get()
			enq['email']=eqemail.get()
			enq['course']=eqcourse.get()
			enq['background']=eqbg.get()
			enq['demo']=eqdemo.get()
			enq['other']=eqother.get()

			if os.path.exists('enq.json'):
				f = open('enq.json','r')
				fdata = json.load(f)
				f.close()
				d = dict(fdata)
				newKey = int(max(fdata))+1
				d.setdefault(newKey,enq)
				f = open('enq.json','w')
			else:
				f = open('enq.json','x')
				d = {1:enq}
			json.dump(d, f)
			f.close
			e1.delete(0,tk.END);e2.delete(0,tk.END);e3.delete(0,tk.END);e4.delete(0,tk.END)
			e5.delete(0,tk.END);e6.delete(0,tk.END);e7.delete(0,tk.END)
			e1.focus()
			dataFr['text']='DATA Saved....Enter again'

		else:
			dataFr['text']='Incomplete DATA....Enter again'

	def resetBT():
		e1.delete(0,tk.END);e2.delete(0,tk.END);e3.delete(0,tk.END);e4.delete(0,tk.END)
		e5.delete(0,tk.END);e6.delete(0,tk.END);e7.delete(0,tk.END)
		e1.focus()
		dataFr['text']='Incomplete DATA....Enter again'

	dataFr = tk.LabelFrame(app)
	dataFr['borderwidth'] = 2
	dataFr['text'] = '........DATA........'
	dataFr.grid(row=0, column=5, ipadx=5, ipady=5, padx=10)

	btnFr = tk.LabelFrame(app)
	btnFr['borderwidth'] = 2
	btnFr.grid(row=6, column=5, ipadx=2)

	l1 = ttk.Label(dataFr, text="Full name ")
	l1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=2)
	eqname = tk.StringVar()
	e1 = ttk.Entry(dataFr, width=12, textvariable=eqname)
	e1.grid(column=1, row=0, sticky=tk.E, padx=5, pady=2)
	e1.focus()

	l2 = ttk.Label(dataFr, text="Phone no. ")
	l2.grid(column=0, row=1, sticky=tk.E, padx=5, pady=2)
	eqphone = tk.StringVar()
	e2 = ttk.Entry(dataFr, width=12, textvariable=eqphone)
	e2.grid(column=1, row=1, sticky=tk.E, padx=5, pady=2)

	l3 = ttk.Label(dataFr, text="E-mail ")
	l3.grid(column=0, row=2, sticky=tk.E, padx=5, pady=2)
	eqemail = tk.StringVar()
	e3 = ttk.Entry(dataFr, width=12, textvariable=eqemail)
	e3.grid(column=1, row=2, sticky=tk.E, padx=5, pady=2)

	l4 = ttk.Label(dataFr, text="Course Intrested ")
	l4.grid(column=0, row=3, sticky=tk.E, padx=5, pady=2)
	eqcourse = tk.StringVar()
	e4 = ttk.Entry(dataFr, width=12, textvariable=eqcourse)
	e4.grid(column=1, row=3, sticky=tk.E, padx=5, pady=2)

	l5 = ttk.Label(dataFr, text="Background ")
	l5.grid(column=0, row=4, sticky=tk.E, padx=5, pady=2)
	eqbg = tk.StringVar()
	e5 = ttk.Entry(dataFr, width=12, textvariable=eqbg)
	e5.grid(column=1, row=4, sticky=tk.E, padx=5, pady=2)

	l6 = ttk.Label(dataFr, text="Demo date & timings ")
	l6.grid(column=0, row=5, sticky=tk.E, padx=5, pady=2)
	eqdemo = tk.StringVar()
	e6 = ttk.Entry(dataFr, width=12, textvariable=eqdemo)
	e6.grid(column=1, row=5, sticky=tk.E, padx=5, pady=2)

	l7 = ttk.Label(dataFr, text="other details ")
	l7.grid(column=0, row=6, sticky=tk.E, padx=5, pady=2)
	eqother = tk.StringVar()
	e7 = ttk.Entry(dataFr, width=12, textvariable=eqother)
	e7.grid(column=1, row=6, sticky=tk.E, padx=5, pady=2)


	resetBtn = tk.Button(btnFr, text='RESET', command=resetBT)
	resetBtn.grid(column=1, row=0, padx=2)
	saveBtn = tk.Button(btnFr, text='SAVE', command=saveBT)
	saveBtn.grid(column=2,row=0, padx=2)


#-----------------------------------------------------------------------

app = tk.Tk()

app.title("Enquiry")
app.geometry("500x400")

sel = tk.LabelFrame(app, text='.......MENU.......')
sel['borderwidth'] = 3
sel.grid(row=0, column=0, ipadx=5, ipady=5, padx=20)

createEnquiry = tk.Button(sel, text="Create an Enquiry", command=create_enq)
createEnquiry.grid(column=0, row=0, padx=2, pady=5)

listEnquiry = tk.Button(sel, text="Show all Enquiries", command=show_enq)
listEnquiry.grid(column=0, row=2, padx=2, pady=5)


app.mainloop()