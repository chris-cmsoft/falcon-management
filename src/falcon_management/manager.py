import sys
from .exceptions import \
    NoCommandSpecified, \
    CommandNotFound, \
    CommandFailed
from .logger import error


class CommandManager():
    def __init__(self, commands: list = None):
        if not commands:
            commands = list()
        self.commands = commands

    def execute(self):
        """
        Run the specified command and catch errors to fail gracefully
        :return: void
        """
        try:
            self.validate_command(sys.argv)

            command = self.instantiate_command_class()

            args = command.arg_parser.parse_args(sys.argv[1:])

            try:
                command.handle(vars(args))
            except CommandFailed as err:
                error(str(err))
                exit(1)
        except NoCommandSpecified:
            # @TODO List available commands with their help text
            error('No command specified')
            exit(1)
        except CommandNotFound:
            # @TODO List available commands with their help text
            error('Command not found')
            exit(1)

    def validate_command(self, args):
        """
        Validate args and execute the command
        :return: void
        """
        if len(args) == 1:
            """
            The first item in args is usually 'console.py'.
            If a command is specified the length of args wil be > 1
            If not raise NoCommandSpecified
            """
            raise NoCommandSpecified

        if args[1] not in self.commands:
            """
            If command does not exists in the command mapping specified,
                raise a CommandNotFound error
            """
            raise CommandNotFound

        return True

    def instantiate_command_class(self):
        """
        Create a new instance of the command class and add its arguments
        :return: BaseCommand
        """
        command = self.commands[sys.argv[1]]()
        command.add_default_arguments()
        command.add_arguments()
        return command
