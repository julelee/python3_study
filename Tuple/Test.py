def Test():
    T = (".com",".org",".gov",123,0xff)
    T1=(3.14,"PI")
    print(T+T1)
   
    
def Show(T):
    print("{0}items in {1}".format(len(T),T.__class__.__name__))
    for t in T:
        print(t)