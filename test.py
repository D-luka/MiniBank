from models.account import Account
from models.client import Client

felicity: Client = Client('Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '02/09/1987')
angelina: Client = Client('Angelina Jolie', 'angelina@gmail.com', '234.567.890-02', '08/07/1978')

# print(felicity)
# print(angelina)

accountf: Account = Account(felicity)
accounta: Account = Account(angelina)

print(accounta)
print(accountf)
