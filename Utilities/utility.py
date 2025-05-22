import inspect
import logging
import configparser


class utility:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def readConfig(section, key):
            config = configparser.ConfigParser()
            config.read("/Users/lekhraj/StudentAndroidApp/Student-App-Web/testdata/testdata.ini")
            return config.get(section, key)




