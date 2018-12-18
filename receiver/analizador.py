import pylab as pl
import pandas as pd
import numpy as np
r = np.arange(0,17,.01)
c = 1.1*r**3 - 3.8*r**2 + 520*r +.62
pl.plot(r,c)
pl.grid()
pl.show()
