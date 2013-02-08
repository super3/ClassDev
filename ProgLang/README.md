Programming Languages - Assignment 1
=========
A program to read in an initial file of strings to start with and another operation file to run on the input file

Operations
---
* `?` Check if a string is in the first file.
* `+` Insert a string into the list.
* `-` Remove a string fro the list.
* `*` Print all strings one-by-one.

Algorithm 
---
1. Initialize FileOp object. Pass initial and operation file.

        obj = FileOp('initial_file.txt', 'operation_file.txt')
        
2. Constructor loads in the initial and operation text files into a list structure, and sets both to internal object data. Supported by a function to load the text file into the list structure.
    
        FileOp.table = FileOp.in_file(path_to_initial_file)
		FileOp.op_table = FileOp.in_file(path_to_operation_file)

3. Perform run method on FileOp object. Pass output file.

        obj.run('result.txt')
        
4. Iterate though the list, and isolate the first character, which will be the operation character. Compare this character with our allowed operations. If a valid operation is found then use one of the object's methods to do the operation as well as return the correct output string. Append this all to the final output string.

        for line in FileOp.table:
			if line[first_character] == "operation_character":
				output_string += word.strip('\n').add_padding() + " "
                output_string += FileOp.operation("word")
                
5. Run method saves output_string to the result file. Supported by a function to save a string to a text file.

        FileOp.out_file(outfile, output)
       
Unit Testing
---
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis gravida quam sed sagittis. Aliquam rutrum ullamcorper porttitor. Fusce semper tellus non leo commodo facilisis. Mauris vestibulum tortor elementum neque vestibulum convallis. Morbi tincidunt feugiat vehicula. Duis faucibus arcu at erat lacinia eu mollis odio varius. Vivamus cursus gravida dui, in consequat libero cursus vitae. 