import argparse # 转换coco到yolo
parser = argparse.ArgumentParser()
parser.add_argument('-p', help='path/to/coco/annotations/', dest='path', required=True)
args = parser.parse_args()
path = args.path

from ultralytics.data.converter import convert_coco
convert_coco(labels_dir=path, use_segments=True)