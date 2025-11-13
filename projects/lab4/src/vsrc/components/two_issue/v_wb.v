
module v_wb #(
  parameter VREG_DW = 256,
  parameter VREG_AW = 5,
  parameter REG_DW  = 32
) (
  input                   clk,
  input                   rst,

  input                   vid_wb_en_i,
  input                   vid_wb_sel_i,
  input   [VREG_AW-1:0]   vid_wb_addr_i,
  input                   vid_wb_from_rs1,
  input   [VREG_DW-1:0]   valu_result_i,
  input   [VREG_DW-1:0]   vmem_result_i,

  output                  vwb_en_o,
  output  [VREG_AW-1:0]   vwb_addr_o,
  output  [VREG_DW-1:0]   vwb_data_o,

  input   [REG_DW-1:0]    rs1_data
);

assign vwb_en_o     = (rst == 1'b1) ? 0 : vid_wb_en_i ;
assign vwb_addr_o   = (rst == 1'b1) ? 0 : vid_wb_addr_i ;

assign vwb_data_o   = (rst == 1'b1)   ? 0                          : 
                      vid_wb_from_rs1 ? {VREG_DW/REG_DW{rs1_data}} : 
                      vid_wb_sel_i    ? vmem_result_i              : valu_result_i ;

endmodule 
