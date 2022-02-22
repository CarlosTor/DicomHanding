import numpy as np
from scipy.ndimage import gaussian_filter
import cv2

from dicomhandling.dcm import DcmFile
from dicomhandling.exceptions import WrongAngle


class DcmFilter(DcmFile):
    '''
    Class for applying a Gaussan filter to a Dicom image
    '''

    def __init__(self, input_path: str, sigma: float = 3):
        DcmFile.__init__(self, input_path)
        self._sigma = sigma
        self.filtered = self.apply_gaussian()

    def apply_gaussian(self) -> np.ndarray:
        '''
        Apply a Gaussian filter
        '''
        return gaussian_filter(self.original, self._sigma)


class DcmRotate(DcmFile):
    '''
    Class for applying a rotation to a Dicom image
    '''

    def __init__(self, input_path: str, angle: int = 180):
        DcmFile.__init__(self, input_path)
        self._angle = self.normalize_angle(angle)
        self.rotated = self.apply_rotation()

    def normalize_angle(self, angle) -> int:
        '''
        Normalize the angle by 90
        '''
        if angle % 90 != 0:
            raise WrongAngle(message)
        return angle // 90

    def apply_rotation(self) -> np.ndarray:
        '''
        Apply rotation to the image
        '''
        return np.rot90(self.original, k=self._angle)


def check_ipp(dcm_file_1: DcmFile, dcm_file_2: DcmFile) -> bool:
    '''
    Check the Information Position Patient attribute of two images.
    If they are equal, it returns True, otherwise False.
    '''
    return dcm_file_1.ipp == dcm_file_2.ipp


def write_image(image: np.ndarray, output_path: str, image_format: str = '.jpg'):
    '''
    Write a numpy array to a image (jpg by default)
    '''
    cv2.imwrite(f'{output_path}{image_format}', image)
