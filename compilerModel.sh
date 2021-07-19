cd /media/shared/maix_train
rm -rf out
python3 ../cvtTMFile.py ../kmodels/$1
python3 train.py -t classifier -d ../kmodels/$1.datasets train
python3 ../getKmodel.py ../kmodels/$1