
from Controller import funcoes as f

W = '\033[0m'  # white
C = '\033[1;36m' #cyanClaro

try:
    ff = f.funcoes()
    
    ff.banner()
    ff.escolheDep()
except KeyboardInterrupt:
    print('\n\n\n\n' +  C + 'Program Ended!'+ W)