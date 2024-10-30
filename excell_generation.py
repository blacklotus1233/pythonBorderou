from openpyxl import load_workbook

#TODO: sablonul excell de aranjat cant la monede si bancnote pe centru
#TODO: de verificat sablonul ca fontul size si font sa coincida peste tot

def fill_excel_template(data):
    # Load the template
    workbook = load_workbook("template2.xlsx")
    sheet = workbook.active

    # Populate cells with data from inputs
    #bancnote
    #Completam  bancnote cant D13-D21
    sheet["D13"] = data['input_0']
    sheet["D14"] = data['input_1']
    sheet["D15"] = data['input_2']
    sheet["D16"] = data['input_3']
    sheet["D17"] = data['input_4']
    sheet["D18"] = data['input_5']
    sheet["D19"] = data['input_6']
    sheet["D20"] = data['input_7']
    sheet["D21"] = data['input_8']
    # Completam  bancnote lei E13-E21
    sheet["E13"] = data['input_9']
    sheet["E14"] = data['input_10']
    sheet["E15"] = data['input_11']
    sheet["E16"] = data['input_12']
    sheet["E17"] = data['input_13']
    sheet["E18"] = data['input_14']
    sheet["E19"] = data['input_15']
    sheet["E20"] = data['input_16']
    sheet["E21"] = data['input_17']

  #Monede metalice
    #completam cant de monede metalice D24-D32
    sheet["D24"] = data['input_21']
    sheet["D25"] = data['input_22']
    sheet["D26"] = data['input_23']
    sheet["D27"] = data['input_24']
    sheet["D28"] = data['input_25']
    sheet["D29"] = data['input_26']
    sheet["D30"] = data['input_27']
    sheet["D31"] = data['input_28']
    sheet["D32"] = data['input_29']

    #completam val de monede metalice E24-E32
    sheet["E24"] = data['input_30']
    sheet["E25"] = data['input_31']
    sheet["E26"] = data['input_32']
    sheet["E27"] = data['input_33']
    sheet["E28"] = data['input_34']
    sheet["E29"] = data['input_35']
    sheet["E30"] = data['input_36']
    sheet["E31"] = data['input_37']
    sheet["E32"] = data['input_38']

    #completam totalurile
     #bancnote
    sheet["E23"] = data['input_45']
    #monede
    sheet["E34"] = data['input_46']

    # Save as a new file
    workbook.save("filled_template.xlsx")

input_dict={'input_0': '1', 'input_1': '2', 'input_2': '3', 'input_3': '4', 'input_4': '5', 'input_5': '6', 'input_6': '7', 'input_7': '8', 'input_8': '9', 'input_9': '1.0', 'input_10': '10.0', 'input_11': '30.0',
 'input_12': '80.0', 'input_13': '250.0', 'input_14': '600.0', 'input_15': '1400.0', 'input_16': '4000.0', 'input_17': '9000.0', 'input_18': '30.10.2024', 'input_19': 'genata', 'input_20': 'casier', 'input_21': '10',
 'input_22': '11', 'input_23': '12', 'input_24': '13', 'input_25': '14', 'input_26': '15', 'input_27': '16', 'input_28': '17', 'input_29': '18', 'input_30': '10.0', 'input_31': '22.0', 'input_32': '60.0', 'input_33': '130.0',
 'input_34': '0.14', 'input_35': '0.75', 'input_36': '1.6', 'input_37': '4.25', 'input_38': '9.0', 'input_39': 'Moldtelecom SA', 'input_40': '1002600048836', 'input_41': 'cont', 'input_42': 'locul', 'input_43': 'sdvz',
 'input_44': 'telefon', 'input_45': '15371.0', 'input_46': '237.74'}
fill_excel_template(input_dict)
