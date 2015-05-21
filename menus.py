import settings
import sys
from prompts import Password, Deposit, Withdraw


class Menu(object):
    def __init__(self, message, options):
        self.message = message
        self.options = options

    def exit(self):
        sys.exit()

    def display_message(self):
        print self.message

    def display_options(self):
        for k, v in self.options.items():
            print "{0}) {1}".format(k, v)

    def get_input(self):
        choice = raw_input('>>  ')
        while choice not in self.options.keys():
            print 'Invalid selection, please try again.\n'
            self.display_options()
            choice = raw_input('>>  ')
        return choice

    def go(self):
        self.display_message()
        self.display_options()
        self._parse_choice(self.get_input())

    def _parse_choice(self):
        raise NotImplementedError

    def _get_options(self):
        raise NotImplementedError

    def _get_message(self):
        raise NotImplementedError


class Login(Menu):
    def __init__(self):
        super(Login, self).__init__(self._get_message(), self._get_options())

    def _parse_choice(self, choice):
        if choice == '1':
            prompt = Password()
            prompt.go()
        elif choice == '2':
            self.exit()

    def _get_options(self):
        return settings.LOG_IN_MENU['options']

    def _get_message(self):
        return settings.LOG_IN_MENU['message']


class Main(Menu):
    def __init__(self):
        super(Main, self).__init__(self._get_message(), self._get_options())

    def _get_options(self):
        return settings.MAIN_MENU['options']

    def _get_message(self):
        return settings.MAIN_MENU['message']


if __name__ == '__main__':
    a = Login()
    a.display_options()
