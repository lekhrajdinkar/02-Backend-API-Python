import __main__

a,b=2,4;  c=a + b #  + is def __add__

class Fund:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.active=False
        self.share=10
        #return self

    def shareee(self):
        return self.share

    def marketValue(self, price):
        return self.share * price

tdf10 = Fund("TDF10", 11000061)
print(tdf10.name, tdf10.number, type(tdf10))
print('share : ', tdf10.shareee())
print('mkt: ', tdf10.marketValue(10))

tdf20 = Fund('TDF20', 11000062); tdf20.name = 'XXXX'
print(tdf20.name, tdf20.number, type(tdf10))
print()
print('str format 1: {0}'.format(tdf20))
print('str format 2: {0.name}:{0.number}'.format( tdf20))

s=str('hello Liu'); print(s, type(s))
s='hello Liu'; print(s, type(s))

# __main__ expriment
print('\n===== __main__ ===========')
print(__main__.tdf10)
print(__main__.tdf10.__init__)
__main__.tdf10.__init__('TDF30',11000063); print(tdf20.name, tdf20.number) # no impact