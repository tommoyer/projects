import typer
from data.project import Project

from typing_extensions import Annotated

app = typer.Typer()


@app.command(rich_help_panel='Project Commands')
def new(name: Annotated[str, typer.Argument(help='The name of a project to create')]):
    '''
    Create a new project titled NAME
    '''
    new_project = Project(name)
    new_project.save()


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


if __name__ == '__main__':
    app()
