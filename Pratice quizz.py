print("-----Welcome to the Quizz-------")
print("---------------------")
questions =[
        { 
          "question" :"1. what is the capital of india" ,
          "options" : ["A.karnataka", "B.Mumbai", "C.Delhi", "D.bangalore"],
          "answer" : "C"
         },
         {
           "question": "2) Which one is a programming language?",
           "options": ["A) Python", "B) Mango", "C) Car", "D) Tea"],
            "answer": "A"  
         }
]
score = 0
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Enter the answer:").upper()
    if user_answer ==q["answer"]:
        print("Correct !") 
        score +=1
    else:
        print("wrong answer")    
        print("Correct answer is", q["answer"])

print("\n------------------")        
print("quiz finished!")
print("your score", score,"/", len(questions))
persentage = score /len(questions)*100
print("persentage is", persentage,"%")
if score == len(questions):
    print("Exelent")
elif score >=3:
    print("Good")  
else:
    print("Keep practicing")      




         