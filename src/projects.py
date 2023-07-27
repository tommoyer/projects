#!/usr/bin/python3

# External libraries
import typer
import pprint
import logging

from typing import Optional
from typing_extensions import Annotated
from pathlib import Path
from importlib.metadata import version

# Internal files
import notes
import resources
import times
import containers
import project
from core_commands import *


app.add_typer(notes.app, name='notes', help='Manage notes for a project', rich_help_panel='Subcommands', callback=notes.project_callback)
app.add_typer(resources.app, name='resources', help='Manage resources for a project', rich_help_panel='Subcommands', callback=resources.project_callback)
app.add_typer(times.app, name='time', help='Manage time tracking for a project', rich_help_panel='Subcommands', callback=times.project_callback)
app.add_typer(containers.app, name='containers', help='Manage containers for a project', rich_help_panel='Subcommands', callback=containers.project_callback)

pp = pprint.PrettyPrinter()
state = project.ProjectsState()
logging.basicConfig(level=logging.WARNING,)
_logger = logging.getLogger(__name__)


def version_callback(value: bool):
    if value:
        typer.echo(f'Projects version: {version("projects")}')
        raise typer.Exit()


def first_run() -> None:
    '''
    Does the initial creation stuff when things like config files and directories don't exist
    This function should never make changes to existing files
    '''
    _logger.debug('Running first_run()')
    state.config_directory.mkdir(mode=0o755, parents=True, exist_ok=True)
    state.config_directory.joinpath('config.toml').touch(mode=0o644, exist_ok=True)
    state.config_directory.joinpath('projects.state').touch(mode=0o644, exist_ok=True)


@app.callback()
def callback(config_directory: Annotated[Optional[Path], typer.Option(help='Directory to use for configuration files')] = Path('~/.config/projects/').expanduser(),
             version: Annotated[Optional[bool], typer.Option("--version", callback=version_callback, is_eager=True, help='Print the version of projects')] = None,
             debug: Annotated[Optional[bool], typer.Option("--debug", help='Enable debugging output')] = False,):
    if debug:
        _logger.setLevel(logging.DEBUG)
        state.set_debug(debug)

    state.config_directory = config_directory

    first_run()


if __name__ == '__main__':
    app()
