import argparse, os, sys, shutil
from os import walk

path = './out/result_root_dir/'
destPath = sys.argv[1]

# 遞迴列出所有子目錄與檔案
labels = 'labels.txt'
report = 'report.jpg'
kmodel = 'm.kmodel'

for root, dirs, files in walk(path):
	if len(dirs)==0:
		shutil.move(root+"/"+labels , destPath+"."+labels)
		shutil.move(root+"/"+report , destPath+"."+report)
		shutil.move(root+"/"+kmodel , destPath+".kmodel")

print("OK")