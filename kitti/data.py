import numpy as np
import tensorflow as tf
import pandas as pd
import os

def read_label_3d(label_file):
    """Read and parse label information of kitti 3d object detection dataset

    Data Format Description
    =======================

    The data for training and testing can be found in the corresponding folders.
    The sub-folders are structured as follows:

      - image_02/ contains the left color camera images (png)
      - label_02/ contains the left color camera label files (plain text files)
      - calib/ contains the calibration for all four cameras (plain text file)

    The label files contain the following information, which can be read and
    written using the matlab tools (readLabels.m, writeLabels.m) provided within
    this devkit. All values (numerical or strings) are separated via spaces,
    each row corresponds to one object. The 15 columns represent:

    #Values    Name      Description
    ----------------------------------------------------------------------------
       1    type         Describes the type of object: 'Car', 'Van', 'Truck',
                         'Pedestrian', 'Person_sitting', 'Cyclist', 'Tram',
                         'Misc' or 'DontCare'
       1    truncated    Float from 0 (non-truncated) to 1 (truncated), where
                         truncated refers to the object leaving image boundaries
       1    occluded     Integer (0,1,2,3) indicating occlusion state:
                         0 = fully visible, 1 = partly occluded
                         2 = largely occluded, 3 = unknown
       1    alpha        Observation angle of object, ranging [-pi..pi]
       4    bbox         2D bounding box of object in the image (0-based index):
                         contains left, top, right, bottom pixel coordinates
       3    dimensions   3D object dimensions: height, width, length (in meters)
       3    location     3D object location x,y,z in camera coordinates (in meters)
       1    rotation_y   Rotation ry around Y-axis in camera coordinates [-pi..pi]
       1    score        Only for results: Float, indicating confidence in
                         detection, needed for p/r curves, higher is better.
    """
    return pd.read_csv(label_file, sep=" ", names=['label', 'truncated', 'occluded', 'alpha', 'bbox_xmin', 'bbox_ymin', 'bbox_xmax', 'bbox_ymax', 'dim_height', 'dim_width', 'dim_length', 'loc_x', 'loc_y', 'loc_z', 'rotation_y', 'score'])


def get_image_names(img_dir):
    """Returns names of all .png files"""
    imgs = [fname for fname in os.listdir(img_dir) if fname.endswith('.png')]
    return imgs
