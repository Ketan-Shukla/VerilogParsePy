 module TopCell (data, out1, out2, out3, out4, out5);
     output out1;
     output out2;
     output out3;
     output out4;
     output out5;
     input  [7:0] data;

     wire [7:0] data;

     cellA IcellAK0 (.in1(data[7]), .in2(data[6]), .in3(data[5]),
         .in4(data[4]), .out1(net14));
     cellC IcellCK0 (.inA(data[3]), .inB(data[2]), .inC(data[1]),
         .inD(data[0]), .outA(out2), .outB(out3));
     cellD IcellDK0 (.data(data[7:0]), .out1(out4), .out2(out5));
     invN1 X0 (.A(net14), .Y(out1));

 endmodule // TopCell

 // Cell: designLib bufferCell schematic
 // Last modified: Jun 14 11:00:42 2017
 module bufferCell (in, out);
     output out;
     input  in;

     invN1 X0 (.A(in), .Y(net5));
     invN1 X1 (.A(net5), .Y(out));
 endmodule // bufferCell


 // Cell: designLib cellA schematic
 // Last modified: Jun 14 10:58:49 2017
 module cellA (in1, in2, in3, in4, out1);
     output out1;
     input  in1;
     input  in2;
     input  in3;
     input  in4;

     invN1 X0 (.A(in1), .Y(net13));
     invN1 X1 (.A(in2), .Y(net11));
     invN1 X2 (.A(in3), .Y(net12));
     invN1 X3 (.A(in4), .Y(net14));
     nand4N1 X4 (.A(net13), .B(net11), .C(net12), .D(net14), .Y(out1));
 endmodule // cellA


 // Cell: designLib cellB schematic
 // Last modified: Jun 14 11:09:05 2017
 module cellB (in1, in2, in3, in4, out1, out2);
     output out1;
     output out2;
     input  in1;
     input  in2;
     input  in3;
     input  in4;

     bufferCell IbufferCellK0 (.in(in1), .out(net17));
     bufferCell IbufferCellK1 (.in(in2), .out(net16));
     bufferCell IbufferCellK2 (.in(in3), .out(net15));
     bufferCell IbufferCellK3 (.in(in4), .out(net14));
     invN1 X0 (.A(net13), .Y(out2));
     invN1 X1 (.A(net19), .Y(net18));
     nand2N1 X2 (.A(net17), .B(net16), .Y(net19));
     nor2N1 X3 (.A(net15), .B(net14), .Y(net13));
     nor2N1 X4 (.A(net18), .B(net13), .Y(out1));
 endmodule // cellB


 // Cell: designLib cellC schematic
 // Last modified: Jun 14 11:16:40 2017
 module cellC (inA, inB, inC, inD, outA, outB);
     output outA;
     output outB;
     input  inA;
     input  inB;
     input  inC;
     input  inD;

     cellA IcellAK0 (.in1(inA), .in2(inB), .in3(inC), .in4(inD),
         .out1(net22));
     cellA IcellAK1 (.in1(inD), .in2(inA), .in3(inB), .in4(inC),
         .out1(net18));
     cellA IcellAK2 (.in1(inC), .in2(inD), .in3(inA), .in4(inB),
         .out1(net17));
     cellA IcellAK3 (.in1(inB), .in2(inC), .in3(inD), .in4(inA),
         .out1(net21));
     invN1 X0 (.A(net22), .Y(net20));
     invN1 X1 (.A(net21), .Y(net19));
     nand2N1 X2 (.A(net20), .B(net18), .Y(outA));
     nand2N1 X3 (.A(net17), .B(net19), .Y(outB));
 endmodule // cellC


 // Cell: designLib cellD schematic
 // Last modified: Jun 14 11:34:42 2017
 module cellD (data, out1, out2);
     output out1;
     output out2;
     input  [7:0] data;

     wire [7:0] data;

     cellB IcellBK0 (.in1(data[0]), .in2(data[1]), .in3(data[2]),
         .in4(data[3]), .out1(net10), .out2(net8));
     cellB IcellBK1 (.in1(data[4]), .in2(data[5]), .in3(data[6]),
         .in4(data[7]), .out1(net7), .out2(net9));
     cellC IcellCK0 (.inA(net10), .inB(net8), .inC(net7), .inD(net9),
         .outA(out1), .outB(out2));
 endmodule // cellD