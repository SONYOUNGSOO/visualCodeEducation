#pip install pylint 를 통해 파이썬 오류 표시줄을 업데이트 할수있다.
from tkinter import Tk,ttk,Label,Button,Text,END

stationfares = [
    {"station":"청량리" , "fare":1000},
    {"station":"성북" , "fare":1100},
    {"station":"의정부" , "fare":1200},
    {"station":"소요산" , "fare":1300}
]
selected_index = 0

def stationfares_selected(event):
    global selected_index
    for item in treeStationfares.selection():  #treeStationfares에서 selection 된것을 불러온다.
        selected_index = int(treeStationfares.item(item,"text"))
    stationfare = stationfares[selected_index]
    station= stationfare['station']
    fare= str(stationfare['fare'])
    text_Station.delete("1.0",END)#초기화
    text_Station.insert("end",station)
    text_Fare.delete("1.0",END)#초기화
    text_Fare.insert("end",fare)

def setTreeItems():
    # 기존에 treeStationfares에정보를 가져온 것이 있으면 모두 지워줌
    treeStationfares.delete(*treeStationfares.get_children())
    for idx, stationfare in enumerate(stationfares):
        station= stationfare['station']
        fare= stationfare['fare']
        treeStationfares.insert("",'end', iid=None, text=str(idx), values=[station,fare])
def insert_content():
    station= text_Station.get("1.0",END) #get 가져오는 함수
    fare= int(text_Fare.get("1.0",END))
    stationfare= {'station':station , 'fare':fare}
    stationfares.append(stationfare)
    setTreeItems()


def update_content():
    global selected_index
    station= text_Station.get("1.0",END) #get 가져오는 함수
    fare= int(text_Fare.get("1.0",END))
    selectedItem = stationfares[selected_index]
    selectedItem['station']= station
    selectedItem['fare']= fare
    setTreeItems()


def delete_content():
    global selected_index
    stationfares.pop(selected_index)
    setTreeItems()

window = Tk()  #c언어로 치면 다이얼 창
window.title("Station Fare Management")
window.geometry("600x600")
window.resizable(0,0)
title = "정류장 요금관리"
lbl_title = Label(window,text=title, font = ("돋움체",20))
lbl_title.pack(padx = 5, pady=15 ) 

#정류장 요금관리 표시 하는 treeStationfares
treeStationfares= ttk.Treeview(window)
treeStationfares["columns"]=("station","fare")
treeStationfares.column("#0", width=50)
treeStationfares.column("station", width=200)
treeStationfares.column("fare", width=150)
#treeStationfares에는 순번 ,정류장 , 요금표시
treeStationfares.heading("#0", text="순번")
treeStationfares.heading("station", text="정류장")
treeStationfares.heading("fare", text="요금")
treeStationfares.place(x=100,y=100,width=400,height=250) #.place 위치
setTreeItems()
#검색한 정류장 요금을 선택하면 stationfares_selected를 실행함
treeStationfares.bind("<<TreeviewSelect>>",stationfares_selected)
#버튼 생성 ( 함수 설정 포함)
btn_Insert= Button(window,text="Insert",command= insert_content, font=("돋움체",14))
btn_Insert.place (x=100,y=400,width=100,height=30)

btn_Update= Button(window,text="Update",command= update_content, font=("돋움체",14))
btn_Update.place (x=250,y=400,width=100,height=30)

btn_Delete= Button(window,text="Delete",command= delete_content, font=("돋움체",14))
btn_Delete.place (x=400,y=400,width=100,height=30)

labelStation= Label(window,text="정류장")
labelStation.place(x=100,y=450,width=50,height=25)
labelFare= Label(window,text="요금")
labelFare.place(x=100,y=500,width=50,height=25)
text_Station=Text(window,width=30,height=1)
text_Station.place(x=200,y=450)
text_Fare=Text(window,width=30,height=1)
text_Fare.place(x=200,y=500)



window.mainloop()