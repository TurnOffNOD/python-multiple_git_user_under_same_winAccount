# Project Overview

This project is a git-ssh-wrapper, which will provide ability that multiple git users can doing git pull/push and other git-ssh related operations to the same git-hosting service with their own ssh-keys under the same windows accounts.

## Repository Contents

- `.git/`: Git repository metadata.
- `AGENTS.md`: this project-status and agent-guidance document.
- `user-prompt.md`: user prompt input to LLM.
- Other unlist files or directories here: code and development related files, will be defined afterwards.

## Configuration and Technology Stack

- Programming language: `Python 3.15`.
- Target python version: mainly `Python 3.15`, whose compatilility is strictly required, with `pre-Python3.10` compatibility if it is possible.
- After python source code (`.py`) is generated, check the compatiblity to make sure it can use `pyinstaller` to be packed to 1 standalone `.exe` file, and can run at other computer that has no `python` installed.
- After python source code (`.py`) generation and pyinstaller packing, the `.exe` file's usage is: config the git's `core.sshCommand` pointing to this `.exe` command, globally
- After python source code (`.py`) generated and pyinstaller packed to `.exe`, when running it, no Internet connection is allowed, the source code must be able to run without Internet access from the first time. (The git hosting is in LAN network)
- 3rd-party library is allowed, 3rd-party installation is allowed to make Internet connections, but the final result is also shall be packed into the 1 standalone `.exe` file, and can run wihout Internet access. (The git hosting is in LAN network)

## Build and Run Commands

- The python source code `.py` file shall be saved.
- Use `pyinstaller` to pack the `.py` to `.exe` file. The `pyinstaller`'s commandline parameter should be decided by AI model.
- After each code generation, add the generated code `git-ssh-wrapper.py`, the prompt file `user-prompt.md`, and `AGENTS.md` if it is modified, to git staged, then doing a `git commit` to the branch `develop-AIgenerated`, auto-generated a commit message.

## Code Organization and Runtime Architecture

### Code Organization

- Repository Contents are not list here.
- `git-ssh-wrapper.py`: generated python source code, one of project target.
- `git-ssh-wrapper.exe`: pyinstaller packed from generated python source code, the other project target.
- `private_id-example`: example ssh private key, it shall be provided in advance and it is not generated. This file itself should not be used in production environment. This filename will be full manually named in production environment.
- `config-example.user.name`: example SSH config for `example user.name`, it shall be provided in advance and it is not AI-model generated. After code generation, report a `file not found error` if this file doesn't exist when running the code. This file itself should not be used in production environment. The filename will follow a file name regularation.

### Runtime Architecture

- When developing, generated `.py` source code and packed `.exe` will be at working space, and the example private key and example SSH config is at the same directory, as above defined.
- When in production environment, the packed `.exe` file will be copied to production envrionment, which is directory `%USERPROFILE%\.ssh` of another windows intallation. And production ssh private id file (for example, `user1-gitHost1-productionEnvName-ssh-private-id`, `user2-gitHost1-productionEvnName-ssh-private-id`, `user1-gitHost2-productionEnvName-ssh-private-id` etc) and production SSH config file (for example, `config-user_name1`, `config-user_name2`) is already in the same directory before `.exe` running in production.
