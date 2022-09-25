docker run --name $1 -v /home/wa/docker/work/ai/$1:/media/shared/ webai/gpu_maix_train \
/bin/bash -c \
"cd /media/shared/maix_train && ../compilerModel.sh $2" \
&& docker rm -f $1