# pip3 install --upgrade pip
# mkdir /tmp
# apt update
# pip3 install -r requirements.txt
# git clone 

cd /media/shared/maix_train
rm -rf out
python3 ../utils/cvtTMFile.py ../kmodels/$1
python3 train.py -t classifier -d ../kmodels/$1.datasets train
python3 ../utils/getKmodel.py ../kmodels/$1


