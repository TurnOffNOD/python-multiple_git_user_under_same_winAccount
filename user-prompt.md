# git-ssh-wrapper implementation

create a python script, whose name is `git-ssh-wrapper.py`, and then use `pyinstaller` to pack it to `git-ssh-wrapper.exe`, software feature requirement:

## Feature request

- The script should get the effective git's `user.name` and `user.email` configuration in a git repo. The following text will use `<git_user_name>` as variable name of effective `user.name`, and `<git_user_email>` as variable name of effective `user.email`.
- When doing git's SSH related operations (including but not limit to git push, git pull, git fetch etc.) and the remote url is using SSH protocol, the script should get the remote url, whose format is `ssh://git@<gitHosting_Server>/<gitHosting_Username>/<git_repo_name>.git` or `git@<gitHosting_Server>/<gitHosting_Username>/<git_repo_name>.git`, the following text will use `<gitHosting_Server>` as variable name of git hosting server addr, `<gitHosting_Server>` following a digit represents different server address.
- In production environment, SSH private key file `<user-ssh-private-key>` and per-user's ssh config file `config---<git_user_name>` will be exist before scipt being called by git's `core.sshCommand`. `<user-ssh-private-key>` followed by digit means the same user's different private keys.
- SSH private file's filename is totally manual defined, and per-user's ssh config file have the format: literal string `config---` followed by variable value `<git_user_name>`, i.e. `config---<git_user_name>`.
- for each `<git_user_name>`, file `config---<git_user_name>` will have content like follows, in which variables' value should be used:

  ```sshconfig
  Host <gitHosting_Server1>
    IdentityFile ~/.ssh/<user-ssh-private-key1>

  Host <gitHosting_Server2>
    IdentityFile ~/.ssh/<user-ssh-private-key2>
  ```

- Value of `<git_user_name>` may contains spaces, make sure handle it.
- The script should use `<git_user_name>` to determine the config file `config---<git_user_name>` to use, and assemble the ssh command `ssh -F config---<git_user_name>`, and make sure `<gitHosting_Server>` can still be recognized by config file `config---<git_user_name>` and make successful match of `Host`. The ssh config file `config---<git_user_name>` will be at the same directory of generated `.py` or `.exe` file and script should use it.
- The script running output should be identical as common SSH command, so it can work compatible.

## The final result requirement

- Final generate file: `git-ssh-wrapper.py` and its `pyinstaller` packing result `git-ssh-wrapper.exe`
