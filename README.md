![Screenshot from 2025-03-07 18-41-34](https://github.com/user-attachments/assets/8aa9ec85-14e8-4f06-8116-1630846216ab)
![Screenshot from 2025-03-07 18-42-42](https://github.com/user-attachments/assets/68f673b8-aed7-4339-87d1-d58e3aa9d718)
![Screenshot from 2025-03-07 18-55-43](https://github.com/user-attachments/assets/409caf0d-62e4-4800-90df-6d0465fca547)
![Screenshot from 2025-03-07 18-54-37](https://github.com/user-attachments/assets/e46b8404-09f4-4ed6-89cc-6f650cefe67f)
![Screenshot from 2025-03-07 18-53-31](https://github.com/user-attachments/assets/e932070c-b162-4299-970e-e8f0d15e1dc3)
![Screenshot from 2025-03-07 18-48-04](https://github.com/user-attachments/assets/7fd8c9fa-0f90-47c9-8841-83b428c38c98)
![Screenshot from 2025-03-07 18-46-31](https://github.com/user-attachments/assets/24285c52-56c2-4c4d-be55-286c5ebeca17)

### Library Management System

A web based system for managing books, members and transactions in a library.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app library_management_system
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management_system
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
