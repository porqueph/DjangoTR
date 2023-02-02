from abc import ABC, abstractclassmethod

class Notificacao(ABC):
    def __init__(self,mensagem):
      self.mensagem = mensagem


    @abstractclassmethod  
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
     
  def enviar(self):
    print('email: enviando', self.mensagem)


class NotificacaoPush(Notificacao):
     
  def enviar(self):
    print('push: enviando', self.mensagem)



def notificar(notificacao: Notificacao):
  notificacao_enviada = notificacao.enviar()


  if notificacao_enviada:
    print('notificação enviada')
  else:
    print('não enviada')