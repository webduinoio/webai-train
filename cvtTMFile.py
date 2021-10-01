# 解壓縮指定檔案

import argparse, os, sys, shutil
import zipfile 
import sys

path = sys.argv[1]
print('processing...',path)
files = zipfile.ZipFile(path)

try:	 
	os.mkdir(path)
except:
	pass

for i in files.namelist():
	dir =''
	filename = i
	try:
		idx = filename.index('-')
	except:
		continue
	try:	
		dir = filename[:idx]
		os.mkdir(path+'.datasets/'+dir)
	except:
		pass
	try:
		filePath=path+'.datasets/'+dir+'/'+filename
		if os.path.exists(filePath) == False:
			ext = filename.index('.jpg')
			files.extract(filename, path+'.datasets/'+dir)
			print('extract:',filePath)
	except:
		pass
