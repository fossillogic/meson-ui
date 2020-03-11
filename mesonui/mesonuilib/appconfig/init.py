#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from ..utilitylib import MesonUiException
import typing as T


class MesonInitConfig:
    def __init__(self):
        self.meson_configure: T.Dict = {
            '--type': None,
            '--name': None,
            '--version': None,
            '--language': None,
        }

    def extract(self):
        for conf in self.meson_configure:
            if self.meson_configure[conf] is None:
                raise MesonUiException('Meson cache failed do to "None" value found while loading value')

        return self.meson_configure

    def config(self, option: T.AnyStr, value: T.AnyStr = '') -> None:
        if option == '':
            raise MesonUiException('Option key passed as empty string object')

        self.meson_configure[f'--{option}'] = value