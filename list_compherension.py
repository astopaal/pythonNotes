#listeler kullanarak başka listeler oluşturmak istediğimizde list comprehension kullanabiliriz
#you can use list comprehension when you want to create other lists using lists

liste = [x for x in range(100)] # [0,1,2,......98,99]

letters = [x for x in "letters"] # ['l', 'e', 't', 't', 'e', 'r', 's']

#listeyi oluştururken bir işlem de uygulayabilirsiniz
#you can also apply an action while creating the list

numbers = [1,2,3,4,5,6,7,8,9]

x2 = [i*2 for i in numbers]  # [2,4,6,8,10,12,14,16,18]

#if ile bir koşul belirleyebilirsiniz
#you can set conditions using if

numbers = [1,2,3,4,5,6,7,8,9]

odds = [x for x in numbers if x%2==1] #[1,3,5,7,9]

