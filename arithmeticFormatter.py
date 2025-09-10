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
        first_number, operator, second_number = elements
     
        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        # Validate digits
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        # Validate number length
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Get width (max length of operands + 2 for operator and space)
        max_length = max(len(first_number), len(second_number)) + 2

        # Format each line
        first_line.append(f'{first_number:>{max_length}}')
        second_line.append(f'{operator} {second_number:>{max_length-2}}')
        dashes_line.append('-' * max_length)

        # Calculate and format answer if show_answers is True
        if show_answers:
            if operator == '+':
                result = int(first_number) + int(second_number)
            else:
                result = int(first_number) - int(second_number)
            answers_line.append(f'{result:>{max_length}}')

    # Join lines with 4 spaces between problems    
    result = '    '.join(first_line) + '\n' + '    '.join(second_line) +'\n' + '    '.join(dashes_line)
    if show_answers:
        result += '\n' + '    '.join(answers_line)

    return result

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
