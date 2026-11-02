class Employee:

    def calculate_salary(self):
        pass


class fulltime(Employee):

    def calculate_salary(self):
        return 10000


class parttime(Employee):

    def calculate_salary(self):
        hours = 80
        hourly_rate = 100
        return hours * hourly_rate


employee1 = fulltime()
employee2 = parttime()


print(employee1.calculate_salary())
print(employee2.calculate_salary())