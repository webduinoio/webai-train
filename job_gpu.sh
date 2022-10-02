# $1:{{jobName}} , $2:{jobHomePath} , $2/../ <-- ncc folder
docker rm -f $1
docker run --name $1 -v $2:/media/shared/ -v $2/../:/usr/src/ webai/gpu_maix_train \
/bin/bash -c \
"cd /media/shared/maix_train && ../compilerModel.sh project.tm" && docker rm -f $1
