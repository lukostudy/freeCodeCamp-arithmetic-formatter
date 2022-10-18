def arithmetic_arranger(problems, print_res = False):

    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    arranged_line_1 = ""
    arranged_line_2 = ""
    arranged_line_3 = ""
    arranged_line_4 = ""
  
    for problem in problems:
        
        # checking if the input is correct

        problem_elements = problem.split(" ")
        if len(problem_elements) != 3:
            return "Error: Incorrect format."

        left_number = problem_elements[0].strip()
        right_number = problem_elements[2].strip()
        operator = problem_elements[1].strip()

        if operator not in {"+", "-"}:
            return "Error: Operator must be '+' or '-'."

        if len(left_number) > 4 or len(right_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        try:
            left_int = int(left_number)
            right_int = int(right_number)
        except:
            return "Error: Numbers must only contain digits."
        
        # checking finished - it's ok
        # proceeding with calculating the result and formatting the lines
        
        result = left_int + right_int if operator == "+" else left_int - right_int

        number_length = max(len(left_number),len(right_number))
        arranged_line_1 += (2 + number_length - len(left_number)) * " " + left_number + 4 * " "
        arranged_line_2 += operator + " " + (number_length - len(right_number)) * " " + right_number + 4 * " "
        arranged_line_3 += (number_length + 2) * "-" + 4 * " "
        arranged_line_4 += (2 + number_length - len(str(result))) * " " + str(result) + 4 * " "

    arranged_line_1 = arranged_line_1.rstrip()
    arranged_line_2 = arranged_line_2.rstrip()
    arranged_line_3 = arranged_line_3.rstrip()
    arranged_line_4 = arranged_line_4.rstrip()
    arranged_problems = arranged_line_1 + "\n" + arranged_line_2 + "\n" + arranged_line_3
    if print_res:
        arranged_problems += "\n" + arranged_line_4

    return arranged_problems

