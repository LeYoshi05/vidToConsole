---------------------------------------------------
Thank you for choosing to look at my small program!
---------------------------------------------------

---------------------------------------------------
Requirements and Execution:

Requirements:
    Python 3.7 or newer
    Windows 10 or newer, Linux not tested
    Basic Knowledge of the Command Line.


Install of Requirements:
    After having installed Python, open a new Command line (CMD / Terminal)
    Navigate to the directory the software downloaded is stored in and type in

    python -m pip install -r requirements.txt.
    
    If that fails, try replacing python with python3 or typing only the following:

    pip install -r requirements.txt.
    
    After that, all required librarys should be installed automatically

Execution of the program:
    First, copy the video you would like to view in the console to the directory in .mp4 format.

    Open a new Command line and navigate to the directory the program is stored in.

    If you are using Windows, type in
        python .\vidToText.py
    
    On Linux, it may be necessary to type either
        python ./ vidToText.py or python3 ./vidToText.py
    
    Assuming the program started correctly, you should now see the following prompt:

        Please enter the name of the video:
        -->
    
    Now, enter the name of the video you copied to the directory previously.
    For example, type: "--> vid.mp4".

    Now, press enter.

    After that, you are asked whether you want to disable colored output.
    Type y or Y if you want to disable color and n or N if you want to keep color enabled.

    Press enter again to confirm your selection.

    Lastly, the program asks you to press Enter to start the video. Follow said instruction and enjoy.

~LeYoshi05


If the video is not displayed correctly, try adjusting the value of the following variables in the file vidToText.py

lines = 60#Adjust these variables
chars = 60#to suit your needs.

lines refers to the vertical number of characters, while chars refers to the number of characters per line horizontally.