This is a small program/project I created in Python. During my time at University, I found myself needing to combine PDFs. The main option was to use an online tool, in which you have to upload the pdfs to the website, typically up to 10 files, wait for it to combine, and then have to download the new file that contained the combined pdfs. I wanted to create something that was a quicker and better solution for myself.

To create this, I used the Python library PdfMerger. In addition to make the program better and more efficient, I used PySimpleGUI to create a basic interface. This allows me to easily upload and choose the path to the files I need combined. I also created some basic error handling in case a file isn't uploaded. There is a default path for the file to get uploaded to as well. I have some screenshots of the program below. 

Here is the basic interface with no data: 

![image](https://github.com/kkinsey01/CombinePDFs/assets/104642932/1b889fd3-410e-46f7-a6ff-bfa35f99a41e)

Here is the interface letting the user know of an error

![image](https://github.com/kkinsey01/CombinePDFs/assets/104642932/bacaf732-ad96-410a-af1b-4f326f44167b)

Here is the interface with some data entered

![image](https://github.com/kkinsey01/CombinePDFs/assets/104642932/640fa272-cfcb-4caf-996d-ac6887c95877)

The browse button will open the windows file explorer, letting the user either select a pdf or a folder location. 
