import argparse, os, sys, shutil
from os import walk

path = './out/result_root_dir/'
destPath = sys.argv[1]

labels = 'labels.txt'
report = 'report.jpg'
kmodel = 'm.kmodel'

for root, dirs, files in walk(path):
	if len(dirs)==0:
		shutil.move(root+"/"+labels , destPath+"."+labels)
		shutil.move(root+"/"+report , destPath+"."+report)
		shutil.move(root+"/"+kmodel , destPath+".kmodel")

print("OK")