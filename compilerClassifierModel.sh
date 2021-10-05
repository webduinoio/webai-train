cd maix_train
rm -rf out
cp /content/drive/MyDrive/$1 ../kmodels
mkdir -p /content/drive/MyDrive/webai-train
cp /content/drive/MyDrive/$1 /content/drive/MyDrive/webai-train/$1
python3 ../cvtTMFile.py ../kmodels/$1
python3 train.py init
python3 train.py -t classifier -d ../kmodels/$1.datasets train
python3 ../getKmodel.py $1 classifier