from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import random

Regije = {"Ljubljanska_kotlina" : 600000, "Maribor": 100000, "Morje":  50000, "Cigani" : 30000, "Lom pod storžičem" : 300}

def mocarela(regije : dict, time_span, filename="data/temp.png"):
    """
    Parameters
    ----------
    regije dict{"ime regije" : (število_prebivalcev, cas ukuzbe)}
    """
    # pokraden sirmodel iz https://medium.com/towards-artificial-intelligence/graphing-the-sir-model-with-python-e3cd6edb20de
    a = 1 # infection rate
    b = 1/14 # recovery rate
    # FUNCTION TO RETURN DERIVATIVES AT T
    def f(y,t):
        S, I, _ = y # get previous values of S, I, R and store them in array y
        d0 = -a*S*I # derivative of S(t)
        d1 = a*S*I - b*I # derivative of I(t)
        d2 = b*I # derivative of R(t)

        return [d0, d1, d2]

    ans = None
    for (N, t0) in regije.values():
        S_0 = 1
        I_0 = 1/N
        R_0 = 0
        y_0 = [S_0,I_0,R_0]

        t = np.linspace(start=t0,stop=time_span,num=time_span)
        y = odeint(f,y_0,t) 

       # print("y: ", y)

        if ans is None:
            ans = y 
        else:
          #  print("a + y: ", ans + y)
            ans = ans + y
   # print(ans)
    S = ans[:,0]
    I = ans[:,1]
    R = ans[:,2]
    
    plt.figure()
    plt.plot(t,S,"r",label="izpostavljeni")
    plt.plot(t,I,'b',label="bolni")
    plt.plot(t,R,'g',label="avtisti ( so odporni ker so avtisti)")
    plt.legend()
    #plt.show()
    plt.savefig(filename)
    plt.close()

#mocarela({"as" : (10000, 0)}, 100) PASSED
regije_test = {"Ljubljanska_kotlina" : (600000, 0), "Maribor": (100000, 0), "Morje":  (50000, 0), "Cigani" : (30000, 0), "Lom pod storžičem" : (300, 0)}
#mocarela(regije_test, 100)

def testiraj_gauss(stevilo_testov, cas_opazovanja = 100, max_cas_ukuzbe=100):
    for test in range(stevilo_testov):
        filename = f"data/radtrpim_{test}.png"
        novi_dict = {}
        for k, v in Regije.items():
            novi_dict[k] = (v, abs(random.uniform(0, max_cas_ukuzbe)) )
        mocarela(novi_dict, cas_opazovanja, filename=filename)

testiraj_gauss(50)