### Python

Make sure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

To check if Python is installed, open a terminal (command prompt on Windows) and type:


* Check Python Installation: First, ensure that Python is installed on your system. You can do this by typing 

```bash
python --version or python3 --version
``` 

in your terminal. If Python is installed, it should print out the version number. If it's not installed, you'll need to install it.

* Check Python Path: Sometimes, the Python executable path is not added to the system's PATH environment variable. You'll need to add it manually. The location of the Python executable depends on your operating system and how you installed Python.

* Install pip: If Python is installed but pip is missing, you may need to install it separately. You can download get-pip.py from https://bootstrap.pypa.io/get-pip.py and run it using Python:

```bash
python get-pip.py
``` 

This will install pip for your Python installation.

Verify pip Installation: After installing pip, you can verify its installation by typing 

```bash 
pip --version
```
in your terminal. It should print out the version number of pip.

Restart Terminal: After making any changes, restart your terminal to ensure that the changes take effect.

Once pip is installed and working, you can proceed with installing FastAPI and Uvicorn using the command:

```bash 
pip install fastapi uvicorn
```