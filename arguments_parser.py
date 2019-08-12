import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Process UTXO set from chainstate and return unspent output per'
                                                 ' address for P2PKH and P2SH addresses')
    parser.add_argument(
        '--chainstate',
        metavar='<chainstate-file>',
        default='/root/.bitcoin/chainstate',
        type=str,
        help='Path to Bitcoin chainstate directory to use'
    )
    parser.add_argument(
        '--outputFile',
        metavar='<file>',
        type=str,
        default=None,
        help='Write address to file as CSV'
    )
    parser.add_argument(
        '--bitcoin-version',
        type=float,
        default=0.15,
        help='Version of Bitcoin node. Acceptable values 0.08 - 0.15 (Default 0.15 should be OK)'
    )
    parser.add_argument(
        '--database',
        metavar='<database-file>',
        type=str,
        default=None,
        help='Path to SQLite database file to use'
    )
    return parser.parse_args()
