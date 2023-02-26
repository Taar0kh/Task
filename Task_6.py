!pip install CoolProp
import CoolProp.CoolProp as CP
Sat_Temp = CP.PropsSI('T','P',20*100000,'Q',1,'Water')
print("saturated temperature for water at 20 bar is " + str(Sat_Temp) + " Kelvin"
