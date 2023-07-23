#!/usr/bin/python3

import typer
import notes
import resources
import pprint

pp = pprint.PrettyPrinter()


app = typer.Typer()
app.add_typer(notes.app, name='notes', help='Manage notes for a project', rich_help_panel='Subcommands', callback=notes.project_callback)
app.add_typer(resources.app, name='resources', help='Manage resources for a project', rich_help_panel='Subcommands', callback=resources.project_callback)


state = {'project': None}


@app.callback()
def callback(project: str = None):
    if project:
        state['project'] = project


@app.command(rich_help_panel='Project Commands')
def new(name: str):
    '''
    Create a new project titled NAME
    '''
    typer.echo(f'Called new {name}')


@app.command(rich_help_panel='Project Commands')
def list():
    '''
    List existing projects
    '''
    typer.echo(f'Called list')


@app.command(rich_help_panel='Project Commands')
def archive(name: str):
    '''
    Archive project NAME
    '''
    typer.echo(f'Called archive {name}')


@app.command(rich_help_panel='Project Commands')
def delete(name: str):
    '''
    Delete project NAME
    '''
    typer.echo(f'Called delete {name}')


@app.command(rich_help_panel='Project Commands')
def grep(name: str, search: str):
    '''
    Search project NAME for SEARCH
    '''
    typer.echo(f'Called search {name} for {search}')


@app.command(rich_help_panel='Project Commands')
def set_status(name: str, status: str):
    '''
    Set status of project NAME to STATUS
    '''
    typer.echo(f'Called set-status for {name} to {status}')


@app.command(rich_help_panel='Project Commands')
def get_status(name: str):
    '''
    Get status of project NAME
    '''
    typer.echo(f'Called get-status for {name}')


@app.command(rich_help_panel='Project Commands')
def register(name: str):
    '''
    Register existing project NAME
    '''
    typer.echo(f'Called register for {name}')


@app.command(rich_help_panel='Project Commands')
def sync(name: str):
    '''
    Sync project NAME, ensuring metadata is in syync
    '''
    typer.echo(f'Called sync for {name}')


@app.command(rich_help_panel='Project Commands')
def set_tags(name: str, tags: str):
    '''
    Set tags of project NAME to TAGS
    '''
    typer.echo(f'Called set-tags for {name} to tags {tags}')


@app.command(rich_help_panel='Project Commands')
def get_tags(name: str):
    '''
    Get tags of project NAME
    '''
    typer.echo(f'Called get-tags for {name}')


@app.command(rich_help_panel='Project Commands')
def add_tag(name: str, tag: str):
    '''
    Add a tag TAG to project NAME
    '''
    typer.echo(f'Called add-tag for {name} to add tag {tag}')


@app.command(rich_help_panel='Project Commands')
def remove_tag(name: str, tag: str):
    '''
    Remove tag TAG from project NAME
    '''
    typer.echo(f'Called remove-tag for {name} to remove tag {tag}')


@app.command(rich_help_panel='Project Commands')
def set_keywords(name: str, keys: str):
    '''
    Set keywords of project NAME to KEYS
    '''
    typer.echo(f'Called set-keywords for {name} to set keywords {keys}')


@app.command(rich_help_panel='Project Commands')
def get_keywords(name: str):
    '''
    Get keywords of project NAME
    '''
    typer.echo(f'Called get-keywords for {name}')


@app.command(rich_help_panel='Project Commands')
def add_keyword(name: str, key: str):
    '''
    Add a keyword KEY to project NAME
    '''
    typer.echo(f'Called add-keyword for {name} to add keyword {key}')


@app.command(rich_help_panel='Project Commands')
def remove_keyword(name: str, key: str):
    '''
    Remove keyword KEY from project NAME
    '''
    typer.echo(f'Called remove-keyword for {name} to remove keyword {key}')


if __name__ == '__main__':
    app()
