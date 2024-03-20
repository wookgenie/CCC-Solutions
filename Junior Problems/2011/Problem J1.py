anten = int(input('안테나는 몇개 인가요?'))
eye = int(input('눈이 몇개 있나요?'))


if(anten >= 3 and eye <= 4):
    print('트로이마션')


if(anten <= 6 and eye >= 2):
    print('블라드사투르니안')

if(anten <= 2 and eye <= 3):
    print('그레이메머큐리언')
