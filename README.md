# selenium-bandaid
An example of working with flaky selenium tests, as generated by Selenium IDE.

# See example
run `pytest` in directory. It'll invoke a test with any file named test_*.py, which
should run test_example.py.

# installation requirements
pip install -r requirements.txt

- aka selenium and pytest
- also firefox needs to be installed
- selenium will automatically install the webdriver so don't worry about that one.

# How-To:
record your own tests by installing Selenium IDE. Be wary of fake extensions. I recommend going to
https://www.selenium.dev/selenium-ide/
and installing the browser extension from there.
You can then record a test, and then right click on the recorded test, select export, and now you have a test.
The test must be slightly modified (see example_test.py) and then it should take advantage of the waiting & refetching
code that I've written
