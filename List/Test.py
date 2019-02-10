def Test():
    listDomain = [".com",".org",".gov"]

    ShowList(listDomain)
    print("<Append domain to list>")
    listDomain.append(".tv")
    ShowList(listDomain)
    print("<Delete domain from list>")
    del listDomain[0]
    ShowList(listDomain)
    print("<Sort domain list>")
    listDomain.sort()
    ShowList(listDomain)
    
def ShowList(L):
    print("<Show domain list>")
    print(len(L),"items in domain  List")
    for item in L:
        print(item)