cd maix_train
rm -rf out
cp /content/drive/MyDrive/$1 ../kmodels
mkdir -p /content/drive/MyDrive/webai-train/detector/$1
cp /content/drive/MyDrive/$1 /content/drive/MyDrive/webai-train/detector/$1/$1
python3 train.py init
python3 train.py -t detector -z ../kmodels/$1 train
python3 ../getKmodel.py $1 detector