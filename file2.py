import logging

# Setting up logger is a simple 5 step process

# Create logger
logger = logging.Logger(__name__, logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/test2.log')

# Create formatters
common_formatter = logging.Formatter("%(message)s in %(name)s")

# Add formatters to handlers
file_handler.setFormatter(common_formatter)
console_handler.setFormatter(common_formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def function2():
    logger.debug("inside "+ function2.__name__)
    logger.debug("leaving "+ function2.__name__)
