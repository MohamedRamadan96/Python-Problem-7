# Question 7 : Return the number of times that the string “Emma”
# appears anywhere in the given string

def count_Text(Statement):
    count = 0
    for i in range(len(Statement)-1):
        count += Statement[i:i+7] == 'Mohamed'
    return count

count = count_Text("Mohamed is good developer. Mohamed is aslo a Designer and Mohamed Experiance")
print(count)