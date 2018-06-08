# Falcon Management Commands

A simpler management command creator.

> This package was born out of necessity for simpler management commands

# Installation

`pip install falcon_management`

# Getting Started

First we need to create a management command:

The command can be any class extending from `falcon_management.command.BaseCommand`  
    and containing a `handle` method

eg. in `foo/commands.py`
```python
from falcon_management import logger, command


class TestCommand(command.BaseCommand):
    """
    A command to test commands
    """

    def handle(self, options, *args):
        """
        The method which handles the job.

            All command options passed in eg. python console.py test --foo=bar --baz bav
                will be available in `options`
                
            eg. for the above command `options` will be:
                {
                    'command': 'test'
                    'foo': 'bar',
                    'baz': 'bav',
                }

        :param options: dict
        :param args:
        :return: void
        """
        logger.success('The command has run.')

```

Now to running the command.

In order to run management commands, create a console.py file in your project with the following contnts:

```python
# Import the falcon_management CommandManager. This will take care of mapping your commands
from falcon_management.manager import CommandManager

# Import our command class
from foo.commands import TestCommand

if __name__ == '__main__':
    # Mapping of commands in the fashion: `cli_name` -> `command_class`
    manager = CommandManager({
        'test': TestCommand
    })

    manager.execute()
```

Now run `PYTHONPATH=. python foo/console.py test` and you should see a 'The command has run.' message which is the message from your command.

When a command fails raise a CommandFailed exception:

```python
from falcon_management.exceptions import CommandFailed

def handle(self, options, *args):
    # Raising this exception will exit the process with status 1 and display error text in red.
    raise CommandFailed('Command Failed.')
```


From here the sky is the limit

# Logging

Falcon management includes a small logger to add colors to your console output.
 
### Usage

```python
from falcon_management.logger import info, success, warn, error

info('This text will be displayed in blue.')
success('This text will be displayed in green.')
warn('This text will be displayed in yellow.')
error('This text will be displayed in red.')
```

# Features coming soon:
* Easy to use interactive console for input
