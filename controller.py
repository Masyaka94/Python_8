import view

def controller():
    chislo_1, chislo_2, oper = view.get_value()
    match oper:
        case '+': return(chislo_1 + chislo_2)
        case '-': return(chislo_1 - chislo_2)
        case '*': return(chislo_1 * chislo_2)
        case '/': return(chislo_1 / chislo_2)
        case '**': return(chislo_1 ** chislo_2)