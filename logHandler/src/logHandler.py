import logging
import sys


class Logger:
    def __init__(self, log_path: str) -> None:
        self.log_path = log_path

        try:
            with open(f'{self.log_path}/id.txt', 'r') as ids:
                self.id = int(ids.read())
        except FileNotFoundError:
            with open(f'{self.log_path}/id.txt', 'w') as ids:
                ids.write('1')
                self.id = 1

        if self.id > 10:
            with open(f'{self.log_path}/id.txt', 'w') as ids:
                ids.write(str(1))
        else:
            with open(f'{self.log_path}/id.txt', 'w') as ids:
                ids.write(str(self.id+1))

        self.infoLogger()
        self.infoLogger()

    def initLogger(self) -> None:
        logging.basicConfig(
            format='%(asctime)s %(threadName)s [%(filename)s : %(funcName)s()] %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            filename=f'{self.log_path}/log/log_{self.id}_DEBUG.log',
            encoding='utf-8',
            level=logging.DEBUG
        )

    def infoLogger(self) -> None:
        _log = logging.getLogger('infoLogger')
        _format = '%(asctime)s [%(filename)s : %(funcName)s()] %(levelname)s: %(message)s'
        _datefmt = '%m/%d/%Y %I:%M:%S %p'
        _filepath = f'{self.log_path}/log/log_{self.id}_INFO.log'

        formatter = logging.Formatter(_format, datefmt=_datefmt)

        fileHandler = logging.FileHandler(_filepath, mode='w')
        streamHandler = logging.StreamHandler(sys.stdout)

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        _log.setLevel(logging.INFO)
        _log.addHandler(fileHandler)
        _log.addHandler(streamHandler)
