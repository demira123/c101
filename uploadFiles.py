import dropbox
import os
from dropbox.files import WriteMode


class TransferData:

    def __init__(self, accessToken):
        self.accessToken=accessToken

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    aToken = "sl.BI_cGXRLaJ7YSIgnqvqCwdplzYTR3IES-XoWAQmLh939L9DC0Ao_Ba_hK0mR3KURO3teOW3piskfyghN4wrqH9CDvn42rQfYCrhQPuQchOy9ahuRbZ9MoC3V6CGSZf8trs6pJpRVeSJw"

    transferData = TransferData(aToken)

    src = input("Enter the folder name: ")
    destination = input("Enter the destination of the file: ")

    transferData.upload_file(src , destination)
    print("Files have been moved!!")


main()

# /newFolders
# /new/demo.txt