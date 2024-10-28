def arithmetic_arranger(problems, show_answers=False):

    # Check if there are more than five problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Check if the problems include only addition or subtraction
    for problem in problems:
        if not "+" in problem and "-" not in problem:
            return "Error: Operator must be '+' or '-'."

    # Check if operands contain only digits
    for problem in problems:
        for char in problem:
            if char.isdigit() or char in ["+", "-", " "]:
                continue
            else:
                return "Error: Numbers must only contain digits."

    # Check if operands are no longer than four digits
    for problem in problems:
        for operand in problem.split(" "):
            if len(operand) > 4:
                return "Error: Numbers cannot be more than four digits."

    # Initialize lists to store formatted parts of each problem
    first_operands = []
    second_operands = []
    separators = []
    results = []

    for problem in problems:
        # Split each problem into its components
        first_operand, operator, second_operand = problem.split()

        # Calculate the width needed for formatting (max length of operands + 2)
        width = max(len(first_operand), len(second_operand)) + 2

        # Perform the arithmetic operation
        if operator == "+":
            result = int(first_operand) + int(second_operand)
        else:
            result = int(first_operand) - int(second_operand)

        # Format and store the result
        results.append(f"{result:>{width}}")

        # Format and store the first operand
        first_operands.append(f"{first_operand:>{width}}")

        # Format and store the operator and second operand
        second_operands.append(f"{operator} {second_operand:>{width-2}}")

        # Create and store the separator line
        separators.append("-" * width)

    # Prepare the output
    output = []
    output.append("    ".join(first_operands))
    output.append("    ".join(second_operands))
    output.append("    ".join(separators))

    # If show_answers is True, add the results to the output
    if show_answers:
        output.append("    ".join(results))

    # Join all lines of the output with newline characters
    return "\n".join(output)


# Test the function with a set of problems
print(
    arithmetic_arranger(
        ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
    )
)
