PARENT_DIR=$(basename "${PWD%/*}")
CURRENT_DIR="${PWD##*/}"
CURRENT_DIR="webai-train"
IMAGE_NAME="$CURRENT_DIR"
TAG="latest"

REGISTRY="nest.webduino.tw"

## for x86 CPU
#docker build -t ${IMAGE_NAME}:${TAG} .

## for Mac M2
docker build -t ${IMAGE_NAME}:${TAG} . --platform=linux/amd64

docker tag ${IMAGE_NAME}:${TAG} ${REGISTRY}/${IMAGE_NAME}:latest
docker push ${REGISTRY}/${IMAGE_NAME}:latest