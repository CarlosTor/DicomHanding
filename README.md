# DicomHanding

## Introduction
The dicomhanding package contains a several classes for reading and applying some simple processing and writing Dicom images.
The main function computes the residue of two different images before and after being filtered by a Gaussian filter.

## Requirements
The dicomhandling package requires Python 3.8 and pip to install.
It depends on a list of packages sucha as numpy, pydicom or scipy, which will be installed as part of the installation process (requirements).

## Installation

To install the package, first download the DicomHanding folder tree from the GitHub https://github.com/CarlosTor/DicomHanding.git repository.
At a command prompt in the top-level `DicomHandling` folder, run the command
```
pip install -r requirements/requirements.txt
```
This will install the rawqv package and the rawqv_reader application.

## (Optional) Docker

If there is a preference of using a docker container, install docker and run the following command
```
docker build -t dicom-handling-i -f docker_env/Dockerfile .
```
to build the container (once) and then use the next line
```
docker run --net host --ipc host --name $USER-dicom-handling --rm -it dicom-handling-i

```
to launch docker.

## The main application

Once all Python packages are installed, the usage follows this rule
```
usage: python3 -m dicomhandling <input_folder> [<output_folder>]
```
