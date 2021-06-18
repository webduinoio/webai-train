docker run --name train -v `pwd`:/media/shared/ webai/maix_train \
/bin/bash -c \
"cd /media/shared/maix_train && ../utils/compiler_Model.sh $1" \
&& docker rm train