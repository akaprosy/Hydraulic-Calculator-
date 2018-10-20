#Pressure spike app development code

#Hydraulics
print("Cylinder formulas")
cylinder_calculator = input("""Choose a calculator
0 - Calculate Force given pressure and area
1 - Calculate Pressure given force and area
2 - Calculate Area given force and pressure
3 - Calculate Area of a cylinder given diameter
4 - Calculate Velocity given stroke and time
5 - calculate Velocity given flow and area
""")

if cylinder_calculator == '0':  

#Calculate force - Force = Pressure * Area
  print('Calculate force - Force = Pressure * Area')
  def pascals_law_force():
      pressure = input('Enter Pressure(psi):')
      area = input('Enter Area(inches squared):')
      return float(pressure) * float(area)

  print('Force =', pascals_law_force(),'lbs.')

elif calculator == '1':
#Calculate Pressure - Pressure = Force / Area
  print('Calculate Pressure - Pressure = Force / Area')
  def pascals_law_pressure():
      force = input('Enter Force(lbs.):')
      area = input('Enter Area(inches squared):')
      return float(force)/float(area)

  print('Pressure =',pascals_law_pressure(),'psi')
elif calculator == '2':
    
#Calculate Area - Area = Force / Pressure
  print('Calculate Area - Area = Force / Pressure')
  def pascals_law_area():
      force = input('Enter Force(lbs.):')
      pressure = input('Enter Pressure(psi):')
      return float(force)/float(pressure)

  print('Area =', pascals_law_area(),'inches squared')

elif calculator == '3':
#Calculate Area of a cylinder - Area = Diameter * Diameter x .7854
  print('Calculate Area of a cylinder - Area = Diameter * Diameter x .7854')
  def cylinder_area():
      diameter = input('Enter diameter:')
      return float(diameter) * float(diameter) * .7854

  print('Cylinder Area:',cylinder_area(),'inches squared')

elif calculator == '4':
#Cylinder Velocity Formulas

#Find velocity of a cylinder(velocity(in/min) = Stroke(inches) * (60/Time(seconds))
  print('Find velocity of a cylinder(velocity(in/min) = Stroke(inches) * (60/Time(seconds')
  def cylinder_velocity_stroke_time():
      stroke = input('Enter stroke(inches):')
      time = input('Enter Time(seconds) to fully extend:')
      return float(stroke) * (60/float(time))

  print('Cylinder Velocity =',cylinder_velocity_stroke_time(),'inches/minutes')

elif calculator == '5':
#Find cylinder velocity - Velocity = (Flow(gpm) * 231)/area(inches squared)
  print('Find cylinder velocity - Velocity = (Flow(gpm) * 231)/area(inches squared)')
  def cylinder_velocity_flow_area():
      flow = input('Enter Flow(gpm):')
      area = input('Enter Area(inches squared):')
      return float(flow) * 231 /float(area)

  print('Cylinder Velocity =', cylinder_velocity_flow_area(), 'inches/minutes')

#Fluid Dynamics

#Find Head inlet pressure - Inlet pressure(psig) = Specific Gravity * .433(psi/ft-H2O)









