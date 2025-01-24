import copy
my_list = [8, "red", ['a', 'b']]
ref_list = my_list
shallow_list = copy.copy(my_list)
deep_list = copy.deepcopy(my_list)
ref_list[1] = "green"
print("my_list:",my_list)
print("ref_list:",ref_list)
print("shallow_list:",shallow_list)
print("deep_list:",deep_list)
my_list[2][0] = 'x'
print("my_list:",my_list)
print("ref_list:",ref_list)
print("shallow_list:",shallow_list)
print("deep_list:",deep_list)