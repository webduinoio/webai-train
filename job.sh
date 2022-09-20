docker run --name $1 -v /home/wa/docker/work/ai/webai-train-$1:/media/shared/ webai/cpu_maix_train \
/bin/bash -c \
"cd /media/shared/maix_train && ../compilerModel.sh $2" \
&& docker rm $1