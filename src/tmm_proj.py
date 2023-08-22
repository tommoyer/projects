#!/usr/bin/python3

# External libraries
import typer
import pprint
import logging
import tomli

from typing import Optional
from typing_extensions import Annotated
from pathlib import Path
from importlib.metadata import version

# Internal files
import data.project

import subcommands.note
import subcommands.resource
import subcommands.time
import subcommands.container
import subcommands.task


app = typer.Typer()
app.add_typer(subcommands.note.app, name='note', help='Manage notes for a project', rich_help_panel='Subcommands', callback=subcommands.note.project_callback)
app.add_typer(subcommands.resource.app, name='resource', help='Manage resources for a project', rich_help_panel='Subcommands', callback=subcommands.resource.project_callback)
app.add_typer(subcommands.time.app, name='time', help='Manage time tracking for a project', rich_help_panel='Subcommands', callback=subcommands.time.project_callback)
app.add_typer(subcommands.container.app, name='container', help='Manage containers for a project', rich_help_panel='Subcommands', callback=subcommands.container.project_callback)
app.add_typer(subcommands.task.app, name='task', help='Manage tasks for a project', rich_help_panel='Subcommands', callback=subcommands.task.project_callback)

pp = pprint.PrettyPrinter()
logging.basicConfig(level=logging.WARNING,)

state = dict()
state['logger'] = logging.getLogger(__name__)

default_config = '''

'''


@app.command(rich_help_panel='Project Commands')
def new(name: Annotated[str, typer.Argument(help='The name of a project to create')]):
    '''
    Create a new project titled NAME
    '''
    # status
    status = data.project.ProjectStatus.in_progress

    # keywords
    keywords = None

    # tags
    tags = None

    # notes_driver
    note_driver = None

    # notes_location
    note_location = None

    # resource_driver
    resource_driver = None

    # resource_location
    resource_location = None

    # container_driver
    container_driver = None

    # time_driver
    time_driver = None

    new_project = data.project.Project(name=name,
                                       status=status,
                                       keywords=keywords,
                                       tags=tags,
                                       note_driver=note_driver,
                                       notes=note_location,
                                       resource_driver=resource_driver,
                                       resource=resource_location,
                                       container_driver=container_driver,
                                       time_driver=time_driver,)
    state['projects'].add_project(new_project)


@app.command(rich_help_panel='Project Commands')
def list():
    '''
    List existing projects
    '''
    for project in state['projects'].list():
        print(f'{project}')


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
def register(name: Annotated[str, typer.Argument(help='The name of a project to register')]):
    '''
    Register existing project NAME
    '''
    print(f'Called register for {name}')


@app.command(rich_help_panel='Project Commands')
def sync(name: Annotated[str, typer.Argument(help='The name of a project to sync')]):
    '''
    Sync project NAME, ensuring metadata is in syync
    '''
    print(f'Called sync for {name}')


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
def set_keywords(name: Annotated[str, typer.Argument(help='The name of a project to set keywords for')],
                 keys: Annotated[str, typer.Argument(help='The keywords for this project')]):
    '''
    Set keywords of project NAME to KEYS
    '''
    print(f'Called set-keywords for {name} to set keywords {keys}')


@app.command(rich_help_panel='Project Commands')
def get_keywords(name: Annotated[str, typer.Argument(help='The name of a project to get keywords for')]):
    '''
    Get keywords of project NAME
    '''
    print(f'Called get-keywords for {name}')


@app.command(rich_help_panel='Project Commands')
def add_keyword(name: Annotated[str, typer.Argument(help='The name of a project to add a keyworkd to')],
                key: Annotated[str, typer.Argument(help='The keyword to add')]):
    '''
    Add a keyword KEY to project NAME
    '''
    print(f'Called add-keyword for {name} to add keyword {key}')


@app.command(rich_help_panel='Project Commands')
def remove_keyword(name: Annotated[str, typer.Argument(help='The name of a project to remove a keyworkd from')],
                   key: Annotated[str, typer.Argument(help='The keyword to remove')]):
    '''
    Remove keyword KEY from project NAME
    '''
    print(f'Called remove-keyword for {name} to remove keyword {key}')


def version_callback(value: bool) -> None:
    if value:
        print(f'Projects version: {version("projects")}')
        raise typer.Exit()


def first_run(state: dict) -> None:
    '''
    Does the initial creation stuff when things like config files and directories don't exist
    This function should never make changes to existing files
    '''
    state['logger'].debug('Running first_run()')
    state['config_directory'].mkdir(mode=0o755, parents=True, exist_ok=True)
    if not state['config_directory'].joinpath('config.toml').exists():
        state['logger'].debug('Creating config.toml')
        with open(state['config_directory'].joinpath('config.toml'), 'w') as f:
            f.write(default_config)
    if not state['config_directory'].joinpath('projects.pickle').exists():
        state['logger'].debug('Creating state file')
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
        state['logger'].setLevel(logging.DEBUG)

    state['config_directory'] = config_directory
    state['config'] = None
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
