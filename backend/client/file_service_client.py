from backend.config import FILE_SERVICE
from backend.client.__base__ import ServiceClient


class FileServiceClient(ServiceClient):
    def __init__(self):
        super().__init__(FILE_SERVICE)

    def get_file_by_id(self, file_id):
        return self.get(f"files/{file_id}")
    
    