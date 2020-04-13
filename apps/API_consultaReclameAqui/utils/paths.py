#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#sys.path.append('/app')

from pathlib import Path

def get_project_root():
    """Returns project root folder."""
    return Path(__file__).parent.parent

def get_url():
    return 'https://www.reclameaqui.com.br'
    #return '107.154.102.99'