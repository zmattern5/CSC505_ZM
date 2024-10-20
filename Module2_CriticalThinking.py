
import time
from time import sleep


class Mattern:
    def p_status(self):
        print("Type 'Y' if the answer is yes for all of the following questions")
        while True:
            communication = input('Has conversation between client and the team building the project begun?:\n')
            if communication == 'Y':
                com_info = input('Enter any initial information for the client:\n')
                break
            else:
                print('Continue communicating with client')
                time.sleep(1)
                continue
        while True:
            requirements = input('Have all requirements been defined by the client?:\n')
            if requirements == 'Y':
                req_info = input('Enter requirements from the client:\n')
                break
            else:
                print('Go back to complete communications with the client')
                time.sleep(1)
                com_info = com_info +" , "+ input('Enter additional information for the client:\n')
                continue
        while True:
            planning = input('Has the project been designed and is planning completed?:\n')
            if planning == 'Y':
                plan_info = input('Enter any project design information or plans:\n')
                break
            else:
                print('Go back to complete requirements defined by the client')
                time.sleep(1)
                req_info = req_info +" , "+ input('Enter additional requirement information:\n')
                continue
        while True:
            development = input('Has development been completed?:\n')
            if development == 'Y':
                dev_info = 'Development Completed'
                break
            else:
                print('Go back to planning')
                time.sleep(1)
                plan_info = plan_info +" , "+ input('Enter any additional project design information or plans:\n')
                continue
        while True:
            testing = input('Was testing successful?:\n')
            if testing == 'Y':
                test_info = 'Testing Completed'
                break
            else:
                print('Go back to complete development')
                time.sleep(1)
                continue
        while True:
            deploy = input('Is additional support of the project required?:\n')
            if deploy == 'Y':
                print('Restart communication with client')
                time.sleep(1)
                self.p_status()
            else:
                print('Project had been completed')
                proj_info = 'Project Completed'
                break
        print('Communication Info:\n',com_info)
        print('Planning Info:\n',plan_info)
        print('Requirements Info:\n',req_info)
        print('Development Info:\n',dev_info)
        print('Test Info:\n',test_info)
        print('Project Info:\n',proj_info)
c1 = Mattern()
c1.p_status()