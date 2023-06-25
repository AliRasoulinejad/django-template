#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

project_slug = "{{cookiecutter.project_slug}}"

use_simple_user_app = "{{cookiecutter.use_simple_user_app}}"
use_jwt_authentication = "{{cookiecutter.use_jwt_authentication}}"
use_logging = "{{cookiecutter.use_logging}}"
use_tracing = "{{cookiecutter.use_tracing}}"
use_metrics = "{{cookiecutter.use_metrics}}"

if use_simple_user_app.lower() == "n":
    os.remove(f'{project_slug}/application/user')

if use_jwt_authentication.lower() == "n":
    os.remove(f'{project_slug}/application/authentication')

if use_logging.lower() == "n":
    os.remove(f'{project_slug}/config/settings/logging')

if use_tracing.lower() == "n":
    os.remove(f'{project_slug}/config/settings/tracing')

if use_metrics.lower() == "n":
    os.remove(f'{project_slug}/config/settings/')
