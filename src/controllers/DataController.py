from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes
    def validate_uploaded_file(self,file:UploadFile):
        allowed_extensions = {
            ".txt",
            ".pdf"
        }

        extension = os.path.splitext(file.filename)[1].lower()

        if extension not in allowed_extensions:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXCEEDED.value
    
        
        

        return True , ResponseSignal.FILE_VALIDATED_SUCCESS.value