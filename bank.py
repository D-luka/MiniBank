from typing import List
from time import sleep

from models.client import Client
from models.account import Account


accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('============================================================')
    print('========================== ATM =============================')
    print('============================================================')

    print('Select an option from the menu: ')
    print('1 - Create an Account')
    print('2 - Withdraw')
    print('3 - Make Deposit')
    print('4 - Transfer')
    print('5 - List Account')
    print('6 - Exit System')

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        withdraw()
    elif option == 3:
        make_deposit()
    elif option == 4:
        transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('Check back often')
        sleep(2)
        exit(0)
    else:
        print('Invalid option')
        sleep(2)
        menu()


def create_account() -> None:
    print('Report customer data: ')

    name: str = input('Client name: ')
    email: str = input('Customer email: ')
    nif: str = input('Customer nif: ')
    birth_date: str = input('Customer date of birth: ')

    client: Client = Client(name, email, nif, birth_date)

    account: Account = Account(client)

    accounts.append(account)

    print('Account created successfully')
    print('Account data')
    print('============================')
    print(accounts)
    sleep(2)
    menu()


def withdraw() -> None:
    if len(accounts) > 0:
        number: int = int(input('Provide your account number: '))

        account: Account = search_account_by_number(number)

        if account:
            value: float = float(input('Inform the withdrawal amount: '))

            account.withdraw(value)
        else:
            print(f'Account number not found {number}')

    else:
        print('There are no registered accounts yet. ')
    sleep(2)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input('Provide your account number: '))

        account: Account = search_account_by_number(number)

        if account:
            value: float = float(input('Inform the amount of the deposit: '))

            account.deposit(value)

        else:
            print(f'Account numer not found{number}')

    else:
        print('There are no registered accounts yet.')
    sleep(2)
    menu()


def transfer() -> None:
    if len(accounts) > 0:
        number_origin: int = int(input('Provide your account number: '))

        account_origin: Account = search_account_by_number(number_origin)

        if account_origin:
            number_destination: int = int(input('Enter the destination account number: '))

            account_destination: Account = search_account_by_number(number_destination)

            if account_destination:
                value: float = float(input('Inform the amount of the transfer: '))

                account_origin.transfer(account_destination, value)

            else:
                print(f'The destination account with number {number_destination} was not found.')

        else:
            print(f'Your account number{number_origin} was not found.')
    else:
        print('There are no registered accounts yet.')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('Account listing')

        for account in accounts:
            print(account)
            print('===================================')
            sleep(1)
    else:
        print('There are not registered accounts.')
    sleep(2)
    menu()


def search_account_by_number(number: int) -> Account:
    c: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == number:
                c = account
    return c


if __name__ == '__main__':
    main()
