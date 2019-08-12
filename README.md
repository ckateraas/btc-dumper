# Find Bitcoin addresses with a positive balance

Simple utility to list all bitcoin addresses with a positive balance.

The approach is analyzes all current unspent transaction output (UTXO) sets and aggregates the outputs to same addresses together. It then writes the result to a CSV file or an SQLite database.

## Getting started

Install Docker and you're ready to go.

```sh
docker build -t btc-dumper .
docker run -v $(pwd):/build btc-dumper python main.py result.csv --database sqlite3.db
```

Or, if you do not want to install Docker, install the dependencies with `pip` on your host system manually:

```sh
pip install -r requirements.txt
```

### Chainstate database

You will need local copy of the BTC chainstate database. This can be created by [Bitcoin core](https://bitcoin.org/en/bitcoin-core/) after the client has been synced with the Bitcoin network.

To get an up to date collection of transactions, refresh it using `bitcoind`. Wait until the daemon has fetched all the latest blocks from the network, which you can check with `bitcoin-cli getblockchaininfo`. Then stop `bitcoind`, using `bitcoin-cli stop`, _before_ running this utility.

## Usage:

To write each address balance to `result.csv` you can run the snippet below:

```py
./main.py --outputFile result.csv
```

If you instead want to save the results to a SQLite database instead of a file, you can instead run this snippet:

```py
./main.py --database sqlite.db
```

### CLI flags

Use `./main.py -h` to print the options and flags available.

- `chainstate`: If you do not have a `chainstate` file in `$HOME/.bitcoin/chainstate`, then you can specify another path the `--chainstate` flag.
- `outputFile`: Path to file to write address balances to.
- `database`: Path to SQLite database to store address balances to.

This utility builds on very nice [bitcoin_tools](https://github.com/sr-gi/bitcoin_tools/) lib, which does the UTXO parsing.

## Acknowledgement

This repo is based on Graymauser's [btcposbal2csv](https://github.com/graymauser/btcposbal2csv). This repo is merely a refactor of that repo.

Another acknowledgement goes to [bitcoin_tools](https://github.com/sr-gi/bitcoin_tools), which is the basis for `utils.py`, which does _all_ the heavy lifting.

## Support

If you like this utility, please consider supporting and starring both `btcposbal2csv` and `bitcoin_tools`.

To support `bitcoin_tools` you can send BTC to [`1srgihPwqtNkY3MWDNu6sxgCFcmp5Ne8n`](https://github.com/sr-gi/bitcoin_tools/blob/master/FAQ.md#but-i-really-really-like-it).
