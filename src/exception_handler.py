import sys
from logger import logging

def errorMessageDetails(error, errorDetails:sys):
    _, _, exception = errorDetails.exc_info()
    fileName = exception.tb_frame.f_code.co_filename
    lineNumber = exception.tb_lineno
    errorMessage = f"| ERROR | File: {fileName} | Line Number: {lineNumber} |  Error: {error}"
    
    return errorMessage

class CustomException(Exception):
    def __init__(self, errorMessage, errorDetail:sys):
        super().__init__(errorMessage)
        self.errorMessage = errorMessageDetails(errorMessage, errorDetail)

    def __str__(self):
        return self.errorMessage
            