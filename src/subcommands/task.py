#!/usr/bin/python3

import typer


app = typer.Typer()


state = {'project': None}


@app.command()
def list():
    pass


@app.command()
def new():
    pass


@app.command()
def mark():
    pass


@app.command()
def delete():
    pass


def project_callback(project: str):
    state['project'] = project


if __name__ == '__main__':
    app()
