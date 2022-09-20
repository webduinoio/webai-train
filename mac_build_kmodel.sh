docker run --name train --platform=linux/amd64 -v `pwd`:/media/shared/ webai/cpu_maix_train \
/bin/bash -c \
"cd /media/shared/maix_train && ../compilerModel.sh $1" \
&& docker rm train
