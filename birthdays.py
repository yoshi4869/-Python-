birthdays = {' アリス': '4/ 1', 'ボブ': '12/ 12', 'キャロル': '4/ 4'} #
while True: 
    print(' 名前 を 入力 してください: (終了 するには Enter だけ 押 してください)') 
    name = input()
    if name == '':
         break
    if name in birthdays: # 
        print( name + 'の 誕生日 は' + birthdays[ name]) 
    else:
        print( name + 'の 誕生日 は 未登録 です。') 
        print(' 誕生日 を 入力 してください:') 
        bday = input()
        birthdays[name] = bday # ❹ 
        print(' 誕生日 データベース を 更新 しました。')

