from collections import Counter
import pandas as pd
from chempy import Substance


def main():
    # Reading from User
    leaving = Substance.from_formula('H2O')
    # Reading of conjungates CSV
    data = pd.read_csv('conjugates_input.csv', index_col=0, skipinitialspace=True)
    formula = data["formula"]
    conjugate = data["conjugate"]
    # Creating od necessary variables
    formula_list = []
    conjugate_list = []
    # Creating of two lists
    for position in formula:
        conjungate1 = Substance.from_formula(position)
        for x in formula:
            conjungate2 = Substance.from_formula(x)
            dict_formula = dict(Counter(conjungate1.composition) + Counter(conjungate2.composition) - Counter(leaving.composition))
            formula_list.append(dict_to_formula(dict_formula))
    for cona in conjugate:
        firstcon = cona
        for conb in conjugate:
            secondcon = conb
            conjugate_list.append(firstcon + '-' + secondcon)
    results_to_csv(conjugate_list, formula_list)


def results_to_csv(conjugate_list, formula_list):
    summon_list = []
    for i in range(0, len(conjugate_list)):
        summon_list.append([conjugate_list[i], formula_list[i]])
    summon_df = pd.DataFrame.from_records(summon_list, columns=('Name', 'Formula'))
    summon_df.to_csv('readyforpcdl.csv', index=False)


def dict_to_formula(y: dict):
    p = ''
    for item in y:
        if item == 1:
            p = p + 'H' + str(y[item])
        elif item == 6:
            p = p + 'C' + str(y[item])
        elif item == 7:
            p = p + 'N' + str(y[item])
        elif item == 8:
            p = p + 'O' + str(y[item])
        elif item == 9:
            p = p + 'F' + str(y[item])
        elif item == 11:
            p = p + 'Na' + str(y[item])
        elif item == 15:
            p = p + 'P' + str(y[item])
        elif item == 16:
            p = p + 'S' + str(y[item])
        elif item == 17:
            p = p + 'Cl' + str(y[item])
        elif item == 19:
            p = p + 'K' + str(y[item])
        elif item == 35:
            p = p + 'Br' + str(y[item])
        elif item == 53:
            p = p + 'I' + str(y[item])
        else:
            print('Element not in Database!')
    return p


if __name__ == "__main__":
    main()
    print('Done... BITCH')
