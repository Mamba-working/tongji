import re
def get_file(path):
    file = open(path, 'r',encoding='utf-8')
    #words = file.read().replace('\n','').replace('，','').replace('。','').replace('、','')
    string = ''
    flag = 0
    while flag == 0:
        line = file.readline()
        if len(line) >6:
            #line=line.replace('。','').replace('，','').replace('/','').replace('、','').replace('“','').replace('”','').replace('：','').replace('（','').replace('）','').replace('；','')
            string=string + line
        if line =='':
            flag = 1
    file.close()
    return string

def count(st,path,path2):
    count_dic1={}
    count_dic2={}
    st2 = re.split('[，。“”；：、（）＿！*？＊?＜\n]',st)
   # st3 = re.sub('【.*?】','',temp)

    for word in st2:
       word = word.replace('□','').replace(' ','')
       point = 0
       word1 = re.sub('【.*?】','',word)
       final = len(word1)
       while point <final:

              if word[point] in count_dic1.keys():
                  count_dic1[word[point]] = count_dic1[word[point]] + 1
              else:
                  count_dic1[word[point]] = 1
              point = point + 1

       point = 0
       while point < final -1 :

               if word1[point:point + 2] != '【 www.txtbbs.com ， TXT论坛，TXT BBS，搜刮各类TXT小说。欢迎您来推荐好书！】':
                   if word1[point:point + 2] in count_dic2.keys():
                       count_dic2[word1[point:point + 2]] = count_dic2[word1[point:point + 2]] + 1
                   else:
                       count_dic2[word1[point:point + 2]] = 1
                   point = point + 1



    file2 = open(path,'w',encoding='utf8')
    count_list2=sorted(count_dic2.items(),key=lambda items:items[1],reverse=True)
    count_list1 = sorted(count_dic1.items(), key=lambda items: items[1], reverse=True)
    for i in count_list2:
          file2.write(str(i)+'\n')
    file2.close()
    file1= open(path2,'w',encoding='utf-8')
    for i in count_list1:
            file1.write(str(i)+'\n')






count(get_file('E://learning//ci1.txt'),'E://learning//2.txt','E://learning//1.txt')
#print(get_file('E://learning//ci1.txt'))