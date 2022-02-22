
class IncorrectNumberOfImages(Exception):

    def __init__(self):
        self.message = "Incorrect number of images. Aborting."

    def __str__(self):
        return self.message


class SameImagePositionPatient(Exception):

    def __init__(self):
        self.message = "The DICOM files appear to be the same. Aborting."

    def __str__(self):
        return self.message


class WrongAngle(Exception):

    def __init__(self):
        self.message = "Angle must be a multiple of 90. Aborting."

    def __str__(self):
        return self.message
