def Test_FuncArg():
    Say_Default("hi")
    Say_Default("hello","Mr.Y")
    Say_Keyword("Hi",Msg="Happy New Year.")
    Say_Any("msg:","notice,I don't know what I said.","sorry")

def Say_Default(Hi,Name="Mr.X"):
    print(Hi,Name)

def Say_Keyword(Hi,Name="Mr.X",Msg=""):
    print(Hi,Name,Msg)

def Say_Any(Hi="hi",*Msg):
  print(Hi)
  for s in Msg:
    print(s)
