import getopt
import sys
import numpy as np

def read_txt(path):
    matrix = []
    with open(path,'r') as f:
        str_lines = f.readlines()

        for the_line in str_lines:
            line = []
            list_line = the_line.replace("\n",'').split("\t")
            for i in list_line:
                i = i.replace(" ",'')
                if (i!=''):
                    line.append( int(i) )
            matrix.append(line)
    return matrix

def extract_golden(path, num_lines):
    Q = 16
    Q_16 = 1 << Q
    SAFE_SHIFT = 2
    LUT_SIZE = 64

    raw_ints = []
    with open(path, 'r') as f:
        for idx, line in enumerate(f):
            if num_lines is not None and idx >= num_lines:
                break
            nums = [int(i) for i in line.strip().split() if i]
            raw_ints.extend(nums)
    X_q16_16 = np.array(raw_ints, dtype=np.int32)

    t_vals = np.linspace(-8.0, 0.0, LUT_SIZE, dtype=np.float64)
    exp_table = np.round(np.exp(t_vals) * Q_16).astype(np.int32)

    x_max = np.max(X_q16_16).astype(np.int32)
    delta = (X_q16_16 - x_max).astype(np.int32)
    delta = np.clip(delta, -8 * Q_16, 0).astype(np.int32)

    idx_num = (delta + 8 * Q_16).astype(np.int32) * (LUT_SIZE - 1)
    idx     = (idx_num // (8 * Q_16) ).astype(np.int32)
    idx     = np.clip(idx, 0, LUT_SIZE - 1).astype(np.int32)

    exp_delta = exp_table[idx].astype(np.int32)

    exp_sum = np.sum(exp_delta, dtype=np.int32).astype(np.int32)
    if exp_sum <= 0:
        exp_sum = 1

    exp_delta_shr = (exp_delta >> SAFE_SHIFT).astype(np.int32)
    exp_sum_shr   = int(exp_sum >> SAFE_SHIFT)
    if exp_sum_shr <= 0:
        exp_sum_shr = 1

    num = (exp_delta_shr.astype(np.int32) * Q_16)
    softmax_q16_16 = (num // exp_sum_shr).astype(np.int32)

    data_float = X_q16_16.astype(np.float64) / Q_16
    softmax = softmax_q16_16.astype(np.float64) / Q_16
    return data_float, softmax


def extract_matrix(matrix):
    return [item for row in matrix for item in row]

def show_original(original_data):
    length = len(original_data)
    context = ""
    for i in range(length):
        res_a = original_data[i]
        context += ("{:16.6f}".format( res_a )) 
        if((i+1)%8==0):
            context += "\n"
    print(context)

def show_accurate_softmax(original_data):
    x = np.asarray(original_data, dtype=np.float64)
    z = x - np.max(x)
    ez = np.exp(z)
    sm = ez / np.sum(ez)

    length = len(original_data)
    context = ""
    for i in range(length):
        res_a = sm[i]
        context += ("{:16.6f}".format( res_a )) 
        if((i+1)%8==0):
            context += "\n"
    print(context)

def show_golden(golden_result):
    length = len(golden_result)
    context = ""
    for i in range(length):
        res_a = golden_result[i]
        context += ("{:16.6f}".format( res_a )) 
        if((i+1)%8==0):
            context += "\n"
    print(context)

def compare( golden_result, test_list ):
    length = len(golden_result)
    
    flag_same = True 
    error_cnt = 0 
    error_list = []
    context = ""

    SCALE = 65536.0 # 2^16
    for i in range(length):
        res_a = golden_result[i]
        res_b = test_list[i] / SCALE
        diff = abs(res_a - res_b)
        if diff > 1e-3:
            flag_same = False
            error_cnt += 1
            error_list.append(i)
            context += ("\033[31m{:16.6f}\033[0m".format(res_b))
        else:
            context += ("\033[32m{:16.6f}\033[0m".format(res_b))

    print(context)

    if(flag_same):
        print("=====================================")
        print("                \033[32mPass\033[0m                 ")
        print("=====================================")
    else:
        print("=====================================")
        print("                \033[31mFail\033[0m                 ")
        print("=====================================")
        print("Total {} errors !!!".format(error_cnt))



def arg_handler():
    dumppath = ""
    goldpath = ""
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv, "d:g:", ["dumpfile=", "goldfile="])
    except getopt.GetoptError:
        print('\033[31mTest.py Arg EROOR!!!\033[0m')
        sys.exit(2)
    
    for opt,arg in opts:
        if opt in ("-d", "--dumpfile"):
            dumppath = arg 
        if opt in ("-g", "--goldfile"):
            goldpath = arg
    
    return dumppath, goldpath

if __name__== '__main__':

    dumppath, goldpath = arg_handler()
    if( dumppath == ""):
        dumppath = '../../build/sw/dumpdata_task5.txt'
    if goldpath == "":
        goldpath = "../../build/sw/ramdata_task3_2.txt"

    original_data, golden_result = extract_golden(goldpath, num_lines=1)
    matrix_dump = read_txt(dumppath)
    test_list = extract_matrix(matrix_dump)

    
    print('-----------------------------')
    print("The Original Data:")
    show_original(original_data)

    print('-----------------------------')
    print("The Reference (Float) Softmax:")
    ref_sm = show_accurate_softmax(original_data)

    print('-----------------------------')
    print("The Golden Result:")
    show_golden( golden_result )

    print('-----------------------------')
    print("The Dumped Result:")
    compare(golden_result, test_list )
