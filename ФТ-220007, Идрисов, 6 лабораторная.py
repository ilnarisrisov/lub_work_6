while True:
    try:
        number_of_criteria = int(input('\nВведите количество критериев: '))
        break
    except ValueError:
        print('\nВведено, вероятно, не целое число, попробуйте ввести натуральное')

def weight_of_criterias(number_of_criteria):

    matrix = [[0 for _ in range(number_of_criteria)] for _ in range(number_of_criteria)]

    for i in range(number_of_criteria):
        for j in range(number_of_criteria):
            if i == j:
                matrix[i][j] = 1
            elif j < i:
                matrix[i][j] = 1 / matrix[j][i]
            else:
                criteria_weights = 0
                while criteria_weights == 0:
                    try:
                        criteria_weights = float(input(f"\nВведите попарное сравнение для критериев {i} и {j}: "))
                        break
                    except ValueError:
                        print('\nВведено не число, попробуйте что-то другое')
                matrix[i][j] = criteria_weights

    weights = [1 for _ in range(number_of_criteria)]
    for i in range(number_of_criteria):
        for j in range(number_of_criteria):
            weights[i] *= matrix[i][j]
        weights[i] **= 1 / number_of_criteria

    totale = sum(weights)
    round_criteria_weights = [round(criteria_weights / totale, 2) for criteria_weights in weights]

    return round_criteria_weights

weights = weight_of_criterias(number_of_criteria)

print('\nВесовые коэффициенты: ')
for criteria_weights in weights:
    print(f"\n{criteria_weights:.2f}")
