# python ../../RE_checker.py
# if len(sys.argv) == 2: sys.stdin = open(sys.argv[1])
import sys,os
from random import randint,choices,sample
out_file = "in.txt"
out = open(out_file, 'w') 
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def str_min_26(n): # 重複なし英小文字n文字
  return sample(alp,n)
def str_over_26(n): # 重複あり英小文字n文字
  return choices(alp,k=n)

# 入力生成
def generate():
  with open(out_file, 'w') as out: 
    pass

  res = os.system("python main.py in.txt")
  if res!=0:
    print('!ERROR!')
    exit()
  
while True:
  generate()


