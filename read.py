data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案已讀取完畢,總共有:', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))
	

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')

good = [d for d in data if 'good' in d]

#文字計數
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Jocelyn'])

while True:
	word = input('請問您要查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用此留言查詢功能')
