import random

word = ["piano", "gatoo", "pular", "livro", "canto", "falar", "tocar", "plano", "festa", "pesar"]
secret_word = random.choice(word).upper()

trys = 6

for tentativas in range(1,trys+1):
    print(f'{tentativas} de {trys}')
    user_word = input('DIGITE UMA PALAVRA DE 5 LETRAS').upper()
    array = []

    if len(user_word) != 5:
        print('DIGITE EXATAMENTE 5 CARACTERES')
    else:
        for i in range(5):
            if user_word[i] == secret_word[i]:
                array.append(f'[{user_word[i]}]')
            elif user_word[i] in secret_word:
                array.append(f'({user_word[i]})')
            else:
                array.append(user_word[i])
                
    print(" ".join(array))

    if user_word == secret_word:
        print('VOCÊ ADIVINHOU A PALAVRA')
        break
else:
    print('SUAS TENTATIVAS ACABARAM')
    print(f'A PALAVRA ERA {secret_word}')
            
    
        

