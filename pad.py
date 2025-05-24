import tkinter as tk
from tkinter import filedialog, messagebox

# 텍스트 패드 클래스 정의
class SimpleTextPad:
    def __init__(self, root):
        self.root = root
        self.root.title("간단한 텍스트 패드")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # 텍스트 영역
        self.text_area = tk.Text(self.root, wrap="word", font=("Arial", 12))
        self.text_area.pack(padx=10, pady=10, fill="both", expand=True)

        # 버튼 프레임
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        # 둥근 버튼 스타일을 위한 공통 옵션
        button_style = {
            "font": ("Arial", 10, "bold"),
            "bg": "#4CAF50",
            "fg": "white",
            "activebackground": "#45a049",
            "relief": "flat",
            "bd": 0,
            "width": 10,
            "height": 2,
        }

        # 저장 버튼
        self.save_button = tk.Button(
            self.button_frame, text="💾 저장", command=self.save_file, **button_style
        )
        self.save_button.pack(side="left", padx=10)

        # 불러오기 버튼
        self.open_button = tk.Button(
            self.button_frame, text="📂 불러오기", command=self.open_file, **button_style
        )
        self.open_button.pack(side="left", padx=10)

    # 파일 저장
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("저장 완료", "파일이 저장되었습니다.")
            except Exception as e:
                messagebox.showerror("오류", f"저장 실패: {e}")

    # 파일 열기
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("오류", f"불러오기 실패: {e}")


# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTextPad(root)
    root.mainloop()
