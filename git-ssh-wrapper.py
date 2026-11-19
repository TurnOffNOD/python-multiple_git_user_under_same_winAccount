"""Select an OpenSSH configuration using the effective Git user name.

Git supplies the SSH host and remote command as arguments, so the wrapper
forwards those arguments unchanged after adding the per-user -F option.
"""

import subprocess
import sys
from pathlib import Path


class WrapperError(Exception):
    """An error that prevents the wrapper from invoking SSH."""


def read_git_config(name, required=False):
    try:
        result = subprocess.run(
            ["git", "config", "--get", name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as exc:
        raise WrapperError("could not run git: {}".format(exc)) from exc

    if result.returncode == 1:
        value = None
    elif result.returncode != 0:
        detail = result.stderr.decode("utf-8", "replace").strip()
        if not detail:
            detail = "git config exited with status {}".format(result.returncode)
        raise WrapperError("could not read {}: {}".format(name, detail))
    else:
        value = result.stdout.decode("utf-8", "surrogateescape").rstrip("\r\n")

    if required and not value:
        raise WrapperError("git user.name is not configured")
    return value


def application_directory():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def build_ssh_command():
    user_name = read_git_config("user.name", required=True)
    read_git_config("user.email")

    config_path = application_directory() / ("config---" + user_name)
    if not config_path.is_file():
        raise WrapperError(
            "file not found error: SSH config file does not exist: {}".format(
                config_path
            )
        )

    return ["ssh", "-F", str(config_path)] + sys.argv[1:]


def main():
    try:
        command = build_ssh_command()
        result = subprocess.run(command, check=False)
    except WrapperError as exc:
        print("git-ssh-wrapper: {}".format(exc), file=sys.stderr)
        return 1
    except FileNotFoundError:
        print("git-ssh-wrapper: ssh executable not found", file=sys.stderr)
        return 127
    except OSError as exc:
        print("git-ssh-wrapper: could not run ssh: {}".format(exc), file=sys.stderr)
        return 126

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
