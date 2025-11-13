// =======================================
// You need to finish this module
// =======================================

`include "define_rv32v.v"

module v_id #(
  parameter VLMAX     = 8,
  parameter VALUOP_DW = 5,
  parameter VMEM_DW   = 256,
  parameter VMEM_AW   = 32,
  parameter VREG_DW   = 256,
  parameter VREG_AW   = 5,
  parameter INST_DW   = 32,
  parameter REG_DW    = 32,
  parameter REG_AW    = 5
) (
  input                   clk,
  input                   rst,

  input   [INST_DW-1:0]   inst_i,

  output                  rs1_en_o,
  output  [REG_AW-1:0]    rs1_addr_o,
  input   [REG_DW-1:0]    rs1_dout_i,

  output                  rd_w_en_o,
  output  [REG_AW-1:0]    rd_addr_o,

  output                  vs1_en_o,
  output  [VREG_AW-1:0]   vs1_addr_o,
  input   [VREG_DW-1:0]   vs1_dout_i,

  output                  vs2_en_o,
  output  [VREG_AW-1:0]   vs2_addr_o,
  input   [VREG_DW-1:0]   vs2_dout_i,

  output  [VALUOP_DW-1:0] valu_opcode_o,
  output  [VREG_DW-1:0]   operand_v1_o,
  output  [VREG_DW-1:0]   operand_v2_o,

  output                  vmem_ren_o,
  output                  vmem_wen_o,
  output  [VMEM_AW-1:0]   vmem_addr_o,
  output  [VMEM_DW-1:0]   vmem_din_o,

  output                  vid_wb_en_o,
  output                  vid_wb_sel_o,
  output  [VREG_AW-1:0]   vid_wb_addr_o,

  output                  vid_wb_from_rs1
);

  localparam VALU_OP_NOP        = 5'd0  ;
  localparam VALU_OP_VADD       = 5'd1  ;
  localparam VALU_OP_VMUL       = 5'd2  ;
  localparam VALU_OP_VSUB       = 5'd3  ;
  localparam VALU_OP_VMIN       = 5'd4  ;
  localparam VALU_OP_VMAX       = 5'd5  ;
  localparam VALU_OP_VSRA       = 5'd6  ;
  localparam VALU_OP_VREDSUM_VS = 5'd7  ;
  localparam VALU_OP_VREDMAX_VS = 5'd8  ;
  localparam VALU_OP_VMV_V_X    = 5'd9  ;
  localparam VALU_OP_VMV_X_S    = 5'd10 ;
  localparam VALU_OP_VDIV       = 5'd11 ; 


endmodule

