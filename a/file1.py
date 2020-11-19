import logging
# SETTING UP LOGGING IS A SIMPLE 5-STEP PROCESS

# Create logger
logger = logging.Logger(__name__, logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/test.log')

# Create formatters
console_formatter = logging.Formatter("%(message)s in %(name)s")
file_formatter = logging.Formatter("%(message)s in %(name)s")

# Add formatters to handlers
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

import file2

def function1():
    logger.debug('inside '+ function1.__name__)
    file2.function2()
    logger.debug("leaving "+ function1.__name__)


function1()
    