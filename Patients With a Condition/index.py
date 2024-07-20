import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients_with_diabetes = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    
    # Select only the required columns
    result_df = patients_with_diabetes[['patient_id', 'patient_name', 'conditions']]
    
    return result_df
