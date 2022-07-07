from tkinter import *


root = Tk()
root.title("로그인 및 회원가입")

def signIn():
    f = open("user_list.txt", 'r', encoding="UTF-8")
    lines = f.readlines()
    f.close

    id = sign_id_Entry.get()
    passwd = sign_passwd_Entry.get()
    passwd_re = sign_passwd_re_Entry.get()


    id_lst = lines[0::2]


    if id+"\n" in id_lst:
        sign_in_result.config(text="가입 결과 : 이미 존재하는 ID입니다.")
        sign_id_Entry.delete(0, END)

    elif passwd != passwd_re:
        sign_in_result.config(text="가입 결과 : 패스워드 재입력을 확인해주세요")

    else:
        sign_in_result.config(text="가입 결과 : 가입 완료")

        # with을 사용함으로써, f.close를 통해 파일을 닫지 않아도 됨
        with open("user_list.txt", "a") as f:
            f.write(id+"\n")
            f.write(passwd+"\n")

        sign_passwd_Entry.delete(0, END)
        sign_passwd_re_Entry.delete(0, END)

        sign_id_Entry.delete(0, END)
        login_id_Entry.delete(0, END)
        login_id_Entry.insert(0, id)
        

def logIn():
    f = open("user_list.txt", 'r', encoding="UTF-8")
    lines = f.readlines()
    f.close
    
    id = login_id_Entry.get()
    passwd = login_passwd_Entry.get()

    id_lst = lines[0::2]
    passwd_lst = lines[1::2]

    if id+"\n" not in id_lst:
        login_result.config(text="로그인 결과 : 실패 - 아이디가 존재하지 않습니다.")
    
    elif passwd+"\n" != passwd_lst[id_lst.index(id+"\n")]:
        login_result.config(text="로그인 결과 : 실패 - 비밀번호를 확인하세요.")

    else:
        login_result.config(text="로그인 결과 : 성공 - {%s}님 안녕하세요" % id)

gui_Frame = Frame(root, width=100).grid(row=0,column=0)


sign_in_Label = Label(gui_Frame, text="회원가입 창").grid(row=0, column=0, pady=2)

sign_id = Label(gui_Frame, text="사용할 아이디").grid(row=1, column=0)
sign_id_Entry = Entry(gui_Frame, width=25)
sign_id_Entry.grid(row=1, column=1, columnspan=2, sticky=E+W, pady=2)

sign_passwd = Label(gui_Frame, text="사용할 패스워드").grid(row=2, column=0)
sign_passwd_Entry = Entry(gui_Frame, width=25, show="*")
sign_passwd_Entry.grid(row=2, column=1, columnspan=2, sticky=E+W, pady=2)

sign_passwd_re = Label(gui_Frame, text="패스워드 재입력").grid(row=3, column=0)
sign_passwd_re_Entry = Entry(gui_Frame, width=25, show="*")
sign_passwd_re_Entry.grid(row=3, column=1, columnspan=2, sticky=E+W, pady=2)

sign_in_Button = Button(gui_Frame, text="가입하기", width=9, command=signIn).grid(row=4, column=1)
cancel_Button = Button(gui_Frame, text="취소", width=9, command=quit).grid(row=4, column=2)

sign_in_result = Label(text="가입결과 = ")
sign_in_result.grid(row=5, pady=2, columnspan=3, sticky=W)



login_Label = Label(gui_Frame, text="로그인 창").grid(row=0, column=3)

login_id = Label(gui_Frame, text="로그인 아이디").grid(row=1, column=3, pady=2)
login_id_Entry = Entry(gui_Frame, width=25)
login_id_Entry.grid(row=1, column=4, columnspan=2, sticky=E+W, pady=2)

login_passwd = Label(gui_Frame, text="로그인 패스워드").grid(row=2, column=3, pady=2)
login_passwd_Entry = Entry(gui_Frame, width=25, show="*")
login_passwd_Entry.grid(row=2, column=4, columnspan=2, sticky=E+W, pady=2)


login_Button = Button(gui_Frame, text="로그인 하기", width=9, command=logIn).grid(row=4, column=4, pady=2)
cancel_Button2 = Button(gui_Frame, text="취소", width=9, command=quit).grid(row=4, column=5, pady=2)

login_result = Label(gui_Frame, text="로그인 결과 = ")
login_result.grid(row=5, column=3, pady=2, columnspan=3, sticky=W)


root.mainloop()