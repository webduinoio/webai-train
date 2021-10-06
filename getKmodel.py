import argparse, os, sys, shutil
from os import walk

path = './out/result_root_dir/'
destName = sys.argv[1]
modelType = sys.argv[2]

# 遞迴列出所有子目錄與檔案
labels = 'labels.txt'
report = 'report.jpg'
kmodel = 'm.kmodel'
labels_blockly = 'labels_blockly.txt'
anchor = 'anchor.txt'

for root, dirs, files in walk(path):
	if len(dirs)==0:
		shutil.copy(root+"/"+labels , "../kmodels/"+destName+"."+labels)
		shutil.copy(root+"/"+report , "../kmodels/"+destName+"."+report)
		shutil.copy(root+"/"+kmodel , "../kmodels/"+destName+"."+kmodel)
		shutil.copy(root+"/"+labels_blockly , "../kmodels/"+destName+"."+labels_blockly)
		shutil.copy(root+"/"+labels , "/content/drive/MyDrive/webai-train/{modelType}/{destName}/{fileName}".format(modelType=modelType,destName=destName,fileName=destName+"."+labels))
		shutil.copy(root+"/"+report , "/content/drive/MyDrive/webai-train/{modelType}/{destName}/{fileName}".format(modelType=modelType,destName=destName,fileName=destName+"."+report))
		shutil.copy(root+"/"+kmodel , "/content/drive/MyDrive/webai-train/{modelType}/{destName}/{fileName}".format(modelType=modelType,destName=destName,fileName=destName+"."+kmodel))
		shutil.copy(root+"/"+labels_blockly , "/content/drive/MyDrive/webai-train/{modelType}/{destName}/{fileName}".format(modelType=modelType,destName=destName,fileName=destName+"."+labels_blockly))
		if modelType == "detector":
			shutil.copy(root+"/"+anchor , "../kmodels/"+destName+"."+anchor)
			shutil.copy(root+"/"+anchor , "/content/drive/MyDrive/webai-train/{modelType}/{destName}/{fileName}".format(modelType=modelType,destName=destName,fileName=destName+"."+anchor))
		print(root+"/"+labels , destName+"."+labels)
		print(root+"/"+report , destName+"."+report)
		print(root+"/"+kmodel , destName+"."+kmodel)

print("OK")