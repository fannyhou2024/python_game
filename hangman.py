import streamlit
import random
import hangman_art
import hangman_words

#https://pypi.org/project/art/
# import art
# print(art.text2art("Frankie"))

print(hangman_art.logo)
word = hangman_words.word_list
answer = word[random.randint(0, len(word))]
#print(random.choice(word))
#print(random.shuffle((word)))

print(answer)
stage1 = hangman_art.stages
stage1.reverse()
word_list=[]
#print("Answer is : ", answer)

def create_list():
    for i in range(len(answer)):
        word_list.append("_")

def start_game(char):
    found=False
    for i in range(len(answer)):
        if answer[i]==char:
           word_list[i]=char
           found=True
    if found:
        if word_list.count("_")==0:#Bingo
           return 0
        else:
           print(" Corrected !", word_list)
           return 1
    else:
        return -1

fail_cnt=0
game=True
create_list()
while game:
    letter = input("It has " + str(len(answer)) + " words, please guess the letter or q to quit !")
    if letter=="q":
        game=False
    else:
        result = start_game(letter)
        if result<0:
           if fail_cnt<6:
               print(" Incorrect !!!", stage1[fail_cnt])
               fail_cnt+=1
           else:
               print(hangman_art.gameover," Answer is :" + answer, stage1[fail_cnt])
               game=False
        else:
            if result==0:##Bingo
                print(hangman_art.bingo)#, 'You are answer : ', ''.join(word_list))
                game=False





