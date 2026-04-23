## markdown 基础入门

### 1、标题

几个 # 表示几级标题语法，# 与标题之间用空格隔开。  

如：# title —— 一级标题

![](./images/2.png)

### 2、段落

不要用空格（spaces）或制表符（ tabs）缩进段落。

![image-20250930093736241](./images/3.png)

### 3、换行

在一行的末尾添加两个或多个空格，然后按回车键,即可创建一个换行(`<br>`)。

### 4、强调

**粗体**（Bold）

要加粗文本，请在单词或短语的前后各添加两个星号（asterisks）或下划线（underscores）。

![image-20250930093954280](./images/4.png)

**斜体（Italic）**

要用斜体显示文本，请在单词或短语前后添加一个星号（asterisk）或下划线（underscore）。要斜体突出单词的中间部分，请在字母前后各添加一个星号，中间不要带空格。

![image-20250930094507575](./images/5.png)

**粗体（Bold）和斜体（Italic）**

要同时用粗体和斜体突出显示文本，请在单词或短语的前后各添加三个星号或下划线。

![image-20250930094636415](./images/6.png)

### 5、引用

要创建块引用，请在段落前添加一个 `>` 符号。如下：

>```text
>> Dorothy followed her through many of the beautiful rooms in her castle.
>```

**多个段落的块引用**

块引用可以包含多个段落。为段落之间的空白行添加一个 `>` 符号。如下：

```text
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

**嵌套块引用**

块引用可以嵌套。在要嵌套的段落前添加一个 `>>` 符号。如下：  

```text
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

> 11
>
> > 22
>
> 33

**带有其他元素的块引用**

块引用可以包含其他 Markdown 格式的元素。并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。

```text
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.
```

> #### The quarterly results look great!
>
> - Revenue was off the chart.
>
> - Profits were higher than ever.  
> - *Everything* going according to **plan**.

### 6、列表

**有序列表**

要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。  

![image-20250930100026026](./images/7.png)

1. first item
2. second item

**无序列表**

要创建无序列表，请在每个列表项前面添加破折号 (-)、星号 (*) 或加号 (+) 。缩进一个或多个列表项可创建嵌套列表。

![image-20250930100257205](./images/8.png)

**在列表中嵌套其他元素**

要在保留列表连续性的同时在列表中添加另一种元素，请将该元素缩进四个空格或一个制表符，如下例所示：

```text
*   This is the first list item.
*   Here's the second list item.

    I need to add another paragraph below the second list item.

*   And here's the third list item.
```

* 1

  second item.

* 3

**引用块**

```text
*   This is the first list item.
*   Here's the second list item.

    > A blockquote would look great below the second list item.

-   And here's the third list item.
```

* This is the first list item.

  > A blockquote would look great below the second list item.

- And here's the third list item.

### 7、代码语法

要将单词或短语表示为代码，请将其包裹在反引号 (` 代码`) 中。反引号位置位于英文状态下，和波浪线同一个键位。

| Markdown语法                          | HTML                                             | 预览效果                            |
| ------------------------------------- | ------------------------------------------------ | :---------------------------------- |
| `At the command prompt, type `nano`.` | `At the command prompt, type <code>nano</code>.` | At the command prompt, type `nano`. |

**代码块**

要创建代码块，创建一个引用块，将 text 调整为需要的代码语言或者直接创建一个代码块 ` ctrl+shift+k` 后直接选择语言。

> 公式块 ` ctrl+shift+m`

```python
import numpy
import math

j = 0
for i in range(1,8,1):
    i += 1
    print("i")
while(j <= 100):
    j += 1
    
print("hello world!{}".format(j))
```

```c
#include <stdio.h>

int main()
{
    printf("hello world!");
    return 0;
}
```

### 8、分割线

要创建分隔线，请在单独一行上使用三个或多个星号 (`***`)、破折号 (`---`) 或下划线 (`___`) ，并且不能包含其他内容。

![image-20250930101503040](data:image/png;base64,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)

### 9、链接

**链接**

链接文本放在中括号内，链接地址放在后面的括号中，链接title可选。

超链接Markdown语法代码：`[超链接显示名](超链接地址 "超链接title")`

对应的HTML代码：`<a href="超链接地址" title="超链接title">超链接显示名</a>`

这是一个链接 [Markdown教程](https://markdown.com.cn)。

```text
这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。
```

这是一个链接 [Markdown教程](https://markdown.com.cn "仅供学习使用")。

**网址和Email地址**

使用尖括号可以很方便地把URL或者email地址变成可点击的链接。

```text
<https://markdown.com.cn>
<fake@example.com>
```

<https://markdown.com.cn>

<weic@gmail.com>

**带格式化的链接**

强调链接, 在链接语法前后增加星号。 要将链接表示为代码，请在方括号中添加反引号。

```text
I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](#code).
```

**Tips:**

不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用%20代替空格。

| ✅ Do this                                           | ❌ Don't do this                                 |
| --------------------------------------------------- | ----------------------------------------------- |
| `[link](https://www.example.com/my%20great%20page)` | `[link](https://www.example.com/my great page)` |

### 10、图片

**添加图片**

要添加图像，请使用感叹号 (`!`), 然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

插入图片Markdown语法代码：`![图片alt](图片链接 "图片title")`。

对应的HTML代码：`<img src="图片链接" alt="图片alt" title="图片title">`

**链接图片**

```text
[![沙漠中的岩石图片](/assets/img/shiprock.jpg "Shiprock")](https://markdown.com.cn)
```

试着点击图片试一试（链接点击方式：Ctrl + 鼠标左键）。

[![示例图片](./images/9.png "角色-阿狸")](https://zh.wikipedia.org/wiki/阿狸)

### 11、转义字符

要显示原本用于格式化 Markdown 文档的字符，请在字符前面添加反斜杠字符 \ 。

```text
\* Without the backslash, this would be a bullet in an unordered list.
```

\* Without the backslash, this would be a bullet in an unordered list.

**可做转义的字符**

以下列出的字符都可以通过使用反斜杠字符从而达到转义目的。

| Character | Name                                           |
| --------- | ---------------------------------------------- |
| \         | backslash                                      |
| `         | backtick (see also escaping backticks in code) |
| *         | asterisk                                       |
| _         | underscore                                     |
| { }       | curly braces                                   |
| [ ]       | brackets                                       |
| ( )       | parentheses                                    |
| #         | pound sign                                     |
| +         | plus sign                                      |
| -         | minus sign (hyphen)                            |
| .         | dot                                            |
| !         | exclamation mark                               |
| \|        | pipe (see also escaping pipe in tables)        |

### 12、扩展语法

一些个人和组织开始通过添加其他元素（例如表，代码块，语法突出显示，URL自动链接和脚注）来[扩展基本语法](https://markdown.com.cn/extended-syntax/)。可以通过使用基于基本Markdown语法的轻量级标记语言，或通过向兼容的Markdown处理器添加扩展来启用这些元素。
