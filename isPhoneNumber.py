def is_phone_number(text):
    if len(text) != 12:#文字列がピッタリ12文字になっているかを調べる
        return False
    for i in range(0,3):
        if not text[i].isdecimal():#最初の3桁が数字だけかを調べる
            return False
    if text[3] != '-':#4桁目がハイフンになっていることを調べる
        return False
    for i in range(4,7):
        if not text[i].isdecimal():#3桁の数字が続くこと
            return False
    if text[7] != '-':#ハイフンが来ること
        return False
    for i in range(8,12):
        if not text[i].isdecimal():#最後に4桁の数字があること
            return False
    return True #すべて一致すればOK

print('415-555-4242は電話番号：')
print(is_phone_number('415-555-4242'))
print('Moshi moshiは電話番号：')
print(is_phone_number("Moshi moshi"))