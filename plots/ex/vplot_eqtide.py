#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import, unicode_literals
import matplotlib.pyplot as plt
import vplot as vpl

# Grab the output from a run
output = vpl.GetOutput('e0.1')

# Set up a matplotlib plot as usual
fig, ax = plt.subplots(3, figsize = (8,12))

# Make font size smaller
plt.rcParams.update({'font.size': 15})

# Background lines
ax[1].plot([0,7e9],[0.0485,0.0485],linestyle='dashed',color='k')
ax[1].text(6e9,0.048,'Best Fit',color='k')
ax[2].plot([0,7e9],[2,2],linestyle='dashed',color='k')
ax[2].text(6e9,1,'Io',color='k')
ax[2].plot([0,7e9],[0.08,0.08],linestyle='dashed',color='k')
ax[2].text(6e9,0.03,'Earth',color='k')


# Now use ``vpl.plot`` instead of ``plt.plot`` to do the
# plotting to get customized VPLOT plots. You can specify
# keyword arguments in the same way you would for ``plt.plot``.
vpl.plot(ax[0], output.proxima.Time, output.b.Eccentricity, label='e = 0.1',color=vpl.colors.pale_blue)
vpl.plot(ax[1], output.proxima.Time, output.b.SemiMajorAxis,color=vpl.colors.pale_blue)
vpl.plot(ax[2], output.proxima.Time, output.b.SurfEnFluxEqtide,color=vpl.colors.pale_blue)

output = vpl.GetOutput('e0.2')
vpl.plot(ax[0], output.proxima.Time, output.b.Eccentricity, label='e = 0.2',color=vpl.colors.pale_blue,linestyle='dashed')
vpl.plot(ax[1], output.proxima.Time, output.b.SemiMajorAxis,color=vpl.colors.pale_blue,linestyle='dashed')
vpl.plot(ax[2], output.proxima.Time, output.b.SurfEnFluxEqtide,color=vpl.colors.pale_blue,linestyle='dashed')

output = vpl.GetOutput('e0.05')
vpl.plot(ax[0], output.proxima.Time, output.b.Eccentricity, label='e = 0.05',color=vpl.colors.pale_blue,linestyle='dotted')
vpl.plot(ax[1], output.proxima.Time, output.b.SemiMajorAxis,color=vpl.colors.pale_blue,linestyle='dotted')
vpl.plot(ax[2], output.proxima.Time, output.b.SurfEnFluxEqtide,color=vpl.colors.pale_blue,linestyle='dotted')


# Fuss with figures
ax[0].legend(); ax[0].set_ylim(0,0.21)
ax[0].set_ylabel('Eccentricity')

ax[1].set_ylim(0.0434,0.05)

ax[2].set_ylim(0.001,100)
ax[2].set_yscale('log')
ax[2].set_ylabel('Surface Energy Flux (W/m$^2$)')


# Show it
#vpl.show()

plt.tight_layout()
plt.savefig('eqtide.ps')
