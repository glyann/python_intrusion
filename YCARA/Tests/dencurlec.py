# coding: utf-8
# pip install clipboard
'''
Coded by Glyann
Python3
18-02-2019
Encode and Decode characters two folds in base64 and ROT13'ed.
Need better graphics, a little change of mechanics but it works...
'''

from tkinter import Tk, Label, Button, LEFT, RIGHT, Entry, BOTTOM, messagebox
import base64, codecs, clipboard

class Encoder_Decoder:
    def __init__(self, master):
        self.master = master
        master.title("Encodeur et Décodeur")
        master.geometry("275x75")

        self.label = Label(master, text="Entrez des caractères à encoder ou décoder")
        self.label.grid(row=0,column=0,columnspan=3,padx=20)
        
        self.input = Entry(master,width=40, text="Caractères")
        self.input.grid(row=1,column=0,columnspan=3)

        self.Encoder_button = Button(master, text="Encoder", command=self.encoder)
        self.Encoder_button.grid(row=2,column=0,padx=0)

        self.decoder_button = Button(master, text="Décoder", command=self.decoder)
        self.decoder_button.grid(row=2,column=1,padx=0)
        
        self.quit_button = Button(master, text=" Quitter ", command=self.quitting)
        self.quit_button.grid(row=2,column=2,padx=0)
    
    def encoder(self):
        # Encoding base64/base64/rot13 and return the result
        url = bytes(self.input.get(), 'utf-8')
        first = base64.b64encode(url)
        second = base64.b64encode(first).decode()
        global rot
        rot = codecs.encode(second, 'rot_13')
        messagebox.showinfo("Information","Voilà ! \n\"" + rot + "\"\n C'est copié dans le presse-papier !")
        clipboard.copy(rot)


    def decoder(self):
        # Decoding rot13/base64/base64 and return the result
        first = codecs.decode(self.input.get(), 'rot_13')
        second = base64.b64decode(first)
        global rot
        rot = base64.b64decode(second).decode()
        messagebox.showinfo("Information","Voilà ! \n\"" + rot + "\"\n C'est copié dans le presse-papier !")
        clipboard.copy(rot)

    def quitting(self):
        messagebox.showwarning("Error","Application quittée ! ")
        aw.quit()


aw = Tk()
fen = Encoder_Decoder(aw)
aw.mainloop()
