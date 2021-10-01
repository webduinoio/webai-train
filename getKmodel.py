import argparse, os, sys, shutil
from os import walk

path = './out/result_root_dir/'
destName = sys.argv[1]

# 遞迴列出所有子目錄與檔案
labels = 'labels.txt'
report = 'report.jpg'
kmodel = 'm.kmodel'

for root, dirs, files in walk(path):
	if len(dirs)==0:
		shutil.copy(root+"/"+labels , "../kmodels/"+destName+"."+labels)
		shutil.copy(root+"/"+report , "../kmodels/"+destName+"."+report)
		shutil.copy(root+"/"+kmodel , "../kmodels/"+destName+"."+kmodel)
		shutil.copy(root+"/"+labels , "/content/drive/MyDrive/webai-train/"+destName+"."+labels)
		shutil.copy(root+"/"+report , "/content/drive/MyDrive/webai-train/"+destName+"."+report)
		shutil.copy(root+"/"+kmodel , "/content/drive/MyDrive/webai-train/"+destName+"."+kmodel)
		print(root+"/"+labels , destName+"."+labels)
		print(root+"/"+report , destName+"."+report)
		print(root+"/"+kmodel , destName+"."+kmodel)

print("OK")