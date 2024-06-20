logger_ready = True

try:
    import logging
    from datetime import date
except ImportError:
    logger_ready = False


def calc_logs(message: str, message_type: str) -> None:
    """Creates logs in a calculator.log file.
    Message types are debug, info, warn, error and critical."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"simple-calculator-python-main/calculatorlog{date.today()}.log",
        filemode="w",
    )

    if message_type == "debug":
        logging.debug(message)
    elif message_type == "info":
        logging.info(message)
    elif message_type == "warn":
        logging.warning(message)
    elif message_type == "error":
        logging.error(message)
    elif message_type == "critical":
        logging.critical(message)
    else:
        logging.error("Invalid message type provided!")
