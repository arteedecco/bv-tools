#! /usr/bin/env python

import logging
import click
from datetime import datetime as dt
import hashlib
import binascii
import urllib


# configure logging
logging.basicConfig(level=logging.DEBUG)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--date', default=dt.now().strftime('%Y%m%d'),
              help=('override today\'s date using format "YYYYmmdd". '
                    'Default is today\'s date.'))
@click.option('--maxage', default=360,
              help=('override maxage of UAS in days. '
                    'Default is 360 days.'))
@click.option('--userid', default=None,
              help=('add userid if you have one. '
                    'Required if using Site Authentication. '
                    'Default is None.'))
@click.option('--emailaddress', default=None,
              help=('add a user email address. '
                    'Default is None.'))
@click.option('--slaved_data', default=None,
              help=('Send through any slaved data to be added to the '
                    'encoded UAS, such as IncentivizedReview=True. '
                    'Pass as a string of "&" sepearated name=value pairs.'))
@click.argument('encoding_key')
def uas(encoding_key, date, maxage, userid, emailaddress,
        slaved_data, *args, **kwargs):
    """Generate a valid UAS."""
    click.echo(('Parameters to be encoded:'
                '\n\tencoding_key: {0}'
                '\n\tdate: {1}'
                '\n\tmaxage: {2}'
                '\n\tuserid: {3}'
                '\n\temailaddress: {4}'
                '\n\tsalved_data: {5}').
               format(encoding_key, date, maxage, userid, emailaddress,
                      slaved_data))
    params = ('date={0}&maxage={1}'.
              format(date, maxage))
    if userid is not None:
        params = (params + '&userid={0}'.
                  format(str(userid)))
    if emailaddress is not None:
        params = (params + '&emailaddress={0}'.
                  format(urllib.quote(emailaddress)))
    if slaved_data is not None:
        params = (params + '&{0}'.
                  format(slaved_data))
    click.echo('unencoded param string: {0}'.format(params))
    click.echo('md5 of encodingKey + param: {0}'.
               format(hashlib.md5(encoding_key + params).hexdigest()))
    click.echo('hex string of params: {0}'.
               format(binascii.hexlify(params)))
    click.echo('{0}\nencoded UAS: {1}{2}\n{0}'.
               format(('-' * 80),
                      hashlib.md5(encoding_key + params).hexdigest(),
                      binascii.hexlify(params)))


if __name__ == "__main__":
    cli()
