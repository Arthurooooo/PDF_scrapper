import re
import os
import PyPDF2 as p2

import glob


class Device:  # Définition de Device

    def __init__(self):  # Notre méthode constructeur
        self.type
        self.model
        self.emission
        self.error_margin


for filename in glob.glob('*.pdf'):
    with open(os.path.join(os.getcwd(), filename), 'rb') as f:
        PDFfile = f

        pdfread = p2.PdfFileReader(PDFfile)

        x = pdfread.getPage(0)
        fulltext = x.extractText()
        firstlines = '\n'.join(fulltext.split('\n')[:15])
      #  print(firstlines)
        regex = re.compile('kgCO2e')
        co2_emitted = re.findall("(\d+)\s+kgCO2e", fulltext)
        Device.type = ""
        Device.model = ""
        fullstring = re.findall("Dell\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines)
       # print("entered the condition")
    if fullstring:
        if fullstring[0].split()[0].replace(' ', '') == "Latitude" or fullstring[0].split()[0].replace(' ', '') == "OptiPlex" or fullstring[0].split()[0].replace(' ', '') == "PowerEdge":
            Device.type = fullstring[0].split()[0].replace(' ', '')
            Device.model = fullstring[0].split(' ', 1)[1].replace('\n', '')
     #       print(Device.type, "TEST:",fullstring.split(' ')[1])
     #       print("fullstring is", fullstring)
      #      print("est de type:", Device.type, "modele:", Device.model)
        else:
            Device.type = "        "
            Device.model = fullstring[0].split()[0].replace(' ', '')
     #       print("pas de type pour:", Device.model)
    #   Device.model = Device.type.split(' ')[1]
        #Device.model = Device.model[0].replace(r'\n', "").splitlines()[1]
    else:
        fullstring = ""
        fullstring = re.findall("OptiPlex\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines)[0].split()[0]
        if fullstring:
            Device.type = "OptiPlex"
            Device.model = fullstring
        #    print("not found for ", filename, "but found",fullstring[0].split()[0])
    if fullstring:
        print(Device.type, Device.model,"taux de co2 egal a", co2_emitted[0], "KgCO2")