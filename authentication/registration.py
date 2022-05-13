import json


class Registeration:

    def get_all_users(self):
        with open('user.json') as f:
            all_users = json.load(f)
        return all_users

    def create_new_user(self, f_name, l_name, email, password):
        users = self.get_all_users()
        user = {
            "f_name": f_name,
            "l_name": l_name,
            "email": email,
            "password": password
        }
        users.append(user)
        with open('user.json', 'w') as f:
            json.dump(users, f, indent=4)
