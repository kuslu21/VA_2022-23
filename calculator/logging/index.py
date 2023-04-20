# Použít oficiální dokumentaci Pythonu (https://docs.python.org/3/library/logging.html)

import logging
import time

# logging.basicConfig(filename=f"{time.time()}.log", filemode="w")
# logging.basicConfig(filename="01.log", filemode="w")
# logging.basicConfig(level=logging.ERROR)
fmt = "%(asctime)s [%(levelname)s]: %(message)s" # formátování stringu (aby bylo logování zpětně kompatibilní)
logging.basicConfig(level=10, format=fmt)

logging.debug("Tohle je debug.")
logging.info("Tohle je info.")
logging.warning("Tohle je varování.")
logging.error("Tohle je chyba.")
logging.fatal("Tohle je fatal.")

try:
    x = int(input("x: "))
    logging.debug(x)
    y = int(input("y: "))
    logging.info(y)
    z = x / y
    logging.info(z)
except ZeroDivisionError:
    logging.error("Nelze dělit nulou.")

except Exception as e:
    # logging.error("Něco se pokazilo.")
    # raise Exception("Něco se pokazilo.")
    logging.warning("POZOR, PROGRAM POKRAČUJE.")
    logging.error(e)