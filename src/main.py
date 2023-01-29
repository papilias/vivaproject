from src.serviceA import ServiceA
from src.serviceB import ServiceB
from src.serviceC import ServiceC

if __name__ == '__main__':
    serviceA = ServiceA()
    serviceB = ServiceB()
    serviceC = ServiceC()

    serviceA.start()
    serviceB.start()
    serviceC.start()

    serviceA.call_b_and_c()