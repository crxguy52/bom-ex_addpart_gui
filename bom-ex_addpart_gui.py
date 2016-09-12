# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:32:33 2016

@author: Victor
"""

import sys
import subprocess
if sys.version_info[0] < 3:
    #If we're executing with Python 2
    import Tkinter as tk
    import tkMessageBox as messagebox
    import ttk
    import tkFileDialog as filedialog
    import tkColorChooser as colorchooser
else:
    #Otherwise we're using Python 3
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import colorchooser


def add2db():
    part = partnum.get()
    part = part.strip()

    if part != '':
        print part
        sys.argv = [part]
        #subprocess.call(['python addDKPartToBom-ex.py', part])
        subprocess.call([sys.executable, 'addDKPartToBom-ex.py', part])
        #execfile('addDKPartToBom-ex.py')
    
root = tk.Tk()
root.title('bom-ex part add util')
root.resizable(width=False, height=False)
partnum = tk.StringVar(value='')

ttk.Label(root, text='Digikey Part Number').grid(row=1,column=1,padx=2,pady=2)
ttk.Entry(root, textvariable=partnum).grid(row=1,column=2,padx=2,pady=2)
ttk.Button(root, text='Add Part to partsdb', command=add2db).grid(row=2,column=1,columnspan=2,sticky='nsew')

#GObut = ttk.Button(root, text='Go!', command=self.goButton)
#GObut.grid(row=6, column = 0, sticky = 'we')


root.mainloop()