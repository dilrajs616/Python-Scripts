This script was made for a job on upwork. It scrapes the data from Kasikorn Bank website and sends an alert everytime a new transaction is made in user's account.
To run this script you have to follow the following steps:
1. Clone this repository on your local device.
2. Update your chrome and then download compatible chromedriver on your machine.
3. Enter the chromedriver.exe path in the .env file as "DRIVER_PATH".
4. Now Enter the Kasikorn login page path in .env file as "AUTH_LINK", transaction history link as "MAKER_LINK", your username as "USERNAME" and password as "PASSWORD".
5. Finally make an virtual environment to install the requirements. To install all requirements simply run "pip install -r requirements.txt"
6. And all set.
