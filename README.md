# Petrarch_Test_Suite
To run the Petrarch Test Suite Builder :
- py TestSuite_Builder.py <input_xml_file>

The TestSuiteBuilder will generate test_script.py with the test cases coded in python for all scenarios in the <input_xml_file>

To run test_script.py:
- Copy the test_script.py to the directory containing Petrarch2.py
- py test_script.py

Output of test_script.py :
The test suite generates report in "~" separated Text File, which can be inported in Excel. It reports the Text,  Parse Tree, Expected Output as per Petrarch and the Output from Petrarch2

Limitations of Test Suite :
Currently the test suite does  not support scenarios to validate errors.
