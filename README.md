# SysML.py

> A Python package for the Systems Modeling Language (SysML) - a general-purpose modeling language for systems engineering applications.

This project is intended to provide an object-oriented programming (OOP) paradigm for practicing Model-Based Systems Engineering (MBSE).

[![Build Status](https://travis-ci.com/spacedecentral/SysML.py.svg?branch=dev)](https://travis-ci.com/spacedecentral/SysML.py)
[![Coverage Status](https://coveralls.io/repos/github/spacedecentral/SysML.py/badge.svg?branch=dev)](https://coveralls.io/github/spacedecentral/SysML.py?branch=dev)

## Package Contents

- `sysml/system.py` - contains the `Model()` class for creating `Model` objects, which serves as a central namespace for model elements (and relationships between elements).

- `sysml/element.py` - contains classes for creating *model element* objects (s.a., `Package`, `Block`, `Requirement`, `Activity`, etc.). These objects are intended for internal use by `Model` objects, using a factory method design pattern.

- `sysml/parser.py` - module for serializing/deserializing `Model` objects.

## Developer Notes

This project is still in pre-alpha. For a more detailed overview on design, usage, and features, please refer to
[#1](https://github.com/spacedecentral/SysML.py/issues/1).

Optional (but recommended for viewing GitHub issues): Install the [ZenHub for GitHub](https://chrome.google.com/webstore/detail/zenhub-for-github/ogcgkffhplmphkaahpmffcafajaocjbd?hl=en-US) chrome extension.

### Development Pipeline

The following semantic version names and corresponding features are being considered for the current development pipeline for `SysML.py`:

- `0.x.y` - standalone python package for SysML (coming soon to PyPI)
- `1.x.y` - to include features to support data interchange as per the current SysML (v1.4) specification
- `2.x.y` - to include features to support data interchange as per the upcoming SysML (v2.0) specification

## Contributing

1. Fork it (<https://github.com/yourusername/SysML.py/fork>)
2. Create your feature branch (`git checkout -b feature/logarithms`)
3. Commit your changes (`git commit -am 'Add some logarithms'`)
4. Push to the branch (`git push origin feature/logarithms`)
5. Create a new Pull Request
