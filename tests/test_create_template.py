"""
test_create_template
--------------------
"""

import os
import subprocess
import pytest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def run_tox(plugin) -> None:
    """Run the tox suite of the newly created plugin."""
    try:
        subprocess.check_call(
            ["tox", "-c", os.path.join(plugin, "tox.ini"), "-e", "py", "--", plugin]
        )
    except subprocess.CalledProcessError:
        pytest.fail("Subprocess fail", pytrace=True)


@pytest.mark.parametrize("plugin_model_type", ["Detector", "Motor"])
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_template_model_bluesky(copie: "Copie", plugin_model_type: str) -> None:
    """Create a new plugin."""

    answers = {
        "full_name": "plugin bot",
        "email": "yourmail@mail.com",
        "plugin_name": "foo-bar",
        "display_name": "Foo Bar",
        "module_name": "foo_bar",
        "short_description": "Super fast foo for all the bars",
        "github_username_or_organization": "githubuser",
        "github_repository_url": "provide later",
        "plugin_engine": "Bluesky",
        "plugin_type": "Model",
        "plugin_model_type": plugin_model_type,
        "install_precommit": False,
        "license": "MIT",
    }

    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# foo-bar\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "foo_bar", "__init__.py").is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", "bluesky", "__init__.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", "bluesky", "config.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", "bluesky", "model.py"
    ).is_file()


@pytest.mark.parametrize("plugin_engine", ["ExEngine", "Bluesky"])
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_controller(copie: "Copie", plugin_engine: str) -> None:
    """Create a new plugin."""

    answers = {
        "full_name": "plugin bot",
        "email": "yourmail@mail.com",
        "plugin_name": "foo-bar",
        "display_name": "Foo Bar",
        "module_name": "foo_bar",
        "short_description": "Super fast foo for all the bars",
        "github_username_or_organization": "githubuser",
        "github_repository_url": "provide later",
        "plugin_engine": plugin_engine,
        "plugin_type": "Controller",
        "install_precommit": False,
        "license": "MIT",
    }
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# foo-bar\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "foo_bar", "__init__.py").is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", plugin_engine, "__init__.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", plugin_engine, "config.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", plugin_engine, "controller.py"
    ).is_file()
