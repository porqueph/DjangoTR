# abstração
#Log

class Log:
    def log(self, msg):
        raise NotImplementedError(
            'implemente o método Log'
        )
    
class LogFileMixin(Log):
    def log(self,msg):
        print(msg)

if __name__ == '__main__':

    #l = Log()
    l = LogFileMixin()
    l.log('qualquer coisa')