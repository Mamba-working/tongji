import random

cipai = [2,2,'，',2,2,1,'，',2,2,2,'。',2,2,2,'，',2,2,2,'，',2,2,2,'。',2,2,2,'，',2,2,2,'。']
string=''
for i in cipai:
    if type(i) == int:
        if i == 1:
            file = open('E://learning//1.txt', 'r', encoding='utf-8')
            ran_num = random.randint(0, 150)
            temp = file.readlines()[ran_num].replace('\n', '')[2:3]
            string = string + temp
            file.close()
        if i == 2:
            file = open('E://learning//2.txt', 'r', encoding='utf-8')
            ran_num = random.randint(0, 150)
            temp = file.readlines()[ran_num].replace('\n', '')[2:4]
            string = string + temp
            file.close()
    else:
        string = string + i
print(string)

