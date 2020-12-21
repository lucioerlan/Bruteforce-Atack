from Service.service import service
from Customs.style import style

try:
    servico = service()
    servico.inputlist()

except KeyboardInterrupt:
    print(style.OKBLUE + 'Program Ended!' + style.ENDC)
