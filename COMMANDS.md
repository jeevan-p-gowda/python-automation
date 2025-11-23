# Commands

## Pytest <img src="https://camo.githubusercontent.com/4dfd51f878f6fba7010fb7e1ee7a9ddd9e1a689a6a6210e1068369a1e2e0e9fe/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f622f62612f5079746573745f6c6f676f2e737667" align=right width="100" height="100" title="pytest"/>

1. **Running Tests**:

- Run all tests: Execute every test script in your project with `uv run pytest tests/api/` or `uv run pytest tests/ui/`
- Run a single test file: Target a specific file, e.g., `uv run pytest tests/api/test_rtt_api.py`
- Run a set of test files: Group multiple test files, e.g., `uv run pytest tests/api/test_rtt_api.py tests/api/test_connections_api.py`

2. **Filtering and Specifying Tests**:

- Run test files by name pattern: Use patterns to target tests, e.g., `uv run pytest tests/api/ -k "rtt"`
- Run test files by excluding name pattern: Use patterns to target and exclude tests, e.g., `uv run pytest tests/api/ -k "not rtt"`
- Run tests by its name pattern or marker: Execute tests with a matching title, e.g., `uv run pytest tests/api/ -m rate_limit`
- Run tests by its name pattern in a file: Execute tests with a matching title, e.g., `uv run pytest tests/api/test_connections_api.py::TestConnectionsApi -m rate_limit`

3. **Browser and Visualization Options**:

- Run tests in headed browsers: For visual debugging, use `uv run pytest tests/api/ --headed`
- Run tests in a specific browser: To test in a single browser, e.g., `uv run pytest tests/ui/ --browser=firefox`

4. **Parallel Execution and Debugging**:

- Install [pytest-xdist](https://github.com/pytest-dev/pytest-xdist): `'n'` defines no. of parallel workers to be spawn, use `uv run pytest -n 3 tests/api/`
- Debug tests: Launch tests in debug mode with `PWDEBUG=1 uv run pytest tests/ui/` to enable Playwright Inspector.
- Avoid flakiness by running tests multiple times: `uv run pytest tests/api/ --count=10`

5. **Interactive Testing and Code generation**:

- Help command: Access detailed command options with `uv run pytest --help`.
- Check pytest version `uv run pytest -V`
- Basic codegen: Record user interactions and generate test scripts with `playwright codegen`
- Generate with specific URL: Target a particular browser for recording, e.g., `playwright codegen https://google.com`

## Locust <img src="https://avatars.githubusercontent.com/u/2641063?s=200&v=4" align=right width="100" height="100"/>

`uv run locust -f <relative_path_of_test_file> --env <env_file_name> --users <int> --spawn-rate <int> --run-time <time_in_sec> --headless`

**Command Breakdown:**
- `uv run locust` - Uses uv package manager to run Locust load testing tool
- `-f <relative_path_of_test_file>` - Specifies the performance test file (e.g., `tests/perf/perf_connections_api.py`)
- `--env <env_file_name>` - Environment configuration file name (e.g., `int`, `prod`)
- `--users <int>` - Total number of concurrent virtual users to simulate
- `--spawn-rate <int>` - Rate at which users are spawned per second
- `--run-time <time_in_sec>` - Duration of the test in seconds (e.g., `60s`, `5m`)
- `--headless` - Runs without the web UI for automated execution

`locust -V` - check locust version
`locust --help` - seek locust help


## UV <img src='https://docs.astral.sh/uv/assets/logo-letter.svg' align=right title='UV' width="60" height="100">
1. `uv init <app_name>` - Initialize a new project
2. `uv add <dependency>` - Add a dependency to a run time dependency
3. `uv add --group dev <dependency>` - Add a dependency to a specific group
4. `uv add --group <group> <dependency> --group <group> <dependency>` - Add a multiple dependency across multiple group
5. `uv lock --upgrade-package <dependency>` - Upgrades specific dependency
6. `uv lock --upgrade` - Upgrades all dependencies
7. `uv remove <dependency>` - Remove a dependency
8. `uv remove --group <group> <dependency>` - Remove a dependency from specific group
9. `uv run <module.py>` - Run the python module
10. `uv tool install <tool_name>` - Install a tool Example: `uv tool install ruff`
11. `uv tool uninstall <tool_name>` - Uninstall a tool`
12. `uv tool list` - List all installed tools
13. `uv tool upgrade -all` - Upgrade all tools if available
14. `uv tool run ruff check` - Run a tool by installing it temporarily
15. `uv sync` - Installs all the dependencies and tools in the project
16. `uv sync --all-groups` - Installs dependencies from all groups
17. `uv sync --group <group>` - Installs dependecies from specific group
18. `uv python list --only-installed` - lists all python versions installed
18. `uv version` - check uv version
19. `uv help` - seek uv help

## Ruff <img src='https://docs.astral.sh/ruff/assets/bolt.svg' align=right title='UV' width="60" height="100">
1. `ruff check <file_or_directory>` - Check the code for issues
2. `ruff format <file_or_directory>` - Format the code
3. `ruff check --fix <file_or_directory>` - Check and fix issues in the code
4. `ruff check --fix --diff <file_or_directory>` - Check issues in the code, showing a diff of changes to be made
5. `ruff check --watch <file_or_directory>` - Watch for issues on fly
6. `ruff version` - check ruff version
7. `ruff help` - seek ruff help

> [!TIP]
> Experiment with different CLI commands to tailor test runs according to your needs.
> Use environment variables alongside CLI commands for more dynamic test configurations.
> Regularly review respective dependency documentation for updates on CLI options.