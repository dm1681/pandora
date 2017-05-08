from __future__ import division, print_function, absolute_import, unicode_literals
import matplotlib.pyplot as plt
import vplot as vpl

# Figure 5 --> low e/i case

#Left (short)
output = vpl.GetOutput('circ_copl')
time_l = output.star.Time/(1e6)

fig, ax = plt.subplots(2,2, figsize = (7,9))
plt.rcParams.update({'font.size':12})

#Eccentricity
vpl.plot(ax[0,0],time_l, output.b.Eccentricity, label='b',color=vpl.colors.pale_blue, rasterized=True) # planet b
vpl.plot(ax[0,0],time_l, output.c.Eccentricity, label='c',color=vpl.colors.orange, rasterized=True) # planet c

#Inclination
vpl.plot(ax[1,0],time_l, output.b.Inc, label='b', color=vpl.colors.pale_blue, rasterized=True) # planet b
vpl.plot(ax[1,0],time_l, output.c.Inc, label='c', color=vpl.colors.orange, rasterized=True) # planet c



#Right 
output = vpl.GetOutput('circ_copl_long')
time_r = output.star.Time/(1e9)
#Eccentricity
vpl.plot(ax[0,1],time_r, output.b.Eccentricity, label='b', color=vpl.colors.pale_blue, rasterized=True) # planet b
vpl.plot(ax[0,1],time_r, output.c.Eccentricity, label='c', color=vpl.colors.orange, rasterized=True) # planet c
#Inclination
vpl.plot(ax[1,1],time_r, output.b.Inc, label='b', color=vpl.colors.pale_blue, rasterized=True) # planet b
vpl.plot(ax[1,1],time_r, output.c.Inc, label='c', color=vpl.colors.orange, rasterized=True) # planet c

fig.subplots_adjust(wspace=0.5, hspace = 0.2)
#Formatting
ax[0,0].set_ylabel('Eccentricity')
ax[0,0].set_ylim(0.0002,0.0012)
ax[0,0].set_xlim(0,1)
ax[1,0].set_xlim(0,1)
ax[0,1].set_ylabel('')
ax[0,1].set_ylim(0.0002,0.0012)
ax[1,0].set_ylabel('Inclination ($^\circ$)')
ax[1,1].set_ylabel('')
ax[0,0].legend(loc=3)
ax[0,0].set_xlabel('Time (10$^6$ year)')
ax[0,1].set_xlabel('Time (10$^9$ year)')
ax[1,0].set_xlabel('Time (10$^6$ year)')
ax[1,1].set_xlabel('Time (10$^9$ year)')

#vpl.show()
plt.savefig("fig5_5test.pdf",dpi=300)
