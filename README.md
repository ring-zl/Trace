# Trace
# 列置换加密及破译
## 项目背景：
### 项目实现了基于带密钥的列置换加密、解密以及破译算法。
密钥为英文单词，对应英文字符出现的顺序作为列置换的顺序。明文字符串末尾做补‘x’操作，以确保长度为密钥的整数倍

## 运行须知：
运行前确保你拥有**numpy**、**re**以及**wordninja**包（**pip install wordninja**）

## 项目介绍：

### <u> utils.py </u>
#### 包含了项目中使用的库函数以及加密解密函数方法
### <u> encryption.py </u>
#### 加密程序
### <u> decryption.py </u>
#### 破译程序
##### 程序提供了三种破译方法：
###### 1.已知密钥破译，对应于解密程序。
已知密钥将补充入密钥本
###### 2.搜索密钥破解（搜索可能的英语单词作为密钥进行破解）
密钥为常用的125K英文单词中，没有重复字母的英文单词（约38K个），对可能的密钥长度进行搜索，以密钥本中密钥尝试解密。  
破译明文筛选方式为：    
（1）利用用户猜测的可能出现的英文单词做正则搜索  
（2）所有英文单词的平均长度为4.79，利用分词包对破译明文进行分词。若明文不是具有意义的英文字符串，分词将出现过多短字符。对单词数合理范围进行约束
###### 3.暴力穷举破解（当密钥长度过长时，破解过程可能会花费很长时间）
递归生成所有列置换的可能性，利用上述方式进行明文筛选  
！！！当搜索密钥长度较长时，程序将运行非常长时间！！！
### <u> words-by-frequency.txt </u>
#### txt文件包含了常用的125K个英文单词
### <u> possiblekeys.txt </u>
#### txt文件包含了所有可能的英文单词密钥
### <u> possiblekeys_n.txt </u>
#### txt文件包含了长度为n的合法英文单词密钥