def arithmetic_arranger(problems, show_answers=False):


    # Raise error if there are more than five problems
    if len(problems) > 5:
        return "Error: Too many problems." 
        
    
    # Raise error if the problems include multiplication or division
    for problem in problems:
        if not '+' in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
                 
    # Raise error if operands contain something different that numbers:
    for problem in problems:     
        for char in problem:
            if char.isdigit() or char in ['+', '-', ' ']:
                continue
            else:
                return "Error: Numbers must only contain digits."
                
                

    # Raise error if operands are longer than four digits
    for problem in problems:
        for operand in problem.split(' '):
            if len(operand) > 4:
                return "Error: Numbers cannot be more than four digits."
                
                
    
    # Compute arithmetic of operands
    first_operands = []
    second_operands = []
    separators = []
    results = []


    for problem in problems:
        
        first_operand, operator, second_operand = problem.split()
        width = max(len(first_operand), len(second_operand)) + 2

        if operator == '+':
            result = int(first_operand) + int(second_operand)
        else:
            result = int(first_operand) - int(second_operand)
        
        results.append(f"{result:>{width}}")

        
        first_operands.append(f"{first_operand:>{width}}")
        second_operands.append(f"{operator} {second_operand:>{width-2}}")
        separators.append('-' * width)
        
    
    output = []
    output.append("    ".join(first_operands))
    output.append("    ".join(second_operands))
    output.append("    ".join(separators))
    
    print("    ".join(first_operands))
    print("    ".join(second_operands))
    print("    ".join(separators))
    
    if show_answers:
        output.append("    ".join(results))
    
    return "\n".join(output)

arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) 
