import csv
from collections import Counter
import matplotlib.pyplot as plt
while(1):
    print("#################################################################################################")
    print("輸入欲執行功能")
    select=input("1.鄉民活躍(發文、回文)分布圖.\n2.各版的活躍帳號 .\n3.輸入帳號及時間區間，查詢歷史動態.\n輸入代號:")


    if(select=="3"):
        id_num=input("輸入欲查詢id:")

        start_month = input("輸入欲查詢開始時間(月):")
        end_month = input("輸入欲查詢結束時間(月):")
        row=[]
        print("推文")
        with open('message.csv', newline='',encoding="utf-8") as csvfile:
            rows = csv.reader(csvfile)

            for row in rows:
                if(row[-1]==id_num):
                    #print(row[0],row[2],row[-2])
                    if(row[-3].find("推")+1):
                        #print(row[-3].strip().split(' ')[-1].split("/")[0])
                        if(int(row[-3].strip().split(' ')[-1].split("/")[0])>=int(start_month) and int(row[-3].strip().split(' ')[-1].split("/")[0])<=int(end_month)):
                            print("推文", row[2])
                    else:
                        #print(row[-3].strip().split(' ')[0].split("/")[1]+"/"+row[-3].strip().split(' ')[0].split("/")[2])
                        if(int(row[-3].strip().split(' ')[0].split("/")[1])>=int(start_month) and int(row[-3].strip().split(' ')[0].split("/")[1])<=int(end_month)):
                            print("推文",row[2])

        print("發文")
        month_list=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        with open('title.csv', newline='', encoding="utf-8") as csvfile:
            rows = csv.reader(csvfile)
            #print(month_list[int(start_month) - 1],month_list[int(end_month) - 1])
            for row in rows:
              #print(row[2].find(id_num))
              if (row[2].find(id_num)==0):
                    # print(row[0],row[2],row[-2])

                    for i in month_list[int(start_month)-1:int(end_month)-1] :
                        if(len(row[-1].split(' '))==6):
                            if(i==row[-1].split(' ')[1]):
                                #print (6,row[-1])
                                print("發文 標題:"+row[1]+" 內容:"+row[-2][0:20]+"...")
                        elif (len(row[-1].split(' ')) == 5):
                            if (i == row[-1].split(' ')[1]):
                                print("發文 標題:"+row[1]+" 內容:"+row[-2][0:20]+"...")
    if(select=="2"):
        kind=input('想要搜尋哪個板的資料:')
        print("推文最多(前三名)")
        with open('message.csv', newline='',encoding="utf-8") as csvfile:
            user_list=[]
            rows = csv.reader(csvfile)
            for row in rows:
                if(row[1]==kind):
                    user_list.append(row[-1].split("(")[0])
            word_counts = Counter(user_list)
            most_wr_count=[]
            most_wr_count=word_counts.most_common(3)
            print(most_wr_count[0][0],"次數:",most_wr_count[0][1])
            print(most_wr_count[1][0], "次數:", most_wr_count[1][1])
            print(most_wr_count[2][0], "次數:", most_wr_count[2][1])
        print("發文最多(前三名)")
        with open('title.csv', newline='', encoding="utf-8") as csvfile:
            user_list = []
            rows = csv.reader(csvfile)
            for row in rows:
                if (row[-3] == kind):
                    if(row[2].find(" ")>=0):
                        user_list.append(row[2].split("(")[0])
            word_counts = Counter(user_list)
            most_count = []
            most_count = word_counts.most_common(3)

            print(most_count[0][0], "次數:", most_count[0][1])
            print(most_count[1][0], "次數:", most_count[1][1])
            print(most_count[2][0], "次數:", most_count[2][1])
    if(select=="1"):
        m_joke=0
        m_HatePolitics=0
        m_MobileComm=0
        m_movie=0

        t_joke = 0
        t_HatePolitics = 0
        t_MobileComm = 0
        t_movie = 0
        with open('message.csv', newline='', encoding="utf-8") as csvfile:
            user_list = []
            rows = csv.reader(csvfile)
            for row in rows:
                if (row[1] =="movie"):
                    m_movie=m_movie+1
                if (row[1] =="HatePolitics"):
                    m_HatePolitics=m_HatePolitics+1
                if (row[1] =="MobileComm"):
                    m_MobileComm=m_MobileComm+1
                if (row[1] =="joke"):
                    m_joke=m_joke+1

        plt.subplot(2, 2, 1)
        plt.plot([0, 1], [0, 1])
        size = [m_joke,  m_HatePolitics, m_MobileComm, m_movie]
        labels = ['joke', 'HatePolitics', 'MobileComm', 'movie']
        plt.pie(size,labels=labels,autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('comment hot')


       # print("發文最多(前三名)")
        with open('title.csv', newline='', encoding="utf-8") as csvfile:
            user_list = []
            rows = csv.reader(csvfile)
            for row in rows:
                if (row[-3] =="movie"):
                    t_movie=t_movie+1
                if (row[-3] =="HatePolitics"):
                    t_HatePolitics=t_HatePolitics+1
                if (row[-3] =="MobileComm"):
                    t_MobileComm=t_MobileComm+1
                if (row[-3] =="joke"):
                    t_joke=t_joke+1
        plt.subplot(2, 2, 2)
        size = [t_joke, t_HatePolitics, t_MobileComm, t_movie]
        labels = ['joke', 'HatePolitics', 'MobileComm', 'movie']
        plt.pie(size, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('article  hot')

        plt.subplot(2, 2, 3)
        size = [m_joke + t_joke, m_HatePolitics + t_HatePolitics, m_MobileComm + t_MobileComm, m_movie + t_movie]
        labels = ['joke', 'HatePolitics', 'MobileComm', 'movie']
        plt.pie(size, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('number of article add message')

        plt.subplot(2, 2, 4)
        size = [m_joke/t_joke, m_HatePolitics/t_HatePolitics, m_MobileComm/t_MobileComm, m_movie/t_movie]
        labels = ['joke', 'HatePolitics', 'MobileComm', 'movie']
        plt.pie(size, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('how many comment per article')
        plt.show()
    print("#################################################################################################")








