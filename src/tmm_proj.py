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


app = typer.Typer()
app.add_typer(subcommands.note.app, name='note', help='Manage notes for a project', rich_help_panel='Subcommands', callback=subcommands.note.project_callback)
app.add_typer(subcommands.resource.app, name='resource', help='Manage resources for a project', rich_help_panel='Subcommands', callback=subcommands.resource.project_callback)
app.add_typer(subcommands.time.app, name='time', help='Manage time tracking for a project', rich_help_panel='Subcommands', callback=subcommands.time.project_callback)
app.add_typer(subcommands.container.app, name='container', help='Manage containers for a project', rich_help_panel='Subcommands', callback=subcommands.container.project_callback)

pp = pprint.PrettyPrinter()
state = data.project.ProjectsState()
logging.basicConfig(level=logging.WARNING,)
runtime_state = dict()
runtime_state['logger'] = logging.getLogger(__name__)

default_config = '''

'''


@app.command(rich_help_panel='Project Commands')
def new(name: Annotated[str, typer.Argument(help='The name of a project to create')]):
    '''
    Create a new project titled NAME
    '''
    pass


@app.command(rich_help_panel='Project Commands')
def list():
    '''
    List existing projects
    '''
    typer.echo(f'Called list')


@app.command(rich_help_panel='Project Commands')
def archive(name: Annotated[str, typer.Argument(help='The name of a project to archive')]):
    '''
    Archive project NAME
    '''
    typer.echo(f'Called archive {name}')


@app.command(rich_help_panel='Project Commands')
def delete(name: Annotated[str, typer.Argument(help='The name of a project to delete')]):
    '''
    Delete project NAME
    '''
    typer.echo(f'Called delete {name}')


@app.command(rich_help_panel='Project Commands')
def grep(name: Annotated[str, typer.Argument(help='The name of a project to search')],
         search: Annotated[str, typer.Argument(help='The search string to look for')]):
    '''
    Search project NAME for SEARCH
    '''
    typer.echo(f'Called search {name} for {search}')


@app.command(rich_help_panel='Project Commands')
def set_status(name: Annotated[str, typer.Argument(help='The name of a project to set the status of')],
               status: Annotated[str, typer.Argument(help='The updated status of the project')]):
    '''
    Set status of project NAME to STATUS
    '''
    typer.echo(f'Called set-status for {name} to {status}')


@app.command(rich_help_panel='Project Commands')
def get_status(name: Annotated[str, typer.Argument(help='The name of a project to get the status of')]):
    '''
    Get status of project NAME
    '''
    typer.echo(f'Called get-status for {name}')


@app.command(rich_help_panel='Project Commands')
def register(name: Annotated[str, typer.Argument(help='The name of a project to register')]):
    '''
    Register existing project NAME
    '''
    typer.echo(f'Called register for {name}')


@app.command(rich_help_panel='Project Commands')
def sync(name: Annotated[str, typer.Argument(help='The name of a project to sync')]):
    '''
    Sync project NAME, ensuring metadata is in syync
    '''
    typer.echo(f'Called sync for {name}')


@app.command(rich_help_panel='Project Commands')
def set_tags(name: Annotated[str, typer.Argument(help='The name of a project to work with')],
             tags: Annotated[str, typer.Argument(help='The tags for this project')]):
    '''
    Set tags of project NAME to TAGS
    '''
    typer.echo(f'Called set-tags for {name} to tags {tags}')


@app.command(rich_help_panel='Project Commands')
def get_tags(name: Annotated[str, typer.Argument(help='The name of a project to get tags for')]):
    '''
    Get tags of project NAME
    '''
    typer.echo(f'Called get-tags for {name}')


@app.command(rich_help_panel='Project Commands')
def add_tag(name: Annotated[str, typer.Argument(help='The name of a project to add a tag to')],
            tag: Annotated[str, typer.Argument(help='The tag for a project')]):
    '''
    Add a tag TAG to project NAME
    '''
    typer.echo(f'Called add-tag for {name} to add tag {tag}')


@app.command(rich_help_panel='Project Commands')
def remove_tag(name: Annotated[str, typer.Argument(help='The name of a project to remove a tag from')],
               tag: Annotated[str, typer.Argument(help='The tog to remove')]):
    '''
    Remove tag TAG from project NAME
    '''
    typer.echo(f'Called remove-tag for {name} to remove tag {tag}')


@app.command(rich_help_panel='Project Commands')
def set_keywords(name: Annotated[str, typer.Argument(help='The name of a project to set keywords for')],
                 keys: Annotated[str, typer.Argument(help='The keywords for this project')]):
    '''
    Set keywords of project NAME to KEYS
    '''
    typer.echo(f'Called set-keywords for {name} to set keywords {keys}')


@app.command(rich_help_panel='Project Commands')
def get_keywords(name: Annotated[str, typer.Argument(help='The name of a project to get keywords for')]):
    '''
    Get keywords of project NAME
    '''
    typer.echo(f'Called get-keywords for {name}')


@app.command(rich_help_panel='Project Commands')
def add_keyword(name: Annotated[str, typer.Argument(help='The name of a project to add a keyworkd to')],
                key: Annotated[str, typer.Argument(help='The keyword to add')]):
    '''
    Add a keyword KEY to project NAME
    '''
    typer.echo(f'Called add-keyword for {name} to add keyword {key}')


@app.command(rich_help_panel='Project Commands')
def remove_keyword(name: Annotated[str, typer.Argument(help='The name of a project to remove a keyworkd from')],
                   key: Annotated[str, typer.Argument(help='The keyword to remove')]):
    '''
    Remove keyword KEY from project NAME
    '''
    typer.echo(f'Called remove-keyword for {name} to remove keyword {key}')


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f'Projects version: {version("projects")}')
        raise typer.Exit()


def first_run() -> None:
    '''
    Does the initial creation stuff when things like config files and directories don't exist
    This function should never make changes to existing files
    '''
    runtime_state['logger'].debug('Running first_run()')
    runtime_state['config_directory'].mkdir(mode=0o755, parents=True, exist_ok=True)
    if not runtime_state['config_directory'].joinpath('config.toml').exists():
        with open(runtime_state['config_directory'].joinpath('config.toml'), 'w') as f:
            f.write(default_config)
    runtime_state['config_directory'].joinpath('projects.state').touch(mode=0o644, exist_ok=True)


@app.callback()
def callback(config_directory: Annotated[Optional[Path], typer.Option(help='Directory to use for configuration files')] = Path('~/.config/projects/').expanduser(),
             version: Annotated[Optional[bool], typer.Option("--version", callback=version_callback, is_eager=True, help='Print the version of projects')] = None,
             debug: Annotated[Optional[bool], typer.Option("--debug", help='Enable debugging output')] = False,) -> None:
    if debug:
        runtime_state['logger'].setLevel(logging.DEBUG)

    runtime_state['config_directory'] = config_directory
    runtime_state['config'] = None
    first_run(runtime_state)

    # Try to read configuration file
    try:
        with open(f'{runtime_state["config_directory"]}/config.toml', 'rb') as inputFile:
            runtime_state['config'] = tomli.load(inputFile)
    except IOError as e:
        print('Configuration file not found, using sane defaults')

    # Load project state

if __name__ == '__main__':
    app()
