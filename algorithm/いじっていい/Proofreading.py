# def preefreadin(text:str):
# 	ans=""
# 	i=0
# 	while i!=len(text)-1:
# 		flg=False
# 		if text[i]=='{':
# 			open_mark_count=1
# 			ans+='{'
# 			i+=1
# 			while i!=len(text)-1:
# 				## 通常
# 				if text[i]=='}':
# 					flg=True
# 					ans+='}'
# 					break
# 				## オワコン
# 				if text[i]=='{':
# 					break
# 				ans+=text[i]
# 				i+=1
# 			i+=1
# 			if not flg:
# 				count=0
# 				while i!=len(text)-1 and count!=2:
# 					if text[i]=='}':
# 						count+=1
# 					else:
# 						ans+=text[i]
# 					i+=1
# 				ans+='}'
# 		else:
# 			ans+=text[i]
# 			i+=1
# 	return ans
				
def preefreadin(text):
	open_mark=0
	ans=""
	for ch in text:
		if ch=='{':
			## 通常
			if open_mark==0:
				ans+='{'
			open_mark+=1
		elif ch=='}':
			## 通常
			if open_mark==1:
				ans+='}'
			open_mark-=1
		else:
			ans+=ch
	return ans
		


if __name__ == "__main__":
	text = "{ハードウェア}については{演算処理装置}の高速化や搭載量の拡大や演算時の{メモリ搭載量}の大容量化や高速化や{{演算処理装置}間}での{メモリ共有方式}が特徴的である他に{ベクトル計算}に特有の{演算処理装置}を備える等取り扱われる演算に特有のハードウエア方式が採用されることがあるまた高い計算能力は演算処理を担う電子回路の大規模高速な{スイッチング動作}により実現されるため大量の電力消費と発熱に対応した電源設備や排熱冷却機構が必要である"
	#このtextの{A{B}C}となっているところを{ABC}に直す(※{ABC}は{ABC}のままで)
	# text = "{{演算{処理}装置}間}での{メモリ共有方式}aaa"

	# print(preefreadin(text))
	print(preefreadin(text))