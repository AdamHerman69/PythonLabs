import sys

class Logger:
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.printers = []

    def set_level(self, level):
        self.level = level

    def add_printer(self, printer):
        if callable(getattr(printer, "print", None)):
            self.printers.append(printer)
        else:
            raise ValueError

    def log(self, level, message):
        if level > self.level:
            for printer in self.printers:
                printer.print(message)


class StandardPrinter:
    def print(self, message):
        print(message)

class ErrorPrinter:
    def print(self, message):
        sys.stderr.write(message)
