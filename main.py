AdNe = 2

from tkinter import *
from pyperclip import copy, paste

def add(t, c):
	string = t.get()
	copy(string)
	c.config(text = 'Copied', bg='white', fg='black')
	

def paste_(t, p):
	string = paste()
	t.insert(END, string)
	p.config(bg='green')


def add_new(r):
	text_E = Entry(root, background = 'khaki', width=20)
	text_E.grid(row = r, column = 0, stick = 'w', columnspan=3)
	pasteButton = Button(root, text='Paste', command=lambda: paste_(text_E, pasteButton), bg='red')
	pasteButton.grid(row = r, column = 4)
	b_copy = Button(root, text = 'Copy', width = 7, command = lambda: add(text_E, b_copy), fg='white', bg='black')
	b_copy.grid(row = r, column = 5)	
	global AdNe
	AdNe+=1

def main():
	global root, AdNe
	root = Tk()
	root.title('Copy King')

	addNewRow = Button(root, text = 'To Add New Row Click on Me', command = lambda: add_new(AdNe))
	addNewRow.grid(row = 0, column=0, columnspan=5)

	add_new(AdNe)

	root.mainloop()

if __name__ == '__main__':
	main()
