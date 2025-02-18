import ctypes
from loggings import loggers # type: ignore

def check_so_file(path='./java-grammar.so'):
    '''
    This function checks the integrity of the shared object file.
    This file is necessary to parse Java repos as it contains the Java grammar
    for parsing Java repos.
    '''

    log = loggers('logs/check.log')
    error = f"Java grammar file not found at path: {path}"

    try:
        lib = ctypes.CDLL(path)
        log.info(f"Java grammar file at '{path}' is OK.")
        return True
    except OSError as e:
        if "No such file" in str(e):
            print(error)
            log.error(error)
        else:
            log.warning(f"Shared Object integrity compromised at path: {e}")

    return False

# check_so_file()