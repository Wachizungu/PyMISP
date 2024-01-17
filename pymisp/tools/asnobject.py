#!/usr/bin/env python

from __future__ import annotations

from .abstractgenerator import AbstractMISPObjectGenerator
import logging

logger = logging.getLogger('pymisp')


class ASNObject(AbstractMISPObjectGenerator):

    def __init__(self, parameters: dict, strict: bool = True, **kwargs):
        super().__init__('asn', strict=strict, **kwargs)
        self._parameters = parameters
        self.generate_attributes()

    def generate_attributes(self):
        first = self._sanitize_timestamp(self._parameters.pop('first-seen', None))
        self._parameters['first-seen'] = first
        last = self._sanitize_timestamp(self._parameters.pop('last-seen', None))
        self._parameters['last-seen'] = last
        super().generate_attributes()
