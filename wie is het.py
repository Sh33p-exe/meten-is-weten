Geel = input('Is de kaas geel? ')
if Geel == 'ja': 
    Gaten = input('Zitten er gaten in? ')
    if Gaten == 'ja':
        Duur = input('Is de kaas belachelijk duur? ')
        if Duur == 'ja':
            print('Emmenthaler')
        elif Duur == 'nee':
            print('Leerdammer')
    elif Gaten == 'nee':
        Hard = input('Is de kaas hard als steen? ')
        if Hard == 'ja':
            print('Pamigiano Reggiano')
        elif Hard == 'nee':
            print('Goudse kaas')
elif Geel == 'nee':
    Schimmel = input('Heeft de kaas blauwe schimmels? ')
    if Schimmel == 'ja':
        Korst = input('Heeft de kaas een korst? ')
        if Korst == 'ja':
            print('Bleu de Rochbaron')
        elif Korst == 'nee':
            print('Foume d\'Ambertt')
    elif Schimmel == 'nee':
        Korst2 = input('Heeft de kaas een korst? ')
        if Korst2 == 'ja':
            print('Camembert')
        elif Korst2 == 'nee':
            print('Mozzarella')