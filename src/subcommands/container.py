#!/usr/bin/python3

# TODO; These files in the subcommands directory should just load the Typer app from the configured plugin for the project and return it

import typer


app = typer.Typer()


state = {'project': None}


@app.command()
def new():
    pass


@app.command()
def status():
    pass


@app.command()
def start():
    pass


@app.command()
def stop():
    pass


@app.command()
def delete():
    pass


@app.command()
def shell():
    pass


@app.command()
def list():
    pass


def project_callback(project: str):
    state['project'] = project


if __name__ == '__main__':
    app()
