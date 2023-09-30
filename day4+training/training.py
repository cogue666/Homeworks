

#დავწეროთ პროგრამა რომელიც ეკითხება ადამიანს სახელს
name = input ('What is your name? ') 
print('Hi '+ name)
#დავწეროთ პროგრამა რომელიც ეკითხება ადამიანს საყვარელ ფერს
favourite_color = input ('What is your favourite Color ?' )
print(name + ' likes ' +  favourite_color)

#დაბადების თარიღი
birth_year = input('Birth Year: ')
age = 2023 - int(birth_year)
print (age)
print(age + 25) 


#გადავიყვანოთ წონა LB-დან KG-ზე
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * (0.45)
print(weight_kg)

course = "Python's Course for Begginers"
print (course)

#''' შეგვიძლია ჩავშალოთ ტექსტი ქვემოთ და დავწეროთ მოცემულ სტილში
course = '''
Hello Tato,

Thanks for Contacting us

We Will get back to you soon.
'''

print(course)

course = 'Python for Beginners'
print(course[0:123])





