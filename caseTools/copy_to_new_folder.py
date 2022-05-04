import os
import shutil

def copy_to_new_folder(caseID):
    src = './excelOutput/'+ caseID + '_output.xlsx'    # 欲複製的檔案
    dst = './excelUpload/'+ caseID + '_output.xlsx'  # 存檔的位置與檔案名稱
    shutil.copyfile(src,dst) 