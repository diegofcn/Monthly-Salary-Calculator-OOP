from employees_timeline import employee_timeline
from datetime import datetime

# - Employee's name
# - Employee's role
# - Employee's pay per hour
# - Employee's total worked hours
# - Employee's monthly salary

manager_hourly_pay = 24
chef_hourly_pay = 20
bartender_hourly_pay = 16

days_in_month = list(range(1, 31, 1))


class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hourly_pay = self.get_hourly_pay()
        self.total_hours = self.get_total_hours()
        self.monthly_salary = self.get_monthly_salary()

    def get_hourly_pay(self):
        if self.role == 'manager':
            return manager_hourly_pay
        elif self.role == 'bartender':
            return bartender_hourly_pay
        elif self.role == 'chef':
            return chef_hourly_pay
        else:
            return None

    def get_all_shift_duration(self):
        daily_work_time_list = []
        for working_day in days_in_month:
            time_tuple = employee_timeline[working_day]
            start_time = datetime.strptime(time_tuple[0], '%H:%M')
            finish_time = datetime.strptime(time_tuple[1], '%H:%M')
            work_time = finish_time - start_time
            daily_work_time_list.append(work_time.seconds)
        return daily_work_time_list

    def get_total_hours(self):
        return round(sum(self.get_all_shift_duration()) / 3600, 2)

    def get_monthly_salary(self):
        return f'{self.total_hours * self.hourly_pay}$'

    def monthly_paycheck(self):
        return {
            "employee_name" : self.name,
            "employee_role" : self.role,
            "hourly_pay" : self.hourly_pay,
            "total_worked_hours" : self.total_hours,
            "final_salary" : self.monthly_salary
        }

emp1 = Employee(name=employee_timeline['employee_name'],
                role=employee_timeline['role'])

print(emp1.monthly_paycheck())