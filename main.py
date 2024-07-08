import os
from ftplib import FTP
from dotenv import load_dotenv
import logging

load_dotenv()

import sys


def upload_file_ftp() -> bool:
    ftp = FTP()
    ftp.connect(os.getenv("host"), 21)
    # Enable active mode
    ftp.set_pasv(False)
    # Login
    ftp.login(os.getenv("user"), os.getenv("password"))
    response = ftp.voidcmd("NOOP")
    if response.startswith("200"):
        print("Connection is valid")
        # uploading files
        demo_file = open("files/AMZ SPO050 Jan 17_erp.xlsx", "rb")
        upload = ftp.storbinary("STOR AMZ+SPO050+Jan+17_erp.xlsx", demo_file)
        print(upload)
        demo_file.close()
        ftp.quit()
        return True
    else:
        print("Connection failed")
        ftp.quit()
        return False


upload_file_ftp()
