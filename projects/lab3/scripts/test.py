import sys
import os
from turtle import width
import numpy as np

IMG_BASE    = 0x00000000
WEIGHT_BASE = 0x00001000
IM2COL_BASE = 0x00002000
OUTPUT_BASE = 0x00003000

mem_file1 = './mem/mem_init.txt'
mem_file2 = './mem/mem_out.txt'

IMG_C       = int(sys.argv[1])
IMG_W       = int(sys.argv[2])
IMG_H       = int(sys.argv[3])
FILTER_NUM  = int(sys.argv[4])
FILTER_SIZE = int(sys.argv[5])

def im2col_fun(input_data, filter_h, filter_w):

    N, C, H, W = input_data.shape
    out_h = H 
    out_w = W
    pad = int((filter_h - 1)/2)
    img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w), dtype='int')

    for y in range(filter_h):
        y_max = y + out_h
        for x in range(filter_w):
            x_max = x + out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max, x:x_max]
    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
    mem_list = []
    for i in range(col.T.shape[0]):
        for j in range(col.T.shape[1]):
            mem_list.append(int(col.T[i,j]))
    return col,mem_list

def print_hex_array(arr, indent=0):
    if isinstance(arr, np.ndarray):
        if arr.ndim == 1:
            print("[", end='')
            for i, val in enumerate(arr):
                
                if i > 0:
                    print("", end='')
                print("%02X " % val, end='')
            print("]", end='')
        else:
            print("[", end='')
            for i, sub_arr in enumerate(arr):
                if i > 0:
                   print("\n" + " " * (indent), end='')
                print_hex_array(sub_arr, indent+1)
            print("]", end='')
    else:
        print("%02X " % arr, end='')

def main():
    M = IMG_H * IMG_W 
    N = FILTER_SIZE * FILTER_SIZE * IMG_C
    K = FILTER_NUM
    f1 = open(mem_file1, 'r')
    f2 = open(mem_file2, 'r')
    mem = f1.readlines()
    mem_out = f2.readlines()
    weight = []
    im2col = []
    output = []
    golden = []
    print('M:', M)
    print('N:', N)
    print('K:', K)

    print('\ninput:')
    in_list = []
    for i in range(IMG_C*IMG_H*IMG_W):
        val = int(eval('0x'+mem[IMG_BASE + i].strip()))
        in_list.append(val)
    input_nhwc = np.array(in_list).reshape((1,IMG_H,IMG_W,IMG_C))
    input_nchw = np.transpose(input_nhwc,(0,3,1,2))
    print_hex_array(input_nchw)
    print('')

    print('\nim2col:')
    for i in range(IMG_H*IMG_W):
        row = []
        for j in range(FILTER_SIZE*FILTER_SIZE*IMG_C):
            val = int(eval('0x'+mem_out[IM2COL_BASE + j * IMG_H*IMG_W + i].strip()))
            row.append(val)
            print("%02X "%val, end='')
        print('')
        im2col.append(row)
    
    im2col_groundtruth,_ = im2col_fun(input_nchw,FILTER_SIZE,FILTER_SIZE)
    print("###############")
    if im2col == im2col_groundtruth.tolist():
        print('im2col pass')
    else:
        print('im2col fail')
    print("###############")

    print('\nweight:')
    for i in range(FILTER_SIZE*FILTER_SIZE*IMG_C):
        row = []
        for j in range(FILTER_NUM):
            val = int(eval('0x'+mem[WEIGHT_BASE + i * FILTER_NUM + j].strip()))
            row.append(val)
            print("%02X "%val, end='')
        weight.append(row)
        print('')
    
    print('\noutput:')
    for i in range(IMG_H*IMG_W):
        row = []
        for j in range(FILTER_NUM):
            val = int(eval('0x'+mem_out[OUTPUT_BASE + i * FILTER_NUM + j].strip()))
            row.append(val)
            print("%08X "%val, end='')
        print('')
        output.append(row)

    groundtruth = np.matmul(im2col_groundtruth,np.array(weight))
    print('\ngroundtruth:')
    for i in range(groundtruth.shape[0]):
        row = []
        for j in range(groundtruth.shape[1]):
            val = int(groundtruth[i][j])
            row.append(val)
            print("%08X "%val, end='')
        print('')
        golden.append(row)
    
    print("###############")
    if ((output == golden) and output != []):
        print("Congratulate!")
        os.system('echo "PASS" > mem/status')
    else:
        print("Somthing Wrong!")
        os.system('echo FAIL > mem/status')
    print("###############")

if __name__ == '__main__':
    main()