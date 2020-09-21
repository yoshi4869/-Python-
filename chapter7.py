#%%
#7.3.4アスタリスクを用いた0回以上のマッチ
import re
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
mo1.group()

# %%
mo2 = bat_regex.search('The Adventures of Batwoman')
mo2.group()


# %%
mo3 = bat_regex.search('The Adventures of Batwowowowoman')
mo3.group()

# %%
#7.3.5 プラスを用いた1回以上のマッチ
#+は1回以上マッチすることを表す
import re
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batwoman')
mo1.group()
mo2 = bat_regex.search('The Adventures of Batwowowowoman')
mo2.group()
mo3 = bat_regex.search('The Adventures of Batman')
#Bat(wo)+manはwoが少なくとも1回出現する必要がある
mo3 == None
# %%
#7.3.6　波カッコを用いて繰り返し回数を指定する
ha_regex = re.compile(r'(Ha){3,5}')
mo1 = ha_regex.search('HaHaHaHaHa')
mo1.group()
mo2 == ha_regex.search('Ha')
mo2 == None #Ha{3}はHaHaHaにはマッチするが，'Ha'にはマッチしない
# %%
#7.4 貪欲マッチと非貪欲マッチ
import re
greedy_Ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_Ha_regex.search('HaHaHaHaHa')
mo1.group()
#閉じカッコの前に？をつけると最も短いものにマッチする
nongreedy_Ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_Ha_regex.search('HaHaHaHaHa')
mo2.group()
# %%
#7.5 findall()メソッド
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()


# %%
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_num_regex.findall('Cell: 415-555-9999 Work: 215-555-0000')

# %%
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phone_num_regex.findall('Cell: 415-555-9999 Work:215-555-0000')

# %%
#7.6 文字集合