#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Farzad Farahani

Plot the feasible region for linear programming

"""
import numpy as np
import matplotlib.pyplot as plt
import pylab as P
import string

#%% First plot
fig = plt.figure(figsize=(6, 6))

lb = -0.5
ub = 1.5
step = 0.5
n_bin = int((ub-lb)/step + 1)

x = 1
d = np.linspace(lb,ub,300)
y1,y2 = np.meshgrid(d,d)
plt.imshow(((y1 - y2 >= -0.6) & (-y1 - y2 >= -1.2+(0.5*pow(x, 1))) & (y1 <= 1) & (y2 <= 1) & (y1 >= 0) & (y2 >= 0)).astype(int), 
                extent=(y1.min(), y1.max(), y2.min(), y2.max()), origin="lower", cmap="Greys", alpha = 0.3);

# plot the lines defining the constraints
y1 = np.linspace(lb,ub,300)
# y1 - y2 >= -0.6
y21 = y1 + 0.6
# -y1 - y2 >= -1.2 + (0.5*pow(x, 1))
y22 = -y1 + 1.2 - (0.5*pow(x, 1))
plt.plot(y1, np.zeros(len(y1)), color='b') # y1 >= 0
plt.plot(np.zeros(len(y1)), y1, color='b') # y2 >= 0
plt.plot(y1, np.ones(len(y1))*1, color='b') # y1 <= 1
plt.plot(np.ones(len(y1))*1, y1, color='b') # y2 <= 1
plt.plot(y1, y21, color='b')
plt.plot(y1, y22, color='b')
# plot intersection points
idx = np.argwhere(np.diff(np.sign(y22 - y21))).flatten()
plt.plot(y1[idx], y21[idx], 'ko', markersize=8, clip_on=False)
xy = (float(y1[idx]),float(y21[idx]))
loc = (float(y1[idx]+step/10),float(y21[idx]+step/10))
plt.annotate('(%.2f, %.2f)' % xy, xy=loc, xycoords='data')

plt.xticks(np.linspace(lb,ub,n_bin))
plt.yticks(np.linspace(lb,ub,n_bin))

plt.xlim(lb,ub)
plt.ylim(lb,ub)

plt.xlabel('$y_1$', fontsize=14)
plt.ylabel('$y_2$', fontsize=14)
plt.title(r'Scenario 1 ($\omega_1$): x=%d' %x)

# Save plot
plt.tight_layout()
plt.savefig('/Users/Farzad/Desktop/Behshad/feasible_area_s1.pdf') 
plt.show() 

#%% Second plot
fig = plt.figure(figsize=(6, 6))

lb = -0.5
ub = 1.5
step = 0.5
n_bin = int((ub-lb)/step + 1)

x = 1
d = np.linspace(lb,ub,300)
y1,y2 = np.meshgrid(d,d)
plt.imshow(((y1 - y2 >= -0.6) & (-y1 - y2 >= -1.4+(0.5*pow(x, 1))) & (y1 <= 1) & (y2 <= 1) & (y1 >= 0) & (y2 >= 0)).astype(int), 
                extent=(y1.min(), y1.max(), y2.min(), y2.max()), origin="lower", cmap="Greys", alpha = 0.3);

# plot the lines defining the constraints
y1 = np.linspace(lb,ub,300)
# y1 - y2 >= -0.6
y21 = y1 + 0.6
# -y1 - y2 >= -1.4 + (0.5*pow(x, 1))
y22 = -y1 + 1.4 - (0.5*pow(x, 1))
plt.plot(y1, np.zeros(len(y1)), color='b') # y1 >= 0
plt.plot(np.zeros(len(y1)), y1, color='b') # y2 >= 0
plt.plot(y1, np.ones(len(y1))*1, color='b') # y1 <= 1
plt.plot(np.ones(len(y1))*1, y1, color='b') # y2 <= 1
plt.plot(y1, y21, color='b')
plt.plot(y1, y22, color='b')
# plot intersection points
idx = np.argwhere(np.diff(np.sign(y22 - y21))).flatten()
plt.plot(y1[idx], y21[idx], 'ko', markersize=8, clip_on=False)
xy = (float(y1[idx]),float(y21[idx]))
loc = (float(y1[idx]+step/10),float(y21[idx]+step/10))
plt.annotate('(%.2f, %.2f)' % xy, xy=loc, xycoords='data')

plt.xticks(np.linspace(lb,ub,n_bin))
plt.yticks(np.linspace(lb,ub,n_bin))

plt.xlim(lb,ub)
plt.ylim(lb,ub)

plt.xlabel('$y_1$', fontsize=14)
plt.ylabel('$y_2$', fontsize=14)
plt.title(r'Scenario 2 ($\omega_2$): x=%d' %x)

# Save plot
plt.tight_layout()
plt.savefig('/Users/Farzad/Desktop/Behshad/feasible_area_s2.pdf') 
plt.show() 

#%% Third plot
fig = plt.figure(figsize=(12, 6))

lb = -0.5
ub = 1.5
step = 0.5
n_bin = int((ub-lb)/step + 1)

plt.subplot(1, 2, 1)

x = 1
d = np.linspace(lb,ub,300)
y1,y2 = np.meshgrid(d,d)
plt.imshow(((y1 - y2 >= -0.6) & (-y1 - y2 >= -1.2+(0.5*pow(x, 1))) & (y1 <= 1) & (y2 <= 1) & (y1 >= 0) & (y2 >= 0)).astype(int), 
                extent=(y1.min(), y1.max(), y2.min(), y2.max()), origin="lower", cmap="Greys", alpha = 0.3);

# plot the lines defining the constraints
y1 = np.linspace(lb,ub,300)
# y1 - y2 >= -0.6
y21 = y1 + 0.6
# -y1 - y2 >= -1.2 + (0.5*pow(x, 1))
y22 = -y1 + 1.2 - (0.5*pow(x, 1))
plt.plot(y1, np.zeros(len(y1)), color='b') # y1 >= 0
plt.plot(np.zeros(len(y1)), y1, color='b') # y2 >= 0
plt.plot(y1, np.ones(len(y1))*1, color='b') # y1 <= 1
plt.plot(np.ones(len(y1))*1, y1, color='b') # y2 <= 1
plt.plot(y1, y21, color='b')
plt.plot(y1, y22, color='b')
# plot intersection points
idx = np.argwhere(np.diff(np.sign(y22 - y21))).flatten()
plt.plot(y1[idx], y21[idx], 'ko', markersize=8, clip_on=False)
xy = (float(y1[idx]),float(y21[idx]))
loc = (float(y1[idx]+step/10),float(y21[idx]+step/10))
plt.annotate('(%.2f, %.2f)' % xy, xy=loc, xycoords='data')

plt.xticks(np.linspace(lb,ub,n_bin))
plt.yticks(np.linspace(lb,ub,n_bin))

plt.xlim(lb,ub)
plt.ylim(lb,ub)

plt.xlabel('$y_1$', fontsize=14)
plt.ylabel('$y_2$', fontsize=14)
plt.title(r'Scenario 1 ($\omega_1$): x=%d' %x)

plt.subplot(1, 2, 2)

x = 1
d = np.linspace(lb,ub,300)
y1,y2 = np.meshgrid(d,d)
plt.imshow(((y1 - y2 >= -0.6) & (-y1 - y2 >= -1.2+(0.5*pow(x, 1))) & (y1 <= 1) & (y2 <= 1) & (y1 >= 0) & (y2 >= 0) & (-y1-y2 >= -1+x)).astype(int), 
                extent=(y1.min(), y1.max(), y2.min(), y2.max()), origin="lower", cmap="Greys", alpha = 0.3);

# plot the lines defining the constraints
y1 = np.linspace(lb,ub,300)
# y1 - y2 >= -0.6
y21 = y1 + 0.6
# -y1 - y2 >= -1.2 + (0.5*pow(x, 1))
y22 = -y1 + 1.2 - (0.5*pow(x, 1))
plt.plot(y1, np.zeros(len(y1)), color='b') # y1 >= 0
plt.plot(np.zeros(len(y1)), y1, color='b') # y2 >= 0
plt.plot(y1, np.ones(len(y1))*1, color='b') # y1 <= 1
plt.plot(np.ones(len(y1))*1, y1, color='b') # y2 <= 1
plt.plot(y1, y21, color='b')
plt.plot(y1, y22, color='b')
# plot the cut line: -y1 - y2 >= -1 + x
y23 = -y1 + 1 - x
plt.plot(y1, y23, color='r', linewidth=3)
P.arrow( -0.2, 0.2, -0.06, -0.06, fc="r", ec="r", head_width=0.05, head_length=0.1)
plt.annotate('FD cut', xy=(-0.42, 0.1), xycoords='data', color='red', rotation=45)
# plot intersection points
idx = np.argwhere(np.diff(np.sign(y23 - y1))).flatten()
plt.plot(y1[idx], y23[idx], 'ko', markersize=8, clip_on=False)
xy = (float(y1[idx]),float(y23[idx]))
loc = (float(y1[idx]+step/10),float(y23[idx]+step/10))
plt.annotate('(%d, %d)' % xy, xy=loc, xycoords='data')

plt.xticks(np.linspace(lb,ub,n_bin))
plt.yticks(np.linspace(lb,ub,n_bin))

plt.xlim(lb,ub)
plt.ylim(lb,ub)

plt.xlabel('$y_1$', fontsize=14)
plt.ylabel('$y_2$', fontsize=14)
plt.title(r'Scenario 1 ($\omega_1$): x=%d' %x)

# Annotate Subplots in a Figure with A, B 
for n, ax in enumerate(fig.axes):
    ax.text(-0.1, 1.05, string.ascii_uppercase[n], transform=ax.transAxes, 
            size=16, weight='regular')

# Save plot
plt.tight_layout()
plt.savefig('/Users/Farzad/Desktop/Behshad/feasible_area_s1_cut.pdf') 
plt.show() 

#%% Fourth plot
fig = plt.figure(figsize=(12, 6))

lb = -0.5
ub = 1.5
step = 0.5
n_bin = int((ub-lb)/step + 1)

plt.subplot(1, 2, 1)

x = 1
d = np.linspace(lb,ub,300)
y1,y2 = np.meshgrid(d,d)
plt.imshow(((y1 - y2 >= -0.6) & (-y1 - y2 >= -1.4+(0.5*pow(x, 1))) & (y1 <= 1) & (y2 <= 1) & (y1 >= 0) & (y2 >= 0)).astype(int), 
                extent=(y1.min(), y1.max(), y2.min(), y2.max()), origin="lower", cmap="Greys", alpha = 0.3);

# plot the lines defining the constraints
y1 = np.linspace(lb,ub,300)
# y1 - y2 >= -0.6
y21 = y1 + 0.6
# -y1 - y2 >= -1.4 + (0.5*pow(x, 1))
y22 = -y1 + 1.4 - (0.5*pow(x, 1))
plt.plot(y1, np.zeros(len(y1)), color='b') # y1 >= 0
plt.plot(np.zeros(len(y1)), y1, color='b') # y2 >= 0
plt.plot(y1, np.ones(len(y1))*1, color='b') # y1 <= 1
plt.plot(np.ones(len(y1))*1, y1, color='b') # y2 <= 1
plt.plot(y1, y21, color='b')
plt.plot(y1, y22, color='b')
# plot intersection points
idx = np.argwhere(np.diff(np.sign(y22 - y21))).flatten()
plt.plot(y1[idx], y21[idx], 'ko', markersize=8, clip_on=False)
xy = (float(y1[idx]),float(y21[idx]))
loc = (float(y1[idx]+step/10),float(y21[idx]+step/10))
plt.annotate('(%.2f, %.2f)' % xy, xy=loc, xycoords='data')

plt.xticks(np.linspace(lb,ub,n_bin))
plt.yticks(np.linspace(lb,ub,n_bin))

plt.xlim(lb,ub)
plt.ylim(lb,ub)

plt.xlabel('$y_1$', fontsize=14)
plt.ylabel('$y_2$', fontsize=14)
plt.title(r'Scenario 2 ($\omega_2$): x=%d' %x)

plt.subplot(1, 2, 2)

x = 1
d = np.linspace(lb,ub,300)
y1,y2 = np.meshgrid(d,d)
plt.imshow(((y1 - y2 >= -0.6) & (-y1 - y2 >= -1.4+(0.5*pow(x, 1))) & (y1 <= 1) & (y2 <= 1) & (y1 >= 0) & (y2 >= 0) & (-y1-y2 >= -1+x)).astype(int), 
                extent=(y1.min(), y1.max(), y2.min(), y2.max()), origin="lower", cmap="Greys", alpha = 0.3);

# plot the lines defining the constraints
y1 = np.linspace(lb,ub,300)
# y1 - y2 >= -0.6
y21 = y1 + 0.6
# -y1 - y2 >= -1.4 + (0.5*pow(x, 1))
y22 = -y1 + 1.4 - (0.5*pow(x, 1))
plt.plot(y1, np.zeros(len(y1)), color='b') # y1 >= 0
plt.plot(np.zeros(len(y1)), y1, color='b') # y2 >= 0
plt.plot(y1, np.ones(len(y1))*1, color='b') # y1 <= 1
plt.plot(np.ones(len(y1))*1, y1, color='b') # y2 <= 1
plt.plot(y1, y21, color='b')
plt.plot(y1, y22, color='b')
# plot the cut line: -y1 - y2 >= -1 + x
y23 = -y1 + 1 - x
plt.plot(y1, y23, color='r', linewidth=3)
P.arrow( -0.2, 0.2, -0.06, -0.06, fc="r", ec="r", head_width=0.05, head_length=0.1)
plt.annotate('FD cut', xy=(-0.42, 0.1), xycoords='data', color='red', rotation=45)
# plot intersection points
idx = np.argwhere(np.diff(np.sign(y23 - y1))).flatten()
plt.plot(y1[idx], y23[idx], 'ko', markersize=8, clip_on=False)
xy = (float(y1[idx]),float(y23[idx]))
loc = (float(y1[idx]+step/10),float(y23[idx]+step/10))
plt.annotate('(%d, %d)' % xy, xy=loc, xycoords='data')

plt.xticks(np.linspace(lb,ub,n_bin))
plt.yticks(np.linspace(lb,ub,n_bin))

plt.xlim(lb,ub)
plt.ylim(lb,ub)

plt.xlabel('$y_1$', fontsize=14)
plt.ylabel('$y_2$', fontsize=14)
plt.title(r'Scenario 2 ($\omega_2$): x=%d' %x)

# Annotate Subplots in a Figure with A, B 
for n, ax in enumerate(fig.axes):
    ax.text(-0.1, 1.05, string.ascii_uppercase[n], transform=ax.transAxes, 
            size=16, weight='regular')

# Save plot
plt.tight_layout()
plt.savefig('/Users/Farzad/Desktop/Behshad/feasible_area_s2_cut.pdf') 
plt.show() 

#%%

import matplotlib.pyplot as plt

plt.axvspan(76, 76, facecolor='g', alpha=1)
plt.annotate('Cut', xy=(76, 0.75), xycoords='data', color='red', rotation=45)
plt.show()
