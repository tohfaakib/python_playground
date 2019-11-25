# Monkey Patching means modify some code at the run time!

class Parent():
    def get_sample_api_data(self):
        return "sample_api_data"


def get_sample_api_data(self, *args):
    for arg in args:
        print(arg)


Parent.get_sample_api_data = get_sample_api_data
Parent.get_sample_api_data(Parent.get_sample_api_data, 'test data1', 'test data 2')
