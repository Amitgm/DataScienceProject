''' BIG NOTE: WHEN IMPORTING MODULES FROM A DIRECTORY, AND IMPORTING A LOGGER DEFINED IN THE __INIT__.PY FILE, THE LOGGER 

MUST BE DEFINED AS logger = logging.getLogger("datasciencelogger") IN __INIT__.PY FILE.'''

from src.datascience import logger

logger.info("Welcome to our custom logger!")

