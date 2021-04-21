from tkinter import *
import urllib.request, os, sys, time

def download():
    installation.destroy()
    dFiles = Tk()
    dFiles.geometry('400x100')
    dFiles.title('Download ...')
    downloadinformations = StringVar()
    Label(dFiles, textvar = downloadinformations).place(x = 10, y = 10)
    downloadpath = 'c:\\'
    createfolder = 'test123'
    path = os.path.join(downloadpath, createfolder)
    try:
        os.mkdir(path)
    except:
        pass
    urldownload = 'https://serverdownload2021test.web.app/test.txt'
    urllib.request.urlretrieve(urldownload, 'c:\\test123\\test.txt')
    downloadinformations.set('Téléchargement et installation terminée ! \n Un raccourci a été créer ...')
    dFiles.mainloop()
    return

installation = Tk()
installation.geometry('300x200')
installation.title('Installation - Login')

emailvar = StringVar()
passwordvar = StringVar()
informations = StringVar()

def installer():
    email = emailvar.get()
    password = passwordvar.get()
    if email == 'admin':
        if password == 'root':
            time.sleep(1)
            download()
        else:
            informations.set('Password incorrect !')
    else:
        informations.set('email incorrect !')
    return

Label(installation, text = "Email :").place(x = 50,y = 50)
Label(installation, text = "Password :").place(x = 30, y = 90)
email = Entry(installation, textvar = emailvar).place(x = 110, y = 50)
password = Entry(installation, textvar = passwordvar).place(x = 110, y = 90)
Button(installation, text = "Valider", command = installer).place(x = 150, y = 120)
Label(installation, textvar = informations).place(x = 110, y = 140)

installation.mainloop()
