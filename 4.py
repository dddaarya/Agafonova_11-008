def salt_lang(string):
  a = "аоуыэяюёиеАОУЫЭЯЮЁИЕ"
  b = str()
  for i in range(len(string)):
    if (string[i] in a):
        b += string[i] + "с" + string[i]
    else:
        b += string[i]
return b

print(salt_lang("Привееет! Как Дела?"))
