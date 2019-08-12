#! /usr/bin/env python

import os
import sqlite3
from utils import parse_ldb
from db_helper import initialize, get_database_file, fetch_addresses_from_database, add_address
from arguments_parser import get_arguments
from csv_helper import write_to_csv

def get_all_txs(arguments):
    return parse_ldb(
        fin_name=arguments.chainstate,
        version=arguments.bitcoin_version,
        types={0, 1}
    )

def in_memory(arguments):
    address_dict = dict()
    for address, amount, height in get_all_txs(arguments):
        if address in address_dict:
            address_dict[address][0] += amount
            address_dict[address][1] = height
        else:
            address_dict[address] = [amount, height]

    for key in address_dict.iterkeys():
        row = address_dict[key]
        yield key, row[0], row[1]


def with_sqlite(arguments):
    database_file = get_database_file(arguments)

    with sqlite3.connect(database_file) as database:
        cursor = initialize(database)

        for address, amount, height in get_all_txs(arguments):
                    add_address(address, amount, height, cursor)
                    database.commit()

        fetch_addresses_from_database(cursor, arguments)

        for result in cursor:
            yield result[0], result[1], result[2]

        database.commit()
        cursor.close()

if __name__ == '__main__':
    args = get_arguments()

    print('Reading BTC chainstate from [' + args.chainstate + ']')

    if args.database:
        print('Storing transactions in SQLite database [' + args.database + ']')
        address_iterator = with_sqlite(args)
    else:
        print('Running everything in-memory')
        address_iterator = in_memory(args)

    if args.outputFile:
        print('Saving output to [' + args.outputFile + ']')
        write_to_csv(address_iterator, args.outputFile)
    else:
        print('Not yet implemented printing to stdout')
