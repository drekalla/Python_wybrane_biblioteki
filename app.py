import tkinter as tk
from tkinter import filedialog
import os


class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Sprawdzarka")

        # Start folderString value (GUI text)
        self.folderString = tk.StringVar()
        self.folderString.set("Nie wybrałeś folderu!")

        # Start resultString value (GUI text)
        self.resultString = tk.StringVar()
        self.resultString.set(0)

        # Start timeString value (GUI text)
        self.timeString = tk.StringVar()
        self.timeString.set(0)

        # Fonts
        self.uiFontNormal = "Verdana 9 normal"
        self.uiFontUnderline = "Verdana 9 underline"

        # Labels
        self.folderLabel = tk.Label(
            window, text="Wybrany folder:", font=self.uiFontUnderline)
        self.folderLabelVariable = tk.Label(
            window, textvariable=self.folderString, font=self.uiFontNormal)

        self.resultLabel = tk.Label(
            window, text="Wynik: ", font=self.uiFontUnderline)
        self.resultLabelVariable = tk.Label(
            window, textvariable=self.resultString, font=self.uiFontNormal)

        self.timeLabel = tk.Label(
            window, text="Czas: ", font=self.uiFontUnderline)
        self.timeLabelVariable = tk.Label(
            window, textvariable=self.timeString, font=self.uiFontNormal)

        # Buttons
        self.refreshListboxButtton = tk.Button(
            window, text="Odśwież liste", font=self.uiFontNormal, height=1, width=30, command=self.refresh_listbox_command)
        self.chooseFolderButtton = tk.Button(
            window, text="Wybierz folder", font=self.uiFontNormal, height=1, width=30, command=self.choose_folder_command)
        self.runFileButtton = tk.Button(window, text="Uruchom wybrany plik", font=self.uiFontNormal,
                                        height=6, width=30, bg="#A9A9A9", command=self.run_app_command)

        # Listbox
        self.javaFilesListbox = tk.Listbox(window, height=15, width=40)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(window)

        # Listbox and Scrollbar configuration
        self.javaFilesListbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.javaFilesListbox.yview)

        # Handle Listbox select
        self.javaFilesListbox.bind("<<ListboxSelect>>", self.get_selected_file)

        # Grid configuration
        self.javaFilesListbox.grid(row=0, column=0, rowspan=4)
        self.refreshListboxButtton.grid(row=4, column=0)
        self.chooseFolderButtton.grid(row=5, column=0)
        self.folderLabel.grid(row=6, column=0)
        self.folderLabelVariable.grid(row=7, column=0)

        self.scrollbar.grid(row=0, column=1, rowspan=4)

        self.resultLabel.grid(row=0, column=2)
        self.resultLabelVariable.grid(row=1, column=2)
        self.timeLabel.grid(row=2, column=2)
        self.timeLabelVariable.grid(row=3, column=2)
        self.runFileButtton.grid(row=4, column=2, rowspan=4)

    def refresh_listbox_command(self):
        allFiles = os.listdir(self.selectedFolder)
        javaFiles = [file for file in allFiles if file[-5:] == ".java"]

        self.javaFilesListbox.delete(0, tk.END)
        for file in javaFiles:
            self.javaFilesListbox.insert(tk.END, file)

    def choose_folder_command(self):
        self.selectedFolder = filedialog.askdirectory()
        self.folderString.set(self.selectedFolder)

        self.refresh_listbox_command()

    def run_app_command(self):
        # ToDo
        # Oprogramować uruchamianie wybranego pliku
        # self.selectedFolder - zawiera ścieżke do wybranego folderu
        # self.selectedFile - zawiera nazwę wybranego pliku

        print("Plik uruchomiony")

    def get_selected_file(self, event):
        try:
            index = self.javaFilesListbox.curselection()[0]
            self.selectedFile = self.javaFilesListbox.get(index)

            print(self.selectedFile)
        except IndexError:
            pass


window = tk.Tk()
Window(window)
window.mainloop()
