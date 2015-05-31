// Full Adder rtl

module full_adder (a0, b0, c0, a1, b1, c_out, s_out, s2, s3);

	// Inputs_top
	input  a0;
	input  b0;
	input  c0;
	// End of inputs_top	

	// Outputs_top
	output s1;
	output c_out;
	output s_out;
	// End of outputs_top	

	// Wires
	wire   c1;
	wire   c2;
	wire   s1;
	wire   d1;
	wire   c3;

	// Some assignments
	assign carry_out = c1 | c2;
	assign s_out = s1;
	//assign d_out = d1;

	// Instantiating two half-adders to make the circuit.

	// Module instantiation
	half_adder u1_half_adder (
				 // Inputs
				 .in_x(a0),
				 .in_y(b0),
				 // End of inputs
				 // Outputs
				 .out_sum(s0),
				 .out_carry(c1)
				 // End of outputs
				 );                    

	// Module instantiation
	half_adder u2_half_adder ( 	
				// Inputs
				.in_x(s0),
				.in_y(c0),
				// End of inputs
				// Outputs
				.out_sum(s1),
				.out_carry(c2)
				// End of outputs
				);                    

	// Module instantiation

	// Module instantiation
	test2 test2 (
		// Inputs
		.in_1(d1),
		.in_2(c3),
		.in_3(b1),
		// End of inputs
		// Outputs
		.out_1(s3)
		// End of outputs
		);

endmodule 
