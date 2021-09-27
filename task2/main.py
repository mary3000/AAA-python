import csv
import math

DEPARTMENT = 'Department'
EMPLOYER_COUNT = 'Employer count'
SALARY_MIN = 'Salary minimum'
SALARY_MAX = 'Salary maximum'
SALARY_AVG = 'Salary avg'


class Company:
    def __init__(self):
        self.departments = {}

    def add(self, department: str, team: str, salary: int):
        """Adds to company information about new employer."""
        if department not in self.departments:
            self.departments[department] = Department(department)
        self.departments[department].add(team, salary)

    def report(self) -> str:
        """Constructs a string with a report for every company department (employer count, salary range, etc)."""
        reports_shifted = ['\t' + '\n\t'.join(d.report_str().splitlines()) for d in self.departments.values()]
        return 'Company departments:\n' + '\n'.join(reports_shifted)

    def hierarchies(self) -> str:
        """Constructs a string with department hierarchies (i.e. with team memberships)."""
        departments_shifted = ['\t' + '\n\t'.join(d.hierarchy().splitlines()) for d in self.departments.values()]
        return 'Company departments:\n' + '\n'.join(departments_shifted)

    def write_csv(self, csv_name: str):
        """Writes report into a csv file."""
        with open(csv_name, 'w', newline='') as csvfile:
            fieldnames = [DEPARTMENT, EMPLOYER_COUNT, SALARY_MIN, SALARY_MAX, SALARY_AVG]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for d in self.departments.values():
                writer.writerow({row[0]: row[1] for row in d.report()})


class Department:
    def __init__(self, name: str):
        self.name = name
        self.teams = set()
        self.employer_count = 0
        self.min_salary = math.inf
        self.max_salary = -math.inf
        self.salary_sum = 0

    def add(self, team: str, salary: int):
        """Adds a new employer to a department."""
        self.teams.add(Team(team))
        self.employer_count += 1
        self.min_salary = min(self.min_salary, salary)
        self.max_salary = max(self.max_salary, salary)
        self.salary_sum += salary

    def report(self) -> []:
        """Constructs a report with info about employers and their salaries."""
        info = []
        info.append((DEPARTMENT, self.name))
        info.append((EMPLOYER_COUNT, self.employer_count))
        info.append((SALARY_MIN, self.min_salary))
        info.append((SALARY_MAX, self.max_salary))
        info.append((SALARY_AVG, f'{self.salary_sum / self.employer_count}'))
        return info

    def report_str(self) -> str:
        """Constructs a string from a report."""
        info = self.report()
        return '\n\t'.join([f'{row[0]}: {row[1]}' for row in info])

    def hierarchy(self) -> str:
        """Constructs a string with team hierarchies."""
        return f'Department {self.name}.\n' + 'Teams:\n\t' + '\n\t'.join([str(team) for team in self.teams])


class Team:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __hash__(self): return hash(self.name)

    def __eq__(self, x): return x.name == self.name

    def __ne__(self, x): return x.name is not self.name


def parse_company(csv_name: str) -> Company:
    """
    Parses company information from a csv file.
    """
    with open(csv_name, newline='') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=';')
        company = Company()
        for row in reader:
            department = row[1]
            team = row[2]
            salary = int(row[-1])
            company.add(department, team, salary)
        return company


if __name__ == '__main__':
    company = parse_company('Corp_Summary.csv')

    print('Welcome to the UltraMegaCompanyAnalyzer!')

    while True:
        print('Please, choose a command.\n'
              '1 - for Department hierarchy.\n'
              '2 - for Department summary.\n'
              '3 - for dumping output of the 2nd command into a csv file.')

        cmd = int(input())
        if 1 <= cmd <= 3:
            break
        print('Wring command!')

    if cmd == 1:
        print(company.hierarchies())
    elif cmd == 2:
        print(company.report())
    else:
        out_csv = 'out.csv'
        company.write_csv(out_csv)
        print(f'Information was written to {out_csv}.')
