# gas-(and-gas-cost)-estimation-of-solidity-contracts
This repo contains a series of Python scripts for estimating gas (and gas cost) of Solidity contracts.

### Prerequisites

> Software
   * We recommend [Python 3](https://www.python.org/downloads/) which is needed to execute 'installer.py' and 'main.py'; Other versions of Python should work, however for the best compatibility Python 3 is highly recommended.
   * The program requires the [Solidity compiler](https://github.com/ethereum/solidity/releases) to be installed on the host system.

### Organisation

The 'database.py' script (Python 3) ensures the connection with the database used by the program.

The 'gas_station_service.py' script (Python 3) realises the communication with the ETH Gas Station service via requests.

The 'installer.py' script will install the necessary modules required to run the application.

The 'solc_compiler.py' script (Python 3) handles the communication between our Python scripts and the Solidity compiler.

The 'text_processing.py' script (Python 3) is tasked with processing information (different types of text) in order to output a well-formatted string.

The 'main.py' script (Python 3) initialises the interface through which the user can communicate with the program and utilises all of the aforementioned scripts.

## Setup

### Python

Go to the [Python downloads page](https://www.python.org/downloads/), download any 3.x.x Python version, open and install following the on-screen instructions. Make sure to choose the "Customize installation" option.

```diff
- IMPORTANT: When you reach the "Advanced Options" section of the installer, make sure to check the box titled "Add Python to environment variables."
```

### Solidity

Go to the [Solidity releases page](https://github.com/ethereum/solidity/releases) and download the latest version (found in the Assets dropdown menu) based on your operating system. On Windows, the procedure is as follows:
   * download the zip file
   * extract the contents of the zip file in a folder anywhere on your computer
   * right click on the Start button and click "Run", type in 'sysdm.cpl' and press enter. This should open the System Properties window.
   * go to the 'Advanced' tab and click the 'Environment Variables' button
   * in the 'System variables' window find the 'Path' variable and click "Edit"
   * in the newly opened window click "New" and fill in the absolute path to the folder in which you extracted the contents of the zip file mentioned earlier

### Installing the Necessary Modules

To install the modules required to run the program open a terminal (command prompt) in the folder containing the 'installer.py' script. On Windows, this can be easily achieved by typing 'cmd' in the address bar in Windows Explorer.

Run the following command in the terminal (command prompt):

```
py installer.py
```

### Contact

You can contact me at alexandru . mendela at info . uaic . ro.