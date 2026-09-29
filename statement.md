# Project Statement

## Problem Statement

People often rely on memory, scattered notes or loose paper to keep track of the things they need to do. This leads to forgotten tasks, no clear view of what is finished and what is pending, and a cluttered way of managing daily work. A simple tool is needed that lets a user quickly record tasks, see their progress and remove tasks that are no longer needed, without the complexity of a large application.

## Solution

This project is a command line to do list application built in Python. It stores tasks in a list of dictionaries, where each task holds its text and a done status. A menu driven loop lets the user choose what to do until they decide to exit.

The program tackles the problem in the following way:

- Adding tasks: the user types a task and it is saved instantly to the list.
- Viewing tasks: every task is shown with a number and a marker that tells whether it is done or pending, giving a clear picture of progress.
- Marking tasks as done: the user picks a task number and its status is updated.
- Deleting tasks: the user picks a task number and it is removed from the list.
- Error handling: invalid menu options, out of range task numbers and non numeric input are all caught and the user is asked to try again, so the program does not crash.

The result is a lightweight, easy to use tool that helps users stay organised and shows core Python concepts such as lists, dictionaries, functions, loops, conditionals and exception handling.
