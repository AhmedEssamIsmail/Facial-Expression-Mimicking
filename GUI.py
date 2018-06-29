import matplotlib.pyplot as plt
import csv
import numpy as np
import math
import tkinter as tk
from tkinter import *

top = tk.Tk()

def MLPTrain():
    print("mlp train")
    no_hiddenNeurons = int(E1_hiddenLayer.get())
    eta = float(E1_learningrate.get())
    epoch = int(E1_epochs.get())
    mse = float(E1_mseThreshold.get())
    return 
def RBFTrain():
    print ("RBF Train")
    R_no_hiddenNeurons = int(RE1_hiddenNeurons.get())
    R_eta = float(RE1_learningrate.get())
    R_epoch = int(RE1_epoch.get())
    R_mse = float(RE1_msethreshold.get())

top.geometry('800x400')


def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

######################################## MLP #################################

var = IntVar()


L = Label(top, text="MLP" , font = ("Courier", 14) )
L.pack( side = TOP  )
L.place(x=5,y=5)


L1 = Label(top, text="neurons in hidden layers")
L1.pack( side = TOP)

E1_hiddenLayer = Entry(top, bd =5)
E1_hiddenLayer.pack(side = TOP)
L1.place(x=5,y=25)
E1_hiddenLayer.place(x=150 , y=25)

L2 = Label(top, text="learning rate")
L2.pack( side = TOP)

E1_learningrate = Entry(top, bd =5)
E1_learningrate.pack(side = TOP)
L2.place(x=5,y=70)
E1_learningrate.place(x=150 , y=70)

L3 = Label(top, text="number of epochs")
L3.pack( side = TOP)
E1_epochs = Entry(top, bd =5)
E1_epochs.pack(side = TOP)
L3.place(x=5,y=120)
E1_epochs.place(x=150 , y=120)

ac = Label(top, text="activation function")
ac.pack( side = TOP)
ac.place(x = 5 , y = 170)

R_sigmoid = IntVar()
R_tanh = IntVar()
C1 = Checkbutton(top, text = "sigmoid", variable = R_sigmoid).place(x = 150 , y = 170)
C2 = Checkbutton(top, text = "tanh", variable = R_tanh).place(x = 250 , y=170)



L4 = Label(top, text="stopping criteria")
L4.pack( side = TOP)
L4.place(x=5,y=200)


R_fixEpoch = IntVar()
R_mse = IntVar()
R_validationError = IntVar()
C3 = Checkbutton(top, text = "number of epoch", variable = R_fixEpoch).place(x = 150 , y = 200)
C4 = Checkbutton(top, text = "mse threshold", variable = R_mse).place(x = 290 , y=200)
C6 = Checkbutton(top, text = "validation error", variable = R_validationError).place(x = 150 , y=220)



L5 = Label(top, text="mse threshold")
L5.pack( side = TOP)

E1_mseThreshold = Entry(top, bd =5)
E1_mseThreshold.pack(side = TOP)
L5.place(x=5,y=250)
E1_mseThreshold.place(x=150 , y=250)

R_bais = IntVar()
C5 = Checkbutton(top, text = "bais", variable = R_bais).place(x= 160 ,y= 300)

MLPbutton = Button(top, text ="MLP Train",width = 15 , command = MLPTrain).place(x = 150 , y=350)
label = Label(top)
label.pack()

######################################## RBF #################################
RL = Label(top, text="RBF" ,font = ("Courier", 14))
RL.pack( side = TOP)
RL.place(x=500,y=5)

RL1 = Label(top, text="Number of hidden neurons")
RL1.pack( side = TOP)

RE1_hiddenNeurons = Entry(top, bd =5)
RE1_hiddenNeurons.pack(side = TOP)
RL1.place(x=500,y=25)
RE1_hiddenNeurons.place(x=650 , y=25)


RL2 = Label(top, text="MSE threshold")
RL2.pack( side = TOP)

RE1_msethreshold = Entry(top, bd =5)
RE1_msethreshold.pack(side = TOP)
RL2.place(x=500,y=70)
RE1_msethreshold.place(x=650 , y=70)

RL2 = Label(top, text="MSE threshold")
RL2.pack( side = TOP)

RE1_msethreshold = Entry(top, bd =5)
RE1_msethreshold.pack(side = TOP)
RL2.place(x=500,y=70)
RE1_msethreshold.place(x=650 , y=70)

RL3 = Label(top, text="Learning rate")
RL3.pack( side = TOP)

RE1_learningrate  = Entry(top, bd =5)
RE1_learningrate.pack(side = TOP)
RL3.place(x=500,y=120)
RE1_learningrate.place(x=650 , y=120)


RL4 = Label(top, text="number of epoch")
RL4.pack( side = TOP)

RE1_epoch  = Entry(top, bd =5)
RE1_epoch.pack(side = TOP)
RL4.place(x=500,y=170)
RE1_epoch.place(x=650 , y=170)
MLPbutton = Button(top, text ="RBF Train",width = 15 , command = RBFTrain).place(x = 650 , y=350)

top.mainloop()