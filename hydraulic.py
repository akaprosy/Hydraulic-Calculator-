#Hydraulic module
import math

class HydraulicFormulas(object):

    def force_pascal(self,pressure, area):
        """Calculate pressure given pressure and area"""
        return pressure * area

    def pressure_pascal(self,area, force):
        """Calculate pressure given area and force"""
        return force/area

    def area_pascal(self,pressure, force):
        """Calculate area given pressure and force"""
        return force / pressure

    def horsepower_pump(self,pressure,flow):
        """Calculate horsepower given pressure and flow"""
        return (pressure * flow)/1714

    def pump_flow(self,displacement, speed):
        """Calculate flow given displacement and speed"""
        return (displacement * speed)/231


    def horsepower_motor1(self,torque, speed):
        """Calculate horsepower given torque(in-lbs) and rpm"""
        return (torque * speed)/5252

    def horsepower_motor2(self,torque, speed):
        """Calculate horsepower given torque(ft-lbs) and rpm"""
        return (torque * speed)/63025

    def torque_motor(self,displacement, pressure):
        """Calculate torque given displacement and pressure"""
        return (displacement * pressure)/6.28
    
    def cylinder_velocity(self,stroke, time):
        """Calculate cylinder velocity given stroke and time"""
        return stroke * (60/time)

    def flow_velocity(self,velocity, area):
        """Calculate flow given velocity and area"""
        return (velocity*area)/231

    def cyl_velocity(self, flow, area):
        """Calculate velocity given area and flow"""
        return (flow * 231)/area

    def bore_area(self,diameter):
        """Calculate cylinder bore area given diameter"""
        return diameter * diameter * .7854

    def flow_valve(self,cv, pressure_drop, specific_gravity):
        """Calculate valve flow rating given cv coefficient, pressure drop and specific gravity"""
        return cv * math.sqrt(pressure_drop/specific_gravity)

    def velocity_conductor(self,flow, area):
        """Calculate fluid velocity in a conductor given flow and area"""
        return (flow * .3208)/area

    def burst_pressure(self,working_press, sf):
        """Calculate burst pressure given working pressure and safety factor"""
        return working_press * sf
    
    def gearpump_flow(self,width, diameter, length):
        """Calculate flow given gear diameter, length across both gear chambers and gear width"""
        return 47 * width * (2 * diameter - length) * ((length - diameter)/2)


    def gearpump_disp(self,width, diameter, length):
        """Calculate displacement given gear diameter, length across both gear chambers and gear width"""
        return 6 * width * (2 * diameter - length) * ((length - diameter)/2)
 
