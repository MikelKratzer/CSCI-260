import matplotlib.pyplot as plt
import math

def addChart(axes,x,y,showXlabel=False):
    xlimits=(min(x),max(x)) # x limits for all the charts
    ylimits=(min(y),max(y)) # y Limits for all the charts
    axes.stem(x, y)
    if showXlabel:
        axes.set_xlabel("angle")
    axes.set_ylabel("amplitude")
    axes.set(xlim=xlimits,ylim=ylimits)

fig, ax = plt.subplots(nrows=4)
numSteps=20
steps=range(0,numSteps)
x=[]
y=[]
z=[]
w=[]
u=[]
for i in steps:
  a=i*2.0*math.pi/numSteps
  x.append(a)
  yt=math.sin(a)
  y.append(yt)
  zt=yt+math.sin(3.0*a)/3.0
  z.append(zt)
  wt=zt+math.sin(5.0*a)/5.0
  w.append(wt)
  ut=wt+math.sin(7.0*a)/7.0
  u.append(ut)

addChart(ax[0],x,y)
addChart(ax[1],x,z)
addChart(ax[2],x,w)
addChart(ax[3],x,u)

plt.show()