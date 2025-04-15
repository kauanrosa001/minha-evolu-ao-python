medida = float(input('uma distancia em metros:'))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('a medida de {}m, corresponde a:\n{}km\n{}hm\n{:.1}dam'.format(medida,km,hm,dam),end='')
print('\n{}dm\n{}cm\n{}mm'.format( medida,dm,cm,mm))