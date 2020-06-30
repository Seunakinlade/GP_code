print("Hello, lets calculate your GP")
tc_without_gst = input("Enter the total number of courses taken without GST ")
tc_without_gst = int(tc_without_gst)
number_of_courses = 1
course_unit_s = 0
course_u = 0

while number_of_courses <= tc_without_gst:
	number_of_courses += 1
	course_unit = input("Enter the course unit for each course ")
	course_unit = int(course_unit)

	course_score = input("Enter your score for the respective couse unit ")
	course_score = float(course_score)
#	if course_score != "":
	if course_score <= 39.4:
		course_point = 0
	elif course_score >39.4 and course_score <= 44.4:
		course_point = 1
	elif course_score > 44.4 and course_score <= 49.4:
		course_point = 2
	elif course_score > 49.4 and course_score <= 59.4:
		course_point = 3
	elif course_score > 59.4 and course_score <= 69.4:
		course_point = 4
	elif course_score > 69.4 and course_score <= 100:
		course_point = 5
	else:
		print (f"Kindly confirm your entry as {course_score} is an invalid score")

	course_unit_score = (course_unit) * (course_point)
	course_unit_s += course_unit_score
	course_u += course_unit


	#print(course_p)
	#print(course_unit_s)
	#print(f" course unit score 2 is {course_unit_score}")
	#total_course_point = course_point
	#if number_of_courses < tc_without_gst

print(course_u)	
print(course_unit_s)

students_total_gp = float((course_unit_s) / (course_u))
total_gp = (round(students_total_gp, 2))

print(f"Your total GP for the semester is {total_gp}")