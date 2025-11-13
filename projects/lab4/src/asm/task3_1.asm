; =======================================
; task3_1
; Do not modify this file !!!
; =======================================

lui         x5,     2157969408          ; nop                                       ;   0x80a00000

# Test for vadd.vi & vse32.v
addi        x5,     x5,     0           ; nop                                       ;
add         x5,     x5,     x0          ; vadd.vi     vx2,    vx0,    8,    1       ;
nop                                     ; vadd.vi     vx2,    vx0,    8,    1       ;
add         x5,     x5,     x0          ; vse32.v     vx2,    x5,             1     ;   mem[0][0:7]=8
addi        x5,     x5,     32          ; nop                                       ;

# Test for vadd.vx
addi        x7,     x0,     9           ; nop                                       ;
nop                                     ; vadd.vx     vx3,    vx0,    x7,     1     ;
nop                                     ; vse32.v     vx3,    x5,             1     ;   mem[1][0:7]=9
addi        x5,     x5,     32          ; nop                                       ;

# Test for vadd.vv
nop                                     ; vadd.vv     vx2,    vx2,    vx3,    1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[2][0:7]=17

# Test for vle32.v
nop                                     ; vadd.vv     vx2,    vx2,    vx0,    1     ;
nop                                     ; vle32.v     vx2,    x5,             1     ;
addi        x5,     x5,     32          ; nop                                       ; 
nop                                     ; vadd.vv     vx2,    vx2,    vx3,    1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[4][0:7]=26
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vmin.vv
nop                                     ; vadd.vi     vx2,    vx0,    1,      1     ;
nop                                     ; vadd.vi     vx3,    vx0,    10,     1     ;
nop                                     ; vmin.vv     vx2,    vx2,   vx3,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=1
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vmin.vx
nop                                     ; vadd.vi     vx2,    vx0,    7,      1     ;
addi        x7,     x0,     2           ; nop                                       ; 
nop                                     ; vmin.vx     vx2,    vx2,    x7,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=2
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vmax.vv
nop                                     ; vadd.vi     vx2,    vx0,    1,      1     ;
nop                                     ; vadd.vi     vx3,    vx0,    10,     1     ;
nop                                     ; vmax.vv     vx2,    vx2,   vx3,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=10
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vmax.vx
nop                                     ; vadd.vi     vx2,    vx0,    7,      1     ;
addi        x7,     x0,     2           ; nop                                       ; 
nop                                     ; vmax.vx     vx2,    vx2,    x7,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=7
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vsra.vv
nop                                     ; vadd.vi     vx2,    vx0,   16,      1     ;
nop                                     ; vadd.vi     vx3,    vx0,    3,      1     ;
nop                                     ; vsra.vv     vx2,    vx2,   vx3,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=2
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vsra.vx
nop                                     ; vadd.vi     vx2,    vx0,   16,      1     ;
addi        x7,     x0,     2           ; nop                                       ; 
nop                                     ; vsra.vx     vx2,    vx2,    x7,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=4
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vsra.vi
nop                                     ; vadd.vi     vx2,    vx0,   16,      1     ;
nop                                     ; vsra.vi     vx2,    vx2,    2,      1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=4
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vredsum.vs
nop                                     ; vadd.vi     vx2,    vx0,   17,      1     ;
nop                                     ; vredsum.vs  vx3,    vx2,  vx0,      1     ;
nop                                     ; vse32.v     vx3,    x5,             1     ;   mem[5][0:7]=17*8=136
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vredmax.vs
nop                                     ; vadd.vi     vx2,    vx0,   17,      1     ;
nop                                     ; vredsum.vs  vx3,    vx2,  vx0,      1     ;
nop                                     ; vredmax.vs  vx4,    vx3,  vx0,      1     ;
nop                                     ; vse32.v     vx4,    x5,             1     ;   mem[5][0:7]=17*8=136
addi        x5,     x5,     32          ; nop                                       ; 

halt                                    ; nop                                       ;

