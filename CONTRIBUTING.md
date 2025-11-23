# Contributing

The framework has been built following industry best practices to ensure robustness. We encourage contributors to adhere to the guidelines below to maintain this standard.

Get a walkthrough of the framework before stepping into it.

## Coding

Strictly follow **SRP** while coding.
- **Branching** - Always pull the latest changes from the `main` branch before creating a new branch from it.
- **Scripting**
  - pytest's test file and function name must have prefix or suffix as `test`
  - Create page objects, client, assertions, utilities, resources, and test files only if they do not already exist.
    - Python and its dependency configuration resides in [pyproject.toml](pyproject.toml)
    - [conftest.py](conftest.py) is configured with setup and teardown functions for the tests.
    - Leverage API's for creating and cleaning up test data for UI automation.
    - Attach pytest markers to test scripts for grouping tests.
    - Follow the AAA pattern when designing test scripts.
  > Refer to existing scripts for better understanding.

- **Linting and formatting** - **_Ruff_** is [configured](.vscode/settings.json) for any VS Code family editors to automatically format and lint the code on saving it.

## Execution and debugging
  - Run tests using Playwright CLI [commands](COMMANDS.md), VS Code Playwright Test Runner, or Playwright UI.
  - Use Playwright Debugger or VS Code Debugger or `page.pause()` for step-by-step execution.
  - Utilize Playwright HTML reports, screenshots, videos, or the Trace Viewer for debugging failed tests.

## Style Guide

### Repo

- **File** - follow SnakeCase naming.

  ex: `common_assertion.py`, `login_page.py`

- **Folder** - follow CamelCase naming.

  ex: `api_clients/`, `api_fixtures/`

- **Spec** - any file that is specific to a framework, library, or system should follow its native naming convention.

  ex: `endpoints.json`

### Objects

- **Classes** - follow PascalCase naming.

  ex: `class ApiUtils:`

- **Functions** - follow SnakeCase naming.

  ex: `def build_api:`

- **Variables** - follow SnakeCase naming.

  ex: `db_host: str`

### Git

- **Branch name** - If a JIRA ticket is created for the task, use its ID (for accountability); otherwise, use a short name (kebab case) for the task.

  ex: `CLSESEN-123`, `src-refactor`, `rtt-tests`

- **Commit message** - A concise summary of the commit, usually limited to 50 characters.

  ex: `improve error handling on login form submission`

### Pull request

- **Title** - Start with JIRA ticket id, followed by an meaningful title.

  ex: `tests[JIRA ticker id]: E2E tests of rtt api`


## Pull Request, CI, and Merging

### Pull Request

- **Description** 
  - Provide additional information if necessary.
  - Attach test results from both local and CI runs.
- **Review** - Add code owners for review.

### CI

Branch validation has been carried out on Jenkins Multi branch pipeline.

- **Pre-requisite**
  - Prepare a `<env_file_name>.env` file with required secrets and store it in credentials scoped to pipeline.
- **Trigger a test run**
  - Navigate to a pipeline and click on Scan Repository Now.
  - Click on Pull Requests -> PR Title -> Build with Parameters.
  - Fill in all required fields and start the build.
  - Review the test results after execution and investigate for any failures.
> [!NOTE]
> First build will fail due to missing params. This will facilitate to run the job with required params.

### Merging

Merging to the `main` branch has to be done only after evaluating the following,

- All reviewer comments must be addressed if any and reviewed again after pushing resolves.
- Test runs on both local and CI environments must pass.

## Best practices

- **Readability** - Use clear and meaningful names when creating files, folders, and objects to enhance understanding.

- **Topology** - Organize files, folders, and objects within their respective modules for better traceability.

- **Optimization** - Avoid duplication and remove unused imports, declarations, and dependencies. Optimize the code for better performance.

- **Comments** - Add comments where necessary to provide tips and hints for better comprehension.

- **Execution** - Run each test locally multiple times before raising a PR to minimize flakiness.

## Enhancements

- Kindly discuss with code owners before making any such.
