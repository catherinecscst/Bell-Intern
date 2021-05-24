import os
import re
import sys
import time

def read_csv(file):
	sub_NOs = []
	flag = 0
	fd = open(file)
	for line in fd:
		if flag != 0:
			#print "LINE======", line.split(",")[2]
			sub_NOs.append(line.split(",")[2])
		else:
			flag += 1
	fd.close()
	return sub_NOs

def read_accounts(file, sub_NOs):

	fd = open(file)
	fd_results = open("results_baseOnSuscriberNO.txt", "w")\

	print "==================1=================="
	extracted = []
	for line in fd:
		splited = line.split(",")
		if len(splited) >= 19:
			extracted.append([splited[1], str(float(splited[19]) / 100)])

	print "==================2=================="

	#print "length of TMP: ", len(extracted)  ====> 776399

	fc_g, fc_b = 1, 1
	for line in extracted:
		id_num = line[0]
		if id_num in sub_NOs:
			print "=====>>>", "sub_NOs: " + str(len(sub_NOs)), line[0] + ", " +  line[1]
			fd_results.write(line[0] + ", " + line[1] + "\n")
			sub_NOs.remove(id_num)
			#print fc_g
			fc_g += 1
		print fc_g, "/", fc_b
		fc_b += 1

	print "==================3=================="

	fd_results.close()
	fd.close()

if __name__ == "__main__":

    csv_file = "CDMA_EOP_July2018_Prepaid.csv"
    sub_NOs = read_csv(csv_file)
 
    #print sub_NOs[0:5]

    print "Done csv"

    hdAccount_file = "hd_account_20180906011900"
    read_accounts(hdAccount_file, sub_NOs)


