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

# Petrarch_Universal Dependencies Test_Suite
To run the Petrarch Universal Dependencies Test Suite Builder :
- py TestSuite_Builder_UD.py <input_xml_file>

The TestSuiteBuilder will generate test_script_ud.py with the test cases coded in python for all scenarios in the <input_xml_file>

To run test_script_ud.py:
- Copy the test_script_ud.py to the directory containing Petrarch_UD.py
- py test_script_ud.py

Output of test_script_ud.py :
The test suite generates report in CSV format. It reports the Text,  Parse Tree, Expected Output as per Petrarch, the Output from PetrarchUD, the verb and noun phrases.

Limitations of Test Suite :
Currently the test suite does  not support scenarios to validate errors.
