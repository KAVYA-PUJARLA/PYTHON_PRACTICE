marks=[100,90,110]
total=0
for mark in marks:
    total = total+mark
average = total/len(marks)
print(f"Total:{total}") 
print(f"Average:{average}")