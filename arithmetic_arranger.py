def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ''
    second_line = ''
    lines = ''
    sum_line = ''
    for i, problem in enumerate(problems):
        num1, op, num2 = problem.split()

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if op == '+':
            sum = str(int(num1) + int(num2))
        else:
            sum = str(int(num1) - int(num2))

        length = max(len(num1), len(num2)) + 2
        top = str(num1).rjust(length)
        bottom = op + str(num2).rjust(length - 1)
        line = ''
        res = str(sum).rjust(length)
        for s in range(length):
            line += '-'

        if i < len(problems) - 1:
            first_line += top + '    '
            second_line += bottom + '    '
            lines += line + '    '
            sum_line += res + '    '
        else:
            first_line += top
            second_line += bottom
            lines += line
            sum_line += res

    if answers:
        arranged_problems = first_line + '\n' + second_line + '\n' + lines + '\n' + sum_line
    else:
        arranged_problems = first_line + '\n' + second_line + '\n' + lines

    return arranged_problems
