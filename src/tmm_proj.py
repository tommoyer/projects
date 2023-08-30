#!/usr/bin/python3

# External libraries
import typer
import pprint
import logging
import tomli
import pkgutil
import os

from typing import Optional
from typing_extensions import Annotated
from pathlib import Path
from importlib.metadata import version
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

# Internal files
import data.project

import subcommands.note
import subcommands.plugins.note
import subcommands.resource
import subcommands.plugins.resource
import subcommands.time
import subcommands.plugins.time
import subcommands.container
import subcommands.plugins.container
import subcommands.task
import subcommands.plugins.task


app = typer.Typer()
app.add_typer(subcommands.note.app, name='note', help='Manage notes for a project', rich_help_panel='Subcommands', callback=subcommands.note.project_callback)
app.add_typer(subcommands.resource.app, name='resource', help='Manage resources for a project', rich_help_panel='Subcommands', callback=subcommands.resource.project_callback)
app.add_typer(subcommands.time.app, name='time', help='Manage time tracking for a project', rich_help_panel='Subcommands', callback=subcommands.time.project_callback)
app.add_typer(subcommands.container.app, name='container', help='Manage containers for a project', rich_help_panel='Subcommands', callback=subcommands.container.project_callback)
app.add_typer(subcommands.task.app, name='task', help='Manage tasks for a project', rich_help_panel='Subcommands', callback=subcommands.task.project_callback)

pp = pprint.PrettyPrinter()
logging.basicConfig(level=logging.WARNING,)

state = {}
_logger = logging.getLogger(__name__)

default_config = '''

'''


@app.command(rich_help_panel='Project Commands')
def new(name: Annotated[str, typer.Argument(help='The name of a project to create')]):
    '''
    Create a new project titled NAME
    '''
    if state['projects'].exists(name):
        print(f'Project {name} already exists')
        return

    # status
    print(data.project.ProjectStatus)
    status = Prompt.ask('Project status [in_progress]', default='in_progress')
    while not hasattr(data.project.ProjectStatus, status):
        print(f'{status} is not a valid choice, please enter a valid choice')
        print(data.project.ProjectStatus)
        status = Prompt.ask('Project status')

    # tags
    tags = []
    tag = Prompt.ask('Tag, enter for none', default=None)
    while tag:
        tags.append(tag)
        tag = Prompt.ask('Next tag, enter to finish', default=None)

    # notes_driver
    note_plugin_path = os.path.dirname(subcommands.plugins.note.__file__)
    note_plugins = [name for _, name, _ in pkgutil.iter_modules([note_plugin_path])]
    print(f'Available notes plugins (enter to select none:')
    for idx, note_plugin in enumerate(note_plugins):
        print(f' - {note_plugin}')
    note_driver = Prompt.ask('Note plugin', choices=note_plugins, default=None, show_choices=False)

    # resource_driver
    resource_plugin_path = os.path.dirname(subcommands.plugins.resource.__file__)
    resource_plugins = [name for _, name, _ in pkgutil.iter_modules([resource_plugin_path])]
    print(f'Available resource plugins (enter to select none:')
    for idx, resource_plugin in enumerate(resource_plugins):
        print(f' - {resource_plugin}')
    resource_driver = Prompt.ask('Resource plugin', choices=resource_plugins, default=None, show_choices=False)

    # container_driver
    container_plugin_path = os.path.dirname(subcommands.plugins.container.__file__)
    container_plugins = [name for _, name, _ in pkgutil.iter_modules([container_plugin_path])]
    print(f'Available container plugins (enter to select none:')
    for idx, container_plugin in enumerate(container_plugins):
        print(f' - {container_plugin}')
    container_driver = Prompt.ask('container plugin', choices=container_plugins, default=None, show_choices=False)

    # time_driver
    time_plugin_path = os.path.dirname(subcommands.plugins.time.__file__)
    time_plugins = [name for _, name, _ in pkgutil.iter_modules([time_plugin_path])]
    print(f'Available time plugins (enter to select none:')
    for idx, time_plugin in enumerate(time_plugins):
        print(f' - {time_plugin}')
    time_driver = Prompt.ask('time plugin', choices=time_plugins, default=None, show_choices=False)

    # task_driver
    task_plugin_path = os.path.dirname(subcommands.plugins.task.__file__)
    task_plugins = [name for _, name, _ in pkgutil.iter_modules([task_plugin_path])]
    print(f'Available task plugins (enter to select none:')
    for idx, task_plugin in enumerate(task_plugins):
        print(f' - {task_plugin}')
    task_driver = Prompt.ask('task plugin', choices=task_plugins, default=None, show_choices=False)

    new_project = data.project.Project(name=name,
                                       status=status,
                                       tags=tags,
                                       note_driver=note_driver,
                                       resource_driver=resource_driver,
                                       container_driver=container_driver,
                                       time_driver=time_driver,
                                       task_driver=task_driver)
    state['projects'].add_project(new_project)


@app.command(rich_help_panel='Project Commands')
def list():
    '''
    List existing projects
    '''
    table = Table(title='Projects')
    table.add_column('Name')
    for project in state['projects'].list():
        table.add_row(f'{project}')
    console = Console()
    console.print(table)


@app.command(rich_help_panel='Project Commands')
def archive(name: Annotated[str, typer.Argument(help='The name of a project to archive')]):
    '''
    Archive project NAME
    '''
    print(f'Called archive {name}')


@app.command(rich_help_panel='Project Commands')
def delete(name: Annotated[str, typer.Argument(help='The name of a project to delete')]):
    '''
    Delete project NAME
    '''
    print(f'Called delete {name}')


@app.command(rich_help_panel='Project Commands')
def grep(name: Annotated[str, typer.Argument(help='The name of a project to search')],
         search: Annotated[str, typer.Argument(help='The search string to look for')]):
    '''
    Search project NAME for SEARCH
    '''
    print(f'Called search {name} for {search}')


@app.command(rich_help_panel='Project Commands')
def set_status(name: Annotated[str, typer.Argument(help='The name of a project to set the status of')],
               status: Annotated[str, typer.Argument(help='The updated status of the project')]):
    '''
    Set status of project NAME to STATUS
    '''
    print(f'Called set-status for {name} to {status}')


@app.command(rich_help_panel='Project Commands')
def get_status(name: Annotated[str, typer.Argument(help='The name of a project to get the status of')]):
    '''
    Get status of project NAME
    '''
    print(f'Called get-status for {name}')


@app.command(rich_help_panel='Project Commands')
def set_tags(name: Annotated[str, typer.Argument(help='The name of a project to work with')],
             tags: Annotated[str, typer.Argument(help='The tags for this project')]):
    '''
    Set tags of project NAME to TAGS
    '''
    print(f'Called set-tags for {name} to tags {tags}')


@app.command(rich_help_panel='Project Commands')
def get_tags(name: Annotated[str, typer.Argument(help='The name of a project to get tags for')]):
    '''
    Get tags of project NAME
    '''
    print(f'Called get-tags for {name}')


@app.command(rich_help_panel='Project Commands')
def add_tag(name: Annotated[str, typer.Argument(help='The name of a project to add a tag to')],
            tag: Annotated[str, typer.Argument(help='The tag for a project')]):
    '''
    Add a tag TAG to project NAME
    '''
    print(f'Called add-tag for {name} to add tag {tag}')


@app.command(rich_help_panel='Project Commands')
def remove_tag(name: Annotated[str, typer.Argument(help='The name of a project to remove a tag from')],
               tag: Annotated[str, typer.Argument(help='The tog to remove')]):
    '''
    Remove tag TAG from project NAME
    '''
    print(f'Called remove-tag for {name} to remove tag {tag}')


@app.command(rich_help_panel='Project Commands')
def info(name: Annotated[str, typer.Argument(help='The name of a project to show infomation from, leave blank to show all projects')] = None):
    '''
    Print detailed information about projects
    '''
    if name:
        try:
            project = state['projects'][name]
            project.info()
        except KeyError:
            print(f'Project {name} does not exist')
    else:
        print(state['projects'].info())


def version_callback(value: bool) -> None:
    if value:
        print(f'Projects version: {version("projects")}')
        raise typer.Exit()


def first_run(state: dict) -> None:
    '''
    Does the initial creation stuff when things like config files and directories don't exist
    This function should never make changes to existing files
    '''
    _logger.debug('Running first_run()')
    state['config_directory'].mkdir(mode=0o755, parents=True, exist_ok=True)
    if not state['config_directory'].joinpath('config.toml').exists():
        _logger.debug('Creating config.toml')
        with open(state['config_directory'].joinpath('config.toml'), 'w') as f:
            f.write(default_config)
    if not state['config_directory'].joinpath('projects.pickle').exists():
        _logger.debug('Creating state file')
        with open(state['config_directory'].joinpath('projects.pickle'), 'wb') as f:
            # create ProjectsState object
            state['projects'] = data.project.ProjectsState(state)
            # Pickle it
            state['projects'].save()


@app.callback()
def callback(config_directory: Annotated[Optional[Path], typer.Option(help='Directory to use for configuration files')] = Path('~/.config/projects/').expanduser(),
             version: Annotated[Optional[bool], typer.Option("--version", callback=version_callback, is_eager=True, help='Print the version of projects')] = None,
             debug: Annotated[Optional[bool], typer.Option("--debug", help='Enable debugging output')] = False,) -> None:
    if debug:
        _logger.setLevel(logging.DEBUG)

    state['config_directory'] = config_directory
    state['config'] = None
    state['debug'] = debug
    first_run(state)

    # Try to read configuration file
    try:
        with open(f'{state["config_directory"]}/config.toml', 'rb') as inputFile:
            state['config'] = tomli.load(inputFile)
    except IOError as e:
        print('Configuration file not found, using sane defaults')

    # Load project state
    state['projects'] = data.project.ProjectsState(state).load()


if __name__ == '__main__':
    app()
