from pypdf import PdfMerger
import PySimpleGUI as sg
from datetime import datetime

def combine_PDFs(file1, file2, output_file_name):
    if not file1 or not file2:
        print("No files inputted")
        return
    file_names = [file1, file2]
    merger = PdfMerger()
    for file in file_names:
        merger.append(file)
    c = datetime.now()
    time = c.strftime('%IH%MM%SS')
    if not output_file_name: 
        output_file_name = f"PDFs/result_{c.month}-{c.day}-{c.year}_{time}.pdf"
    else:
        output_file_name = f"{output_file_name}/result_{c.month}-{c.day}-{c.year}_{time}.pdf"
    print(output_file_name)
    merger.write(output_file_name)
    merger.close()

layout_column = [
    [
        sg.Text("File 1: ", expand_x=True),
        sg.In(size=(25, 1), enable_events=True, key="-FILE1-", expand_x=True),
        sg.FileBrowse(file_types=((('PDFs', '*.pdf'),))),
    ],
    [
        sg.Text("File 2: ", expand_x=True),
        sg.In(size=(25, 1), enable_events=True, key="-FILE2-", expand_x=True),
        sg.FileBrowse(file_types=((('PDFs', '*.pdf'),))),
    ],
    [
        sg.Text("Folder location: ", expand_x=True),
        sg.In(size=(25, 1), enable_events=True, key="-LOCATION-", expand_x=True),
        sg.FolderBrowse()
    ],
    [
        sg.Button("Confirm", key="-CONFIRM-", expand_x=True),
        sg.Text("No file(s) selected", enable_events=True, key="-ERROR-", text_color='red', visible=False, expand_x=True, font=("Helvetica", 20, "bold"))
    ]
]

file1_name, file2_name, file_location = "", "", ""
window = sg.Window("Combine PDFs", layout_column, size=(800, 250))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FILE1-":
        file1_name = values["-FILE1-"]
    elif event == "-FILE2-":
        file2_name = values["-FILE2-"]
    elif event == "-LOCATION-":
        file_location = values["-LOCATION-"]
    elif event == "-CONFIRM-":
        if not file1_name or not file2_name:
            window["-ERROR-"].update(visible=True)
        else:
            window["-ERROR-"].update(visible=False)
            combine_PDFs(file1_name, file2_name, file_location)

window.close()