import time

def now():
    local_time = time.localtime() #抓時間，他會計算從1970/1/1開始到現在經過的秒數
    result = time.strftime("%Y-%m-%d %H-%M-%S", local_time) #這行能將上面抓到的秒數轉換成時間顯示 ex 2022-01-20 09-04-23
    return result