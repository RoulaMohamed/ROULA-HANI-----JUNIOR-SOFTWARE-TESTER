import xlrd

# The function retrieves the test data from the excel sheet that contains the test cases
numSkip = 4


def getDataOfTest(testCase, testScenario):
    if testScenario == 1:
        Test_Case_val = testCase + numSkip  # to get correct row
        workbook = xlrd.open_workbook('C:\\Users\\Rolla\\Desktop\\TRELLA_TASK_3.xls')
        sheet = workbook.sheet_by_name('Sheet1')
        cell_value = sheet.cell(Test_Case_val, 4).value
        # print(cell_value)
        return cell_value
    else:
        Test_Case_val = testCase + 10  # to get correct row
        workbook = xlrd.open_workbook('C:\\Users\\Rolla\\Desktop\\TRELLA_TASK_3.xls')
        sheet = workbook.sheet_by_name('Sheet1')
        cell_value = sheet.cell(Test_Case_val, 4).value
        print(cell_value)
        return cell_value

#getDataOfTest(3, 0)