import argparse


class BaseCommand():
    description = 'Management command'
    automate_help_message = True

    def __init__(self):
        self.arg_parser = argparse.ArgumentParser(
            description=self.description,
            usage='%(prog)s command [options]',
            add_help=self.automate_help_message
        )

    def add_default_arguments(self):
        self.arg_parser.add_argument('command', help='Command to call')
        self.arg_parser.add_argument(
            '--verbose',
            help='Set verbosity',
            type=int,
            default=1
        )
        if not self.automate_help_message:
            self.arg_parser.add_argument(
                '--help',
                help='Show this help message'
            )

    def add_arguments(self):
        pass
