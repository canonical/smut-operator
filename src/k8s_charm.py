#!/usr/bin/env python3

# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""A  juju charm for Grafana Agent on Kubernetes."""
import logging

from smut_charm import SmutCharm

logger = logging.getLogger(__name__)

SMUT_CONFIG = "/smut.cfg"
SMUT_LOGS = "/smut.log"


class SmutK8sCharm(SmutCharm):
    """Kubernetes version of the Smut charm."""

    def __init__(self, *args):
        super().__init__(*args)

    def install(self) -> None:
        """Install the smut software."""

    def start(self) -> None:
        """Start the smut software."""