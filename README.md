# test project

Install dependencies
```bash
pip3 install -r src/requirements.txt
poetry config certificates.gitlab_test_project.cert <path_to_certificate>
poetry self add "poetry-dynamic-versioning[plugin]"
```

Build project

```bash
poetry install
poetry run <cli>
poetry build
```

Publish package

```bash
poetry publish --repository gitlab_test_project -u <user> -p <pass>
```