
#Дана строка -  текст заклинания, заканчивающийся точкой. Необходимо зашифровать 
# его по следующему правилу. Сначала определить длину самого короткого слова 
# в тексте и обозначить полученное число как K. Затем заменить каждую английскую
# букву в тексте на букву, которая находится в английском алфавите на K позиций ранее. 
# При этом строчные буквы остаются строчными, а прописные - прописными. 
# Остальные символы остаются неизменными. Программа должна вывести на экран
# текст зашифрованного заклинания. Например, если исходный текст был таким:
#Zb Ra Ca Dab Ra. 
#то результат шифровки должен быть следующий:
#Xz Py Ay Byz Py.



def shift_char(char, shift):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    else:
        return char


def encrypt_spell(str1):
    words = str1.split()
    min_len = min(len(word) for word in words if word.isalpha())
    encrypted_text = ''.join(shift_char(char, min_len) for char in str1)
    return encrypted_text


str1 = input("Введите текст заклинания: ")


encrypt_str1 = encrypt_spell(str1)
print("Зашифрованное закливание: ", encrypt_str1)
