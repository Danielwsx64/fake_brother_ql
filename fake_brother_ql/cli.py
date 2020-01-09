#!/usr/bin/env python

# Python standard library
import sys

# external dependencies
import click

@click.group()
@click.option('-b', '--backend', envvar='BROTHER_QL_BACKEND')
@click.option('-m', '--model', envvar='BROTHER_QL_MODEL')
@click.option('-p', '--printer', metavar='PRINTER_IDENTIFIER', envvar='BROTHER_QL_PRINTER', help='some printer helper')
@click.option('--debug', is_flag=True)
@click.version_option()
@click.pass_context
def cli(ctx, *args, **kwargs):
    """ Command line interface for the brother_ql Python package. """

    backend = kwargs.get('backend', None)
    model = kwargs.get('model', None)
    printer = kwargs.get('printer', None)

    ctx.meta['MODEL'] = model
    ctx.meta['BACKEND'] = backend
    ctx.meta['PRINTER'] = printer

@cli.command()
@click.pass_context
def discover(ctx):
    """ find connected label printers """

    if(ctx.meta['BACKEND'] != 'NOPRINTERS'):
        print('INFO:brother_ql.output_helpers:  Found a label printer: file:///dev/usb/lp0 (model: unknown)')
        print('file:///dev/usb/lp0')

@cli.command('status')
@click.pass_context
def status_cmd(ctx):
    """ return printer status """

    if(ctx.meta['PRINTER'] == '///dev/usb/error_connect'):
        print('Error: could not connect to printer ' + printer_name)
        sys.exit(2)
    elif(ctx.meta['PRINTER'] == '///dev/usb/error_status'):
        print('Error: could not fetch printer status')
        sys.exit(2)
    else:
        status = {
                "errors": [],
                "media_length": 0,
                "media_type": "Continuous length tape",
                "media_width": 62,
                "phase_type": "Waiting to receive",
                "status_type": "Phase change"
                }

        print(status)

@cli.command('print', short_help='Print a label')
@click.argument('images', nargs=-1, type=click.File('rb'), metavar='IMAGE [IMAGE] ...')
@click.option('-l', '--label', envvar='BROTHER_QL_LABEL', help='The label (size, type - die-cut or endless). Run `brother_ql info labels` for a full list including ideal pixel dimensions.')
@click.option('-r', '--rotate', type=click.Choice(('auto', '0', '90', '180', '270')), default='auto', help='Rotate the image (counterclock-wise) by this amount of degrees.')
@click.option('-t', '--threshold', type=float, default=70.0, help='The threshold value (in percent) to discriminate between black and white pixels.')
@click.option('-d', '--dither', is_flag=True, help='Enable dithering when converting the image to b/w. If set, --threshold is meaningless.')
@click.option('-c', '--compress', is_flag=True, help='Enable compression (if available with the model). Label creation can take slightly longer but the resulting instruction size is normally considerably smaller.')
@click.option('--red', is_flag=True, help='Create a label to be printed on black/red/white tape (only with QL-8xx series on DK-22251 labels). You must use this option when printing on black/red tape, even when not printing red.')
@click.option('--600dpi', 'dpi_600', is_flag=True, help='Print with 600x300 dpi available on some models. Provide your image as 600x600 dpi; perpendicular to the feeding the image will be resized to 300dpi.')
@click.option('--lq', is_flag=True, help='Print with low quality (faster). Default is high quality.')
@click.option('--no-cut', is_flag=True, help="Don't cut the tape after printing the label.")
@click.option('--rasp', is_flag=True, help="Use raspberry printer method")
@click.pass_context
def print_cmd(ctx, *args, **kwargs):
    """ Print a label of the provided IMAGE. """
    if(not kwargs['rasp']):
        print('fake just implemented for raspberry')
        sys.exit(2)
    elif(ctx.meta['PRINTER'] == '///dev/usb/error_connect'):
        print('Error: could not connect to printer ' + printer_name)
        sys.exit(2)
    elif(ctx.meta['PRINTER'] == '///dev/usb/error_status'):
        print('Error: could not fetch printer status')
        sys.exit(2)

if __name__ == '__main__':
    cli()
