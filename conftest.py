import pytest

# when running tests locally, I'd like to run pytest and see actual firefox pop up
# this is a workaround for that: we add the pytest config option, but don't use it.
# this is only so an error isn't thrown when we pass --headless=false
# the actual config check is done through sys.argv because pytest doesn't allow accessing config options
# from within the setup() method, where we set up the browser
# I'll not that for other important features, I ended up using environment variables.
def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store", default="false", help="Run tests in headless mode: true or false"
    )