from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from src.DataPreprocessing import DataPreProcessing
from src.DataClustering import DataClustering



class Clustering:
    df_preProcessing = ""

    def update(self, method):
        if method == "pre-process":
            try:
                if len(self.path.get()) == 0:
                    raise TypeError("Please insert legal path")
                data_preprocessing = DataPreProcessing(self.path.get())
                self.df_preProcessing = data_preprocessing.prepareData()
                messagebox.showinfo("Pre-processing", "Preprocessing completed successfully!")
            except OSError as err:
                messagebox.showerror("Error", "OS error: {0}".format(err))
            except Exception as exception:
                messagebox.showerror("Error", exception)
            except TypeError as exception:
                messagebox.showerror("Error", exception)
        elif method == "cluster":
            try:
                if len(self.clusters.get()) == 0 or len(self.runs.get()) == 0:
                    raise TypeError
                numOfRuns = int(self.runs.get())
                numOfClusters = int(self.clusters.get())
                if numOfRuns < 1 or numOfClusters < 1:
                    raise ValueError("Please insert just positive numbers")
                if numOfClusters > 195:  # 195 is the max number of countries in the world - max number of clustering equals to amounts of dataset points
                    raise ValueError("Please insert number of cluster smaller than 195 - number of all countries in the world")
                data_clustering = DataClustering(self.df_preProcessing, self.path.get(), numOfRuns, numOfClusters)
                data_clustering.runClustering()
                image1 = tk.PhotoImage(file="../resource/scatter.png")
                label1 = tk.Label(image=image1)
                image2 = tk.PhotoImage(file="../resource/choroplethMap.png")
                label2 = tk.Label(image=image2)
                label1.grid(row=15, column=17)
                label2.grid(row=15, column=18)
                msg_box = messagebox.askyesno("Cluster", "Clustering is done, would you like to exit?")
                if msg_box:
                    root.destroy()
                else:
                    root.wait_window(root)
                    # if 'normal' == root.state():
                    #     label1.grid(row=15, column=17)
                    #     label2.grid(row=15, column=18)
            except ValueError as exc:
                messagebox.showerror("Error", "Error occurred:" + exc.__str__())
            except TypeError:
                messagebox.showerror("Error", "Please insert number values for the number of runs and clusters k parameters")
        else:
            self.total = 0


    def __init__(self, master):

        self.master = master
        master.title("K-Means Clustering")

        self.total = 0
        self.entered_number = 0

        self.path = tk.StringVar(root)
        self.clusters = tk.StringVar(root)
        self.runs = tk.StringVar(root)

        def browseFunc():
            filename = filedialog.askopenfilename()
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, filename)


        # LABEL #
        self.label_path = Label(master, text="Enter path:")
        self.label_clusters = Label(master, text="Number of clusters k:")
        self.label_runs = Label(master, text="Number of runs:")

        # ENTRY #
        self.entry_path = Entry(master, textvariable=self.path)
        self.entry_clusters = Entry(master, validate="key", textvariable=self.clusters)
        self.entry_runs = Entry(master, validate="key", textvariable=self.runs)


        # BUTTON #
        self.browse_button = Button(root, text="Browse", command=browseFunc)
        self.cluster_button = Button(master, text="Cluster", width=30, command=lambda: self.update("cluster"))
        self.preProcess_button = Button(master, text="Pre-process", width=30, command=lambda: self.update("pre-process"))

        # LAYOUT #
        self.label_path.grid(row=1, column=0, sticky=W)
        self.label_clusters.grid(row=2, column=0, sticky=W)
        self.label_runs.grid(row=3, column=0, sticky=W)

        self.entry_path.grid(row=1, column=1, columnspan=3, sticky=W+E)
        self.entry_clusters.grid(row=2, column=1, columnspan=3, sticky=W+E)
        self.entry_runs.grid(row=3, column=1, columnspan=3, sticky=W+E)

        self.browse_button.grid(row=1, column=4)
        self.preProcess_button.grid(row=4, column=2, sticky=W+E)
        self.cluster_button.grid(row=5, column=2)


root = tk.Tk()
root.rowconfigure(15, {'minsize': 350})
root.columnconfigure(18, {'minsize': 800})
my_gui = Clustering(root)
# root.geometry("1200x600")
root.mainloop()
