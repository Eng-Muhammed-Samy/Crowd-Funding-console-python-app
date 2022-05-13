import json
import datetime
class UserFunctionality:

    def all_projects(self):
        with open('projects.json') as f:
            all_projects = json.load(f)
        f.close()
        return all_projects

    def save_in_file(self, path, arr):
        with open(path, 'w') as f:
            json.dump(arr, f, indent=4)
        f.close()

    def print_project(self,user_projects):
        for proj in user_projects:
            print("*" * 20)
            print(f"* Title :  {proj['title']}")
            print(f"\n* Detailes :  {proj['detailes']}")
            print(f"\n* Target :  {proj['target']}")
            print(f"\n* Start Date :  {proj['start_date']}")
            print(f"\n* End Date :  {proj['end_date']}")
            print("*" * 20)
            print()

    def create_project(self, email, title, datailes, target, start_time, end_time):
        projects = self.all_projects()
        project = {
            "email": email,
            "title": title,
            "detailes": datailes,
            "target": target,
            "start_date": start_time,
            "end_date": end_time
        }
        projects.append(project)
        self.save_in_file('projects.json', projects)



    def view_all_projects(self, user):
        all_proj = self.all_projects()
        user_projects = []
        for proj in all_proj:
            if proj['email'] == user:
                user_projects.append(proj)
        self.print_project(user_projects)


    def edit_project(self, user, title):
        all_proj = self.all_projects()
        for proj in all_proj:
            if proj['email'] == user and proj['title'] == title:
                proj['title'] = input("Enter New Title: ")
                proj['detailes'] = input("Enter New datailes: ")
                proj['target'] = input("Enter New target: ")
                proj['start_date'] = input("Enter New start_date: ")
                proj['end_date'] = input("Enter New end_date: ")
        self.save_in_file('projects.json', all_proj)


    def delete_project(self, user, title):
        all_proj = self.all_projects()
        print(all_proj)
        for proj in all_proj:
            if proj['email'] == user and proj['title'] == title:
                agree = input("Are You sure ? [Y / N] : ")
                if agree.upper() == 'Y':
                    all_proj.remove(proj)
                    self.save_in_file('projects.json', all_proj)
                    return True
                else:
                    return False


    def search_obout_project(self, user,start_date, end_date):
        s_date = datetime.date(int(start_date.split('/')[0]), int(start_date.split('/')[1]), int(start_date.split('/')[2]))
        e_date = datetime.date(int(end_date.split('/')[0]), int(end_date.split('/')[1]), int(end_date.split('/')[2]))
        all_proj = self.all_projects()
        projects = []
        for proj in all_proj:
            start = datetime.date(int(proj['start_date'].split('/')[0]), int(proj['start_date'].split('/')[1]),
                                  int(proj['start_date'].split('/')[2]))
            end = datetime.date(int(proj['end_date'].split('/')[0]), int(proj['end_date'].split('/')[1]),
                                int(proj['end_date'].split('/')[2]))
            if start >= s_date and end <= e_date and user == proj['email']:
                projects.append(proj)
        self.print_project(projects)