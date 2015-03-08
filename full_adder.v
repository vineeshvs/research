// slice
// Full Adder rtl
// default_slice

module full_adder
  (a0, b0, c0, a1, b1, c_out, s_out, s2, d_out, s3);

   // Inputs
   input  a0;
   input  b0;
   input  c0;
   input  a1;
   input  b1;
      
   // Outputs
   output c_out;
   output s_out;
   output s2;
   output d1;
   output s3;

   // Wires
   wire   c1;
   wire   c2;
   wire   s1;
   wire   d1;
   wire   c3;

   // Some assignments
   assign carry_out = c1 | c2;
   assign s_out = s1;
   assign d_out = d1;
   
   // Instantiating two half-adders to make the circuit.
   
   // slice
   // Instructions : I1, I2
   half_adder u1_half_adder
     (
      // Inputs
      .in_x(a0),
      .in_y(b0),
      // End of inputs
      // Outputs
      .out_sum(s0),
      .out_carry(c1)
      // End of outputs
      );                    
   
   // slice
   // Instructions : I1, I3
   half_adder u2_half_adder
     (
      // Inputs
      .in_x(s0),
      .in_y(c0),
      // End of inputs
      // Outputs
      .out_sum(s1),
      .out_carry(c2)
      // End of outputs
      );                    
   
   // slice
   // Instructions : I4, I5
   test1 test1
     (
      // Inputs
      .in_1(s1),
      .in_2(s0),
      .in_3(a1),
      .in_4(b1),
      // End of inputs
      // Outputs
      .out_1(s2),
      .out_2(d1),
      .out_3(c3)
      // End of outputs
      );                 
   
   // slice
   // Instructions : I6, I7
   test2 test2
     (
      // Inputs
      .in_1(d1),
      .in_2(c3),
      .in_3(b1),
      // End of inputs
      // Outputs
      .out_1(s3)
      // End of outputs
      );
   
   // slice
   // default_slice             
endmodule 
