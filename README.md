# AI-Powered Linux Terminal

An AI-powered Linux terminal that translates natural language prompts into executable Linux commands using Ollama and CodeLlama. This project allows you to interact with your Linux system using plain English, making it easier to perform tasks without memorizing complex commands.

## Features

- **Natural Language to Linux Commands**: Simply type what you want to do (e.g., "list all files in the current directory"), and the AI will generate the appropriate Linux command.
- **Fully Functional Terminal**: Supports commands like `cd`, `ls`, `touch`, `mkdir`, and more. The terminal maintains its state, allowing you to navigate directories seamlessly.
- **CodeLlama Integration**: Uses the CodeLlama model via Ollama to generate accurate and efficient Linux commands.
- **Interactive and User-Friendly**: Features a Linux-style prompt with colors for better readability and includes confirmation before executing commands.
- **Safe Execution**: Commands are displayed for confirmation before execution, preventing accidental execution of dangerous commands.

## Example Usage

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
```

## Installation

#### 1. Auto Install (Recommended)

This method automates the installation process using a script.

```bash
git clone https://github.com/WinewPlayz/ai-linux-terminal.git
cd ai-linux-terminal
chmod +x autoinstallreq.sh
./autoinstallreq.sh
```

#### 2. Manual Install

If you prefer to install the dependencies manually, follow these steps:

##### Prerequisites

- **Ollama**: Install Ollama from [https://ollama.ai/](https://ollama.ai/).
- **CodeLlama Model**: Pull the CodeLlama model using Ollama:

  ```bash
  ollama pull codellama
  ```

- **Python 3.7+**: Ensure Python 3.7 or later is installed on your system.

##### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/WinewPlayz/ai-linux-terminal.git
   cd ai-linux-terminal
   ```

2. Install the required Python packages:

   ```bash
   pip install requests
   ```

3. Run the AI terminal:

   ```bash
   python3 ai_terminal.py
   ```

## How It Works

1. **Natural Language Input**: You type a natural language prompt (e.g., "list all files in the current directory").
2. **AI Command Generation**: The AI (CodeLlama via Ollama) generates the corresponding Linux command (e.g., `ls`).
3. **Command Execution**: The terminal displays the generated command and asks for confirmation before executing it.
4. **Stateful Terminal**: The terminal maintains the current working directory, allowing you to navigate and execute commands seamlessly.

## Customization

- **System Prompt**: Modify the `system_prompt` in the script to tailor the AI's responses to your needs.
- **Model**: Switch to other models supported by Ollama (e.g., `mistral`, `llama2`) by changing the `MODEL` variable in the script.

## Safety

- Always review the generated command before executing it, as the AI might generate potentially dangerous commands (e.g., `rm -rf`).
- The terminal includes a confirmation step to prevent accidental execution of commands.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Ollama**: For providing an easy-to-use interface to run large language models locally.
- **CodeLlama**: For powering the command generation with its code-specific capabilities.

Enjoy using your AI-powered Linux terminal! 😊

