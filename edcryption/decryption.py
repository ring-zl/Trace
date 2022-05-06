from utils import *

def keyencryption():

    ciphertext = input("请输入密文：")
    key=input("请输入密钥：")

    isrepeat = countrepeat(key)
    while isrepeat:
        key = input('密钥字符串不允许出现重复字符，请重新输入密钥：')
        isrepeat = countrepeat(key)
    readorder = getreadorder(key)
    deorder=getdeorder(readorder)

    plaintext=getplaintext(deorder,ciphertext)
    print("明文解密为：",plaintext)
    plaincontext=wordninja.split(plaintext)
    plainresult = ' '.join(plaincontext)
    print("明文内容为：",plainresult)
    modifykeybook(key)
    print("解密完成")

def searchencryption():

    ciphertext = input("请输入密文：")
    patt=input("请输入你对明文中会出现单词的猜测，用逗号隔开，没有可以跳过，全部猜测错误会导致无法解密：")
    patt=patt.split(",")
    splitfactor=input("请输入模式匹配正则因子（0-1），过大可能无法匹配正确结果，过小会导致可能结果过多，默认值0.5：")
    factor=getfactor(splitfactor)

    length = len(ciphertext)
    for testsize in range(1,15):
        if (length % testsize) == 0:
            testkeys=open("possiblekeys_" + str(testsize) + ".txt").read().split()
            for testkey in testkeys:
                readorder=getreadorder(testkey)

                trydecrpt(readorder, ciphertext, patt, factor)

    print("解密完成")


def exhaustencryption():
    ciphertext = input("请输入密文：")
    patt = input("请输入你对明文中会出现单词的猜测，用逗号隔开，没有可以跳过，全部猜测错误会导致无法解密：")
    patt = patt.split(",")
    splitfactor = input("请输入模式匹配正则因子（0-1），过大可能无法匹配正确结果，过小会导致可能结果过多，默认值0.5：")
    factor = getfactor(splitfactor)
    length = len(ciphertext)
    for testsize in range(1,length):
        if (length % testsize) == 0:
            print("正在尝试大小",testsize,"的列置换所有可能排序..........")
            rangelist = []
            for i in range(0, testsize):
                rangelist.append(i)
            res=fullpermutation(rangelist)
            # print(res)
            for testkey in res:
                readorder = getreadorder(testkey)
                trydecrpt(readorder, ciphertext, patt, factor)
    print("解密完成")

def run():
    print("---本程序简单的实现了基于列置换算法的破解方法---")
    print("请输入对应数字，选择破解方法：\n"
          "0.已知密钥破解（对应于密文解密）\n"
          "1.搜索密钥破解（搜索可能的英语单词作为密钥进行破解）\n"
          "2.暴力穷举破解（当密钥长度过长时，破解过程可能会花费很长时间）\n")
    choice=input()
    if choice=='0':
        keyencryption()

    if choice=='1':
        searchencryption()

    if choice == '2':
        exhaustencryption()

if __name__ == '__main__':
    run()


