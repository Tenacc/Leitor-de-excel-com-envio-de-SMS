import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfc2176b9bda9de5140eb3c770c6e627f"
# Your Auth Token from twilio.com/console
auth_token  = "4a73d5e590e425d182406ef1cdfc15ad"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']


for mes in lista_meses:

    print(f'Esté o mes de {mes}')
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') #leitura de xlsx
    print(tabela_vendas)

    if (tabela_vendas['Vendas'] > 55000).any():

        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} o vendedor {vendedor} vendeu {vendas} ')
        message = client.messages.create(
            to="+5511935001915", 
            from_="+13344542429",
            body=f'No mes de {mes} o vendedor {vendedor} vendeu {vendas}')

        print(message.sid)
        
    





