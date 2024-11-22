from argparse import ArgumentParser
from dataclasses import dataclass
import logging
import os
import re
import subprocess
import sys


def module_name_pep8_compliance(module_name: str) -> None:
    """Validate that the plugin module name is PEP8 compliant."""
    if not re.match(r"^[a-z][_a-z0-9]+$", module_name):
        link = "https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
        logger.error("Module name should be pep-8 compliant.")
        logger.error(f"  More info: {link}")
        sys.exit(1)


def pypi_package_name_compliance(plugin_name: str) -> None:
    """Check there are no underscores in the plugin name"""
    if re.search(r"_", plugin_name):
        logger.error("PyPI.org and pip discourage package names with underscores.")
        sys.exit(1)


def initialize_new_repository(
        install_precommit: bool = False,
        plugin_name: str = "redsun-foobar",
        github_repository_url: str = "provide later",
        github_username_or_organization: str ="githubuser",
    ) -> str:
    """Initialize new plugin repository with git, and optionally pre-commit."""

    msg = ""

    # Configure git line ending settings
    # https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration
    if os.name == 'nt':  # if on Windows, configure git line ending characters
        subprocess.run(["git", "config", "--global", "core.autocrlf", "true"])
    else:  # for Linux and Mac
        subprocess.run(["git", "config", "--global", "core.autocrlf", "input"])

    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
    except Exception:
        logger.error("Error in git initialization.")

    if install_precommit is True:
        # try to install and update pre-commit
        try:
            print("install pre-commit ...")
            subprocess.run(["python", "-m", "pip", "install", "pre-commit"], stdout=subprocess.DEVNULL)
            print("updating pre-commit...")
            subprocess.run(["pre-commit", "autoupdate"], stdout=subprocess.DEVNULL)
            subprocess.run(["git", "add", "."])
            subprocess.run(["pre-commit", "run", "black", "-a"], capture_output=True)
        except Exception:
            logger.error("Error pip installing then running pre-commit.")

    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        logger.error("Error creating initial git commit.")
        msg += f"""
Your plugin template is ready!  Next steps:
1. `cd` into your new directory and initialize a git repo
(this is also important for version control!)
    cd {plugin_name}
    git init -b main
    git add .
    git commit -m 'initial commit'
    # you probably want to install your new package into your environment
    pip install -e .
"""
    else:
        msg +=f"""
Your plugin template is ready!  Next steps:
1. `cd` into your new directory
    cd {plugin_name}
    # you probably want to install your new package into your env
    pip install -e .
"""
    # Ensure full reqd/write/execute permissions for .git files
    if os.name == 'nt':  # if on Windows OS
        # Avoid permission denied errors on Github Actions CI
        subprocess.run(["attrib", "-h", "rr", ".git", "/s", "/d"])

    if install_precommit is True:
        # try to install and update pre-commit
        # installing after commit to avoid problem with comments in setup.cfg.
        try:
            print("install pre-commit hook...")
            subprocess.run(["pre-commit", "install"])
        except Exception:
            logger.error("Error at pre-commit install, skipping pre-commit")

    if github_repository_url != 'provide later':
        msg += f"""
    2. Create a github repository with the name '{plugin_name}':
    https://github.com/{github_username_or_organization}/{plugin_name}.git
    3. Add your newly created github repo as a remote and push:
        git remote add origin https://github.com/{github_username_or_organization}/{plugin_name}.git
        git push -u origin main
    4. The following default URLs have been added to `setup.cfg`:
        Bug Tracker = https://github.com/{github_username_or_organization}/{plugin_name}/issues
        Documentation = https://github.com/{github_username_or_organization}/{plugin_name}#README.md
        Source Code = https://github.com/{github_username_or_organization}/{plugin_name}
        User Support = https://github.com/{github_username_or_organization}/{plugin_name}/issues
        These URLs will be displayed on your plugin's napari hub page.
        You may wish to change these before publishing your plugin!"""
    else:
        msg += """
    2. Create a github repository for your plugin:
    https://github.com/new
    3. Add your newly created github repo as a remote and push:
        git remote add origin https://github.com/your-repo-username/your-repo-name.git
        git push -u origin main
    Don't forget to add this url to setup.cfg!
        [metadata]
        url = https://github.com/your-repo-username/your-repo-name.git
    4. Consider adding additional links for documentation and user support to setup.cfg
    using the project_urls key e.g.
        [metadata]
        project_urls =
            Bug Tracker = https://github.com/your-repo-username/your-repo-name/issues
            Documentation = https://github.com/your-repo-username/your-repo-name#README.md
            Source Code = https://github.com/your-repo-username/your-repo-name
            User Support = https://github.com/your-repo-username/your-repo-name/issues"""

    msg += """
    5. Read the README for more info: https://github.com/jacopoabramo/redsun-plugin-template
    """
    return msg

@dataclass
class Arguments:
    plugin_name: str
    module_name: str
    project_directory: str
    install_precommit: bool
    github_repository_url: str
    github_username_or_organization: str


if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("pre_gen_project")
    parser = ArgumentParser()
    parser.add_argument("--plugin_name",
                        dest="plugin_name",
                        help="The name of your plugin")
    parser.add_argument("--module_name",
                        dest="module_name",
                        help="Plugin module name")
    parser.add_argument("--project_directory",
                        dest="project_directory",
                        help="Project directory")
    parser.add_argument("--install_precommit",
                        dest="install_precommit",
                        help="Install pre-commit",
                        default="False")
    parser.add_argument("--github_repository_url",
                        dest="github_repository_url",
                        help="Github repository URL",
                        default='provide later')
    parser.add_argument("--github_username_or_organization",
                        dest="github_username_or_organization",
                        help="Github user or organisation name",
                        default='githubuser')
    args = Arguments(**vars(parser.parse_args()))

    # Since bool("False") returns True, we need to check the actual string value
    if str(args.install_precommit).lower() == "true":
        install_precommit = True
    else:
        install_precommit = False
    module_name_pep8_compliance(args.module_name)
    pypi_package_name_compliance(args.plugin_name)
    msg = initialize_new_repository(
        install_precommit=install_precommit,
        plugin_name=args.plugin_name,
        github_repository_url=args.github_repository_url,
        github_username_or_organization=args.github_username_or_organization,
    )
    print(msg)