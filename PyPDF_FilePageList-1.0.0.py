# ==========================================================================
# Title: PDF File Page List
# Function: SNAP
# Developed by: Earl Lamier
# Date Created: 2022 Mar 3
# Subgroup: NA
# Version 1.0.0
# Description: List PDF pages in CSV
# Status: Release
# Date Updated: 8 Mar 2022
# Release Date: 8 Mar 2022
# Filename: PyPDF_FilePageList_v1.0.0
# ==========================================================================

""" 
Revision History:
2022 Mar 8
1. Initial release
 """

# ==========================================================================
# libraries
from asyncio import coroutines
import enum
from itertools import count
from multiprocessing.sharedctypes import Value
from operator import index
from re import search
from tkinter.messagebox import YES
from typing import Counter

import csv
import os
from pathlib import Path
import fnmatch
from PyPDF2 import PdfFileReader
import numpy as np
import pandas as pd
import arrow # for time and date
import glob
import sys  

# ==========================================================================
print("\n==================== APPLICATION ====================")
print("\t\tPDF Pages File List")
print("------------------------------------------------------")
print("Version: 1.0.0")
print("Developed by: Earl Lamier")
print("Date Created: 2022 March 3")
print("Release Date: 2022 March 8")
print("------------------------------------------------------")

# open current working directory
thisDir = os.getcwd()  

# Time and Date
utc = arrow.utcnow()
localTimeStamp = arrow.now()
#localTimeStamp = arrow.utcnow()
#localTimeStamp = utc.to('US/Pacific')
localDate = localTimeStamp.format('DD-MMM')
stringDateToday = str(localDate)
eventStamp = localTimeStamp.format('ddd DD MMMM YYYY, hh:mm:ss A')
print('*** Start of Event: ', eventStamp, '\n')
print('==================== S T A R T ====================')

# Getting the current work directory (cwd)
print("\nCurrent Directory:\n")
thisdir = os.getcwd()
print("-->",thisdir,"\n")

# get and count total files
onlyfiles = next(os.walk('.'))[2]
totalFiles = len(onlyfiles)
print("List of files in current directory: \n")
for countFiles, theFiles in enumerate(onlyfiles,1):
    print("\t",countFiles,".",theFiles)
print("\nTotal files in current directory: ", totalFiles)

# ==========================================================================
# GET INFORMATION

#print("Current Python File:\n\n", Path(__file__).absolute, "\n")

# declare variables
dateToday = []
mailDate = []
fileSizeList = []

print()
# total PDF Files
pdf_count = len(fnmatch.filter(os.listdir(Path().absolute()), '*.pdf'))
print("Total PDF Files: ", pdf_count)
print()

# display pdf info
print("*** PDF Information: ***\n")
def extract_information(pdf_path):
    #fileNameList = []
    with open(pdf_path, 'r+b') as targetFile: # rb - read binary
        pdf = PdfFileReader(targetFile)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        filePages = str(number_of_pages)
        filePagesList.append(filePages)
        fileRecordsList.append(filePages)
     
        # f is string function
        txt = f"""
        Information about {pdf_path}:  
        Title: {information.title} 
        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Number of pages: {number_of_pages}
        """         
    
    print(txt)            
    return information

if __name__ == '__main__':

    thisdir1 = os.getcwd()
    for root_var1, dir_var1, file_var1 in os.walk(thisdir1):
        fileNameList = []
        filePagesList = []
        fileRecordsList = []
        recIndex = []
        rec = 1

        for file in file_var1:
            if ".pdf" in file:
                path_a = os.path.join(root_var1,file)
                print(os.path.join(root_var1, file))               
                extract_information(path_a)

                # remove .pdf
                cleanName = file.replace(".pdf", "")
                fileNameList.append(cleanName)

                # write to dataframe
                #fileNameList.append(file)
                dateToday.append(stringDateToday)
                mailDate.append(stringDateToday)
                recIndex.append(rec)
                
                #print("\n",fileNameList)
                metaArray = np.column_stack((recIndex, fileNameList, filePagesList, fileRecordsList, dateToday, mailDate))
                df = pd.DataFrame({'Rec Index': metaArray[:, 0],'PDF Filename': metaArray[:, 1], 'No. of Pages': metaArray[:, 2], 'No. of Records': metaArray[:, 3], 'Print Date': metaArray[:, 4], 'Mail Date': metaArray[:, 5]})
                rec = rec + 1

# export print results as CSV file
exFileDate = localTimeStamp.format('MMM-DD')
exportFname = str(f"PDF File Page List - {exFileDate}.csv")
export_csv = df.to_csv(exportFname)

print('==================== E N D ====================\n')
print("*** End of Event (Date & Time): ",eventStamp)
print("\nThank you for using the App! Please find file.")
print("\n\t-->>",exportFname)
input("< Press Any Key to Close App >")

# END OF CODE
