import click
from click import Context
from click.core import ParameterSource


@click.group('namer')
@click.option('--debug', help='Should I run on Debug?', is_flag=True)
@click.pass_context
def main(ctx: Context, **kwargs):
    """ A namer CLI """
    source = ctx.get_parameter_source('debug')
    if source != ParameterSource.DEFAULT:
        click.secho('parameter debug is not default')

    debug = kwargs.get('debug')
    if debug:
        click.secho('is Debug? True', color='green')


@main.command('full')
@click.option('--name', help='The user name', required=True, type=str)
@click.option('--lastName', help='The last Name', required=False, type=str)
def full_name(**kwargs):
    """ A CLI that gets name and last name and returns the full name"""
    firstname = kwargs.get('name')
    lastname = kwargs.get('lastname')

    click.secho(f'The full name is: {firstname} {lastname}', color='yellow')
