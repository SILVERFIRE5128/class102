import cv2
import dropbox
import time
import random

start_time= time.time()

def take_snapshot():
    number= random.randint(0,100)
    videocaptureobject= cv2.VideoCapture(0)
    result= True
    while(result):
        ret,frame= videocaptureobject.read()
        img_name= "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time= time.time
        result= False
    return img_name
    print("snapshot taken") 
    videocaptureobjct.release()
    cv2.destroyAllWindows()
    
def upload_file(img_name):
    accesstoken= "sl.BCMrQUCr0ONKCfScB4Xft3k2cYpZ2jIRPo8A9HdcxobXmaJefhDxWkZwo2THfZbzaCegF4IjZ-ho6CIi9rxn0HlU438GdbHka7ncUYtvP4yKbVjD6FuaGGehE3zUUv8hJDd6unxy"
    file= img_name
    file_from= file
    files_to= "c101/newfolder1"+(img_name)
    dbx= dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name= take_snapshot() 
            upload_file(name)

main()