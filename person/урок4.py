
# import my_module
# print(my_module.secret_key)
#
# from my_module import message, Dog
# message('hello world')
#
#
# sharik = Dog('sharik', 0.5, 20, 'gaf gaf')


from person.create_person import create_person

jack = create_person(first_name='Jack', last_name="Barbaro", age=26)
jack.info()