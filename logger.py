import logging


log = logging.getLogger('chat_bot')


# objects for configuration, add more if needed
logging_handlers = [logging.StreamHandler, logging.FileHandler('bot.log')]
logging_formatters = [logging.Formatter('%(levelname)s %(message)s'), logging.Formatter('%(asctime)s %(levelname)s %(message)s')]
logging_levels = [logging.INFO, logging.DEBUG]


def configure_logger(handlers: tuple, formatters: tuple, levels: tuple):

    for handler, formatter, level in zip(handlers, formatters, levels):
        if isinstance(handler, logging.FileHandler):
            handler.setFormatter(formatter)
            handler.setLevel(level)
            log.setLevel(level)
            log.addHandler(handler)
        else:
            handler_obj = handler()
            handler_obj.setFormatter(formatter)
            handler_obj.setLevel(level)
            log.addHandler(handler_obj)
