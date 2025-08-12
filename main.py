# # import logging
# # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# #                     datefmt='%d/%m/%y %H:%M:%S')
# # logging.debug("this is a debug message")
# # logging.info("this is a info message")
# # logging.warning("this is a warning message")
# # logging.error("this is a error message")
# # logging.critical("this is a critical message")





# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%d/%m/%y %H:%M:%S')
# import helper


# import logging
# logger = logging.getLogger(__name__)

# # cerate handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# #level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("this is a Warning")
# logger.error("this an error")

# import logging
# import logging.config
# logging.config.fileConfig('logging.conf')

# logging.config.dictConfig('logging.conf')


# logger = logging.getLogger("simpleExample")
# logger.debug("this is a debug messsage")

 # #Trouble shooter issues

# import logging

# try:
#     a = [1,2,3]
#     val = a[4]
# except IndexError as r:
#     logging.error(r, exc_info=True)

# import logging
# import traceback

# try:
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error("the error is %s",traceback.format_exc())



# #Rotating file Handler
# import logging
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(1000):
#     logger.info("hello world")


import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s,m,h,d, midninght, W0
handler = TimedRotatingFileHandler("timed_test.log", when="m", interval=5,backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("hello world")
    time.sleep(5)



    
