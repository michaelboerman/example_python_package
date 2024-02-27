# example_python_package

Repo containing a simple, tutorial-based python package with no real functionality.

Based on the [PSF tutorial on creating a package](https://packaging.python.org/en/latest/tutorials/packaging-projects); similar to the [published example project repository](https://github.com/pypa/sampleproject).

[Hosted on Test PyPi](https://test.pypi.org/project/example-package-michaelboerman/).

## Installation

Install from Test PyPi:

```shell
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade example-package-michaelboerman
```

## Usage

This package contains one function: `add_one()`. 

Import it like this:

```python
>>>from example_package_michaelboerman import example
```

Use it like this:

```python
>>>example.add_one(4)
5
```

```python
>>>example.subtract_one(4)
3
```