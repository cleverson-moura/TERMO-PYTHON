import random

word = ["piano", "gatoo", "pular", "livro", "canto", "falar", "tocar", "plano", "festa", "pesar"]
secret_word_one = random.choice(word).upper()
secret_word_two = random.choice(word).upper()

def termo(secret_word,array,i):
    if user_word[i] == secret_word[i]:
        array.append(f'[{user_word[i]}]')
    elif user_word[i] in secret_word:
        array.append(f'({user_word[i]})')
    else:
        array.append(user_word[i])

trys = 10
res_array_one = []
res_array_two = []

for tentativas in range(1,trys + 1):
    print(f'{tentativas} de {trys}')
    user_word = input('DIGITE UMA PALAVRA DE 5 LETRAS').upper()

    array_one = []
    array_two = []

    if len(user_word) != 5:
        print('DIGITE EXATAMENTE 5 CARACTERES')
        continue
    
           
    if not res_array_one:
        for i in range(5):
            termo(secret_word_one,array_one,i)
    if not res_array_two:
        for i in range(5):
            termo(secret_word_two,array_two,i)
                
    print("Palavra 1:" + " ".join(array_one))
    print("Palavra 2:" + " ".join(array_two))
    
    if not res_array_one and user_word == secret_word_one:
            print('VOCÊ ADIVINHOU A PALAVRA 1')
            res_array_one = array_one

    if not res_array_two and user_word == secret_word_two:
            print('VOCÊ ADIVINHOU A PALAVRA 2')
            res_array_two = array_two

    if res_array_two and res_array_two:
        print('VOÇÊ ADIVINHOU AS DUAS PALVARAS')
        print(f'Palavra 1: {"".join(res_array_one)}')
        print(f'Palavra 2: {"".join(res_array_two)}')
        break
else:
    print('SUAS TENTATIVAS ACABARAM')
    print(f'AS PALAVRAS ERAM {secret_word_one} e {secret_word_two}')