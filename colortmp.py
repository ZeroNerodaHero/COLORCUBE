import matplotlib.pyplot as mplt  
fig = mplt.figure()  
ax = fig.add_subplot(111)  
mplt.plot([1,2,3],[1,2,1])  
plotlim = mplt.xlim() + mplt.ylim()  
ax.imshow([[0,0],[1,1]], cmap=mplt.cm.Greens, interpolation='bicubic', extent=plotlim)  
mplt.draw()  
