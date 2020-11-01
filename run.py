#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:42:51 2020

@author: wraith
"""

import scraper
import pandas as pd

df = scraper.get_jobs('data scientist', 2000, False)
