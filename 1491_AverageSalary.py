"""
    1491. Average Salary Excluding the Minimum and Maximum Salary

    You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
    
    Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

    :type salary: List[int]
    :rtype: float

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def average(self, salary):
    return (float(sum(salary)-max(salary)-min(salary)))/(len(salary)-2)
