cd /media/shared/maix_train
rm -rf out
python3 ../cvtTMFile.py ../kmodels/$1
python3 train.py -t classifier -d ../kmodels/$1.datasets train
python3 ../getKmodel.py ../kmodels/$1
tensorflowjs_converter --input_format=keras ./out/m.tflite.h5 ../kmodels/
zip ../kmodels/model.kfpkg ../flash-list.json ../kmodels/project.tm.kmodel
