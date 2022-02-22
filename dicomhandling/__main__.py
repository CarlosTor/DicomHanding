import sys

import dicomhandling


def main(input_folder_path: str, output_path: str = 'residues/'):
    '''
    The command generates the residue of a subtraction given a folder containing two Dicom files.
    Two jpg files will be generated: residue before and after image filtering.

    :param input_folder_path: Path to the input folder with .dcm files.
    :param output_path: Path to the output folder.
    '''

    dicomhandling.compute_residue(input_folder_path, output_path, 3)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise 'Missing arguments.'

    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])
