class BambooleanError(Exception):
    pass


class BambooleanInterpreterError(BambooleanError):
    pass


class BambooleanLexerError(BambooleanError):
    pass


class BambooleanParserError(BambooleanError):
    pass


class BambooleanRuntimeError(BambooleanError):
    pass


class NoSuchVisitorException(BambooleanError):
    pass
