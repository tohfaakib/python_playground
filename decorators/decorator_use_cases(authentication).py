from functools import wraps


def is_authenticated(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        users = [{'username': 'nishan', 'password': '123'}, {'username': 'akib', 'password': '1234'}]

        """
         ==================== searching for users using loop =======================
        for user in users:
            if str(user['username']) == str(kwargs['username']) and str(user['password']) == str(kwargs['password']):
                return func()
        else:  # this else is for loop's else not from if-else
            return "Authentication Failed"
        """

        user = {'username': kwargs['username'], 'password': kwargs['password']}
        if user in users:
            return func()
        else:
            return "Authentication Failed"

    return wrapper


@is_authenticated
def login():
    return "Login successful! Do whatever you want!"


username = input("Enter Username:\n")
password = input("Enter Password:\n")

login = login(username=username, password=password)
print(login)
