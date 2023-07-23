#!/usr/bin/python3

import typer


app = typer.Typer()


state = {'project': None}


@app.command()
def location():
    '''
    Print location of the project PROJECT's resource folder
    '''
    typer.echo(f'Called resources location for {state["project"]}')


@app.command()
def browse():
    '''
    Open a file browser for the project PROJECT's resources
    '''
    typer.echo(f'Called resources browse for {state["project"]}')


@app.command()
def terminal():
    '''
    Open a terminal for the project PROJECT's resources
    '''
    typer.echo(f'Called resources terminal for {state["project"]}')


def project_callback(project: str):
    state['project'] = project


if __name__ == '__main__':
    app()
