import sys
import os
import filecmp
from random import randint, choices, sample, shuffle
import subprocess

out_file = "in.txt"
out_result = "out.txt"
out_ac_result = "out_ac.txt"
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def str_min_26(n):  # 重複なし英小文字n文字
    return sample(alp, n)

def str_over_26(n):  # 重複あり英小文字n文字
    return choices(alp, k=n)

CNT = 0

# 実行時間制限
TIME_LIMIT = 5

# 入力生成
def generate():
  C_MAX = 2*pow(10,5)
  with open(out_file, 'w') as out:
    N = 100
    print(N, file=out)
    C = list()
    SUM = 0
    for i in reversed(range(N)):
        c = randint(0, C_MAX - i - SUM)
        C.append(c)
        SUM += c
    print(*C, file=out)

while True:
    CNT += 1
    generate()
    try:
        with open(out_result, 'w') as f_out:
            res_main = subprocess.run(["python", "main.py", "in.txt"], stdout=f_out, stderr=subprocess.PIPE, timeout=TIME_LIMIT)
            if res_main.returncode != 0:
                print('!!!ERROR!!! SUBMIT_CODE')
                exit()
    except subprocess.TimeoutExpired:
        print('!!!ERROR!!! TIMEOUT EXPIRED (main.py)')
        exit()

    try:
        with open(out_ac_result, 'w') as f_out_ac:
            res_ac = subprocess.run(["python", "../../random_checker_ac.py", "in.txt"], stdout=f_out_ac, stderr=subprocess.PIPE, timeout=TIME_LIMIT)
            if res_ac.returncode != 0:
                print('!!!ERROR!!! AC_CODE')
                exit()
    except subprocess.TimeoutExpired:
        print('!!!ERROR!!! TIMEOUT EXPIRED (random_checker_ac.py)')
        exit()

    if not filecmp.cmp(out_result, out_ac_result):
        print("!!!WRONG ANSWER!!!")
        with open("out.txt", 'r') as f:
            print(f.read())
        exit()

    if CNT < 10 or CNT % 10 == 0:
        print(f"{CNT} case passed")
