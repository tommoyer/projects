#!/usr/bin/python3

import typer


app = typer.Typer()


state = {'project': None}


@app.command()
def start():
    pass


@app.command()
def stop():
    pass


@app.command()
def cancel():
    pass


@app.command()
def edit():
    pass


@app.command()
def status():
    pass


@app.command()
def log():
    pass


@app.command()
def timecards():
    pass


def project_callback(project: str):
    state['project'] = project


if __name__ == '__main__':
    app()
