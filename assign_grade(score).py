def assign_grade(score):
	if score < 0 or score > 100:
		print("Invalid score! Please enter a value between 0 and 100.")
	elif score >= 90 and score <= 100:
		print("Grade: A")
	elif score >= 80 and score <= 89:
		print("Grade: B")
	elif score >= 70 and score <= 79:
		print("Grade: C")
	elif score >= 60 and score <= 69:
		print("Grade: D")
	else:
		print("Grade: F")
	
assign_grade()
	