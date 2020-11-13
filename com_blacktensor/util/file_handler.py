import logging
import pandas as pd
import os

class FileHandler:
    
    @staticmethod
    def save_to_csv(savePath, saveData, columnsList, encodingStr):
        df = pd.DataFrame(saveData, columns=columnsList)
        df.to_csv(savePath, index=False, encoding=encodingStr)

    @staticmethod
    def load_to_csv(filePath, encodingStr):
        return pd.read_csv(filePath, encoding=encodingStr)
    
    @staticmethod
    def crete_folder(path):
        os.mkdir(path)