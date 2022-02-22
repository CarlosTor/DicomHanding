import os

import typer

import dicomhandling


def main():
    '''
    This script is a sort of test that helped to build each step of this package.
    '''


    ## Parameters
    input_path1 = 'data/IM-0001-0035-0001.dcm'
    input_path2 = 'data/IM-0001-0086-0001.dcm'
    sigma = 3
    angle = 180

    ## Tasks
    dcm_filter = dicomhandling.DcmFilter(input_path1, sigma)
    dcm_rotate = dicomhandling.DcmRotate(input_path2, angle)

    same_ipp = dicomhandling.check_ipp(dcm_filter, dcm_rotate)

    dicomhandling.write_image(dcm_filter.filtered, 'residues/original1')
    dicomhandling.write_image(dcm_rotate.rotated, 'residues/original2')


if __name__ == '__main__':
    main()
