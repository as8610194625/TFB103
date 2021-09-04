from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
def goo(x):
    gauth = GoogleAuth()           
    drive = GoogleDrive(gauth)  

    upload_file_list = [x]
    for upload_file in upload_file_list:
        gfile = drive.CreateFile({'parents': [{'id': '1ARhweqIAlUh69NXS_dS0fXTFC4XbljD3'}]})
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(upload_file)
        gfile.Upload() # Upload the file.
        