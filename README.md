# The Flashcard Project

The Flashcard Project is a Windows application that simplifies making, managing, and studying learning flashcards on a desktop. The software is written in Python.


![The Flashcard Project Main Screen](https://github.com/jnwillits/The-Flashcard-Project/blob/master/images-reference/fp-screen_1280x640.png?raw=true)

## About the Software

This features a native Windows GUI interface so the frame is size-adjustable, making it easy to have other applications and study references displayed. This can be useful when studying a computer language so you can switch to a code editor or interpreter for testing and practice.

While other flashcard applications provide extended features, The Flashcard Project offers a simple system that allows content sharing and merging. The files can be shared for use by anyone with the software.

Cards can be categorized with tags and you can save your card decks.

![The Flashcard Project Main Screen](https://github.com/jnwillits/The-Flashcard-Project/blob/master/images-reference/fp-tags.png?raw=true)


## About the Author

Links and more about Jeffrey Willits are available at [jnwillits.com](https://jnwillits.com/).

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

Only one file is needed to use this application. Simply download the Windows executable (fp.exe) from [GitHub Releases](https://github.com/jnwillits/The-Flashcard-Project/releases) and run the program. You can get The Flashcard Project's learning flashcards for Python (fp-python.db) from [GitHub Releases](https://github.com/jnwillits/The-Flashcard-Project/releases) as well.  

As an alternative, you can compile the Python source code [fp.py](https://raw.githubusercontent.com/jnwillits/The-Flashcard-Project/master/fp.py) with dependencies defined in [requirement.txt](https://raw.githubusercontent.com/jnwillits/The-Flashcard-Project/master/requirements.txt).


## Using the Application

Basic instructions are available under the program’s Help menu.

You can edit, add, and delete cards while you are studying. If there is a card you do not want to see again, click the Archive button. The deck can be reset at any time to reactivate the status of archived cards. Otherwise, the deck will be automatically reset once all cards are viewed.

The Flashcard Project provides a way for multiple people to contribute when generating a card deck. To share a deck, the card data can be exported to a human-readable YAML file. The file can be shared and imported by someone else to add the cards to their deck. 

Use the application to help with learning for any subject. If you are an instructor, your students could be tasked with producing their own flashcards and submit them as card files. Their cards can then be consolidated into a single deck that is a useful learning asset for all of your students. 


## Contributing
It would be great to receive contributions to the code and documentation so pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

In addition to the software, The Flashcard Project is a curated deck of Python learning flashcards that were generated and are updated with the application. You are welome to contribute to this. The file is [fp-python.db](https://github.com/jnwillits/The-Flashcard-Project/blob/master/fp-python.db?raw=true) and is kept in The Flashcard Project repository.

To submit flashcard content for Python learning, use the application to export your cards as YAML files. If any of these cards should replace existing cards, you can make a note directly on the cards in uppercase. Any notes will be deleted when your cards are consolidated into the master database.

Most of the cards should include example code for answers. Often a line of code is all that is needed. Using a python CLI makes it easy to distinguish output from code at every step. Please follow the existing format and include tags to categorize the cards.
 

## License
[MIT](https://choosealicense.com/licenses/mit/)