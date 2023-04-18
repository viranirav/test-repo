scm=["12345", "a", "12345", "HOSPICE, CARE"] #,["ABCDE", "", "12345", "World, Hello"]

print(scm[0:])
print("hi")
for scm in scm[0:]:
    scm_values = scm.split(",")
    #print(scm_values[0])
    print (scm_values[:])

    #standard_code = ','.join(scm_values[3:])
    #print(standard_code)
    #scm_values = scm_values[0:2]
    #scm_values.append(standard_code)
