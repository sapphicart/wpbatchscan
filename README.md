# Scan multiple urls with `wpscan` at once

[`wpscan`](https://github.com/wpscanteam/wpscan) is a powerful WordPress vulnerability scanner. However, `wpscan` can only work with one url at a time. `wpbatchscan` is a Python script to scan multiple URLs with `wpscan` at once.

## Usage:

1. Clone the repo.
```bash
git clone https://github.com/sapphicart/wpbatchscan.git
cd wpbatchscan
```

2. Install dependencies.
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API Token. Get a free API Token at [wpscan.com](https://wpscan.com/).
```
API_TOKEN=<your token here>
```

4. Run the script.
```bash
python wpbatchscan.py -u url_list
```

## Options

1. Add the URLs to scan in the given `url_list` file or create a new file:
```bash
python wpbatchscan.py --url /path/to/file
```

2. Modify the enumeration options:
```bash
python wpbatchscan.py --url url_list --enum vp
```

3. Change the output file format:
```bash
python wpbatchscan.py --url url_list --format cli-no-color
```

4. Output the scan results to `stdout` instead of a file:
```bash
python wpbatchscan.py --url url_list --cli
```

## Contributions

We love contributions! Feel free to [fork](https://github.com/sapphicart/wpbatchscan/fork) the repo and create a pull request.
