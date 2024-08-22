import ctypes
from loggings import loggers # type: ignore

def check_so_file(path='./java-grammar.so'):
    '''
    This function checks the integrity of the shared object file.
    This file is necessary to parse Java repos as it contains the Java grammar
    for parsing Java repos.
    '''
    log = loggers('logs/check.log')
    # path error will be print on console as well as on logging
    error = f"Java grammar file not found at path: {path}"

    try:
        lib = ctypes.CDLL(path)
        log.info(f"Java grammar file at '{path}' is OK.")
    except OSError as e:
        if "No such file" in str(e):
            print(error)
            log.error(error)
        else:
            log.warning(f"Shared Object integrity compromised at path: {e}")

# check_so_file()