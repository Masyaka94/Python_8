import user_input

def view_data(data, res):
    title = (f'{user_input.chislo_1} {user_input.oper} {user_input.chislo_2}')
    print(f'{res} {title} = {data}')

def get_value():
    return user_input.inp2()