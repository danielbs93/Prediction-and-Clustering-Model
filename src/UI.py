from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog


class Clustering:

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "pre-process":
            print(self.path.get())
        elif method == "cluster":
            print("clusters: " + self.clusters.get() + " runs: " + self.runs.get())
        else:  # reset
            self.total = 0


    def __init__(self, master):
        self.master = master
        master.title("K-Means Clustering")

        self.total = 0
        self.entered_number = 0

        self.path = tk.StringVar(root)
        self.clusters = tk.StringVar(root)
        self.runs = tk.StringVar(root)

        def browsefunc():
            filename = filedialog.askopenfilename()
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, filename)



        # vcmd = master.register(self.validate) # we have to wrap the command

        # LABEL #
        self.label_path = Label(master, text="Enter path:")
        self.label_clusters = Label(master, text="Number of clusters k:")
        self.label_runs = Label(master, text="Number of runs:")

        # ENTRY #
        self.entry_path = Entry(master, textvariable=self.path)
        self.entry_clusters = Entry(master, validate="key", textvariable=self.clusters)#, validatecommand=(vcmd, '%P'))
        self.entry_runs = Entry(master, validate="key", textvariable=self.runs)#, validatecommand=(vcmd, '%P'))


        # BUTTON #
        self.browse_button = Button(root, text="Browse", command=browsefunc)
        self.cluster_button = Button(master, text="Cluster", width=30, command=lambda: self.update("cluster"))
        self.preProcess_button = Button(master, text="Pre-process", width=30, command=lambda: self.update("pre-process"))

        # LAYOUT #
        self.label_path.grid(row=1, column=0, sticky=W)
        self.label_clusters.grid(row=2, column=0, sticky=W)
        self.label_runs.grid(row=3, column=0, sticky=W)

        self.entry_path.grid(row=1, column=1, columnspan=25, sticky=W+E)
        self.entry_clusters.grid(row=2, column=1, columnspan=3, sticky=W+E)
        self.entry_runs.grid(row=3, column=1, columnspan=3, sticky=W+E)

        self.browse_button.grid(row=1, column=35)
        self.preProcess_button.grid(row=4, column=2, columnspan=15, sticky=W+E)
        self.cluster_button.grid(row=5, column=2)


root = tk.Tk()
root.rowconfigure(15, {'minsize': 500})
root.columnconfigure(25, {'minsize': 850})
my_gui = Clustering(root)
# root.geometry("1200x600")
root.mainloop()
