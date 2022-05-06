import numpy as np
import re
import wordninja

#加密解密程序试验：
# key='computer'
# inputext='HellowordXianJiaotong'
# test密文为：HdolanlioongraxoixeXtwJx

# ciphertext='HdolanlioongraxoixeXtwJx'
# ciphertext='helvgwmoueeeneertrpiityhbacsekaxgptsnlpxmnaametx'/////thumb green apple active assignment weekly metaphor



#检查密钥是否从有重复字符
def countrepeat(key):
    for i in key:
        if key.count(i)>1:
            return True
    return False

#根据密钥生成读取顺序
def getreadorder(key):
    sortkey = sorted(key)
    readorder = []
    for i in key:
        readorder.append(sortkey.index(i))
    return readorder

#明文拼接成数组，使明文长度为密钥整数倍，在字符串尾部加x
def refactorplaintext(inputext,keysize):
    if len(inputext) % keysize != 0:
        inputext += (keysize - len(inputext) % keysize) * "x"
    plaintext = np.array(list(inputext))
    plainarray = plaintext.reshape(-1, keysize)
    print(plainarray)
    return plainarray

#根据读取顺序生成密文
def getciphertext(readorder,plainarray):
    cipherarray = np.array([])
    for i in readorder:
        cipherarray = np.append(cipherarray, plainarray[:, i])
        ciphertext = ''.join((str(i) for i in cipherarray))
    return ciphertext


#根据密钥生成的读取顺序生成明文字符串
def getplaintext(deorder, ciphertext):
    plainarray = np.array([])
    ciphertextarray = np.array(list(ciphertext))
    wide = len(ciphertext) // len(deorder)
    testarray = ciphertextarray.reshape(-1, wide).transpose()
    # print(testarray)
    # print(deorder)
    for j in range(wide):
        for i in deorder:
            plainarray = np.append(plainarray, testarray[j, i])

    plaintext = ''.join((str(i) for i in plainarray))
    return plaintext

#根据密钥加密顺序生成解密顺序
def getdeorder(list):
    size=len(list)
    rangelist = []
    for i in range(0, size):
        rangelist.append(i)
    sortorder = []
    for i in rangelist:
        sortorder.append(list.index(i))
    # print("读取的列顺序为：", sortorder)
    return sortorder

#查看该密钥是否在密钥本里，不是则添加
def modifykeybook(key):
    key_len = str(len(key))
    possiblekeys = open("possiblekeys_" + key_len + ".txt").read().split()

    if key in possiblekeys:
        print("密钥本已存有该密钥")
    else:
        f = open("possiblekeys_" + key_len + ".txt", "a")
        f.write("\n")
        f.write(key)
        print("密钥本现已添加此密钥")

#根据读取顺序，密文，模式匹配，正则因子来输出可能的明文
def trydecrpt(readorder,ciphertext,patt,factor):

    deorder = getdeorder(readorder)
    testplaintext = getplaintext(deorder, ciphertext)

    plaincontext = wordninja.split(testplaintext)

    plainresult = ' '.join(plaincontext)
    result = []
    for item in patt:
        pattern = re.compile(item)
        finditem = pattern.findall(testplaintext)

        result.append(finditem)
    for i in result:
        if i != [] and len(ciphertext) / factor > len(plaincontext):
            # print(result)
            print("明文为：",plainresult)
            # print(readorder)

#给定列表的全排列，尝试暴力破解
def fullpermutation(list):
    if list == None:
        return None
    if len(list) == 1:    # 从list[1]处开始递归的
        return [list]
    res = []
    left = list[0]
    right = fullpermutation(list[1:])
    for i in right:
        for j in range(len(i)+1):
            res.append(i[:j]+[left]+i[j:])
    return res

#得到英文字符串分词的正则因子，英文单词的平均长度为4.79，取3.79作为比较合理的平均词长，差别较大的平均词长认为是不合理的明文
def getfactor(splitfactor):
    if splitfactor=='':
        factor=0.5*2*3.79
    else:
        factor = float(splitfactor) * 2 * 3.79
    return factor