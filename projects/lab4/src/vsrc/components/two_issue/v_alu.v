// =======================================
// You need to finish this module
// =======================================

module v_alu #(
  parameter SEW       = 32,
  parameter VLMAX     = 8,
  parameter VALUOP_DW = 5,
  parameter VREG_DW   = 256,
  parameter VREG_AW   = 5
)(
  input                   clk,
  input                   rst,
  input [VALUOP_DW-1:0]   valu_opcode_i,
  input [VREG_DW-1:0]     operand_v1_i,
  input [VREG_DW-1:0]     operand_v2_i,
  output[VREG_DW-1:0]     valu_result_o
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
