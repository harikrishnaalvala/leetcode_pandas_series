import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])

    # Merge the employee and department DataFrames on 'departmentId' and 'id' columns
    merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes= ('_employee', '_department'))

    # Find the maximum salary in each department
    max_salaries = merged_df.groupby('departmentId')['salary'].transform('max')

    # Filter for employees with maximum salary in each department
    highest_salary_df = merged_df[merged_df['salary'] == max_salaries]

    # Select the required columns
    result_df = highest_salary_df[['name_department', 'name_employee', 'salary']]

    # Rename the columns as specified
    result_df.columns = ['Department', 'Employee', 'Salary']

    return result_df
