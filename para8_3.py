import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='para8_3_logs.log',
                    filemode='a',
                    format="We have a logging message: %(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )

try:
    print(10/0)
except Exception:
    logging.exception("exception")
    