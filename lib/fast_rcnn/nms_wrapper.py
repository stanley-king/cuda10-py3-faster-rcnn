# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

from fast_rcnn.config import cfg
from nms.gpu_nms import gpu_nms
from nms.cpu_nms import cpu_nms
from nms.py_cpu_nms import py_cpu_nms

def nms(dets, thresh, force_cpu=False):
    """Dispatch to either CPU or GPU NMS implementations."""

    if dets.shape[0] == 0:
        return []
    # if cfg.USE_GPU_NMS and not force_cpu:
    #     return gpu_nms(dets, thresh, device_id=cfg.GPU_ID)
    # else:
    return cpu_nms(dets, thresh)

    # ret1 = gpu_nms(dets, thresh, device_id=1)
    # ret2 = cpu_nms(dets, thresh)
    # ret3 = py_cpu_nms(dets, thresh)

    # return py_cpu_nms(dets, thresh)

