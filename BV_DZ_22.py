# BV_DZ
# Бандик Вячеслав
# bvii@mail.ru
# 19.05.2003
#
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Alphabet: ", end="")
        for letter in self.letters:
            print(letter, end=" ")
        print("")

    def letters_num(self):
        return len(self.letters)

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв алфавита
# (можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, lang='En'):
        super().__init__(lang)
        self.alphabet = string.ascii_uppercase

    @staticmethod
    def is_en_letter(letter):
        return letter in string.ascii_uppercase

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."





english_alphabet = Alphabet("English", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
english_alphabet.print()  # Alphabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
print("Number of letters:", english_alphabet.letters_num())  # Number of letters: 26
