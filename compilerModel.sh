cd /media/shared/maix_train
rm -rf out
python3 ../cvtTMFile.py ../kmodels/project.tm
python3 train.py -t classifier -d ../kmodels/project.tm.datasets train
python3 ../getKmodel.py ../kmodels/project.tm
tensorflowjs_converter --input_format=keras ./out/m.tflite.h5 ../kmodels/
zip ../kmodels/model.kfpkg ../flash-list.json ../kmodels/project.tm.kmodel
