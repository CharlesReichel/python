# START PROBLEM SET 2
print("PROBLEM SET 02 \n")

# Setup Code (DO NOT MODIFY)

health_check = [
    "Counseling and Psychological Services (CAPS)|734-764-8312",
    "Wolverine Wellness|",
    "University Health Service (UHS)|734-764-8320",
    "SilverCloud|734-936-8660",
]

addl_academic_resources_check = [
    "Office of Student Conflict Resolution|734-936-6308",
    "Services for Students with Disabilities (SSD)|734-763-3000",
]

academic_check = [
    "Dean of Students Office|734-764-7420",
    "Sweetland Center for Writing|734-764-0429",
    "Office of the Ombuds|734-763-3545",
    "Office of Student Conflict Resolution|734-936-6308",
    "Services for Students with Disabilities (SSD)|734-763-3000",
]

wellbeing_resources = (
    "Dean of Students Office|734-764-7420, "
    "Sweetland Center for Writing|734-764-0429, "
    "Office of the Ombuds|734-763-3545, "
    "Counseling and Psychological Services (CAPS)|734-764-8312, "
    "Wolverine Wellness|, "
    "Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771, "
    "Trotter Multicultural Center|734-763-3670, "
    "Spectrum Center|734-763-4186, "
    "Maize and Blue Cupboard (MBC)|734-936-2794, "
    "Ginsberg Center for Community Service Learning|734-763-3548"
)

# End setup code


# PROBLEM 01
print("\nPROBLEM 01")

# TODO 1.1
resources = wellbeing_resources.split(", ")

#print(f"\n1.1 resource = {resources}")

# TODO 1.2
academic = resources[0:3]

#print(f"\n1.2 academic = {academic}")

# TODO 1.3
health = resources[3:5]

# print(f"\n1.3 health = {health}")

# TODO 1.4
marginalized_comm = resources[-5:-2]

#print(f"\n1.4 marginalized_comm = {marginalized_comm}")

# TODO 1.5
community = resources[-2:]

#print(f"\n1.5 community = {community}")


# PROBLEM 02
print("\nPROBLEM 02")

addl_health_resources = [
    "University Health Service (UHS)|734-764-8320",
    "SilverCloud|734-936-8660",
]

# TODO 2.1
health.extend(addl_health_resources)

#print(f"\n2.1 health = {health}")
#assert health == health_check

embedded_caps = "UMSI Embedded CAPS Psychologist|Ashley Evearitt"

# TODO 2.2
health.append(embedded_caps)

#print(f"\n2.2 health = {health}")

mesa = "Multi-ethnic Student Affairs (MESA)|734-763-9044"

# TODO 2.3
marginalized_comm.insert(2, mesa)

#print(f"\n2.3 marginalized_com = {marginalized_comm}")

addl_academic_resources = [
    "Office of Student Conflict Resolution",
    "Services for Students with Disabilities (SSD)",
]
addl_academic_resource_numbers = ["|734-936-6308", "|734-763-3000"]

# TODO 2.4
addl_academic_resources[0] += addl_academic_resource_numbers[0]
addl_academic_resources[1] += addl_academic_resource_numbers[1]

#print(f"\n2.4 addl_academic_resources = {addl_academic_resources}")
#assert addl_academic_resources == addl_academic_resources_check

# TODO 2.5
academic.extend(addl_academic_resources)

#print(f"\n2.5 academic = {academic}")
#assert academic == academic_check


# PROBLEM 03
print("\nPROBLEM 03")

# TODO 3.1 reverse order of marginalized_comm
marginalized_comm.reverse()

#print(f"\n3.1 marginalized_comm = {marginalized_comm}")

# TODO 3.2 sort health list in ascending alphaanumeric order
health.sort()

#print(f"\n3.2 health = {health}")

# TODO 3.3 sort academic list in descending alphabetical order
academic.sort(reverse=True)

# print(f"\n3.3 academic = {academic}")

# TODO 3.4 return index value of UMSI Embedded CAPS Psychologist in health and assign value to umsi_caps
umsi_caps = health.index("UMSI Embedded CAPS Psychologist|Ashley Evearitt")

# print(f"\n3.4 umsi_caps = {umsi_caps}")

# TODO 3.5
student_focused_health_resources = health[umsi_caps:umsi_caps+2]

# print(f"\n3.5 student_focused_health_resources = {student_focused_health_resources}")


# PROBLEM 04
print("\nPROBLEM 04")

# TODO 4.1 make third_academic_element a tuple
third_academic_element = tuple(academic[2].split("|"))

#print(f"\n4.1 third_academic_element = {third_academic_element}")
#assert third_academic_element == ('Office of the Ombuds', '734-763-3545')

# TODO 4.2
second_last_health = tuple(health[-2].split("|"))

#print(f"\n4.2 second_last_health = {second_last_health}")
#assert second_last_health ==  ('University Health Service (UHS)', '734-764-8320')

# TODO 4.3
marginalized_comm_str = ".".join(marginalized_comm)

#print(f"\n4.3 marginalized_comm_str = {marginalized_comm_str}")
#assert marginalized_comm_str == 'Spectrum Center|734-763-4186.Multi-ethnic Student Affairs (MESA)|734-763-9044.Trotter Multicultural Center|734-763-3670.Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771'


# PROBLEM 05
print("\nPROBLEM 05")

# TODO 5.1
odd_index_health = health[1::2]

#print(f"\n5.1 odd_index_health = {odd_index_health}")

# TODO 5.2
academic_sub_list = academic[-2:-5:-1]

#print(f"\n5.2 academic_sub_list = {academic_sub_list}")
#assert academic_sub_list == ['Office of Student Conflict Resolution|734-936-6308', 'Office of the Ombuds|734-763-3545', 'Services for Students with Disabilities (SSD)|734-763-3000']

# TODO 5.3
marginalized_comm_reversed = marginalized_comm[::-1]
#print(f"\n5.3 marginalized_comm_reversed = {marginalized_comm_reversed}")


# PROBLEM 06
print("\nPROBLEM 06")

# TODO 6.1
student_dean_index = academic.index("Dean of Students Office|734-764-7420")
#print(f"\n6.1 student_dean_index = {student_dean_index}")

# TODO 6.2 Use student_dean_index in a slicing expression that slices two (2) elements from academic in the following order: Dean of Students Office|734-764-7420, Office of the Ombuds|734-763-3545
#academic_sub_list = []
#academic_sub_list.append(academic[student_dean_index])
#academic_sub_list.append(academic[student_dean_index-2])

#academic_sub_list = [academic[student_dean_index]] + [academic[student_dean_index-2]]

academic_sub_list = academic[student_dean_index:student_dean_index-3:-2]

#print(academic)
#print(f"\n6.2 academic_sub_list = {academic_sub_list}")
#assert academic_sub_list ==  ['Dean of Students Office|734-764-7420', 'Office of the Ombuds|734-763-3545']


# END PROBLEM SET
