import os

TEST_PASON_DATA = os.path.join(os.getcwd(), 'test', 'files', 'test_pason.csv')
TEST_EXPECTED_PASON_TIME = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
TEST_EXPECTED_PASON_RPM = [84.73, 84.81, 84.02, 84.04, 84.76, 84.71, 84.1, 83.82, 84.71, 84.88]
TEST_EXPECTED_GPM_SETPOINTS = [(0.0, 0.0), (138.0, 775.3327365045429), (3902.0, 128.795), (3918.0, 0.0)]
TEST_EXPECTED_RPM_SETPOINTS = [(0.0, 0.0), (24.0, 29.030303030303028), (59.0, 0.00934065934065934), (158.0, 27.910909090909097), (261.0, 84.42401117318435), (3892.0, 0.0077192982456140355), (3952.0, 29.03833333333333), (3966.0, 0.0), (3974.0, 28.995500000000003)]
TEST_EXPECTED_PASON_TORQUE = [10.818, 13.228, 12.958, 7.805, 10.584, 13.399, 12.922, 7.968, 10.328, 14.273, 13.868]

TEST_CSV_SURVEY_DATA = os.path.join(os.getcwd(), 'test', 'files', 'test_survey.csv')
TEST_CSV_SURVEY_DATA_MODIFIED = os.path.join(os.getcwd(), 'test', 'files', 'test_survey_modified.csv')
TEST_EXCEL_SURVEY_DATA = os.path.join(os.getcwd(), 'test', 'files', 'test_survey.xls')