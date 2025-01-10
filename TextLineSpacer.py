# -*- coding = utf-8 -*-
import tkinter as tk
from tkinter import filedialog, messagebox

def add_blank_line_needed(text):
    lines = text.splitlines()   # 将文本按行拆分
    result = []
    is_previous_line_blank = False  # 标记前一行是否为空 

    for line in lines:
        line = line.strip() # 去掉每行的前后空格

        if line:    # 如果当前行不为空
            if not is_previous_line_blank:  # 如果前一行不是空行
                result.append('')   # 添加一个空行, 确保两个连续的换行符
                result.append(line) # 添加当前行到结果中
                is_previous_line_blank = False  # 标记当前行非空
                continue
            result.append(line) # 添加当前行到结果中
            is_previous_line_blank = False  # 标记当前行非空
        else: 
            #if not is_previous_line_blank:  # 如果前一行不是空行，则添加一个空行
            result.append(line) # 添加当前行到结果中
            is_previous_line_blank = True  # 标记当前行为空行

    return '\n'.join(result)    # 将所有行返回文本 

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_area.delete(1.0, tk.END)   # 清空文本框
            text_area.insert(tk.END, text)  # 将文件内容加载到文本框

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding="utf-8", newline='') as file:
            file.write(text_area.get(1.0, tk.END))   # 获取文本框的内容并保存到文件

def process_text():
    original_text = text_area.get(1.0, tk.END)  # 获取文本框中的文本
    processed_text = add_blank_line_needed(original_text) # 处理文本
    text_area.delete(1.0, tk.END)   # 清空文本框
    text_area.insert(tk.END, processed_text)    # 将处理后的文本插入回文本框
    print("Done")


# 创建主窗口
root = tk.Tk()
root.title("text process tool")

# 创建一个文本框, 允许多行输入和编辑
text_area = tk.Text(root, wrap=tk.WORD, width=80, height=20)
text_area.pack(pady=10)

# 创建按钮
frame = tk.Frame(root)
frame.pack()

open_button = tk.Button(frame, text="open file", command=open_file)
open_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(frame, text="save file", command=save_file)
save_button.pack(side=tk.LEFT, padx=5)

process_button = tk.Button(frame, text="process file", command=process_text)
process_button.pack(side=tk.LEFT, padx=5)

# 启动界面
root.mainloop()


