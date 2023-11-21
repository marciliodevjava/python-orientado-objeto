
from datetime import datetime
class Data:

    def __init__(self, data):
        self.data = self.formatada(data)

    def formatada(self, data:str):
        data_objeto = datetime.strptime(data, "%Y-%m-%d")
        return data_objeto.strftime("%Y-%m-%d")
