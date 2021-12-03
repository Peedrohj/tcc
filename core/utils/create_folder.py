import os
import csv


def create_folder(path: str):
    """
    @param path: string, name of folder to create

    Create folder if not exists
    """
    if not os.path.exists(path):
        os.makedirs(path)
