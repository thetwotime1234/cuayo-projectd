import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
import io

# 사용 중인 사진 링크를 여기에 넣으세요!
image_url = "https://i.namu.wiki/i/Ob0--Jok1pkNtNu46VjPmTZWbmaql5Xf0pexZ5RBz3B5Nlj8z_xqYSyMqw70Ad5mEYa_i1GHcHda5pbilvBNOA.webp"

def on_button_clicked():
    password = input_entry.get()
    if password == "스핔이 네르지 마세요":
        result_label.config(text='네르는 이렇게 폭력적인 역할이 아니란 말이에요!!!')
    elif password == "쪼아요":
        result_label.config(text="쪼아요 쪼아요 물걸레질 쪼아요")
    elif password == "호박이 쪼아요":
        result_label.config(text="쪼아요 쪼아요 호박이 쪼아요!")
    elif password == "숨박꼭질 쪼아요":
        result_label.config(text="쪼아요 쪼아요 숨박꼭질 쪼아요!")
    elif password == '호박이...':
        result_label.config(text="호, 호박이.... ")
    elif password == '흐에엥':
        result_label.config(text="에우욹..")
    else:
        result_label.config(text="스핔이 열심히 했는데....")

# 프로그램 창 설정
root = tk.Tk()
root.title("스핔이 프로그램")
root.geometry("400x500")

# 인터넷에서 사진 가져오기
try:
    req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as u:
        raw_data = u.read()
    img = Image.open(io.BytesIO(raw_data))
    img = img.resize((250, 250))
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo).pack(pady=10)
except Exception as e:
    tk.Label(root, text="사진을 못 불러왔어요 ㅠㅠ", fg="red").pack(pady=10)
    print(f"에러 내용: {e}")

# 글자와 입력창
tk.Label(root, text="무슨 말을 해줄까?", font=("Arial", 11)).pack()
input_entry = tk.Entry(root, width=30)
input_entry.pack(pady=10)

# 버튼
tk.Button(root, text="말해주기", command=on_button_clicked, bg="skyblue").pack()

# 결과 대사 출력
result_label = tk.Label(root, text="", font=("Arial", 10, "bold"), fg="blue", wraplength=350)
result_label.pack(pady=20)

root.mainloop()
