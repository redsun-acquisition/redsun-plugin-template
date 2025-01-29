"""
test_create_template
--------------------
"""
from __future__ import annotations

import pytest
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie

@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_model(copie: Copie) -> None:
    """Create a new plugin."""

    answers = {
        "full_name": "plugin bot",
        "email": "yourmail@mail.com",
        "github_username_or_organization": "githubuser",
        "plugin_name": "foo-bar",
        "display_name": "Foo Bar",
        "module_name": "foo_bar",
        "short_description": "Super fast foo for all the bars",
        "github_repository_url": "provide later",
        "plugin_type": "Model",
        "class_baseline": "MyBaseModel",
        "add_widget": False,
        "install_precommit": False,
        "license": "MIT",
    }

    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# foo-bar\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "foo_bar", "__init__.py").is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "__init__.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "config.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "model.py"
    ).is_file()

    # make sure a controller was not generated
    assert not result.project_dir.joinpath(
        "src", "foo_bar", "controller.py"
    ).is_file()

    # make sure a widget was not generated
    assert not result.project_dir.joinpath(
        "src", "foo_bar", "widget.py"
    ).is_file()

    # make sure the .vscode folder was generated
    assert result.project_dir.joinpath(".vscode").is_dir()
    
    # check that launch.json exists and
    # contains the correct configuration name
    assert result.project_dir.joinpath(".vscode", "launch.json").is_file()
    with open(result.project_dir.joinpath(".vscode", "launch.json")) as f:
        content = json.load(f)
        assert content["configurations"][0]["name"] == "plugin-debug"


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_controller(copie: Copie) -> None:
    """Create a new plugin."""

    answers = {
        "full_name": "plugin bot",
        "email": "yourmail@mail.com",
        "github_username_or_organization": "githubuser",
        "plugin_name": "foo-bar",
        "display_name": "Foo Bar",
        "module_name": "foo_bar",
        "short_description": "Super fast foo for all the bars",
        "github_repository_url": "provide later",
        "plugin_type": "Controller",
        "class_baseline": "MyBaseController",
        "add_widget": False,
        "install_precommit": False,
        "license": "MIT",
    }
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# foo-bar\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "foo_bar", "__init__.py").is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "__init__.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "config.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "controller.py"
    ).is_file()

    # make sure a model was not generated
    assert not result.project_dir.joinpath(
        "src", "foo_bar", "model.py"
    ).is_file()

    # make sure a widget was not generated
    assert not result.project_dir.joinpath(
        "src", "foo_bar", "widget.py"
    ).is_file()

    # make sure the .vscode folder was generated
    assert result.project_dir.joinpath(".vscode").is_dir()

    # check that launch.json exists and
    # contains the correct configuration name
    assert result.project_dir.joinpath(".vscode", "launch.json").is_file()
    with open(result.project_dir.joinpath(".vscode", "launch.json")) as f:
        content = json.load(f)
        assert content["configurations"][0]["name"] == "plugin-debug"

@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_widget(copie: Copie) -> None:
    answers = {
        "full_name": "plugin bot",
        "email": "yourmail@mail.com",
        "github_username_or_organization": "githubuser",
        "plugin_name": "foo-bar",
        "display_name": "Foo Bar",
        "module_name": "foo_bar",
        "short_description": "Super fast foo for all the bars",
        "github_repository_url": "provide later",
        "plugin_type": "Widget",
        "class_baseline": "MyBaseWidget",
        "install_precommit": False,
        "license": "MIT",
    }
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# foo-bar\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "foo_bar", "__init__.py").is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "__init__.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "config.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "widget.py"
    ).is_file()

    # make sure a model was not generated
    assert not result.project_dir.joinpath(
        "src", "foo_bar", "model.py"
    ).is_file()

    # make sure a controller was not generated
    assert not result.project_dir.joinpath(
        "src", "foo_bar", "controller.py"
    ).is_file()

    # make sure the .vscode folder was generated
    assert result.project_dir.joinpath(".vscode").is_dir()

    # make sure the .vscode folder was generated
    assert result.project_dir.joinpath(".vscode").is_dir()

    # check that launch.json exists and
    # contains the correct configuration name
    assert result.project_dir.joinpath(".vscode", "launch.json").is_file()
    with open(result.project_dir.joinpath(".vscode", "launch.json")) as f:
        content = json.load(f)
        assert content["configurations"][0]["name"] == "plugin-debug"

@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_model_controller_widget(copie: Copie) -> None:
    answers = {
        "full_name": "plugin bot",
        "email": "yourmail@mail.com",
        "github_username_or_organization": "githubuser",
        "plugin_name": "foo-bar",
        "display_name": "Foo Bar",
        "module_name": "foo_bar",
        "short_description": "Super fast foo for all the bars",
        "github_repository_url": "provide later",
        "plugin_type": "Controller",
        "class_baseline": "MyBaseController",
        "add_widget": True,
        "widget_class_baseline": "MyBaseWidget",
        "install_precommit": False,
        "license": "MIT",
    }
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# foo-bar\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "foo_bar", "__init__.py").is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "__init__.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "config.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "controller.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "widget.py"
    ).is_file()

    # make sure a model was not generated
    assert not result.project_dir.joinpath(
        "src", "foo_bar", "model.py"
    ).is_file()

    # make sure the .vscode folder was generated
    assert result.project_dir.joinpath(".vscode").is_dir()

    # check that launch.json exists and
    # contains the correct configuration name
    assert result.project_dir.joinpath(".vscode", "launch.json").is_file()
    with open(result.project_dir.joinpath(".vscode", "launch.json")) as f:
        content = json.load(f)
        assert content["configurations"][0]["name"] == "plugin-debug"