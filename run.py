import csv
import copy

txtfile = open("plantilla.txt", "r")
file_data = txtfile.read().split('\n')

with open('db.csv', newline='', encoding='utf-8') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for i, row in enumerate(spamreader):
    if i > 0:
      # create new txt file
      result_txt = open("data"+str(i)+".txt", "a+")
      new_file = copy.deepcopy(file_data)
      # get row as list split by comma 
      row = ''.join(row).split(',')
      # get olt
      olt = row[2].strip() + '-' + row[1]
      index = new_file[5].index('XXX') 
      # modify OLT data
      new_file[5] = new_file[5][:index] + olt
      new_file[80] = 


      
      # save new txt file
      result_txt.writelines([l for l in new_file])
      result_txt.close()