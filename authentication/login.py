import json


class Login:
    def login(self, email, password):
        with open('user.json') as f:
            all_suers = json.load(f)

        for user in all_suers:
            if user['email'] == email and user['password'] == password:
                return True
        return False
