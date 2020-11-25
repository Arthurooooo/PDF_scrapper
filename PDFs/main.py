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
    with open(os.path.join(os.getcwd(), filename), 'rb') as PDFfile:

        pdfread = p2.PdfFileReader(PDFfile)  # on lit le PDF en entier
        #print("treating file", filename)
        page1 = pdfread.getPage(0)  # on obtient le contenu de la page qui nous interesse
        fulltext = page1.extractText()  # le contenu est transcrit en texte lisible
        firstlines = '\n'.join(fulltext.split('\n')[:15])  # on obtient les 15 premieres lignes
        # regex = re.compile('kgCO2e')
        co2_emitted = re.findall("(\d*\s\d+)\s+kgCO", fulltext)[0].replace('\n', '')  #on trouve le kgCO2e et on clean la string
        Device.type = ""
        Device.model = ""

    if re.findall("Dell\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines):
        full_id = re.findall("Dell\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines)
        #print("issa Dell")
    elif re.findall("PowerEdge\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines):
        full_id = re.findall("PowerEdge\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines)
        Device.type = "PowerEdge"
        #print("issa PowerEdge")
    elif re.findall("Precision\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines):
        full_id = re.findall("Precision\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines)
        Device.type = "Precision"
        #print("found it's a precision")

    if full_id and Device.type == "":  # Si on a match une string

        if full_id[0].split()[0].replace(' ', '') == "Latitude" or\
                full_id[0].split()[0].replace(' ', '') == "OptiPlex" or \
                full_id[0].split()[0].replace(' ', '') == "Precision" or \
                full_id[0].split()[0].replace(' ', '') == "PowerEdge":
            Device.type = full_id[0].split()[0].replace(' ', '')
            Device.model = full_id[0].split(' ', 1)[1].replace('\n', '')

        else:
            Device.type = "        "
            Device.model = full_id[0].replace('\n', '').split()[0]

    else:  # Si on a pas match une string
        #print("entre dans la condition pour ", firstlines)
        if re.match("OptiPlex", firstlines):
            full_id = re.findall("OptiPlex\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines)[0].split()[0]
        #else if re.match("OptiPlex", firstlines) is not None:
        #print("entre dans la condition pour ", full_id)
        #if full_id:
        #    Device.type = "OptiPlex"
        #    Device.model = full_id
        #print(full_id)
        Device.model = full_id[0].replace('\n', '').split()[0]
        #print("entered the condition and device ID is", Device.model)
    #full_id = re.findall("PowerEdge\s+(.*\n*\w*\n*\d*\d*\n*.*)", firstlines)

    if full_id:
        print(Device.type, Device.model, "taux de co2 egal a", co2_emitted, "KgCO2")
    #print(firstlines)
