import cv2

#畫布截圖比對
def canvas_compare(sample, case,num):
    image1 = cv2.imread(sample)
    image2 = cv2.imread(case)
    allpoint = len(image1) * len(image1[0]) #此方式可取出所截的圖上點的總數，因兩圖大小一致，挑其中一張計算即可
    errorCount = 0
    for i in range(len(image1)): #這邊使用三維陣列去將兩圖每一個點抓出做比對
        for j in range(len(image1[0])):
            for k in range(len(image1[0][0])):
                if image1[i][j][k] != image2[i][j][k]: #若有不同處，記錯的變數從0開始往上加
                    errorCount += 1
                    break
    # print("全部的點: ", allpoint)
    # print("誤差值: ", errorCount)
    print("pen"+str(num)+"所有點的數量: ", allpoint, " / menu有誤差的點數量: ", errorCount, " / menu誤差率: ",float(errorCount/allpoint))
    if errorCount / allpoint < 0.01:  #預估錯誤比例不可多於10%，超過即回傳False
        #print("Pass")
        return True
    else:
        #print("Failed")
        return False


#畫布截圖比對,沒參數
def canvas_compare_2(sample, case):
    image1 = cv2.imread(sample)
    image2 = cv2.imread(case)
    allpoint = len(image1) * len(image1[0]) #此方式可取出所截的圖上點的總數，因兩圖大小一致，挑其中一張計算即可
    errorCount = 0
    for i in range(len(image1)): #這邊使用三維陣列去將兩圖每一個點抓出做比對
        for j in range(len(image1[0])):
            for k in range(len(image1[0][0])):
                if image1[i][j][k] != image2[i][j][k]: #若有不同處，記錯的變數從0開始往上加
                    errorCount += 1
                    break
    # print("全部的點: ", allpoint)
    # print("誤差值: ", errorCount)
    print("pen"+"所有點的數量: ", allpoint, " / menu有誤差的點數量: ", errorCount, " / menu誤差率: ",float(errorCount/allpoint))
    if errorCount / allpoint < 0.01:  #預估錯誤比例不可多於10%，超過即回傳False
        #print("Pass")
        return True
    else:
        #print("Failed")
        return False
