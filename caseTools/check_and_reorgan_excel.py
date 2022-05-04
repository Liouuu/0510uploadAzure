import os
excelPath = "./excelOutput"
def checkAndReorganExcel(): 
    allFilesList=os.listdir(excelPath)
    #依照文件最後創建時間重新排進list(最新排第一)
    allFilesList=sorted(allFilesList, key=lambda x:os.path.getctime(os.path.join(excelPath, x))) 
    for i in range(len(allFilesList)): 
        if len(allFilesList) > 20:
            # print("allfilesnow::::::::::::::::::",allFilesList)
            os.remove(excelPath +"/"+ allFilesList[-1])  
            allFilesList=allFilesList = os.listdir(excelPath)  
            allFilesList=allFilesList
            print("經刪除")
            i+1        
        else:
            pass
            # print("未經刪除")



        




