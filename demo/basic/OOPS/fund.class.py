import __main__

a,b=2,4;  c=a+b #  + is def __add__

class Fund:
    category = 'AM'
    def __init__(self, name, number, share=10):
        self.name = name
        self.number = number
        self.active=False
        self.share=share
        #return self

    def shareee(self):
        return self.share * 10

    def marketValue(self, price):
        return self.share * price

# update class attribute
Fund.category = 'American Fund'

tdf10 = Fund("TDF10", 11000061, share=20)
tdf10.category ='AFIS'
print(tdf10.name, tdf10.number,  tdf10.category,  tdf10.share,type(tdf10))
print('share : ', tdf10.shareee())
print('mkt: ', tdf10.marketValue(10))

tdf20 = Fund('TDF20', 11000062); tdf20.share = 50;
print(tdf20.name, tdf20.number, tdf20.category, tdf20.share, type(tdf20))
print()
print('str format 1: {0}'.format(tdf20))
print('str format 2: {0.name}:{0.number}'.format( tdf20))

# print(tdf20.shareee(tdf10))

s=str('hello Liu'); print(s, type(s))
s='hello Liu'; print(s, type(s))



# __main__ expriment
print('\n===== __main__ ===========')
print(__main__.tdf10)
print(__main__.tdf10.__init__)
__main__.tdf10.__init__('TDF30',11000063); print(tdf20.name, tdf20.number) # no impact