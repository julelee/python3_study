def Test():
    listDomain = [".com",".org",".gov"]
    print("<Show domain list>")
    for d in listDomain:
        print(d)
    print(len(listDomain),"items in domain  List")
    print("<Append domain to list>")
    listDomain.append(".tv")
    for d in listDomain:
        print(d)
    print(len(listDomain),"items in domain  List")
    print(listDomain[:10])
    