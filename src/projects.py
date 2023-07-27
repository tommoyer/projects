#!/usr/bin/python3

# External libraries
import typer
import pprint

from typing import Optional
from typing_extensions import Annotated
from pathlib import Path

# Internal files
import notes
import resources
import times
import containers
from core_commands import *


app.add_typer(notes.app, name='notes', help='Manage notes for a project', rich_help_panel='Subcommands', callback=notes.project_callback)
app.add_typer(resources.app, name='resources', help='Manage resources for a project', rich_help_panel='Subcommands', callback=resources.project_callback)
app.add_typer(times.app, name='time', help='Manage time tracking for a project', rich_help_panel='Subcommands', callback=times.project_callback)
app.add_typer(containers.app, name='containers', help='Manage containers for a project', rich_help_panel='Subcommands', callback=containers.project_callback)

pp = pprint.PrettyPrinter()
state = {'project': None}


def first_run() -> None:
    pass


@app.callback()
def callback(config_directory: Annotated[Optional[Path], typer.Option(help='Directory to use for configuration files')] = Path('~/.config/projects/').expanduser()):
    typer.echo('Running the callback function')
    typer.echo(f'The config directory is: {config_directory}')
    first_run()


if __name__ == '__main__':
    app()
