# python-automation <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align=right width="100" height="100"><img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" align="right" width='auto' height="90"/><img src="https://playwright.dev/img/playwright-logo.svg" align="right" width='auto' height="90"/>

[![pytest](https://img.shields.io/badge/pytest-testing-blue?logo=pytest&logoColor=white)](https://docs.pytest.org)
[![Playwright](https://img.shields.io/badge/Playwright-Python-45ba4b?logo=playwright&logoColor=white)](https://playwright.dev/python)
[![Requests](https://img.shields.io/badge/requests-HTTP%20client-black)](https://docs.python-requests.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-6f42c1)](https://docs.astral.sh/uv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An E2E unifying test automation framework template.

### 🏗️Pre-requisite
1. Python foundations and beyond.
2. Exposure on [requests](https://requests.readthedocs.io/en/latest/) and [playwright](https://playwright.dev/python/).

### 🛠️Setup
1. Install Git
    1. For Windows - Install [Git Bash](https://git-scm.com/downloads)
    2. For MacOS X
        1. Install **brew** by executing `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
        2. Install git - `brew install git`
2. Install [Python](https://www.python.org/downloads/) >=3.10 - based on your platform.
3. Execute`git clone` - to clone the repo.
4. Install [Cursor](https://cursor.com/download) AI Code Editor and open the repo.
5. Install recommended VS code [extensions](.vscode/extensions.json)
6. Execute `make setup` - setting up the project.
7. In folder 📁.env create `<env_file_name>.env` file containing variables of app which has to be maintained as a secret. Below is the example,
   ```env
   BASE_URL=https://xxxx.com/xxx
   AUTH_URL=https://xxxx.com/xx/xx/xx
   API_URL=https://xx.sse.xxx.com
   EMAIL=xxxx@cixxo.com
   PASSWORD=Xxxx@xx24
   API_KEY=xxxxxx
   API_SECRET=xxxxxx
   ```
> [!CAUTION]
> Do not hardcode any sensitive information.

### ⏯️Execution
`uv run pytest <relative_path_of_test_file> --env <env_file_name>`
> [!WARNING]
> If using Windows, set IDE terminal to Git Bash and execute.

## Client Side Performance Testing <img src="https://avatars.githubusercontent.com/u/2641063?s=200&v=4" align=right width="100" height="100"/>
[![Locust](https://img.shields.io/badge/Locust-performance-2ecc71)](https://locust.io)

Framework has been equipped with Locust to calculate 95th percentile of all SHM APIs.

### 🏋Load test command
`uv run locust -f <relative_path_of_test_file> --env <env_file_name> --users <int> --spawn-rate <int> --run-time <time_in_sec> --headless`

> [!NOTE]
> Follow [commands](COMMANDS.md) for understanding command breakdown