import pandas as pd
from tkinter import filedialog


inputFile = filedialog.askopenfilename(title="Select file",
                                       filetypes=(("CSV Files", "*.csv"),))  # allows user to select file
outputFile = pd.read_csv(inputFile, usecols=['Tracking Number', 'Scheduled delivery date', 'Recipient contact name',
                                             'Purchase order number', 'Reference', 'Recipient company'])  # select columns to be used in new csv
outputFile.to_csv(inputFile[:-4] + 'Trimmed.csv', index=False)  # write data to new csv
