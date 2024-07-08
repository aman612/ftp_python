from ftplib import FTP
import sys


def upload_file_ftp(
    path: str, fileName: str, host: str, user: str, pwd: str, source: str
) -> bool:
    # ftp = FTP()
    # '' is the source IP address and 0 is the source port.
    # The 0 value for the source port means that the operating system will automatically choose an available port for the FTP connection.
    source = (f"{source}", 0)
    destination = host
    port = 21
    with FTP(destination, source_address=source, port=port) as ftp:
        # ftp.connect(host, 21)
        # Enable active mode
        ftp.set_pasv(False)
        # Login
        ftp.login(user, pwd)
        response = ftp.voidcmd("NOOP")
        if response.startswith("200"):
            print("Connection is valid")
            # uploading files
            file = open(path, "rb")
            upload = ftp.storbinary("STOR " + fileName, file)
            print(upload)
            file.close()
            ftp.quit()
            return True
        else:
            print("Connection failed")
            ftp.quit()
            return False


dataArguments = sys.argv
path = dataArguments[1]
fileName = dataArguments[2]
host = dataArguments[3]
user = dataArguments[4]
pwd = dataArguments[5]
source = dataArguments[6]

upload_file_ftp(path, fileName, host, user, pwd, source)
