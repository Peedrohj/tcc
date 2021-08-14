# Utils
import sys, os

# Config
from config import Config


def download_file(experiment_id):
    url = "https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list={}&format=fasta".format(
        experiment_id)

    try:
        os.system(
            "fasterq-dump {} -O data/genetic_data/{}".format(experiment_id, experiment_id))
    except Exception as error:
        print('Error downloading file for: ', experiment_id, "\n", error)


def main():
    experiment_counter = 0
    download_counter = 0

    for experiment_id in Config.SRA_ID_LIST:
        download_counter += 1

        print("Downloading file: {}/{}".format(download_counter,
              len(Config.SRA_ID_LIST)), end="\r")
        download_file(experiment_id)


if __name__ == "__main__":
    main()
