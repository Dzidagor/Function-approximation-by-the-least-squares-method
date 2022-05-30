from sympy import Symbol, solve
import matplotlib.pyplot as plt


#inp_x_lst_test = [0.78, 1.56, 2.34, 3.12, 3.81]
#inp_y_lst_test = [2.50, 1.20, 1.12, 2.25, 4.28]
#inp_m_test = 2

inp_x_lst = [0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05, 1.2, 1.35, 1.5,
             1.65, 1.8, 1.95, 2.1, 2.25, 2.4, 2.55, 2.7, 2.85, 3.0]
inp_y_lst = [4.01, 4.06, 3.88, 3.98, 4.36, 4.18, 4.16, 4.51, 4.53, 4.38,
             4.76, 4.66, 4.82, 4.77, 5.12, 5.23, 5.40, 5.84, 5.86, 6.01]
inp_m = 4


def least_squares_method(x_lst, y_lst, m):
    x_deg_lst = [[1 for _ in range(len(x_lst))], x_lst]
    for i in range(2, 2*m + 1):
        x_deg_lst.append([round((x**i), 3) for x in x_lst])
    sum_x_deg_lst = [sum(i) for i in x_deg_lst]

    mul_x_y_lst = [y_lst]
    for k in range(1, m + 1):
        mul_x_y_lst.append([round((x_lst[i]**k)*y_lst[i], 3) for i in range(len(x_lst))])
    sum_mul_x_y_lst = [round(sum(i), 3) for i in mul_x_y_lst]

    try:
        deg_1_model = [f'{sum_x_deg_lst[deg]} * a0 + {sum_x_deg_lst[deg + 1]} * a1 - {sum_mul_x_y_lst[deg]}' for deg in
                       range(2)]
        deg_2_model = [
            f'{sum_x_deg_lst[deg]} * a0 + {sum_x_deg_lst[deg + 1]} * a1 + {sum_x_deg_lst[deg + 2]} * a2 - {sum_mul_x_y_lst[deg]}'
            for deg in range(3)]
        deg_3_model = [
            f'{sum_x_deg_lst[deg]} * a0 + {sum_x_deg_lst[deg + 1]} * a1 + {sum_x_deg_lst[deg + 2]} * a2 + {sum_x_deg_lst[deg + 3]} * a3 - {sum_mul_x_y_lst[deg]}'
            for deg in range(4)]
        deg_4_model = [
            f'{sum_x_deg_lst[deg]} * a0 + {sum_x_deg_lst[deg + 1]} * a1 + {sum_x_deg_lst[deg + 2]} * a2 + {sum_x_deg_lst[deg + 3]} * a3 + {sum_x_deg_lst[deg + 4]} * a4 - {sum_mul_x_y_lst[deg]}'
            for deg in range(5)]
    except IndexError:
        pass

    if m >= 1:
        a0 = Symbol('a0')
        a1 = Symbol('a1')
        solution_1 = solve(deg_1_model, (a0, a1))
        print(solution_1)
    if m >= 2:
        a0 = Symbol('a0')
        a1 = Symbol('a1')
        a2 = Symbol('a2')
        solution_2 = solve(deg_2_model, (a0, a1, a2))
        print(solution_2)
    if m >= 3:
        a0 = Symbol('a0')
        a1 = Symbol('a1')
        a2 = Symbol('a2')
        a3 = Symbol('a3')
        solution_3 = solve(deg_3_model, (a0, a1, a2, a3))
        print(solution_3)
    if m >= 4:
        a0 = Symbol('a0')
        a1 = Symbol('a1')
        a2 = Symbol('a2')
        a3 = Symbol('a3')
        a4 = Symbol('a4')
        solution_4 = solve(deg_4_model, (a0, a1, a2, a3, a4))
        print(solution_4)

    try:
        y1_lst = [solution_1[a0] + x*solution_1[a1] for x in x_lst]
        plt.ylabel('y1')
        plt.plot(x_lst, y1_lst, label='функция 1 степени')
    except NameError:
        pass
    try:
        y2_lst = [solution_2[a0] + x * solution_2[a1] + (x ** 2) * solution_2[a2] for x in x_lst]
        plt.ylabel('y1, y2')
        plt.plot(x_lst, y2_lst, label='функция 2 степени')
    except NameError:
        pass
    try:
        y3_lst = [solution_3[a0] + x * solution_3[a1] + (x ** 2) * solution_3[a2] + (x ** 3) * solution_3[a3] for x in x_lst]
        plt.ylabel('y1, y2, y3')
        plt.plot(x_lst, y3_lst, label='функция 3 степени')
    except NameError:
        pass

    try:
        y4_lst = [solution_4[a0] + x * solution_4[a1] + (x ** 2) * solution_4[a2] + (x ** 3) * solution_4[a3] + (x ** 4) * solution_4[a4] for x in x_lst]
        plt.ylabel('y1, y2, y3, y4')
        plt.plot(x_lst, y4_lst, label='функция 4 степени')
    except NameError:
        pass

    plt.xlabel('x')
    plt.grid()
    plt.legend()
    plt.show()


#least_squares_method(inp_x_lst_test, inp_y_lst_test, inp_m_test)
least_squares_method(inp_x_lst, inp_y_lst, inp_m)