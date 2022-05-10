import time
import shutil
import caseTools.get_time

#得先手動創一個excelUpload
def copy_to_new_folder(caseID):
    src = './excelOutput/'+ caseID + '_output.xlsx'   #欲複製的檔案
    dst = './excelUpload/'+ caseID +'_'+ caseTools.get_time.now()+'_output.xlsx'  
    shutil.copyfile(src,dst) 

