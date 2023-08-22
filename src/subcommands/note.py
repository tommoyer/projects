#!/usr/bin/python3

import typer


app = typer.Typer()


state = {'project': None}


@app.command()
def add(name: str):
    '''
    Create a new note named NAME in project PROJECT
    '''
    print(f'Called new note {name} for {state["project"]}')


@app.command()
def list():
    '''
    List existing notes under PROJECT
    '''
    print(f'Called notes list for {state["project"]}')


@app.command()
def delete(note: str):
    '''
    Delete existing note NOTE under PROJECT
    '''
    print(f'Called notes delete for {state["project"]} to delete {note}')


@app.command()
def archive(note: str):
    '''
    Archive existing note NOTE under PROJECT
    '''
    print(f'Called notes archive for {state["project"]} to archive {note}')


@app.command()
def edit(note: str):
    '''
    Edit existing note NOTE under PROJECT
    '''
    print(f'Called notes edit for {state["project"]} to edit {note}')


def project_callback(project: str):
    state['project'] = project


if __name__ == '__main__':
    app()
