import inspect,sys
def retrieve_name(var):
    """
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]
# -------------------------
# Input / typing utilities
# -------------------------
def get_linenumber():
    try:
        return inspect.currentframe().f_back.f_lineno
    except Exception as e:
        raise RuntimeError("error 033 occurred in get_linenumber") from e
import inspect
import sys

def debug(*variables):
    # 1. Get the caller's line number
    line = inspect.currentframe().f_back.f_lineno
    print(f"--- DEBUG: as of line {line} ---")
    for x in variables:
        name = retrieve_name(x)
        v_type = type(x).__name__
        v_size = sys.getsizeof(x)
        v_id = id(x)
        v_dict = getattr(x, '__dict__','N/A')
        v_doc = str(getattr(x, '__doc__','N/A')).strip().split('\n')[0]
        v_methods = [m for m in dir(x) if not m.startswith('_')][:5]
        print(f"------ VARIABLE NAME: {name}")
        print(f"Value: {x} | Type: {v_type}")
        print(f"Size: {v_size} bytes | ID: {v_id}")
        print(f"Doc: {v_doc}")
        print(f"Dict: {v_dict}")
        print(f"Methods: {v_methods}")
        print("-" * 30)