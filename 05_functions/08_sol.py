def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="thor", power="thunder")
print_kwargs(name="dr.strange", power="time", enemy="thanos")
