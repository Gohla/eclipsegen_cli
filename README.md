# eclipsegen_cli

Generate Eclipse instances from a single command-line call.

## Publishing

Ensure twine is installed:

```bash
pip3 install twine
```

Build and publish:

```bash
python3 setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
```
