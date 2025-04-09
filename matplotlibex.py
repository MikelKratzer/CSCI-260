import matplotlib.pyplot as plt
import math

# plt.style.use('_mpl-gallery')

def addChart(axes, x,y, showXlabel = False):
    x_lim = (min(x),max(x))
    y_lim = (min(y),max(y))
    ax[axes].plot(x,y) # scatter: scatter plot; plot: line chart; bar: bar chart; stem: stem plot
    ax[axes].set(xlim=x_lim, ylim=y_lim)
    if showXlabel:
        ax[0].set_xlabel("Angle (rad)")
    ax[axes].set_ylabel("Amplitude")

fig, ax = plt.subplots(nrows=4)
numSteps = 300;
steps=range(0,numSteps);
x = []
y = []
z = []
w = []
u = []
for i in steps:
    angle = i*2.0*math.pi/numSteps
    x.append(angle)
    y_t = math.sin(angle)
    y.append(y_t)
    z_t = y_t + math.sin(3.0*angle)/3.0
    z.append(z_t)
    w_t = z_t + math.sin(5.0*angle)/5.0
    w.append(w_t)
    u_t = w_t + math.sin(7.0*angle)/7.0
    u.append(u_t)

addChart(0,x,y)
addChart(1,x,z)
addChart(2,x,w)
addChart(3,x,u)

plt.show()