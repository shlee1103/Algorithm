grade_val = {'A+':4.5, 'A0':4.0,
             'B+':3.5, 'B0':3.0,
             'C+':2.5, 'C0':2.0,
             'D+':1.5, 'D0':1.0, 'F':0.0}

jh_score_lst = []
for _ in range(20):
    jh_score_lst.append(input().split())

total_credit = 0
total_grade_point = 0

for sub in jh_score_lst:
    subject = sub[0]
    credit = float(sub[1])
    grade = sub[2]

    if grade == 'P':
        continue
    else:
        total_credit += credit
        if grade != 'F':
            grade_point = grade_val[grade]
            total_grade_point += credit * grade_point

if total_credit > 0:
    avg = total_grade_point / total_credit
    print(f"{avg:.6f}")
else:
    print("0.000000")