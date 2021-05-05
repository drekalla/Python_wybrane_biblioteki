import tkinter as tk
from tkinter import filedialog, messagebox
import os
from testJavaProgram import testJavaProgram


class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Sprawdzarka")

        # Start folderString value (GUI text)
        self.folderString = tk.StringVar()
        self.folderString.set("Nie wybrałeś folderu!")

        # Start jdkString value (GUI text)
        self.jdkString = tk.StringVar()
        self.jdkString.set("Nie wybrałeś JDK!")

        # Start testFileString value (GUI text)
        self.testFileString = tk.StringVar()
        self.testFileString.set("Nie wybrałeś pliku z testami!")

        # Start resultFileString value (GUI text)
        self.resultFileString = tk.StringVar()
        self.resultFileString.set("Nie wybrałeś pliku z wynikami!")

        # Start resultString value (GUI text)
        self.resultString = tk.StringVar()
        self.resultString.set(0)

        # Start timeString value (GUI text)
        self.timeString = tk.StringVar()
        self.timeString.set(0)

        # Start selectedFileString value (GUI text)
        self.selectedFileString = tk.StringVar()
        self.selectedFileString.set("Wybrany plik: Brak")

        # Fonts
        self.uiFontNormal = "Verdana 9 normal"
        self.uiFontUnderline = "Verdana 9 underline"

        # Labels
        self.folderLabel = tk.Label(
            window, text="Wybrany folder:", font=self.uiFontUnderline)
        self.folderLabelVariable = tk.Label(
            window, textvariable=self.folderString, font=self.uiFontNormal, bg="red")

        self.jdkLabel = tk.Label(
            window, text="Wybrane JDK:", font=self.uiFontUnderline)
        self.jdkLabelVariable = tk.Label(
            window, textvariable=self.jdkString, font=self.uiFontNormal, bg="red")

        self.testFileLabel = tk.Label(
            window, text="Wybrany plik z testami:", font=self.uiFontUnderline)
        self.testFileLabelVariable = tk.Label(
            window, textvariable=self.testFileString, font=self.uiFontNormal, bg="red")

        self.resultFileLabel = tk.Label(
            window, text="Wybrany plik z wynikami:", font=self.uiFontUnderline)
        self.resultFileLabelVariable = tk.Label(
            window, textvariable=self.resultFileString, font=self.uiFontNormal, bg="red")

        self.resultLabel = tk.Label(
            window, text="Wynik: ", font=self.uiFontUnderline)
        self.resultLabelVariable = tk.Label(
            window, textvariable=self.resultString, font=self.uiFontNormal)

        self.timeLabel = tk.Label(
            window, text="Czas: ", font=self.uiFontUnderline)
        self.timeLabelVariable = tk.Label(
            window, textvariable=self.timeString, font=self.uiFontNormal)

        self.selectedFileLabelVariable = tk.Label(
            window, textvariable=self.selectedFileString, font=self.uiFontNormal)

        # Buttons
        self.refreshListboxButtton = tk.Button(
            window, text="Odśwież liste", font=self.uiFontNormal, height=1, width=30, command=self.refresh_listbox_command)
        self.chooseFolderButtton = tk.Button(
            window, text="Wybierz folder", font=self.uiFontNormal, height=1, width=30, command=self.choose_folder_command)
        self.chooseJDKButtton = tk.Button(
            window, text="Wybierz JDK", font=self.uiFontNormal, height=1, width=30, command=self.choose_jdk_command)
        self.chooseTestFileButtton = tk.Button(
            window, text="Wybierz plik z testami", font=self.uiFontNormal, height=1, width=30, command=self.choose_test_file_command)
        self.chooseResultFileButtton = tk.Button(
            window, text="Wybierz plik z wynikami", font=self.uiFontNormal, height=1, width=30, command=self.choose_result_file_command)
        self.runFileButtton = tk.Button(window, text="Uruchom wybrany plik", font=self.uiFontNormal,
                                        height=1, width=30, bg="#A9A9A9", command=self.run_app_command)

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
        self.javaFilesListbox.grid(row=0, column=0, rowspan=5)
        self.refreshListboxButtton.grid(row=5, column=0)
        self.chooseFolderButtton.grid(row=6, column=0)
        self.folderLabel.grid(row=7, column=0)
        self.folderLabelVariable.grid(row=8, column=0)
        self.chooseTestFileButtton.grid(row=9, column=0)
        self.testFileLabel.grid(row=10, column=0)
        self.testFileLabelVariable.grid(row=11, column=0)

        self.scrollbar.grid(row=0, column=1, rowspan=5)

        self.resultLabel.grid(row=0, column=2)
        self.resultLabelVariable.grid(row=1, column=2)
        self.timeLabel.grid(row=2, column=2)
        self.timeLabelVariable.grid(row=3, column=2)
        self.selectedFileLabelVariable.grid(row=4, column=2)
        self.runFileButtton.grid(row=5, column=2)
        self.chooseJDKButtton.grid(row=6, column=2)
        self.jdkLabel.grid(row=7, column=2)
        self.jdkLabelVariable.grid(row=8, column=2)
        self.chooseResultFileButtton.grid(row=9, column=2)
        self.resultFileLabel.grid(row=10, column=2)
        self.resultFileLabelVariable.grid(row=11, column=2)

    def refresh_listbox_command(self):
        self.javaFilesListbox.delete(0, tk.END)

        self.selectedFile = ""
        self.selectedFileString.set("Wybrany plik: Brak")

        allFiles = os.listdir(self.selectedFolder)
        javaFiles = [file for file in allFiles if file[-5:] == ".java"]
        if len(javaFiles) == 0:
            self.javaFilesListbox.insert(tk.END, "Brak plików JAVA w folderze")
        else:
            for file in javaFiles:
                self.javaFilesListbox.insert(tk.END, file)

    def choose_folder_command(self):
        ask = filedialog.askdirectory()
        if len(ask) == 0:
            pass
        else:
            self.selectedFolder = ask
            self.folderString.set(self.selectedFolder)
            self.folderLabelVariable.config(bg="green")

        self.refresh_listbox_command()

    def choose_jdk_command(self):
        ask = filedialog.askdirectory()
        if len(ask) == 0:
            pass
        else:
            self.selectedJDK = ask
            self.jdkString.set(self.selectedJDK)
            self.jdkLabelVariable.config(bg="green")

    def choose_test_file_command(self):
        ask = filedialog.askopenfilename(
            title="Wybierz plik z testami", filetypes=[("Pliki tekstowe", "*.txt")])
        if len(ask) == 0:
            pass
        else:
            self.selectedTestFile = ask
            self.testFileString.set(self.selectedTestFile)
            self.testFileLabelVariable.config(bg="green")

    def choose_result_file_command(self):
        ask = filedialog.askopenfilename(
            title="Wybierz plik z wynikami", filetypes=[("Pliki tekstowe", "*.txt")])
        if len(ask) == 0:
            pass
        else:
            self.selectedResultFile = ask
            self.resultFileString.set(self.selectedResultFile)
            self.resultFileLabelVariable.config(bg="green")

    def run_app_command(self):
        try:
            result, time = testJavaProgram(self.selectedJDK, self.selectedResultFile,
                                           self.selectedTestFile, self.selectedFolder, self.selectedFile)
        except:
            messagebox.showerror("Wystąpił błąd",
                                 "Musisz wybrać prawidłowe foldery oraz pliki\n"
                                 "Musisz wybrać plik JAVA z listy")
        self.resultString.set(result)
        self.timeString.set(time)

    def get_selected_file(self, event):
        try:
            index = self.javaFilesListbox.curselection()[0]
            self.selectedFile = self.javaFilesListbox.get(index)
            self.selectedFileString.set(f"Wybrany plik: {self.selectedFile}")
        except IndexError:
            pass


window = tk.Tk()
Window(window)
window.mainloop()
