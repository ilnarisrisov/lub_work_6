while True:
    try:
        number_of_criteria = int(input('\nВведите количество критериев: '))
        break
    except ValueError:
        print('\nВведено, вероятно, не целое число, попробуйте ввести натуральное')

def weight_of_criteria(number_of_criteria):

    weight_of_criteria_for_cycle = []

    for i in range(number_of_criteria):
        row = []
        for j in range(number_of_criteria):
            while True:
                try:
                    criteria_weights = float(input('Введите попарное сравнение для критерия ' + str(i+1) + ' и ' + str(j+1) + ': '))
                    break
                except ValueError:
                    print('Введено не число, попробуйте что-то другое')
            row.append(criteria_weights)
        weight_of_criteria_for_cycle.append(row)
    return weight_of_criteria_for_cycle

def calculation_of_weight_coefficients(weight_of_criteria_for_cycle):
    number_of_criteria = len(weight_of_criteria_for_cycle)
    weight = []
    for i in range(number_of_criteria):
        pre_result = 1
        for j in range(number_of_criteria):
            pre_result = pre_result * weight_of_criteria_for_cycle[i][j] / sum(weight_of_criteria_for_cycle[i])
        weight.append(pre_result)
    end_result = sum(weight)
    weight = [criteria_weights / end_result for criteria_weights in weight]
    return weight

weight_of_criteria_for_cycle = weight_of_criteria(number_of_criteria)
weight = calculation_of_weight_coefficients(weight_of_criteria_for_cycle)

print('\nВесовые коэффициенты: ')
for i, criteria_weights in enumerate(weight):
    print(f"\nКритерий {i + 1}: {criteria_weights:.2f}")