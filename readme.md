## 简介:   
这是一个基于 ***Tkinter*** 的简单文本处理工具, 具有以下功能:  
> 1. *打开文件*: 用户可以从文件系统中选择一个 ***.txt*** 文件, 并将文件内容加载到文本框中进行编辑;  
> 2. *保存文件*: 用户可以将编辑后的文本保存为 ***.txt*** 文件;      
> 3. *文本处理*：对文本进行处理，确保每一行非空行之间有一个空行，空行保持原样。   

具体的文本处理逻辑是通过 ***add_blank_line_needed*** 函数实现的。该函数会在每两行非空文本之间插入一个空行，而空行则保持不变。

## 功能说明:  
>*打开文件* (_open_file_)：通过文件对话框选择并读取文本文件;  
>*保存文件* (_save_file_)：通过文件对话框保存文本框中的内容为 .txt 文件;  
>*文本处理* (_process_text_)：获取文本框中的文本，调用 ***add_blank_line_needed*** 进行处理，再将结果展示回文本框;  

## 注意事项:
> **文件编码问题:**  
>  - 本程序假设文件是以 ***UTF-8*** 编码保存的，因此在打开文件和保存文件时，编码均使用 ***utf-8***。  
>  - 如果要处理其他编码的文件，可能需要进一步调整 ***open*** 和 ***save*** 函数中的 ***encoding*** 参数。   

> **空行的处理:**
> - 在处理文本时，每两个连续的非空行之间将会插入一个空行。如果前一行已经是空行，则不会重复插入空行。空行本身保持不变。
> - 这对于保持文本格式尤其重要，尤其是处理如诗歌、日志等文本内容时，空行有时是非常重要的。

> **文本框的使用：**
> - ***Text*** 组件是用来显示和编辑多行文本的。使用时要注意，操作 ***Text*** 组件的内容时应使用 ***get*** 和 ***insert*** 方法，而要清空时可以使用 ***delete*** 方法。

> **文件对话框：**
> - 使用 ***filedialog.askopenfilename*** 来打开文件选择对话框，允许用户选择文件。
> - 使用 ***filedialog.asksaveasfilename*** 来打开保存文件对话框，允许用户选择保存路径和文件名。


这个简单的脚本一开始其实是为了处理txt格式下载下来的小说的,  
个人喜欢用pdf阅读器打开txt文本来看,但行之间没有分割就很费眼,  
因此写了个简单的脚本来处理txt文档,就是示例文件夹里的那个样子