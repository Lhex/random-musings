#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:37:18 2017

@author: yapxiuren
"""

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, :] 