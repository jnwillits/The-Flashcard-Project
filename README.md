# The Flashcard Project

The Flashcard Project is a Windows application that simplifies making, managing, and studying learning flashcards on a desktop. The software is written in Python.


![The Flashcard Project Main Screen](https://github.com/jnwillits/The-Flashcard-Project/blob/master/images-reference/fp-screen_1280x640.png?raw=true)

## About the Software

The native Windows interface and size-adjustable frame makes it easy to have other applications and study references displayed. This can be useful when studying a computer language so you can switch to a code editor or interpreter for testing and practice.

While other flashcard applications provide extended features, this offers a simple system that allows content sharing and merging. Cards can be categorized with tags and you can save your card decks. The files can be shared for use by anyone with the software.

## About the Author

Links and a bit more about Jeffrey Willits is available at [jnwillits.com](https://jnwillits.com/).

## With The Flashcard Project you can…

•	Edit cards on the same screen as they are displayed.

•	Save card decks to a database file.

•	Export files in machine and human-readable formats.

•	Merge card decks.

•	Tag cards to allow filtering.

•	Delete unwanted tags simultaneously from all cards.

•	Display cards randomly or sequentially.

•	Flag cards as archived so they will not be shown.

•	Reset the deck so all archived and excluded cards are shown.


## Installation

Only one file is needed to use this application. Simply download the Windows executable application file [fp.exe](https://github.com/jnwillits/The-Flashcard-Project/blob/master/fp.exe?raw=true) and run the program.

As an alternative, you can compile the Python source code [fp.py](https://raw.githubusercontent.com/jnwillits/The-Flashcard-Project/master/fp.py) with dependencies defined in [requirement.txt](https://raw.githubusercontent.com/jnwillits/The-Flashcard-Project/master/requirements.txt).


## Using the Application

Basic usage instructions are under the program’s Help menu.

You can edit, add, and delete cards while you are studying. If there is a card you do not want to see again, click the “Archive” button. The deck can be reset at any time to return the status of all archived card to active. Otherwise, the deck will be automatically reset once all cards are viewed.

The Flashcard Project provides a way for multiple people to contribute when generating a card deck. To share a card deck, the card data can be exported to a human-readable YAML file. These files can be shared and then imported by someone else. 

Use the application to help with learning for any subject. If you are an instructor your students could be tasked with producing their own flashcards and submit them as card files. Their cards can be easily consolidated into a single card deck file that is a useful learning asset for all of students. 


## Contributing
It would be great to receive contributions to the code and documentation so pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

In addition to the software, The Flashcard Project is a curated deck of Python learning flashcards that are generated with the application. You are welome to contribute to this. The file is fp-python.db and is kept in The Flashcard Project repository.

To submit flashcard content for Python learning, use the application to export your cards as YAML files. If any of these cards should replace existing cards, you can make a note directly on the card in all uppercase characters. Any notes will be deleted when your cards are consolidated into the master database.

Most of the cards should include example code for answers. Often, a line of example of code is all that is needed. Using a python CLI makes it easy to distinguish output from code at every step. Please follow the existing format and include tags to categorize the cards.
 

## License
[MIT](https://choosealicense.com/licenses/mit/)