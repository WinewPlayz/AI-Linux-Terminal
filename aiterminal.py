import subprocess
import requests
import os
import readline  # For better input handling (history, editing, etc.)

# Ollama configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Default Ollama API endpoint
MODEL = "codellama"  # Using CodeLlama

# Terminal prompt customization
USER = os.getenv("USER")  # Get the current Linux username
HOSTNAME = os.getenv("HOSTNAME")  # Get the hostname

def generate_command(prompt: str) -> str:
    """
    Generates a Linux command from a natural language prompt using Ollama and CodeLlama.
    """
    system_prompt = """You are a helpful AI terminal assistant that converts user requests into Linux bash commands. 
    Return ONLY the valid Linux bash command without any explanation. 
    If the request can't be turned into a command, return 'ERROR'.
    Examples:
    - User: list all files in the current directory
      Assistant: ls
    - User: change to the Documents directory
      Assistant: cd Documents
    - User: create a new file called example.txt
      Assistant: touch example.txt
    - User: show disk usage
      Assistant: df -h
    - User: find all .txt files in the current directory
      Assistant: find . -name "*.txt"
    """

    # Prepare the payload for Ollama API
    payload = {
        "model": MODEL,
        "prompt": f"{system_prompt}\n\nUser: {prompt}\nAssistant:",
        "stream": False
    }

    try:
        # Send request to Ollama API
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes

        # Extract the generated command
        generated_text = response.json().get("response", "").strip()

        # Remove Markdown-style backticks if present
        if generated_text.startswith("```") and generated_text.endswith("```"):
            generated_text = generated_text[3:-3].strip()

        # Validate the generated command
        if not generated_text or generated_text.lower() in ["error", "bash", "sh", "zsh"]:
            return "ERROR"

        return generated_text
    except requests.exceptions.HTTPError as e:
        print(f"\033[1;31mHTTP Error: {e}\033[0m")  # Red error message
        print(f"Response: {response.text}")  # Print the server's response for debugging
    except Exception as e:
        print(f"\033[1;31mError calling Ollama API: {e}\033[0m")  # Red error message
    return "ERROR"

def execute_command(command: str, current_dir: str) -> str:
    """
    Executes a Linux command and returns the new current directory.
    """
    try:
        # Handle 'cd' command separately
        if command.startswith("cd "):
            new_dir = command[3:].strip()
            try:
                os.chdir(new_dir)
                return os.getcwd()  # Return the new current directory
            except Exception as e:
                print(f"\033[1;31mError: {e}\033[0m")
                return current_dir  # Return the original directory if 'cd' fails
        else:
            # Execute other commands
            result = subprocess.run(
                command,
                shell=True,
                text=True,
                capture_output=True,
                cwd=current_dir,  # Execute in the current directory
                check=False
            )

            # Print command output
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(f"\033[1;31mError: {result.stderr}\033[0m")

            return current_dir  # Return the same directory (no change)
    except Exception as e:
        print(f"\033[1;31mError: {str(e)}\033[0m")
        return current_dir  # Return the original directory on error

def main():
    # Start in the user's home directory
    current_dir = os.path.expanduser("~")  # Get the user's home directory
    os.chdir(current_dir)  # Set the current working directory

    print("\033[1;33mAI Terminal v0.1 (Powered by Ollama and CodeLlama)\033[0m")
    print("Type 'exit' or 'quit' to exit.\n")

    while True:
        try:
            # Display the Linux-style prompt with the current directory
            prompt = f"\033[1;32m{USER}@{HOSTNAME}\033[0m:\033[1;34m{os.path.relpath(current_dir, os.path.expanduser('~'))}\033[0m$ "
            user_input = input(prompt).strip()

            # Exit condition
            if user_input.lower() in ['exit', 'quit']:
                print("\033[1;33mExiting AI Terminal. Goodbye!\033[0m")
                break

            # Generate command using Ollama and CodeLlama
            command = generate_command(user_input)

            if not command or command == 'ERROR':
                print("\033[1;31mError: Could not generate a valid command.\033[0m")
                continue

            print(f"\033[1;34mGenerated command:\033[0m \033[1;33m{command}\033[0m")  # Blue label, yellow command
            confirmation = input("\033[1;34mExecute this command? (y/n):\033[0m ").lower()

            if confirmation == 'y':
                # Execute the command and update the current directory
                current_dir = execute_command(command, current_dir)
            else:
                print("\033[1;33mCommand execution canceled.\033[0m")  # Yellow message

        except KeyboardInterrupt:
            print("\n\033[1;33mUse 'exit' or 'quit' to exit the terminal.\033[0m")  # Handle Ctrl+C gracefully
        except Exception as e:
            print(f"\033[1;31mError: {str(e)}\033[0m")  # Red error message

if __name__ == "__main__":
    main()