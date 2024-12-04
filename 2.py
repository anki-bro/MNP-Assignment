import csv
grade_map={'AP':10, 'AA':10, 'AB':9, 'BB':8, 'BC':7, 'CC':6}
def process_recs(records):
    stu_data={}
    for rec in records:
        rollno=rec[0]
        credit=int(rec[2])
        coursetype=rec[4]
        grade=rec[5]
        if rollno not in stu_data:
            stu_data[rollno]={"courses":[], "totals":{"core": 0, "department_elective": 0, "flexible_elective": 0, "hasmed_elective": 0, "minor": {}, "honours": 0}}
        stu_data[rollno]["courses"].append({"credits":credit, "type":coursetype, "grade":grade})
        if coursetype in stu_data[rollno]["totals"] and coursetype!="minor":
            stu_data[rollno]["totals"][coursetype]+=credit
        elif coursetype=="minor":
            if grade not in stu_data[rollno]["totals"]["minor"]:
                stu_data[rollno]["totals"]["minor"][grade]=0
            stu_data[rollno]["totals"]["minor"][grade]+=credit
    return stu_data
def ten_rows():
    print("Details of first 10 rows: ")
    for row in records[:10]:
        print(row)
    print()
def cal_cpi(data):
    print("Roll no. wise CPI of all students: ")
    for rollno,details in data.items():
        total_points,total_credits=0,0
        for course in details["courses"]:
            if course["grade"] in grade_map:
                total_points+=grade_map[course["grade"]]*course["credits"]
                total_credits+=course["credits"]
        if total_credits!=0:
            cpi = total_points/total_credits 
        else:
            cpi=0
        print("Roll No: " + rollno + ", CPI: "+str(round(cpi,2)))
    print()
def grad_eligibility(data):
    eligible_students=[]
    for rollno,totals in data.items():
        total_credits=totals["totals"]
        if total_credits["core"]>=20 and total_credits["department_elective"]>=15 and total_credits["flexible_elective"]>=10 and total_credits["hasmed_elective"]>=5:
            eligible_students.append(rollno)
    print("Students meeting graduation requirements: ")
    for student in eligible_students:
        print(student)
    print()
def minor_check(data):
    eligible_students=[]
    for rollno,totals in data.items():
        if "minor" in totals["totals"]:
            for credit in totals["totals"]["minor"].values():
                if credit>=10:
                    eligible_students.append(rollno)
                    break    
    print("Students who completed a minor: ")
    for student in eligible_students:
        print(student)
    print()
def honors_check(data):
    eligible_students=[]
    for rollno,totals in data.items():
        if totals["totals"]["honours"]>=10 and totals["totals"]["core"]>=20:
            eligible_students.append(rollno)
    print("Students who completed honors: ")
    for student in eligible_students:
        print(student)
with open('student_records.csv',mode='r') as file:
     reader=csv.reader(file)
     next(reader)
     records=list(reader)
     rec=process_recs(records)
     ten_rows()
     cal_cpi(rec)
     grad_eligibility(rec)
     minor_check(rec)
     honors_check(rec)
file.close()