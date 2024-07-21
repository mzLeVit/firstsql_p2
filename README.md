# CLI Database CRUD Operations

This project provides a command-line interface (CLI) for performing CRUD (Create, Read, Update, Delete) operations on a database using SQLAlchemy. The CLI allows you to manage records for various models, including `Teacher`, `Student`, `Group`, `Subject`, and `Grade`.

## Requirements

- Python 3.x
- SQLAlchemy
- SQLite (or any other SQLAlchemy-supported database)

## Installation

1. **Clone the repository** (if applicable):

   ```bash
   git clone https://github.com/mzLeVit/firstsql_p2
   cd your-repo
2. Install dependencies:
If you haven't already, you can install SQLAlchemy using pip:
pip install sqlalchemy

3.Set up your database:
Ensure that you have a SQLite database file or adjust the DATABASE_URL in the seed2.py script to point to your database.

      Usage
The CLI tool can be used to perform CRUD operations on different models. The script is called seed2.py and requires two main arguments: --action and --model.

  General Syntax
python seed2.py --action ACTION --model MODEL [--id ID] [--name NAME]
 
      Arguments
--action or -a: The action to perform. Can be one of the following:
  create: To create a new record.
  list: To list all records.
  update: To update an existing record.
  remove: To delete a record.
--model or -m: The model to perform the action on. Can be one of the following:
  Teacher
  Student
  Group
  Subject
  Grade
--id: The ID of the record to update or remove (required for update and remove actions).
--name: The name for the record (required for create and update actions for Teacher model).
        
        Examples
1. Create a new teacher:
python seed2.py --action create --model Teacher --name 'Boris Johnson'
2. List all teachers:
python seed2.py --action list --model Teacher
3.Update a teacher's information:
python seed2.py --action update --model Teacher --id 3 --name 'Andry Bezos'
4. Remove a teacher:
python seed2.py --action remove --model Teacher --id 3


        Adding Other Models
To add functionality for other models like Student, Group, Subject, or Grade, you will need to implement similar functions as shown for Teacher. Update the main function in seed2.py to handle actions for these models.
