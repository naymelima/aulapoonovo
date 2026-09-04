class cartão:
    def pagar(self):
        print(f'Pagamento via cartão.')

class dinheiro:
    def pagar(self):
        print(f'Pagamento em dinheiro.')

class pix:
    def pagar(self):
        print(f'Pagamento via pix.')

def pagar(tipo):
    tipo.pagar()
cartão = cartão()
dinheiro = dinheiro()
pix = pix()

pagar()




