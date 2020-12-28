# hrml: 超莉沫酱自慰语言

你还在为编写html度过一个个孤独难耐的夜晚吗？寂寞长夜，你想找个好的编程语言，来宽慰一下自己吗？

hrml是Python风格的自慰语言，可以容易地编译成html。


## 样例

hrml:
```hrml
div#all:
    div.my_class1:
        span:
            今天天气不错，来散步自慰吧。
        a href='https://散步自慰':
            go!
```

html:
```html
<div id='all'>
    <div class='my_class1'>
        <span>
            今天天气不错，来自慰吧。
        </span>
        <a href='https://散步自慰'>
            go!
        </a>
    </div>
</div>
```

## 使用方法

只要用pip安装——

```sh
pip install hrml
```

然后运行命令就行了——

```sh
python -m hrml {输入hrml文件名} -o {输出html文件名}
```

也可以import它来使用——

```python
import hrml
with open('xxx.hrml') as f:
    print(hrml.masturbate(f.read()))
```

接口只有`masturbate`这一个，输入一个hrml的字符串，将它转为html。

```python
def masturbate(s: str):
    ...
```

## 语法

每一行表示一个元素，缩进表示嵌套的元素。

当元素以冒号或分号结尾时，是一个节点。分号为自闭节点。  
元素的属性和html一样地写在后面，不会被更改。  

不以冒号`:`或分号`;`结尾的是文字。

hrml:
```hrml
div:
    你好
img src='1.jpg'; 
```
html: 
```html
<div>
    你好
</div>
<img src='1.jpg'/>
```

### class和id

用 小点`.` 和 井号`#` 表示元素的class和id，这些要紧跟在名字的后面。   
class和id没有顺序和数量的限制。

hrml: 
```hrml
div.a.b#c:
    你好
```

html:
```html
<div class='a b' id='c'>
   你好
</div>
```
### 注释

使用Python风格注释，如 `# 我是注释` 。  
注释并不会变成html的注释。

### 嵌入html内容

可以用文字的形式直接嵌入html内容。  
这要求嵌入的内容本身没有缩进。

hrml: 
```
div:
    <a href='折跃门'>折跃！</a>
```

html:
```html
<div>
    <a href='折跃门'>折跃！</a>
</div>
```
如果有缩进则会产生错误: 
```hrml
# 这会产生编译错误。
div:
    <a href='折跃门'>
        折跃！
    </a>
# 因为hrml认为「折跃！」是「<a href='折跃门'>」的子节点。
# 但是「<a href='折跃门'>」是文本节点，不能含有子节点。
```
