# outdoorsy-cli

## Install

This tool requires Python3.7+

To verify:
```
python3 --version
```

(![If needed, how to upgrade Python](https://phoenixnap.com/kb/upgrade-python))


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

