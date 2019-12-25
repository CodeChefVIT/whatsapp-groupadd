# Whatsapp-groupadd

Whatsapp-groupadd is a Python code which helps it users to add people to a specific whatsapp group without directly saving their numbers.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install selenium
pip install selenium-requests
```

Use the link [geckodriver](https://github.com/mozilla/geckodriver/releases) to install the webdriver.

## Usage

Clone the repo and in the edit the people.csv in the Samples folder as your need

Import the csv in to your [google account](https://contacts.google.com/)

Now come to the python code

```python
IN LINE 17
driver.find_element_by_xpath('//*[@title="Name of the group you want to add People"]').click()# name of the group

```
Now run the code
Once you get this screen.

![alt text](https://qphs.fs.quoracdn.net/main-qimg-0b74cd2346cee5cb4551a763d3202abe)

Open Whatsapp in your device and scan the QR code displayed on the screen.

Wait for the code to run until you see this screen

![alt text](https://imgur.com/QtZuyKh)

Click on Add Participant

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

