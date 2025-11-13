; =======================================
; task2_1
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

# Test for vsub.vx
nop                                     ; vadd.vi     vx2,    vx0,    1,      1     ;
addi        x7,     x0,     7           ; nop                                       ; 
nop                                     ; vsub.vx     vx2,    vx2,    x7,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=-6
addi        x5,     x5,     32          ; nop                                       ;

# Test for vsub.vv
nop                                     ; vadd.vi     vx2,    vx0,    10,     1     ;
nop                                     ; vadd.vi     vx3,    vx0,    15,     1     ;
nop                                     ; vsub.vv     vx2,    vx2,    vx3,    1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=-5
addi        x5,     x5,     32          ; nop                                       ;  

# Test for vmul.vx
nop                                     ; vadd.vi     vx2,    vx0,    1,      1     ;
addi        x7,     x0,     7           ; nop                                       ; 
nop                                     ; vmul.vx     vx2,    vx2,    x7,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=7
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vmul.vv
nop                                     ; vadd.vi     vx2,    vx0,    10,     1     ;
nop                                     ; vadd.vi     vx3,    vx0,    10,     1     ;
nop                                     ; vmul.vv     vx2,    vx2,    vx3,    1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=100
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vdiv.vx
nop                                     ; vadd.vi     vx2,    vx0,    13,     1     ;
addi        x7,     x0,     7           ; nop                                       ; 
nop                                     ; vdiv.vx     vx2,    vx2,    x7,     1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=1
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vdiv.vv
nop                                     ; vadd.vi     vx2,    vx0,    12,     1     ;
nop                                     ; vadd.vi     vx3,    vx0,    6 ,     1     ;
nop                                     ; vdiv.vv     vx2,    vx2,    vx3,    1     ;
nop                                     ; vse32.v     vx2,    x5,             1     ;   mem[5][0:7]=2
addi        x5,     x5,     32          ; nop                                       ; 

# Test for vmv.x.s and vmv.v.x
nop                                     ; vadd.vi     vx2,    vx0,    13,     1     ;
nop                                     ; vmv.x.s     x8,     vx2,    vx0,    1     ;   x8 = vx2[0]
nop                                     ; vmv.v.x     vx3,    vx31,   x8,     1     ;   vx3[i] = x8
nop                                     ; vse32.v     vx3,    x5,             1     ;   mem[5][0:7]=13
addi        x5,     x5,     32          ; nop                                       ; 

halt                                    ; nop                                       ;

