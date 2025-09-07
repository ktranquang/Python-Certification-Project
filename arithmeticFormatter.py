def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems (more than 5)
    if len(problems) > 5:
         return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        elements = problem.split()
        first_number = elements[0]
        operator = elements[1]
        second_number = elements[2]
        
        # Check operator is '+' or '-'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        # Check number should only contain digits
        elif not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        max_length_operand = max(len(first_number), len(second_number))
        print(max_length_operand)

        if(len(first_number) > len(second_number)):
            longest_width = len(first_number)
            first_line.append(f'  {first_number}')
            print(longest_width)
            print(len(second_number))
            second_line.append(operator + " " * (longest_width) + second_number) 
            print(first_line)
            print(second_line)
    return '\n'.join(first_line) + '\n' + '\n'.join(second_line) + '\n' + '\n'.join(dashes_line) + '\n' + '\n'.join(answers_line)

#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print('  3801      123\n-    2    +  49\n------    -----')


