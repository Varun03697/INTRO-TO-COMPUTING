#5
import math
for i in range (0,23,1):
    SineValue=(math.sin(math.radians(15*i)))
    CosValue=(math.cos(math.radians(15*i)))
    RoundOff1=round(SineValue,4)
    RoundOff2=round(CosValue,4)
    print(RoundOff1,RoundOff2)


