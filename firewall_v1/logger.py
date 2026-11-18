import logging


class Logger:

    @staticmethod
    def get(name="FirewallV1", level=logging.INFO):
        logger = logging.getLogger(name)
        logger.setLevel(level)

        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(
                    "[%(levelname)s] %(name)s: %(message)s"
                )
            )
            logger.addHandler(handler)

        return logger
