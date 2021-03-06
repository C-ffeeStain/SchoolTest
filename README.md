# School Test

Ever wanted to go back to school to relearn a bunch of random facts? Probably not, but here's a test that combines several different school subjects together to create a unique test every time! You'll end up googling the answers, because that's what I did for some of these questions.

## Adding Your Own Questions

To add your own questions, look in the `questions` folder. There you will see a list of files for each subject's questions. There may eventually be true/false questions. The line with the question in it must start with `Q: `, and the answer list line must start with `A: `. Also, the correct answer must be the first one in the list. Don't worry, the answer order will be randomized. Each answer must be seperated by two commas (`,,`).Here's an example:

```text
Q: Is this an example?
A: yes,,no,,idk,,i don't think so
```
## Development

To help with development, you'll need Git and Python 3.8 or later. Here's the list of commands you should run to get the program working. Make sure you're on Windows.

```bash
$ git clone https://github.com/C-ffeeStain/SchoolTest.git
$ cd SchoolTest
$ py -m venv venv
$ "venv/scripts/activate.bat"
$ py -m pip install -r requirements.txt
```
### Building the .exe file
To build the executable file for releases, you should run this command:
```pyinstaller --onefile --icon NONE main.py```
