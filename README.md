# AI-Powered Linux Terminal

An AI-powered Linux terminal that translates natural language prompts into executable Linux commands using **Ollama** and **CodeLlama**. This project allows you to interact with your Linux system using plain English, making it easier to perform tasks without memorizing complex commands.

---

## Features

- **Natural Language to Linux Commands**: Simply type what you want to do (e.g., "list all files in the current directory"), and the AI will generate the appropriate Linux command.
- **Fully Functional Terminal**: Supports commands like `cd`, `ls`, `touch`, `mkdir`, and more. The terminal maintains its state, allowing you to navigate directories seamlessly.
- **CodeLlama Integration**: Uses the **CodeLlama** model via **Ollama** to generate accurate and efficient Linux commands.
- **Interactive and User-Friendly**: Features a Linux-style prompt with colors for better readability and includes confirmation before executing commands.
- **Safe Execution**: Commands are displayed for confirmation before execution, preventing accidental execution of dangerous commands.

---

## Example Usage

Here’s how you can use the AI terminal:

```plaintext
user@host:~$ list all files in the current directory
Generated command: ls
Execute this command? (y/n): y
(output of the `ls` command)

user@host:~$ change to the Documents directory
Generated command: cd Documents
Execute this command? (y/n): y

user@host:~/Documents$ create a new file called example.txt
Generated command: touch example.txt
Execute this command? (y/n): y
(file created successfully)

user@host:~/Documents$ go back to the home directory
Generated command: cd ~
Execute this command? (y/n): y

user@host:~$ exit
Exiting AI Terminal. Goodbye!
