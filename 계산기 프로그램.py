from tkinter import *

window = Tk()
window.title("My Calculator")
display = Entry(window, width = 33, bg = "yellow")
display.grid(row = 0, column = 0, columnspan = 5)

button_list = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ',
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', ' ']

def click(key): # 엔트리 위젯의 끝에 key 추가 , = 를 누르면 결과값 산출
    if(key == "="):
        result = eval(display.get())
        s = str(result) # s에 결과값을 화면에 출력
        display.insert(END, "=" + s) # = 결과값으로 출력한 뒤 END
    else:
        display.insert(END, key)

row_index = 1
col_index = 0
for button_text in button_list:
    def process(t = button_text): # 클릭 함수 정의
        click(t)
    Button(window, text = button_text, width = 5, command = process).grid(row = row_index, column = col_index)
    col_index += 1
    if (col_index > 4):
        row_index += 1
        col_index = 0
