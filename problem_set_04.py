# START PROBLEM SET 4
print("Problem Set 4 \n")

# Setup Code (DO NOT MODIFY)

data = [
    "Company Name, Location, Number of Employees, Website, Industry",
    "Amcor, switzerland, 44000, https://www.amcor.com, consumer packaged goods ",
    "Auto-Owners Insurance, michigan, 5394, https://www.auto-owners.com , insurance ",
    "Blue cross Blue Shield of Michigan, michigan, 850, https://m.bcbsm.com/index.html, Insurance",
    "Cisco, California, 77500, https://www.cisco.com, software",
    "Deloitte, England, 41500, https://www2.deloitte.com/us/en.html, financial",
    "Epic, Wisconsin, 10000, https://www.epic.com, healthcare",
    "Health Management Associates, Michigan, 5394, https://www.healthmanagement.com , healthcare",
    "Johnson Controls, wisconsin, 97000, https://www.johnsoncontrols.com, software",
    "menlo innovations, michigan, 34, https://menloinnovations.com, Software ",
    "MRM, New York, 2300, https://www.mrm.com/en/, software",
    "OneMagnify, Michigan, 520, https://onemagnify.com, Marketing",
    "Plymouth District Library, Michigan, 37, https://www.plymouthlibrary.org, education",
    "PricewaterhouseCoopers (PwC), england, 295000, https://www.pwc.com/us/en, consulting ",
    "Procter & Gamble (P&G), Ohio, 97000, https://us.pg.com, Consumer Packaged Goods",
    "TechSmith Corporation, Michigan, 293, https://www.techsmith.com, Software",
    "United States Federal Bureau of Investigation (FBI), Washington DC, 35000, https://www.fbi.gov, government",
    "University of Michigan Bentley Historical Library, Michigan, 29, https://bentley.umich.edu, education",
    "University of Michigan Center for Academic Innovation, Michigan, 150, https://ai.umich.edu, Education",
    "University of Michigan Desai Accelerator, Michigan, 30, https://desaiaccelerator.umich.edu, Consulting",
    "University of Michigan Innovation Partnerships, michigan, 15, https://innovationpartnerships.umich.edu, consulting",
    "University of Michigan ITS, Michigan, 500, https://its.umich.edu, education",
    "University of Michigan Library, michigan, 400, https://www.lib.umich.edu, Education",
    "VA Center for Clinical Management Research, Michigan, 150, https://www.annarbor.hsrd.research.va.gov, healthcare",
]

employers_check = [
    ["Company Name", "Location", "Number of Employees", "Website", "Industry"],
    ["Amcor", "switzerland", "44000", "https://www.amcor.com", "consumer packaged goods "],
    ["Auto-Owners Insurance", "michigan", "5394", "https://www.auto-owners.com ", "insurance "],
    ["Blue cross Blue Shield of Michigan", "michigan", "850", "https://m.bcbsm.com/index.html", "Insurance"],
    ["Cisco", "California", "77500", "https://www.cisco.com", "software"],
    ["Deloitte", "England", "41500", "https://www2.deloitte.com/us/en.html", "financial"],
    ["Epic", "Wisconsin", "10000", "https://www.epic.com", "healthcare"],
    ["Health Management Associates", "Michigan", "5394", "https://www.healthmanagement.com ", "healthcare"],
    ["Johnson Controls", "wisconsin", "97000", "https://www.johnsoncontrols.com", "software"],
    ["menlo innovations", "michigan", "34", "https://menloinnovations.com", "Software "],
    ["MRM", "New York", "2300", "https://www.mrm.com/en/", "software"],
    ["OneMagnify", "Michigan", "520", "https://onemagnify.com", "Marketing"],
    ["Plymouth District Library", "Michigan", "37", "https://www.plymouthlibrary.org", "education"],
    ["PricewaterhouseCoopers (PwC)", "england", "295000", "https://www.pwc.com/us/en", "consulting "],
    ["Procter & Gamble (P&G)", "Ohio", "97000", "https://us.pg.com", "Consumer Packaged Goods"],
    ["TechSmith Corporation", "Michigan", "293", "https://www.techsmith.com", "Software"],
    ["United States Federal Bureau of Investigation (FBI)", "Washington DC", "35000", "https://www.fbi.gov", "government"],
    ["University of Michigan Bentley Historical Library", "Michigan", "29", "https://bentley.umich.edu", "education"],
    ["University of Michigan Center for Academic Innovation", "Michigan", "150", "https://ai.umich.edu", "Education"],
    ["University of Michigan Desai Accelerator", "Michigan", "30", "https://desaiaccelerator.umich.edu", "Consulting"],
    ["University of Michigan Innovation Partnerships", "michigan", "15", "https://innovationpartnerships.umich.edu", "consulting"],
    ["University of Michigan ITS", "Michigan", "500", "https://its.umich.edu", "education"],
    ["University of Michigan Library", "michigan", "400", "https://www.lib.umich.edu", "Education"],
    ["VA Center for Clinical Management Research", "Michigan", "150", "https://www.annarbor.hsrd.research.va.gov", "healthcare"],
]

headers_check = ["Company Name", "Location", "Number of Employees", "Website", "Industry"]

universities_innovation_check = [["University of Michigan Center for Academic Innovation", "Michigan", "150", "https://ai.umich.edu", "Education"], ["University of Michigan Innovation Partnerships", "michigan", "15", "https://innovationpartnerships.umich.edu", "consulting"]]

other_companies_check = [
    ["Amcor", "switzerland", "44000", "https://www.amcor.com", "consumer packaged goods "],
    ["Auto-Owners Insurance", "michigan", "5394", "https://www.auto-owners.com ", "insurance "],
    ["Blue cross Blue Shield of Michigan", "michigan", "850", "https://m.bcbsm.com/index.html", "Insurance"],
    ["Cisco", "California", "77500", "https://www.cisco.com", "software"],
    ["Deloitte", "England", "41500", "https://www2.deloitte.com/us/en.html", "financial"],
    ["Epic", "Wisconsin", "10000", "https://www.epic.com", "healthcare"],
    ["Health Management Associates", "Michigan", "5394", "https://www.healthmanagement.com ", "healthcare"],
    ["Johnson Controls", "wisconsin", "97000", "https://www.johnsoncontrols.com", "software"],
    ["menlo innovations", "michigan", "34", "https://menloinnovations.com", "Software "],
    ["MRM", "New York", "2300", "https://www.mrm.com/en/", "software"],
    ["OneMagnify", "Michigan", "520", "https://onemagnify.com", "Marketing"],
    ["Plymouth District Library", "Michigan", "37", "https://www.plymouthlibrary.org", "education"],
    ["PricewaterhouseCoopers (PwC)", "england", "295000", "https://www.pwc.com/us/en", "consulting "],
    ["Procter & Gamble (P&G)", "Ohio", "97000", "https://us.pg.com", "Consumer Packaged Goods"],
    ["TechSmith Corporation", "Michigan", "293", "https://www.techsmith.com", "Software"],
    ["United States Federal Bureau of Investigation (FBI)", "Washington DC", "35000", "https://www.fbi.gov", "government"],
    ["University of Michigan Bentley Historical Library", "Michigan", "29", "https://bentley.umich.edu", "education"],
    ["University of Michigan Desai Accelerator", "Michigan", "30", "https://desaiaccelerator.umich.edu", "Consulting"],
    ["University of Michigan ITS", "Michigan", "500", "https://its.umich.edu", "education"],
    ["University of Michigan Library", "michigan", "400", "https://www.lib.umich.edu", "Education"],
    ["VA Center for Clinical Management Research", "Michigan", "150", "https://www.annarbor.hsrd.research.va.gov", "healthcare"],
]

consulting_check = ["PricewaterhouseCoopers (PwC)", "University of Michigan Desai Accelerator"]

education_check = ["Plymouth District Library", "University of Michigan Bentley Historical Library", "University of Michigan ITS", "University of Michigan Library"]

healthcare_check = ["Epic", "Health Management Associates", "VA Center for Clinical Management Research"]

software_check = ["Cisco", "Johnson Controls", "menlo innovations", "MRM", "TechSmith Corporation"]

other_industry_check = ["Amcor", "Auto-Owners Insurance", "Blue cross Blue Shield of Michigan", "Deloitte", "OneMagnify", "Procter & Gamble (P&G)", "United States Federal Bureau of Investigation (FBI)"]

largest_michigan_companies_check = ["Auto-Owners Insurance", "Health Management Associates"]

salaries = """Amcor; Project Engineer; 156857
Auto-Owners Insurance; Systems Analyst; 107997
Blue Cross Blue Shield of Michigan; Senior Analyst; 99793
Cisco; Business analyst; 150000
Deloitte; Senior Consultant; 111176
Epic; Software developer; 152441
Health Management Associates; Senior Consultant; 121856
Johnson Controls; Associate Project Manager; 90541
Menlo Innovations; Software Consultant; 234724
MRM; Associate Project Manager; 70338
OneMagnify; Technical Solutions Manager; 173165
Plymouth District Library; Librarian; 63927
PricewaterhouseCoopers (PwC); Technology Consultant; 123246
Procter & Gamble (P&G); Business Analyst; 116342
TechSmith Corporation; Technical Support Specialist; 62559
United States Federal Bureau of Investigation (FBI); Special agent; 115500
"""

salary_list_check = [
    ["Amcor", "Project Engineer", "156857"],
    ["Auto-Owners Insurance", "Systems Analyst", "107997"],
    ["Blue Cross Blue Shield of Michigan", "Senior Analyst", "99793"],
    ["Cisco", "Business analyst", "150000"],
    ["Deloitte", "Senior Consultant", "111176"],
    ["Epic", "Software developer", "152441"],
    ["Health Management Associates", "Senior Consultant", "121856"],
    ["Johnson Controls", "Associate Project Manager", "90541"],
    ["Menlo Innovations", "Software Consultant", "234724"],
    ["MRM", "Associate Project Manager", "70338"],
    ["OneMagnify", "Technical Solutions Manager", "173165"],
    ["Plymouth District Library", "Librarian", "63927"],
    ["PricewaterhouseCoopers (PwC)", "Technology Consultant", "123246"],
    ["Procter & Gamble (P&G)", "Business Analyst", "116342"],
    ["TechSmith Corporation", "Technical Support Specialist", "62559"],
    ["United States Federal Bureau of Investigation (FBI)", "Special agent", "115500"],
]

consult_manager_salary_check = [111176, 121856, 90541, 234724, 70338, 173165, 123246]

company_salary_one_check = ["Auto-Owners Insurance", "Cisco", "Deloitte", "Health Management Associates"]

company_salary_two_check = ("Menlo Innovations", 234724)

final_salary_check = [306857, 219173, 221649, 387165, 160879, 296411, 180269, 178059]

# End Setup Code


# PROBLEM 01
print("\nPROBLEM 1")

# TODO 1.1

employers = []
for i in range(len(data)):
    employers.append(data[i].split(", "))
# print(f"\n[1.1] employers = {employers}")
# assert employers == employers_check

# TODO 1.2

headers = employers[0]

# print(f"\n[1.2] headers row = {headers}")
# assert headers == headers_check

# PROBLEM 02
print("\nPROBLEM 2")

# TODO 2.1
universities_innovation = []

# TODO 2.2
other_companies = []

# TODO 2.3
for i in employers[1:]:
    if "university" in i[0].lower() and "innovation" in i[0].lower():
        universities_innovation.append(i)
    else:
        other_companies.append(i)

# print(f"\nuniversities_innovation = {universities_innovation}")
# assert universities_innovation == universities_innovation_check

# print(f"\nother_companies = {other_companies}")
# assert other_companies == other_companies_check

# PROBLEM 03
print("\nPROBLEM 3")

# TODO 3.1
consulting = []
education = []
healthcare = []
software = []
other_industry = []

# TODO 3.2, 3.3, 3.4
for i in other_companies:
    industry = i[4].strip().lower()
    if "consulting" in industry:
        consulting.append(i[0])
    elif "education" in industry:
        education.append(i[0])
    elif "healthcare" in industry:
        healthcare.append(i[0])
    elif "software" in industry:
        software.append(i[0])
    else:
        other_industry.append(i[0])


# print(f"\nconsulting = {consulting}")
# assert consulting == consulting_check

# print(f"\neducation = {education}")
# assert education == education_check

# print(f"\nhealthcare = {healthcare}")
# assert healthcare == healthcare_check

# print(f"\nsoftware = {software}")
# assert software == software_check

# print(f"\nother_industry = {other_industry}")
# assert other_industry == other_industry_check

# PROBLEM 04
print("\nPROBLEM 4")

# TODO 4.1
largest_michigan_companies = []

# TODO 4.2
max_num_employees = -1

# TODO 4.3, 4.4, 4.5
for i in other_companies:
    num_employees = int(i[2])
    location = i[1].lower()
    if location == "michigan":
        if num_employees > max_num_employees:
            max_num_employees = num_employees
            largest_michigan_companies = [i[0]]
        elif num_employees == max_num_employees:
            largest_michigan_companies.append(i[0])

# print(f"\nlargest_michigan_companies = {largest_michigan_companies}")
# assert largest_michigan_companies == largest_michigan_companies_check

# PROBLEM 05
print("\nPROBLEM 5")

# TODO 5.1
salary_list = salaries.strip().split("\n")
# print(f"\n[5.1] salary_list = {salary_list}")

# TODO 5.2, 5.3
for i in range(len(salary_list)):
    salary_list[i] = salary_list[i].split("; ")

# print(f"\n[5.2, 5.3] salary_list = {salary_list}")
# assert salary_list == salary_list_check

# PROBLEM 06
print("\nPROBLEM 6")

# TODO 6.1
consult_manager_salary = []

# TODO 6.2
i = 0

# TODO 6.3, 6.4
while i < len(salary_list):
    job_title = salary_list[i][1].lower()
    job_salary = int(salary_list[i][2])
    if "consult" in job_title or "manager" in job_title:
        consult_manager_salary.append(job_salary)
    i += 1

# print(f"\n[6.4] consult_manager_salary = {consult_manager_salary}")
# assert consult_manager_salary == consult_manager_salary_check

# TODO 6.5
avg_consult_manager_salary = round(sum(consult_manager_salary) / len(consult_manager_salary),2)

# print(f"\n[6.5] avg_consult_manager_salary = {avg_consult_manager_salary}")

# PROBLEM 07
print("\nPROBLEM 7")

# TODO 7.1
i = 0

# TODO 7.2
company_salary_one = []

# TODO 7.3, 7.4
while i < len(salary_list):
    if int(salary_list[i][2]) >= 100000 and int(salary_list[i][2]) <= 150000:
        company_salary_one.append(salary_list[i][0])
    elif int(salary_list[i][2]) > 175000:
        company_salary_two = (salary_list[i][0],int(salary_list[i][2]))
        break
    i += 1

# print(f"\ncompany_salary_one = {company_salary_one}")
# assert company_salary_one == company_salary_one_check

# print(f"\ncompany_salary_two = {company_salary_two}")
# assert company_salary_two == company_salary_two_check


# END PROBLEM SET
