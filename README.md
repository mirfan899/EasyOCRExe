### Install packages.
Install packages required to build exe
```shell
pip install -r requirements.txt
```

### Test pyinstaller
Now try to compile the `easyocr.py` to see if it works on Windows.
```shell
pyinstaller --onefile easyocr.py 
```

It will create two directories in current folder. build and dist. `dist` contains the single exe file. 
You can test it on your system. Let me know if it works fine. I will make the complete package then.