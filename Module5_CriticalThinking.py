import itertools
actor_list = ["User", "Repair Crew", "System/Office Employee"]
work_list = {}
mainID = 0
class UserActions:
    def __init__(self):
        self.id_iteration = itertools.count()
    def report(self):
        id = next(self.id_iteration)
        work_list[id] = ({'street': input('Enter street address: '), 'size': input('Enter size 1-10: '),
                            'location': input('Enter location(middle, curb, etc.): '), 'district': input('Enter district: ')})
class SystemActions:
    def priority(self):
        counter = 0
        for i in work_list:
            temp_list = work_list[counter]
            if counter ==0 or temp_list['size'] > current_priority:
                current_priority= temp_list['size']
                worklistID = counter
            counter += 1
        global mainID
        mainID = worklistID
        print('Priority Work Item:','ID',str(counter-1) ,'Street Address', temp_list['street'])
    def generate_report(self,id):
        print(work_list[id])
class RepairCrewActions():
    def beginwork(self):
        print('Work has begun')
    def updateinfo(self,id):
        self.id = id
        work_list[self.id]['damageType'] = 'regular damage'
        work_list[self.id]['dollarAmount'] = '100.00'
        print('System has been updated with work order details')
    def endwork(self):
        print('Work has been completed')
if __name__ == "__main__":
    print('Actors:',actor_list)
    c1 = UserActions()
    c2 = SystemActions()
    c3 = RepairCrewActions()
    print('User Reports a pot hole')
    c1.report()
    print('User Reports another pot hole')
    c1.report()
    print('System Determines Priority')
    c2.priority()
    print('Repair Crew has been assigned')
    c3.beginwork()
    c3.updateinfo(mainID)
    c3.endwork()
    print('Return Report Information:')
    c2.generate_report(mainID)