def Test():
    T = (".com",".org",".gov")

    Show(T)
   
    
def Show(T):
    print("{0}items in {1}".format(len(T),T.__class__.__name__))
    for t in T:
        print(t)