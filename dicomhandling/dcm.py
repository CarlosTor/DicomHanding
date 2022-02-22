import os
from typing import List

import cv2
import numpy as np
import pydicom as dicom


class DcmFile:

    def __init__(self, input_path: str):
        ds = self.read_from(input_path)
        self.filename = os.path.basename(input_path)
        self.original = ds.pixel_array
        self.ipp = self.get_tag_value(ds, 'ImagePositionPatient')

    def read_from(self, input_path: str) -> dicom.multival.MultiValue:
        return dicom.dcmread(input_path)

    def get_tag_value(self, dicom_file: dicom.multival.MultiValue, tag: str) -> List[float]:
        return [float(v) for v in dicom_file.data_element(tag).value]

    def write_to(self, output_path: str, image_format: str = '.jpg'):
        cv2.imwrite(f'{output_path}/{self.filename.replace(".dcm", image_format)}', self.original)
