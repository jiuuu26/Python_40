from currency_converter import CurrencyConverter

cc=CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1000,'KRW','JPY'))
