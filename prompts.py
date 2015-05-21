import settings

class Prompt(object):
    def __init__(self, message):
        self.message = message

    def display_message(self):
        print self.message

    def get_input(self):
        return raw_input('>>  ')

    def go(self):
        self.display_message()
        self._parse_choice(self.get_input())

    def _get_message(self):
        raise NotImplementedError


class Password(Prompt):
    def __init__(self):
        super(Password, self).__init__(self._get_message())

    def _get_message(self):
        return settings.PASSWORD_PROMPT['message']

class Deposit(Prompt):
    def __init__(self):
        super(Deposit, self).__init__(self._get_message())

    def _get_message(self):
        return settings.DEPOSIT_PROMPT['message']

class Withdraw(Prompt):
    def __init__(self):
        super(Withdraw, self).__init__(self._get_message())

    def _get_message(self):
        return settings.WITHDRAW_PROMPT['message']