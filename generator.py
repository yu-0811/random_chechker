# テストケースを作成して愚直解を実行する
# テストケースを作成する際には、generate関数を編集する
# 主に実験とかに使える

import sys,os,filecmp
from random import randint, choices, sample, shuffle
import subprocess

out_file = "in.txt"
out_result = "out.txt"
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def str_min_26(n):  # 重複なし英小文字n文字
    return sample(alp, n)

def str_over_26(n):  # 重複あり英小文字n文字
    return choices(alp, k=n)

CNT = 0

# 実行時間制限
TIME_LIMIT = 500

# 入力生成
def generate():

#   with open(out_file, 'w') as f:
#     f.write(f"{L} {R}\n")

    return
    
generate()

# random_checker_ac.py に書いたコードを実行したいときはコメントアウトを外す

# with open(out_result, 'w') as f_out:
#   res = subprocess.run(["python", "random_checker_ac.py", "in.txt"], stdout=f_out, stderr=subprocess.PIPE, timeout=TIME_LIMIT)
#   if res.returncode != 0:
#       print('!!!RUN TIME ERROR!!!')
#       exit()