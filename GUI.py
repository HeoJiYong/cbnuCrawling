'''
사실상 메인 모듈
새로운 창으로 공지사항 보여준다.
'''

'''
tkinter 모듈로 GUI 구현
tkinter.messagebox.showinfo("제목","내용")

win = Tk()  //기본 영역 설정 win은 Tk영역이다~
win.title("제목~")    //기본 영역의 제목을 설정
win.geometry("400x600+100+200") //400x600 크기를, x축 100 , y축 200 만큼 떨어진곳에
frm = Frame(win)    //설정된 기본영역을 Frame으로 씌운걸 frm이라 칭한다
frm.pack()          //frm을 감싼다(패키징 한다?)
win.mainloop()      //창을 시작한다.
win.destroy()       //창을 종료하고
win.quit()          //창을 닫는다.

==GUI==
pyside
pyqt5
tkinter
'''

from tkinter import *
import tkinter.messagebox
#import yout
import noticeTitle
import urlCrawling
import webbrowser

import threading
def Msgbox1():
    tkinter.messagebox.showinfo("메세지 상자","정보 알려주는 용도의\n메세지 상자 \n(파란 느낌표 아이콘)")
   # t = threading.Thread(target=Msgbox1())i
  #  t.a

def MyMsg(title,msg):
    tkinter.messagebox.showinfo(title,msg)
    #tkinter.messagebox.showinfo("메세지 상자","정보 알려주는 용도의\n메세지 상자 \n(파란 느낌표 아이콘)")
   # t = threading.Thread(target=Msgbox1())
  #  t.a

def close_win():
    win.destroy()
    win.quit()

#기본영역
win  = Tk()

#프레임 영역
base_frm = Frame(win)
base_frm.pack()
win.title("==공지사항 파싱결과==")
win.geometry("+10+10")
frm = Frame(win)
frm.pack()

def main():
    notice_result = noticeTitle.GetNotice()
    url_result = urlCrawling.GetUrl()
    content_result = ""
    print("==content result==")
    NOTICE = notice_result.split('\n')
    URL = url_result.split('\n')
    STR = "--------------------------------------------------------------------------------------------------"
    for a in range(0,25):
        print(NOTICE[a])
        print(URL[a])
        #content_result = content_result +notice_result[a] + url_result[a]
        #content_result = content_result + NOTICE[a] + "\n" + URL[a] + "\n"
        content_result = content_result + NOTICE[a] +"\n"+ STR + "\n"
    print("==content result==")
    #notice = Label(frm,text = notice_result+url_result)
    notice = Label(frm,text=content_result)
    notice.pack()
    win.mainloop()

    #Msgbox1()
   # MyMsg("==공지사항 파싱결과==",msg)
    #print(msg)

if __name__ == "__main__":
    main()
