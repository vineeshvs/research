// slice
// Full Adder rtl
// default_slice

module full_adder
  (in_x, in_y, carry_in, sum_out, carry_out);
   
   input  in_x;
   input  in_y;
   input  carry_in;
   output sum_out;
   output carry_out;

   wire   w_sum1;
   wire   w_carry1;
   wire   w_carry2;

   assign carry_out = w_carry1 | w_carry2;

   // Instantiate two half-adders to make the circuit. Click here for half-adder rtl

   // slice
   // Instructions : I1, I2
   half_adder u1_half_adder
     (
      // Inputs
      .in_x(in_x),
      .in_y(in_y),
      // End of inputs
      // Outputs
      .out_sum(w_sum1),
      .out_carry(w_carry1)
      // End of outputs
      );                    
   
   // slice
   // Instructions : I1, I3
   half_adder u2_half_adder
     (
      // Inputs
      .in_x(w_sum1),
      .in_y(carry_in),
      // End of inputs
      // Outputs
      .out_sum(sum_out),
      .out_carry(w_carry2)
      // End of outputs
      );                    
   
   // slice
   // Instructions : I4, I5
   test_module test
     (
      // Inputs
      .in_x(w_sum1),
      .in_y(carry_in),
      // End of inputs
      // Outputs
      .out_sum(sum_out),
      .out_carry(w_carry2)
      // End of outputs
      );

   // slice 
   // default_slice             
endmodule 
