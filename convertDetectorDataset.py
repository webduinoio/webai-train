import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

import cv2

xml = """
<annotation>
	<folder>{folder}</folder>
	<filename>{filename}</filename>
	<path>{path}</path>
	<source>
        <database>Unknown</database>
	</source>
	<size>
        <width>224</width>
        <height>224</height>
        <depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
        <name>{folder}</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
        	<xmin>{xmin}</xmin>
        	<ymin>{ymin}</ymin>
        	<xmax>{xmax}</xmax>
        	<ymax>{ymax}</ymax>
        </bndbox>
	</object>
</annotation>
"""


@dataclass
class CropParams:
    x: int
    y: int
    w: int
    h: int


@dataclass
class XMLParams:
    folder: str
    filename: str
    path: str
    xmin: int
    ymin: int
    xmax: int
    ymax: int


input_dir = sys.argv[1]
output_dir = sys.argv[2]

try:
    shutil.rmtree(output_dir)
except:
    print(f'{output_dir} not found, no need to remove')

for (dir_path, dir_names, file_names) in os.walk(input_dir):
    for dir in dir_names:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(output_dir, "labels.txt"), "a") as f:
            f.write(f"{dir}\n")

    for name in file_names:
        dataset_name = os.path.basename(dir_path)

        # save label
        output_xml_folder = os.path.join(output_dir, "xml", dataset_name)
        output_label_path = os.path.join(output_xml_folder, f"{Path(name).stem}.xml")
        Path(output_xml_folder).mkdir(parents=True, exist_ok=True)

        match = re.search(r"\d+_\d+_\d+_\d+_\d+_\d+", name)

        x, y, w, h = (
            list(map(int, match.group(0).split("_")[:4])) if match else [0, 0, 224, 224]
        )
        
        if match:
            x = x - 48
            y = y - 10

        print(f"x: {x} y: {y} w: {w} h: {h}")

        xml_params = XMLParams(
            folder=dataset_name,
            filename=name,
            path=os.path.join("images", dataset_name, name),
            xmin=x,
            ymin=y,
            xmax=x + w,
            ymax=y + h,
        )

        with open(output_label_path, "w") as f:
            f.write(
                xml.format(
                    folder=xml_params.folder,
                    filename=xml_params.filename,
                    path=xml_params.path,
                    xmin=xml_params.xmin,
                    ymin=xml_params.ymin,
                    xmax=xml_params.xmax,
                    ymax=xml_params.ymax,
                )
            )

        # save image
        output_images_folder = os.path.join(output_dir, "images", dataset_name)
        output_file_path = os.path.join(output_images_folder, name)
        Path(output_images_folder).mkdir(parents=True, exist_ok=True)

        img = cv2.imread(os.path.join(dir_path, name))
        height, width, _ = img.shape
        print(f"Image size: {width}x{height}")

        if width == 320 and height == 240:
            print(f"Crop to 224 x 224")
            crop_param = CropParams(x=48, y=10, w=224, h=224)
            img = img[
                crop_param.y : crop_param.y + crop_param.h,
                crop_param.x : crop_param.x + crop_param.w,
            ]

        # debug
        left_up = (x, y)
        right_down = (x + w, y + h)
        color = (0, 0, 255)  # red
        thickness = 1  # 寬度 (-1 表示填滿)
        # cv2.rectangle(img, left_up, right_down, color, thickness)

        
        cv2.imwrite(output_file_path, img)


# > INPUT
# input (320 x 240)
#  |---stone
#  |---paper

# > OUTPUT
# dataset
#  |--images (224 x 224)
#  |	|---stone
#  |	|---paper
#  |-- xml
#  |	|---stone
#  |	|---paper
#  |--labels.txt
