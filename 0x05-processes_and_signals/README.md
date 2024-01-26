# 0x05. Processes and Signals

## Description
This repository contains Bash scripts that focus on processes and signals in the Linux environment. Each script addresses specific tasks related to process management and signal handling.

## Project Structure
- **0-what-is-my-pid**: Displays the PID of the script itself.
- **1-list_your_processes**: Displays a list of currently running processes in a user-oriented format.
- **2-show_your_bash_pid**: Displays the PID of the Bash process using command output.
- **3-show_your_bash_pid_made_easy**: Displays the PID and process name of processes containing the word "bash."
- **4-to_infinity_and_beyond**: Displays "To infinity and beyond" indefinitely with a sleep 2 between each iteration.
- **5-dont_stop_me_now**: Stops the 4-to_infinity_and_beyond process.
- **6-stop_me_if_you_can**: Stops the 4-to_infinity_and_beyond process without using kill or killall.
- **7-highlander**: Displays "To infinity and beyond" with "I am invincible!!!" upon receiving a SIGTERM signal.
- **67-stop_me_if_you_can**: Kills the 7-highlander process.
- **8-beheaded_process**: Kills the 7-highlander process.

## Requirements
- All scripts are interpreted on Ubuntu 20.04 LTS.
- Scripts must pass Shellcheck (version 0.7.0) without any errors.
- The first line of all scripts should be `#!/usr/bin/env bash`.
- A README.md file at the root of the project folder is mandatory.

## How to Run
Each script can be executed by running `./script_name` in the terminal.

### Example
```bash
./0-what-is-my-pid

