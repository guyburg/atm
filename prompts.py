from user import User


class Prompt(object):
    def __init__(self):
        self.message = self._get_message()

    def display_message(self, message=None):
        if message:
            print message
        else:
            print self.message

    def get_input(self):
        return raw_input('>>  ')

    def go(self, user=None):
        self.display_message()
        choice = self.get_input()
        self._process_choice(choice, user)

    def _get_message(self):
        raise NotImplementedError

    def _process_choice(self, choice, user):
        raise NotImplementedError


class Password(Prompt):
    def _get_message(self):
        return 'Enter your password: '

    def _process_choice(self, choice, user):
        from menus import Actions, Login

        user = User.get_user(choice)
        if user:
            menu = Actions()
            menu.go(user)
        else:
            self.display_message('User does not exist.')
            menu = Login()
            menu.go()


class MoneyOperation(Prompt):
    def _get_message(self):
        return "Enter amount to {0}: ".format(self._operation_name())

    def _process_choice(self, choice, user):
        from menus import Actions

        try:
            choice = int(choice)
        except ValueError:
            self.display_message("Please enter a number.")
            self.go(user)
        else:
            self._process_amount(user, choice)

            self.display_message("Your new balance is {0}: ".format(user.get_balance()))
            menu = Actions()
            menu.go(user)

    def _operation_name(self):
        raise NotImplemented

    def _process_amount(self, user, amount):
        raise NotImplemented


class Deposit(MoneyOperation):
    def _operation_name(self):
        return "deposit"

    def _process_amount(self, user, amount):
        user.deposit(amount)


class Withdraw(MoneyOperation):
    def _operation_name(self):
        return "withdraw"

    def _process_amount(self, user, amount):
        user.withdraw(amount)
