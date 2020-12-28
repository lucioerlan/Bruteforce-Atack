from service.service import service
from utils.style import style

try:
    servico = service()
    servico.inputlist()

except KeyboardInterrupt:
    print(style.OKBLUE + 'Program Ended!' + style.ENDC)
