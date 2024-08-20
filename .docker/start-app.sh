#!/bin/bash

pdm install

pdm run prisma generate

pdm run prisma migrate dev

tail -f /dev/null
