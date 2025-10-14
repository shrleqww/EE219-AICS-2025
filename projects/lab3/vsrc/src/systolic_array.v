`timescale 1ns / 1ps

module systolic_array#(
  parameter ARRAY_SIZE_M_MAX         = 31,
  parameter ARRAY_SIZE_N_MAX         = 31,
  parameter ARRAY_SIZE_K_MAX         = 31,
  parameter DATA_WIDTH  = 32
) (
  input                                     clk,
  input                                     rst_n,
  input  [31:0]                             M,
  input  [31:0]                             N,
  input  [31:0]                             K,
  input  [DATA_WIDTH*ARRAY_SIZE_M_MAX-1:0]  X,
  input  [DATA_WIDTH*ARRAY_SIZE_K_MAX-1:0]  W,
  output [DATA_WIDTH*ARRAY_SIZE_K_MAX-1:0]  Y,
  output                                    mem_w_en,
  output [31:0]                             mem_addr,
  output                                    done
);

endmodule