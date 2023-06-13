import datetime
import os.path

LAST_TRACE_LOCATION = os.path.join(os.path.dirname(__file__), "last-trace.txt")


def write_last_trace(date: str) -> None:
    """
    Write the last trace to the file.
    :param date: The date.
    :return: None.
    """
    with open(LAST_TRACE_LOCATION, "w") as f:
        last_trace = f"{datetime.datetime.now().isoformat()[0:23]}+0000" if date is None else date
        print(f"Writing [{last_trace}] to file... ", end="")
        f.write(last_trace)
        print("Done")
    pass


def read_last_trace() -> str:
    """
    Read the last trace from the file.
    :return: The last trace.
    """
    with open(LAST_TRACE_LOCATION, "r") as f:
        last_trace = f.read().strip()
        print(f"Read [{last_trace}] from file")
        return last_trace
