# -*- coding: utf-8 -*-
'''
Execute a command and read the output as YAML. The YAML data is then directly overlaid onto the minion's Pillar data
'''
from __future__ import absolute_import

# Don't "fix" the above docstring to put it on two lines, as the sphinx
# autosummary pulls only the first line for its description.

# Import python libs
import logging

# Import third party libs
import yaml

# Set up logging
log = logging.getLogger(__name__)


def ext_pillar(minion_id,  # pylint: disable=W0613
               pillar,  # pylint: disable=W0613
               command):
    '''
    Execute a command and read the output as YAML
    '''
    try:
        command = command.replace('%s', minion_id)
        return yaml.safe_load(
            __salt__['cmd.run_stdout']('{0}'.format(command), python_shell=True))
    except Exception:
        log.critical('YAML data from {0} failed to parse'.format(command))
        return {}
