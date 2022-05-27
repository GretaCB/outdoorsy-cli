# outdoorsy-cli

CLI module for importing Outdoor.sy customer data from a file (comma-separated or pipe-separated) and optionally sorting by either name or vehicle type.

```
usage: list_customers.py [-h] [--sort SORT] file

positional arguments:
  file         filepath to Customer data you would like to list

optional arguments:
  -h, --help   show this help message and exit
  --sort SORT  sort customers by name or vehicle_type (defaults to None)
```

## Usage Examples
```bash
outdoorsy-cli % python3 list_customers.py "tests/commas.txt" --sort vehicle_type
```

Output:
```
Import successful! Printing customer output...

[Customer(...), Customer(...)]
```

You can also use this CLI via prompts by runnng it wthout args:
```bash
outdoorsy-cli % python3 list_customers.py                                      
[?] Which file would you like to import and list?: tests/pipes.txt
[?] Would you like to sort the data in tests/pipes.txt?: name
   No thanks
 > name
   vehicle_type

Import successful! Printing customer output...

[Customer(...), Customer(...)]
```


## Install

This tool requires Python3.7+

To verify:
```
python3 --version
```

([If needed, how to upgrade Python](https://phoenixnap.com/kb/upgrade-python))


### Install Dependenciess
```
pip3 install -r requirements.txt
```

## Tests

To run tests:
```
python3 -m pytest tests/test_cli.py
```

### Troubleshooting
If after running the tests you see `ModuleNotFoundError: No module named 'inquirer'`, then run the following and retry the tests:
```
python3 -m pip install -r requirements.txt
```
This has to do with the python3 version you have and how it was installed.

