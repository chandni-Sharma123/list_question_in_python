 print("welcome to bhaiyao aur bhaneo kaun banega crorepati")
# question_list=[
#     "How  many continents are there",
#     "what is capital of india?",
#     "Ng mei kaun se course padhaya jata hai?",
# ]
# option_list=[
#     ["Four","Nine","seven","Eight"],
#     ["chandigarh","bhopal","chennai","delhi"],
#     ["Software Engineering","counseling","tourism","agriculutre"]
# ]
# solution_list=[3,4,1]

# i=0
# while i<len(question_list):
#     print(question_list[i])
#     j=0
#     while j<=len(option_list):
#         print(j+1,option_list[i][j])
#         j=j+1
#     num=int(input("enter your num............."))
#     if num==solution_list[i]:
#         print("congralations  aap aaj ke vijeta hai")
#     elif num==option_list[i]:
#         print(" badhae ho you are right")

#         break

#     i=i+1













# question_list=["How many continents are there ?","What is the capital of India ?",
# "NG mei kaun se course padhaya jaata hai ? "]
# options_list=[["Four","Nine","Seven","Eight"],
# ["Chandigarh","Bhopal","Chennai","Delhi"],
# ["Software Engineering","Counseling","Tourism",
# "Agriculture"]]
# life_line=[["Seven","Eight"],["Bhopal","Delhi"],["Software Engineering","Counseling"]]
# solution_list2=[1,2,1]
# i=0
# count=0
# solution_list=[3,4,1]
# while i<len(question_list):
# 	print("Q.",i+1,question_list[i])
# 	j=0
# 	while j<len(options_list[i]):
# 		print(j+1,options_list[i][j])
# 		j=j+1
    
# 	user=int(input("jawab do or carorpatti ban jao .....😅😅😅 "))
# 	if user==solution_list[i]:
# 		print("🥳🥳🥳🥳🥳congrates  maan gye beta katai havy driver nikle tum toh🥳🥳🥳🥳🥳")
# 	elif user==5050:
# 		if count==0:
# 			k=0
# 			while k<len(life_line[i]):
# 				print(k+1,life_line[i][k])
# 				k=k+1
# 			count=count+1
# 			user2=int(input(" kya hai apka jawab..😅😅😅."))
# 			if user2==solution_list2[i]:
# 				print("you are right🥳🤩🥳")
# 			else:
# 				print("wrong ans....😱😱😱😱😱😱")
# 		else:
# 			print("😒😒😒aapne life line use kr li hai😒😒😒")
# 			num=int(input(" kya lagta hai kon sa hoga......😅😅😅"))
# 			if num==solution_list[i]:
# 				print("wah bete moj kardi 🥳🤩🥳")
# 			else:
# 				print("😱😱😱😱😱😱wrong answer😱😱😱😱😱😱")
# 				break

# 	else:
# 		print("😅😅😅😅galat jawab bhaiya😅😅😅😅")
# 		break

# 	i=i+1











question_list = [
    "How many continents are there?",              
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"    
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal ", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
fiftyfifty=[['four','seven'],['Delhi','Bhopal'],['Tourism','software engineering']]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solutions=[2,1,2]
solution_list = [3, 4, 1] 

print("Co-Powered by Dabur Amla presents,Kaun Banega Crorepati mein apka swagat hai!!")
print("Sadab,Aadab aur Shastriyakal.")
print("Pehla Question yeh rha apke screen ke upar:")
i= 0
c= 0
while i<len(question_list):
	print('your question is')
	print(i+1,question_list[i])
	
	a= 0
	while a<=len(options_list):
		print(a+1,options_list[i][a])
		a= a+1
	user= int(input('enter solution'))
	if user==solution_list[i]:
			print('congrats')
	elif user==5050:
		if c==0:
			m= 0
			while m<len(fiftyfifty[i]):
				print(m+1,fiftyfifty[i][m])
				m= m+1
			c= c+1
			num= int(input('enter no.'))
			if num==solutions[i]:
				print('correct')
			else:
				print('your option is wrong')
				print('quit')

		else:
			print('you used 5050 lifeline')
			num1= int(input('enter your option'))
			if num1==solution_list[i]:
				print('congrats,ap jeet gye 10000 rupaiye')
				break
			else:
				print('your option is wrong')
				break
	else:
				print('your answer is wrong')
				print('sorry')
				break
	i= i+1
