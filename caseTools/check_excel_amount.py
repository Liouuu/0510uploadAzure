import os
def maintain_20(excelPath): 
    allFilesList=os.listdir(excelPath)
    #依照文件最後創建時間重新排進list
    allFilesList=sorted(allFilesList, key=lambda x:os.path.getctime(os.path.join(excelPath, x))) 
    for i in range(len(allFilesList)): 
        if len(allFilesList) > 20:
            os.remove(excelPath + allFilesList[0])    #檔案只保留20個，超過則從舊的開始刪除
            allFilesList=allFilesList = os.listdir(excelPath)  
            allFilesList=allFilesList
            print("經刪除")
            i+1        
        else:
            pass
            # print("未經刪除")

def maintain_1(excelPath): 
    allFilesList=os.listdir(excelPath)
    #依照文件最後創建時間重新排進list
    allFilesList=sorted(allFilesList, key=lambda x:os.path.getctime(os.path.join(excelPath, x))) 
    for i in range(len(allFilesList)): 
        if len(allFilesList) > 1:
            os.remove(excelPath + allFilesList[0])    #檔案只保留1個，超過則從舊的開始刪除
            allFilesList=allFilesList = os.listdir(excelPath)  
            allFilesList=allFilesList
            print("經刪除")
            i+1        
        else:
            pass
            # print("未經刪除")

#     allFilesList.sort(key=os.path.getctime)  



        




