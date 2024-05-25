# Grocia API

## Requirements

- Python version management tool: [pyenv](https://github.com/pyenv/pyenv)

- Python CLI application installer: [pipx](https://github.com/pypa/pipx)

- Python dependency management tool: [poetry](https://python-poetry.org/)

- Justfile: [just](https://github.com/casey/just)

### Installation

1. Install `just`:

```bash
brew install just
```

2. Install `pyenv` and Python 3.10.14 version:

```bash
brew install pyenv
pyenv install 3.10.14
pyenv local 3.10.14
```

3. Install `pipx`:

```bash
brew install pipx
```

4. Install `poetry` and project dependencies:

```bash
pipx install poetry
poetry env use 3.10.14
poetry install --no-root
```

After the installation, the project dependencies will be installed in the virtual environment created by `poetry` under the `.venv` directory.

### Basic usage of `poetry`

- To display the current virtual environment information:

```bash
poetry env info
```

- To activate the virtual environment:

```bash
poetry shell
```

- To deactivate the virtual environment:

```bash
exit
```

- To add a new dependency:

```bash
# For main dependency
poetry add <package-name>

# For development dependency
poetry add <package-name> --group dev
```

- To remove a dependency:

```bash
# For main dependency
poetry remove <package-name>

# For development dependency
poetry remove <package-name> --group dev
```

### Note:

- The `.python-version` file contains the Python version that the project is using.
- The `pyproject.toml` and `poetry.lock` files contain the project dependencies and some what similar to the `package.json` and `package-lock.json` files in Node.js projects.

## Application usage

The application contains the commands written in the `justfile` which can be executed using the `just` command. To display the list of commands:

```bash
just --list
```

### Running the application

- To build the docker image:

```bash
just build
```

- To run the application:

```bash
just up
```

- To stop the application:

```bash
just down
```

- To run tests of the application:

```bash
just test
```

### Migrations

- To create a new migration:

```bash
just mm <migration-name>
```

- To run the migration:

```bash
just migrate
```

- To downgrade the migration:

```bash
just downgrade <downgrade-version>
# Example:
just downgrade -1 # Downgrade the last migration
just downgrade -2 # Downgrade the last two migrations
```