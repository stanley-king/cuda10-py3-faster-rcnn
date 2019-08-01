set startTime=%time%
python ./tools/train_faster_rcnn_alt_opt.py --net_name=VGG16 --gpu=0
shtudown -s -t 0