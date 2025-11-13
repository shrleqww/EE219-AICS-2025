import getopt
import random
import sys
import numpy as np

MIN = -255
MAX = 255

def MatrixGen(shape=(8,8)):
    matrix = [[random.randint(MIN, MAX) for _ in range(shape[1])] for _ in range(shape[0])]
    return matrix

def dot_product(A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def dump_matrix( path, dump_list ):
    data_str  = ""
    for matrix in dump_list:
        for row in matrix:
            for pixel in row:
                data_str = "{}{:<10}\t".format(data_str, str(pixel))
            data_str = data_str + "\n"
        data_str = data_str + "\n\n"
    with open(path,"w+") as f:
        f.write(data_str) 

def TestCase( ram_path, test_path, test_path_T ):
    A = MatrixGen()
    B = MatrixGen()
    C = MatrixGen()
    D = matrix_add(dot_product(A, B), C)

    A_T = transpose(A)
    B_T = transpose(B)
    C_T = transpose(C)
    D_T = transpose(D)
    
    dump_list = [A, A_T, B, B_T, C, C_T]
    gold_result = [D]
    gold_result_T = [D_T]
    
    dump_matrix( ram_path, dump_list )
    dump_matrix( test_path, gold_result )
    dump_matrix( test_path_T, gold_result_T )

def MatrixGen_np(shape=(8,8)):
    import numpy as np
    matrix = np.random.randint(MIN,MAX, shape)
    return matrix 

def TestCase_np(ram_path, testpath, testfile_T):
    A = MatrixGen()
    B = MatrixGen()
    C = MatrixGen()
    D = A.dot(B) + C 

    A_T = A.T
    B_T = B.T
    C_T = C.T
    D_T = D.T

    dump_list = [ A, A_T, B, B_T, C, C_T ]
    gold_result = D
    gold_result_T = D_T

    data_str  = ""
    for matrix in dump_list:
        for row in matrix:
            for pixel in row:
                data_str = "{}{:<10}\t".format(data_str, str(pixel))
            data_str = data_str + "\n"
        data_str = data_str + "\n\n"
    with open(ram_path,"w+") as f:
        f.write(data_str) 

    data_str = ""
    for row in gold_result:
        for pixel in row:
            data_str = "{}{:<10}\t".format(data_str, str(pixel))
        data_str = data_str + "\n"
    with open(testpath,"w+") as f:
        f.write(data_str)     

    data_str = ""
    for row in gold_result_T:
        for pixel in row:
            data_str = "{}{:<10}\t".format(data_str, str(pixel))
        data_str = data_str + "\n"
    with open(testfile_T,"w+") as f:
        f.write(data_str)  


def GenInt32_Q16_16_Data(path, num):
    SCALE = 1 << 16
    RANGE_MIN = -10.0
    RANGE_MAX = 10.0

    data = []
    for _ in range(num):
        rnd = RANGE_MIN + (RANGE_MAX - RANGE_MIN) * random.random()
        q16_16_val = int(round(rnd * SCALE))

        MAX_Q16_16 = int(10.0 * SCALE)
        MIN_Q16_16 = -MAX_Q16_16
        if q16_16_val > MAX_Q16_16:
            q16_16_val = MAX_Q16_16
        elif q16_16_val < MIN_Q16_16:
            q16_16_val = MIN_Q16_16

        data.append(q16_16_val)

    data_str = ""
    for i, val in enumerate(data):
        data_str += "{:<12}\t".format(str(val))
        if (i + 1) % 8 == 0:
            data_str += "\n"
    if num % 8 != 0:
        data_str += "\n"

    TABLE_SIZE = 64
    S = SCALE

    t_range = np.linspace(-8, 0, TABLE_SIZE)
    exp_table = np.exp(t_range)
    exp_table_fixed = np.round(exp_table * S).astype(np.int32)

    for i, val in enumerate(exp_table_fixed):
        data_str += "{:<12}\t".format(str(val))
        if (i + 1) % 8 == 0:
            data_str += "\n"
    if TABLE_SIZE % 8 != 0:
        data_str += "\n"

    with open(path, "w+") as f:
        f.write(data_str)


def arg_handler():
    rampath = ""
    testpath = ""
    testfile_T = ""
    task3_2_path = ""
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt( argv, "hr:t:T:s:",["ramfile=", "testfile=", "testfile_T="] )

    except getopt.GetoptError:
        print('Example:')
        print( "python MatrixGen.py -r ../data/ramdata.txt -t ../data/testdata.txt -T ../data/testdata_T.txt" )
        sys.exit(2)
    
    for opt,arg in opts:
        if opt in ("-h", "--help"):
            print('Example:')
            print( "python MatrixGen.py -r ../data/ramdata.txt -t ../data/testdata.txt -T ../data/testdata_T.txt" )
            sys.exit()
        elif opt in ("-r", "--ramfile"):
            rampath = arg 
        elif opt in ("-t", "--testfile"):
            testpath = arg 
        elif opt in ("-T", "--testfile_T"):
            testfile_T = arg 
        elif opt in ("-s", "--task3_2_file"):
            task3_2_path = arg

    # return rampath, testpath, testfile_T
    return rampath, testpath, testfile_T, task3_2_path

if __name__ == '__main__':
    rampath, testpath, testfile_T, task3_2_path = arg_handler()

    TestCase(rampath, testpath, testfile_T)

    if task3_2_path != "":
        GenInt32_Q16_16_Data(task3_2_path, num=8)