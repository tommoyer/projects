#!/usr/bin/python3

import click


@click.group(invoke_without_command=True)
@click.option('-d', '--debug', help='Debug output', is_flag=True, show_default=True, default=False,)
@click.pass_context
def cli(ctx, debug):
    if ctx.invoked_subcommand is None:
        click.echo('Do whatever init is required and then run list?')
    else:
        click.echo(f'Doing the subcommand {ctx.invoked_subcommand}')


@cli.command()
@click.pass_context
def list(ctx):
    click.echo('Projects -> list was called')


@cli.command()
@click.pass_context
def new(ctx):
    click.echo('Projects -> new was called')