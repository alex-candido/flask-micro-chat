#!/bin/bash

pdm install

pdm runserver

tail -f /dev/null
