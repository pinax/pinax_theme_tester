# Pinax Theme Tester

![](https://img.shields.io/github/contributors/pinax/pinax_theme_tester.svg)
![](https://img.shields.io/github/issues-pr/pinax/pinax_theme_tester.svg)
![](https://img.shields.io/github/issues-pr-closed/pinax/pinax_theme_tester.svg)
  
[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
* [Documentation](#documentation)
  * [Installation](#installation)
* [Change Log](#change-log)
* [History](#history)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.

## pinax_theme_tester

### Overview

pinax_theme_tester deploys a template browser at http://templates.pinaxproject.com.
Browse there to see each Pinax application template collection, dressed up with Bootstrap 4 styling.

On this site, you can browse all the templates in various different states. In
addition there is a source toggle where you can view the template, see what blocks
are defined, and easily copy and paste into your project if you want to override
or customize the template code.


## Documentation

### Installation

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```shell
$ npm install
$ pip install -r requirements.txt
$ npm install
$ ./manage.py migrate
$ ./manage.py loaddata sites
$ npm run dev
```

Browse to http://localhost:3000/


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
