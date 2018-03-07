from SimPy.Simulation import *
from SimPy.SimPlot import *

class Source(Process):
    def generate(self,number):
        for i in range(number):
            nameOfCustomer = "Customer%d"%i
            c = Customer(name=nameOfCustomer)
            activate(c,c.visit())
            yield hold,self,2
            

class Customer(Process):
    def visit(self):
        arrive = now()
        print now(),self.name,"I'm here"
        yield request,self,k
        wait = now()-arrive
        w.observe(wait)
        print self.name," waited", wait
        yield hold,self,5
        print now(),"I'm leaving"
        yield release,self,k


initialize()
s = Source()
w = Monitor()
k = Resource(monitored=True)
activate(s,s.generate(number=3),at=0)
simulate(until=100)
print w.mean()
fr = k.waitMon

wt = {}
p = 0
for i in range(100):
    wt[i] = 0
for i in range(len(fr)-1):
    #for j in range(3):
    wt[fr[i][1]] = wt[fr[i][1]] + fr[i+1][0] - fr[i][0]
s = 0
#print wt
for i in range(3):
   s = s + i*wt[i]*1.0/fr[len(fr)-1][0]
print fr,s

plt = SimPlot()
plt.plotBars(k.waitMon)

plt.mainloop()
