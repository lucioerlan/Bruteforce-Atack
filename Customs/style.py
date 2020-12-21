from os import system, name 

class style:
    # Colors Terminal
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

    print('\n' + FAIL +
          r'''
            )    )     )         (       )
   (     ( /( ( /(  ( /(     (   )\ ) ( /(
   )\    )\()))\()) )\())    )\ (()/( )\())
((((_)( ((_)\((_)\ ((_)\   (((_) /(_)|(_)\
 )\ _ )\ _((_) ((_) _((_)  )\___(_))__ ((_)
 (_)_\(_) \| |/ _ \| \| | ((/ __| _ \ \ / /
  / _ \ | .` | (_) | .` |  | (__|   /\ V /
 /_/ \_\|_|\_|\___/|_|\_|   \___|_|_\ |_|
        ''' + FAIL)

    print(OKGREEN + '[>]' + OKBLUE +
          ' Created By : ' + ENDC + 'Erlan Lucio' + '\n')
