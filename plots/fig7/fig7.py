from __future__ import division, print_function, absolute_import, unicode_literals
import matplotlib.pyplot as plt
import vplot as vpl

# Figure 7 --> first 1e6 of short, RotPer and Obliquity, both low and mid e/i

#low e/i = blue
output = vpl.GetOutput('circ_copl')
time = output.star.Time/(10**5)

fig, ax = plt.subplots(2,2, figsize = (7,9))
plt.rcParams.update({'font.size':12})
ax[0,0].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax[1,0].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax[0,1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax[1,1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))


#RotPer (low)
vpl.plot(ax[0,0],time, output.b.RotPer, label='low e,i',color=vpl.colors.pale_blue, rasterized=True) # planet b


#Obliquity (low)
vpl.plot(ax[0,1],time, output.b.Obliquity, label='low e,i', color=vpl.colors.pale_blue, rasterized=True) # planet b

#CassiniOne and DynEllip (low)
vpl.plot(ax[1,1], time, output.b.CassiniOne, label='low e,i', color=vpl.colors.pale_blue, rasterized=True) # Cassini - low
vpl.plot(ax[1,0], time, output.b.DynEllip, label='low e,i', color=vpl.colors.pale_blue, rasterized=True) # DynEllip - low



#mid e/i = orange
output = vpl.GetOutput('mid_e_i')
time = output.star.Time/(10**5)
#RotPer (mid)
vpl.plot(ax[0,0], time, output.b.RotPer, label='high e,i', color=vpl.colors.orange, rasterized=True)

#Obliquity (mid)
vpl.plot(ax[0,1], time, output.b.Obliquity, label='high e,i', color=vpl.colors.orange, rasterized=True)

#CassiniOne and DynEllip(mid)
vpl.plot(ax[1,1], time, output.b.CassiniOne, label='high e,i', color=vpl.colors.orange, rasterized=True) # Cassini - high
vpl.plot(ax[1,0], time, output.b.DynEllip, label='high e,i', color=vpl.colors.orange, rasterized=True) # DynEllip - high 

#Formatting
#Legend
ax[0,0].legend(loc = 4)
ax[0,0].set_xlim(0,2)
ax[0,0].set_ylim(0,12)
ax[0,0].set_xlabel('Time (10$^5$ years)')

ax[1,1].set_xlim(0,5)
ax[1,1].set_ylim(-0.05, 1.05) #adjust until best
ax[1,1].set_xlabel('Time (10$^5$ years)')
ax[1,1].set_ylabel('Cassini Parameter')

ax[0,1].set_xlim(0,2)
ax[0,1].set_xlabel('Time (10$^5$ years)')
ax[0,1].set_ylabel('Obliquity ($^\circ$)')
ax[0,1].set_ylim(.001,6*(10**1))
ax[0,1].set_yscale('log')

ax[1,0].set_xlabel('Time (10$^5$ years)')
ax[1,0].set_xlim(0,2)
ax[1,0].set_ylabel('Dynamical Ellipticity')
ax[1,0].set_ylim(0.00001,0.0035)
ax[1,0].set_yscale('log')

fig.subplots_adjust(wspace=0.35, hspace = 0.2)

#vpl.show()
plt.savefig("fig7_12(zord).pdf",dpi=300)
