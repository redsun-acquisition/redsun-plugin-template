"""
test_create_template
--------------------
"""
from __future__ import annotations

import pytest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


@pytest.mark.parametrize("plugin_model_type", ["Detector", "Motor"])
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_template_model_bluesky(copie: Copie) -> None:
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
        "plugin_type": "Model",
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
        "src", "foo_bar", "engine", "bluesky", "__init__.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", "bluesky", "config.py"
    ).is_file()
    assert result.project_dir.joinpath(
        "src", "foo_bar", "engine", "bluesky", "model.py"
    ).is_file()


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_create_controller(copie: Copie) -> None:
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
        "plugin_type": "Controller",
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
