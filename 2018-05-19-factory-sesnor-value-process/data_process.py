import os
import sys
import subprocess
import time
import csv
def file_name(file_dir):
	i = 0
	for root, dirs, files in os.walk(file_dir):
		return files

def main():
	files = file_name('D:\data')
	data = []
	output_data = []
	output = open("D:\\result.txt","w")
	i = 0
	row  = 0
	for file in files:
		path = 'D:\data\%s' %file
		data.append(file.split('.')[0])
		fd = open(path, "r")
		lines = fd.readlines()
		for str in lines:
			data.append(str.split(':')[0])
			temp = str.split(':')[1]
			temp = temp.split('\n')[0]
			data.append(temp)
	
	for item in data:
		raw = i / 15;
		if((i%15) == 0):
			output_data.append([])
		output_data[int(raw)].append(item)
		i = i + 1

	num = len(output_data)
	with open('D:\\example.csv', 'w') as f:
		writer = csv.writer(f)
		for i in range(num):
			writer.writerow(output_data[i])
		
		
if __name__ == "__main__":
	main()