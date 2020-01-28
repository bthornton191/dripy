import os
import pandas as pd

TEST_PASON_DATA = os.path.join(os.getcwd(), 'test', 'files', 'test_pason.csv')
TEST_EXPECTED_PASON_TIME = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
TEST_EXPECTED_PASON_RPM = [84.73, 84.81, 84.02, 84.04, 84.76, 84.71, 84.1, 83.82, 84.71, 84.88]
TEST_EXPECTED_GPM_SETPOINTS = [(0.0, 0.0), (138.0, 775.3327365045429), (3902.0, 128.795), (3918.0, 0.0)]
TEST_EXPECTED_RPM_SETPOINTS = [(0.0, 0.0), (24.0, 29.030303030303028), (59.0, 0.00934065934065934), (158.0, 27.910909090909097), (261.0, 84.42401117318435), (3892.0, 0.0077192982456140355), (3952.0, 29.03833333333333), (3966.0, 0.0), (3974.0, 28.995500000000003)]
TEST_EXPECTED_PASON_TORQUE = [10.818, 13.228, 12.958, 7.805, 10.584, 13.399, 12.922, 7.968, 10.328, 14.273, 13.868]

TEST_CSV_SURVEY_DATA = os.path.join(os.getcwd(), 'test', 'files', 'test_survey.csv')
TEST_CSV_SURVEY_DATA_MODIFIED = os.path.join(os.getcwd(), 'test', 'files', 'test_survey_modified.csv')
TEST_EXCEL_SURVEY_DATA = os.path.join(os.getcwd(), 'test', 'files', 'test_survey.xls')

TEST_LODESTAR_DATA = os.path.join(os.getcwd(), 'test', 'files', 'test_lodestar.csv')

def compare_objects(object_1, object_2):
    differences = []
    if len(object_1.__dict__) != len(object_2.__dict__):
        differences.append('Number of attributes is not equal.  {} in object_1 {} in object_2'.format(len(object_1.__dict__), len(object_2.__dict__)))
        
    for name, value in object_1.__dict__.items():
        if name not in object_2.__dict__:
            differences.append(f'Attribute {name} not in object 2')
            continue

        if isinstance(value, pd.DataFrame):
            # If the attribute is a dataframe
            if compare_list_of_strings(value.columns, object_2.__dict__[name].columns):
                differences.append('Columns of {0} dataframe differ. Columns in object_1 are {1}, columns in object_2 are {2}'.format(name, value.columns, object_2.__dict__[name].columns))
            if len(value) != len(object_2.__dict__[name]):
                differences.append('Length of {0} dataframe differs. Length in object_1 is {1}, length in object_2 is {2}'.format(name, len(value), len(object_2.__dict__[name])))
        elif value != object_2.__dict__[name]:
            differences.append('Value of {0} attribute differs. object_1.{0} = {1}, object_2.{0} = {2}'.format(name, value, object_2.__dict__[name]))
        

    return differences

def compare_list_of_strings(list_1, list_2):    
    for element in list_1:
        if element not in list_2:
            return False
    
    for element in list_2:
        if element not in list_1:
            return False
