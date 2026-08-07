def unit_test_cpu(instructions, expected, test_i):
    global register_file
    original_rf = register_file.copy()

    with open("riscv_code.txt", "w") as riscv_code:
        riscv_code.writelines('\n'.join(instructions))
    
    #main()

    try:
        for reg_i, exp_val in expected:
            assert register_file[reg_i] == exp_val

    except AssertionError:
        print(f"Test {test_i+1} failed.")
        print(f"Expected: x[{reg_i}] = {exp_val:#010x}")
        print(f"Got:      x[{reg_i}] = {register_file[reg_i]:#010x}")
        raise AssertionError
    
    finally:
        register_file = original_rf.copy()

    
def test_cpu():
    tests = [
        ( 
            [   # Test 1 
                "add x5, x5, x5",
                "add x6, x5, x0"
            ],

            [   # Expected 1 (register index, value)
                (5, 0x20020000),
                (6, 0x20020000)
            ]
        ),

        ( 
            [   # Test 2
                "lw x5, 0(x6)",
                "sw x5, 8(x6)",
                "add x5, x5, x5",
                "sub x6, x30, x31"
            ],

            [   # Expected 2 
                (5, 0x00032283),
                (6, 0x108ec168)
            ]
        ),

        ( 
            [   # Test 3
                "and x5, x0, x30",
                "or x6, x30, x31",
                "or x7, x5, x6",
                "sub x30, x7, x6"
            ],

            [   # Expected 3
                (5, 0x00000000),
                (6, 0x11aec2b8),
                (7, 0x11aec2b8),
                (30, 0x00000000)
            ]
        ),

        ( 
            [   # Test 4
                "sw x30, 12(x5)",
                "lw x6, 0(x18)",
                "or x6, x6, x0"
            ],

            [   # Expected 4
                (6, 0x112ec218),
                (30, 0x112ec218)
            ]
        ),

        ( 
            [   # Test 5
                "sw x29, 20(x5)",
                "add x27, x5, x22",
                "lw x7, 0(x27)",
                "sub x7, x0, x7",
                "sub x7, x0, x7",
                "or x7, x7, x7",
                "add x6, x7, x0",
                "and x5, x20, x6"
            ],

            [   # Expected 5
                (5, 0x12000000),
                (6, 0x1200ffff),
                (7, 0x1200ffff),
                (27, 0x10010014),
                (29, 0x1200ffff)
            ]
        ),
    ]

    for i, (instructions, expected) in enumerate(tests):
        try:
            unit_test_cpu(instructions, expected, i)
        except AssertionError:
            return
        else:
            print(f"Test {i+1} passed.")

    print("All tests passed!")


test_cpu()