# function is a first class object

def double_decker():
    print('python sesh korte 2 soptah lagbe')
    def sleep():
        print('na gumai program koro')
        return 'okay'
    return sleep 
print(double_decker())
print(double_decker()())

def do_something(work):
    print('stay hard work')
    work()
    print('one day you will be successful')
    
def coding():
    print('code na kore tumi program sikte parbena')

do_something(coding)