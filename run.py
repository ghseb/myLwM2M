#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is a part of myLwM2M project.
#
# Copyright (c) 2015 Alexander Ellwein <mylwm2m@ellwein.net>,
#
# myLwM2M is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.

import os
from lwm2m.persistence import Hasher, InMemoryPersistence
from lwm2m.server import Server


def main():
    hasher = Hasher(os.urandom(30))
    Server(InMemoryPersistence(hasher), hasher).start()

if __name__ == '__main__':
    main()
