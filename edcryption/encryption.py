from utils import *

def run():
    print("---本程序基于列置换算法的字符串加密方法---")

    key = input('请输入密钥字符串：')
    isrepeat = countrepeat(key)
    while isrepeat:
        key = input('密钥字符串不允许出现重复字符，请重新输入密钥：')
        isrepeat = countrepeat(key)

    inputext = input('请输入待加密英文字符串：')

    readorder = getreadorder(key)
    print("读取的列顺序为：", readorder)

    size = len(key)
    plainarray = refactorplaintext(inputext, size)

    ciphertext = getciphertext(readorder, plainarray)
    print("密文为：", ciphertext)



if __name__ == '__main__':
    run()