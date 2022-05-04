import time
import shutil
import caseTools.get_time

def copy_to_new_folder(caseID):
    src = './excelOutput/'+ caseID + '_output.xlsx'    # 欲複製的檔案
    dst = './excelUpload/'+ caseID +'_'+ caseTools.get_time.now()+'_output.xlsx'  # 複製到excelUpload並把檔名加入時間
    shutil.copyfile(src,dst) 

