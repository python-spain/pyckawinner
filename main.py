# -*- coding: utf-8 -*-
#
# Copyleft PyConES 2013
#
# WTFPL License
# http://www.wtfpl.net/txt/copying/
#
# Contributions: Oscar Carballal Prego <info@oscarcp.com>

"""
PyckaWinner - Simple program to select a random winner from all the tweets
with a determined hashtag.
"""

import os
import sys

HASHTAG = ""  # Hashtag to filter
TOKEN = ""    # Token ID from the user that will perform the query

