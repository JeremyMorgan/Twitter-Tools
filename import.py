import csv

print("VERSION BUILD=8850919 RECORDER=FX")

filename = "pierre.csv";


def getOutput():
import os
outfile=''  #put your file path there
os.system("curl --head www.google.com>>{x}".format(x=str(outfile))  #Outputs command to log file (and creates it if it doesnt exist).
readOut=open("{z}".format(z=str(outfile),"r")  #Opens file in reading mode.
for line in readOut:
	print line  #Prints lines in file
readOut.close()  #Closes file
os.system("del {c}".format(c=str(outfile))  #This is optional, as it just deletes the log file after use.

#----------------------------------------------------------------------
def csv_dict_reader(file_obj, counter):
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		print("TAB T=" + str(counter))
		print("URL GOTO=https://twitter.com/" + line["screen_name"])
		print("TAB OPEN")
		counter += 1


#----------------------------------------------------------------------
if __name__ == "__main__":
	with open(filename) as f_obj:
		csv_dict_reader(f_obj, 1)