import os

import cv2
import numpy as np

from dicomhandling import DcmFilter, DcmRotate, check_ipp, write_image
from dicomhandling.exceptions import IncorrectNumberOfImages, SameImagePositionPatient


def get_2_images(dir_path: str):
    '''
    Find Dicom files given a folder.
    If the number of files is not two, it raises an exception.
    '''
    assert os.path.exists(dir_path)
    dcm_filenames = [f'{dir_path}/{fn}' for fn in os.listdir(dir_path) if fn.endswith('.dcm')]
    if len(dcm_filenames) != 2:
        raise IncorrectNumberOfImages()
    return dcm_filenames


def compute_residue(input_folder_path: str, output_path: str, sigma: float):
    '''
    Compute the residue given a folder containing two different Dicom images.
    It generates two kind of residues: before and after applying a filter.
    '''
    ## Find images in folder and load it
    dcm_filenames = get_2_images(input_folder_path)
    dcm_file_1 = DcmFilter(dcm_filenames[0], sigma)
    dcm_file_2 = DcmFilter(dcm_filenames[1], sigma)

    ## Check ipp attribute and existance of output path
    if check_ipp(dcm_file_1, dcm_file_2):
        raise SameImagePositionPatient()
    os.makedirs(output_path, exist_ok=True)

    ## Create residues
    unfiltered_subtration = dcm_file_1.original - dcm_file_2.original
    filtered_subtration = dcm_file_1.filtered - dcm_file_2.filtered

    ## Save residue images
    write_image(unfiltered_subtration, f'{os.path.dirname(output_path)}/unfiltered_residue')
    write_image(filtered_subtration, f'{os.path.dirname(output_path)}/filtered_residue')
