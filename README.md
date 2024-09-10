# IBM Beacon Trigger
The **IBM Beacon Trigger** program is designed to automatically enable or disable beacon with the use of IBM API and python

## Features
- Trigger actions (`enabled` or `disabled`) for beacon signals.
- Utilize the `subprocess` module to send commands to specified drivers.
- Supports SysLog logging for remote log management.
  
## Requirements
- Python 3.x
- [Docopt](https://github.com/docopt/docopt) - for command-line interface parsing

## Installation

To install the required dependencies, use the following command:

```bash
pip install docopt
