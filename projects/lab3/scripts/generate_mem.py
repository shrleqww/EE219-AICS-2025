import sys
import random
import os
import shutil
import numpy as np

mem_path = "./mem/"
top_file = "./vsrc/sim/top.v"
if not os.path.exists(mem_path):
    os.mkdir(mem_path)

IMG_C       = int(sys.argv[1])
IMG_W       = int(sys.argv[2])
IMG_H       = int(sys.argv[3])
FILTER_NUM  = int(sys.argv[4])
FILTER_SIZE = int(sys.argv[5])
DEBUG       = int(sys.argv[6])

MEM_SIZE    = 0x5000
IMG_BASE    = 0x00000000
WEIGHT_BASE = 0x00001000
IM2COL_BASE = 0x00002000

def init_mem():
    mem_list = []
    for i in range(MEM_SIZE):
        mem_list.append(0)
    return mem_list

def write_mem(mem_list):
    mem_file = open(mem_path+'mem_init.txt', 'w')
    mem_file.seek(0)
    mem_file.truncate()
    for val in mem_list:
        mem_file.write('%08X\n'%val)
    mem_file.close()

def construct_mem(shape):
    N,C,H,W = shape
    input = np.zeros(shape)
    mem_list = []
    for n in range(N):
        for c in range(C):
            for h in range(H):
                for w in range(W):
                    input[n,c,h,w] = int(random.randint(0, 255))
    for n in range(N):
        for h in range(H):
            for w in range(W):
                for c in range(C):
                    mem_list.append(int(input[n,c,h,w]))
    return input,mem_list

def main():
    M = IMG_H * IMG_W 
    N = FILTER_SIZE * FILTER_SIZE * IMG_C
    K = FILTER_NUM
    mem_list = init_mem()

    input_shape     = (1,IMG_C,IMG_H,IMG_W)
    weight_shape    = (FILTER_NUM,IMG_C,FILTER_SIZE,FILTER_SIZE)
    _,input_mem     = construct_mem(input_shape)
    _,weight_mem    = construct_mem(weight_shape)

    mem_list[IMG_BASE:IMG_BASE+len(input_mem)]          = input_mem
    mem_list[WEIGHT_BASE:WEIGHT_BASE+len(weight_mem)]   = weight_mem

    write_mem(mem_list)
    modify_testbench()

def modify_testbench():
    f_testbench = open(top_file, "r+")
    testbench = f_testbench.read().split('\n')
    testbench[1] = '`define IMG_C ' + str(IMG_C)
    testbench[2] = '`define IMG_W ' + str(IMG_W)
    testbench[3] = '`define IMG_H ' + str(IMG_H)
    testbench[4] = '`define FILTER_NUM ' + str(FILTER_NUM)
    testbench[5] = '`define FILTER_SIZE ' + str(FILTER_SIZE)
    testbench[6] = '`define DEBUG ' + str(DEBUG)

    f_testbench.seek(0)
    f_testbench.truncate()
    f_testbench.write("\n".join(testbench))
    f_testbench.close()

if __name__ == '__main__':
    main()