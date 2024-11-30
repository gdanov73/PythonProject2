my_dict={"Aleks":1972,"Sergei":1973,"Val":1949,"Leonid":1958,"Nina":1926,"Ivan":1924} # 1,2,3,4,5,6
print("Dict:",my_dict)
print("Г.р. ",my_dict["Nina"])
print("Нет в списке",my_dict.get("Valera"))

my_dict.update({"Anna":1997,"Sandra":2000})
print(my_dict.pop("Ivan"))

print("Обновленный список:",my_dict)



my_set={1,'ball',10,1917,'cub',3.14,1,'ball',10}
print(my_set)
my_set.remove("ball")
print(my_set)
my_set.add('string')
print(my_set)