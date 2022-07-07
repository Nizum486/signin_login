from tkinter import *


root = Tk()
root.title("로그인 및 회원가입")

def signIn():
    # open을 통해 txt 파일을 'r' 읽기 모드로 열기
    f = open("user_list.txt", 'r', encoding="UTF-8")
    # readlines()를 통해 파일의 모든 내용을 list로 받아옴 -> lines에 저장
    lines = f.readlines()
    # open뒤엔 꼭! close가 붙는다.
    f.close

    # 아이디, 비밀번호, 재입력 입력 부분(Enrty)에 적힌 글자를 get으로 받아온다.
    id = sign_id_Entry.get()
    passwd = sign_passwd_Entry.get()
    passwd_re = sign_passwd_re_Entry.get()

    # 파일에서 받아온 lines를 보면 아이디가 0, 2, 4, ... 짝수 줄에 저장되어 있기 때문에
    # [0부터::(전체) 2칸씩] 받아오면 짝수줄만 받아오게 되고, 이는 id 리스트이다.
    id_lst = lines[0::2]


    # readlines를 통해 받아온 리스트의 원소 하나하나들을 살펴보면
    # aa\n, bb\n, cc\n 이런식으로 뒤에 \n이 붙어있다. 이때문에 우리도 원소를 찾을때
    # \n을 붙여야만 원하는 원소를 찾을 수 있다.

    # id리스트에 id가 없을 시
    if id+"\n" in id_lst:
        # sign_in_result라는 Label의 text값을 아래와 같이 변경
        sign_in_result.config(text="가입 결과 : 이미 존재하는 ID입니다.")
        # sgin_id_Enrty에 적힌 값을 모두 제거 (0 부터 END 까지)
        sign_id_Entry.delete(0, END)

    # 패스워드와 패스워드 재입력 값이 다를 시
    elif passwd != passwd_re:
        # sign_in_result라는 Label의 text값을 아래와 같이 변경
        sign_in_result.config(text="가입 결과 : 패스워드 재입력을 확인해주세요")

    # 위 두 사항에 위배되지 않을 시
    else:
        # sign_in_result라는 Label의 text값을 아래와 같이 변경
        sign_in_result.config(text="가입 결과 : 가입 완료")

        # with을 사용함으로써, f.close를 통해 파일을 닫지 않아도 됨
        # "a" 모드로 열 시, 파일에 추가. "w" 모드는 전부 삭제하고 재작성
        with open("user_list.txt", "a") as f:
            # id와 \n을 추가
            f.write(id+"\n")
            # passwd와 \n을 추가
            f.write(passwd+"\n")

        # 편의를 위한 입력값 삭제 및 전달
        sign_passwd_Entry.delete(0, END)
        sign_passwd_re_Entry.delete(0, END)

        sign_id_Entry.delete(0, END)
        login_id_Entry.delete(0, END)
        login_id_Entry.insert(0, id)
        

def logIn():
    # 파일을 읽어오는 방식은 위와 동일
    f = open("user_list.txt", 'r', encoding="UTF-8")
    lines = f.readlines()
    f.close
    
    # id와 passwd를 읽어오는 방식도 위와 동일
    id = login_id_Entry.get()
    passwd = login_passwd_Entry.get()

    # 아이디는 짝수번째, 비밀번호는 홀수번째에 저장되어 있으므로
    # 짝수 리스트는 id_lst, 홀수 리스트는 passwd_lst로 둔다.
    id_lst = lines[0::2]
    passwd_lst = lines[1::2]

    # 아이디가 아이디 리스트에 없을 시 (not in)
    if id+"\n" not in id_lst:
        login_result.config(text="로그인 결과 : 실패 - 아이디가 존재하지 않습니다.")
    
    # 아이디와 패스워드는 쌍으로 존재하기 때문에
    # id_lst에서의 인덱스와 passwd_lst에서의 인덱스는 동일하다.
    elif passwd+"\n" != passwd_lst[id_lst.index(id+"\n")]:
        login_result.config(text="로그인 결과 : 실패 - 비밀번호를 확인하세요.")

    else:
        # 문자열 포매팅 {%s} % 문자열
        login_result.config(text="로그인 결과 : 성공 - {%s}님 안녕하세요" % id)


# grid로 위치 배치는 사진 참조
gui_Frame = Frame(root, width=100).grid(row=0,column=0)


sign_in_Label = Label(gui_Frame, text="회원가입 창").grid(row=0, column=0, pady=2)

sign_id = Label(gui_Frame, text="사용할 아이디").grid(row=1, column=0)
sign_id_Entry = Entry(gui_Frame, width=25)
# columnspan을 통해 같은 행에서의 병합(2칸), sticky를 통해 동, 서쪽으로 확장
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