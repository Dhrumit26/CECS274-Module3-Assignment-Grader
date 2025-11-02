def uses_sll(input_file):
    try:
        # Open the input .py file in read mode
        with open(input_file, 'r') as f:
            # Read the contents of the .py file
            py_content = f.read()
            f.close()

        # Open the output .txt file in write mode
        with open("temp.txt", 'w') as f:
            # Write the contents into the .txt file
            f.write(py_content)
            f.close()

        print(f"Conversion successful: {input_file} converted to tempt.txt")
        initialized_sll = False
        initialized_arr = False
        with open("temp.txt", 'r') as f:
            for line in f.readlines():
                print(line.strip(), end="\t\t")
                if "SLLStack()" in line and "#" not in line:
                    print("<=== USING SLLStack")
                    initialized_sll = True
                if "ArrayStack()" in line and "#" not in line:
                    initialized_arr = True
                    print("<=== USING ArrayStack")
                print()
        f.close()
        return initialized_sll and not initialized_arr
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return