import sys

import settings
from prompts import Password, Deposit, Withdraw


class Menu(object):
    # Type that knows to display message and options, and direct the user to a prompt or menu base on the user choice

    def __init__(self, message, options):
        self.message = message
        self.options = options

    def exit(self):
        self.display_message('bye, bye.')
        sys.exit()

    def display_message(self, message=None):
        if message:
            print message
        else:
            print self.message

    def display_options(self):
        for item in self.options:
            print "{0}) {1}".format(item[0], item[1])

    def get_input(self):
        choice = raw_input('>>  ')
        while choice not in [item[0] for item in self.options]:
            self.display_message('Invalid selection, please try again.')
            self.display_options()
            choice = raw_input('>>  ')
        return choice

    def go(self, user=None):
        self.display_message()
        self.display_options()
        choice = self.get_input()
        self._process_choice(choice, user)

    def _process_choice(self, choice, user):
        raise NotImplementedError

    def _get_options(self):
        raise NotImplementedError

    def _get_message(self):
        raise NotImplementedError


class Login(Menu):
    def __init__(self):
        super(Login, self).__init__(self._get_message(), self._get_options())

    def _process_choice(self, choice, user):
        if choice == '1':
            prompt = Password()
            prompt.go(user)
        elif choice == '2':
            self.exit()

    def _get_options(self):
        return settings.LOG_IN_MENU['options']

    def _get_message(self):
        return settings.LOG_IN_MENU['message']


class Actions(Menu):
    def __init__(self):
        super(Actions, self).__init__(self._get_message(), self._get_options())

    def _get_options(self):
        return settings.MAIN_MENU['options']

    def _get_message(self):
        return settings.MAIN_MENU['message']

    def _process_choice(self, choice, user):
        if choice == '1':
            balance = user.get_balance()
            self.display_message('Your balance is: {0} '.format(balance))
            self.go(user)
        elif choice == '2':
            prompt = Deposit()
            prompt.go(user)
        elif choice == '3':
            prompt = Withdraw()
            prompt.go(user)
        elif choice == '4':
            menu = Login()
            menu.go(user)
