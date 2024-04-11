# date : 2024-01-19
# desc : 파일 쓰기

# f = open('./Day05/test02.txt', mode='w', encoding='utf-8')
f = open('./Day05/test02.txt', mode='a', encoding='utf-8')

f.write('나는 한국사람입니다.\n')
f.write('그런데 김치를 싫어해요.\n')

f.close()