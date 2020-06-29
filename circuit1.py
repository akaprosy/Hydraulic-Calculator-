from sys import exit
from random import randint
from hydraulic import HydraulicFormulas


class Startup(object):

    def __init__(self,rpm, on_off):
        self.hyd_form = HydraulicFormulas()        
        self.rpm = rpm
        self.on_off = on_off

                    
   

class States(object):
    
    def __init__(self,l_pos, r_pos):
        self.hyd_form = HydraulicFormulas()
        self.pump_info = Pump(1800,0,3.05)
        self.flow = self.pump_info.set_flow()
        self.l_pos = l_pos  #A port to cap end, #B port to tank
        self.r_pos = r_pos  #B port to rod end, #A port to tank
        

    def valve_shift(self):
        if self.l_pos == True and self.r_pos == False:
            print("Cylinder extending.")
        elif self.l_pos == False and self.r_pos == True:
            print("Cylinder retracting")
        elif self.l_pos == False and self.r_pos == False:
            print("Valve centered. Load holding")
        else:
            print("Valve malfunction")

    def cylinder_extending(self):
        if self.flow != 0:
            print("Enter bore diameter: ")
            bore_dia = int(input("> "))
            b_area = self.hyd_form.bore_area(bore_dia)
            print(f"Cylinder extending at{round(self.hyd_form.cyl_velocity(self.flow,b_area))} inches per second")
        else:
            print("Pump off.....")
        


class Pump(Startup):
    
    def __init__(self, rpm, on_off, displacement):
        super().__init__(rpm, on_off)            
        self.displacement = displacement
        
 #flow(gpm) = displacement(cubic inches/revolution) * speed(rpm)/231
    def set_flow(self):
        print("Enter '1' for pump on and '0' for pump off")
        self.on_off = int(input("> "))
        if self.on_off == 1:
            flow =  self.hyd_form.pump_flow(self.displacement, self.rpm)            
        elif self.on_off == 0:
            flow = 0
        return flow
   
       

class Valve(object):
     pass
    

"""a_flow = Pump(1800,0, 305)
a_run_flow = a_flow.set_flow()
print("Pump flow: ",a_run_flow)"""
a_states = States(True,False)
a_motion = a_states.valve_shift()
a_states_extending = a_states.cylinder_extending()
print(a_states_extending)

