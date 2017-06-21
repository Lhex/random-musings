#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 01:19:07 2017

@author: yapxiuren
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')

fileName = "LHLFBComments.csv"
dff = pd.read_csv(fileName)

print("done copy")
# Remove all NAs
dff = dff[dff['scores'] != "N"]
print("done remove nas")
# Change all columns to numerics
dff[['mags_num','scores_num']] = dff[['mags','scores']].apply(pd.to_numeric, errors = 'ignore')

dff.describe()

dff.plot(x = "scores_num", y = "mags_num", kind = "scatter", c = "comment_lengths")
dff.plot(x = "comment_lengths", y = "scores_num", kind = "scatter", c = "mags_num")
dff.plot(x = "scores_num", y = "comment_lengths", kind = "scatter", c = "mags_num", colormap = "summer_r")
dff.hist(column="scores_num")

dfflt50 = dff[dff['comment_lengths'] < 150]
dffgt50 = dff[dff['comment_lengths'] >= 150]

dfflt50.plot(x = "comment_lengths", y = "scores_num", kind = "scatter", c = "mags_num")
dfflt50.plot(x = "scores_num", y = "comment_lengths", kind = "scatter", c = "mags_num")

dffgt50.plot(x = "comment_lengths", y = "scores_num", kind = "scatter", c = "mags_num")
dffgt50.plot(x = "scores_num", y = "comment_lengths", kind = "scatter", c = "mags_num", colormap = "summer_r")


# Plot to show lengthier comments are usually higher in magnitude (which
# should be the case since more words to contribute)
# Also, generally positive comments tend to be higher in magnitude
dff.plot(x = "scores_num", y = "comment_lengths", kind = "scatter", c = "mags_num", colormap = "summer_r")
# A lot more positive then negative
dff.hist(column="scores_num")