import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='para8_2_logs.log',
                    filemode='a',
                    format="We have a logging message: %(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")