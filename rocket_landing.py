# A rocket landing game

from random import randint


M_craft = randint(6000, 9000) # mass of the rocket in kg
Fuel = randint(5000, 9000) # mass of the fuel in kg
H = randint(150000, 250000)   # initial height in meter
V = randint(1300, 2500)  # initial velocity in m/s

dt = 0.1
g_0 = 1.622  # gravity of the moon in m/s^2
V_exhaust = 2800  # in m/s
moon_radius = 1737100  # in meter
g = (g_0 * (moon_radius) ** 2) / (moon_radius + H) ** 2

M_total = M_craft + Fuel

t = 0
print('\t---Welcome to the Rocket Landing Game---\n')
print('You are in a rocket approaching the Moon!')
print('Main computer failed (it was not built by DEC)!')
print('You are to perform manual landing by controlling engines\n')
print("Specify fuel burning rate (kg's per second) for each 10 sec and try to touch down with safe speed. Good luck!!!")
print('Rocket weight:', M_craft, '\n')
print('\tTime\tHeight(m)\tSpeed(m/s)\tFuel(kg)\tGravity(m/s^2)')
print('\t',t,'\t',H,'\t',V,'\t\t',Fuel,'\t\t','%4.2f'% (g))

flag = True
while flag:
    dM = int(input('burning rate: '))
    if dM < 0 or dM > 100:
        print('Please enter a value between 0 and 100')
    else:
        dM = dM / 10
        t += 10
        if (Fuel > 0) and (H >= 0):
            for i in range(100):
                H = H - V * dt
                dV = (V_exhaust * dM) / M_total
                M_total = M_total - dM
                Fuel = Fuel - dM
                g = (g_0 * (moon_radius) ** 2) / (moon_radius + H) ** 2
                V = V + g * dt - dV
            print('\t',t,'\t','%6d' % (H),'\t','%4d' % (V),'\t\t', '%4d' % (Fuel),'\t\t','%4.2f'% (g))
        elif (Fuel <= 0) and (H >= 0):
            while H >= 0:
                H = H - V * dt
                g = (g_0 * (moon_radius) ** 2) / (moon_radius + H) ** 2
                V = V + g * dt
            print('Fuel tank is empty\n You crashed the surface with', '%4d' % (V), 'm/s')
            print('Game Over')
            print('---Thanks for playing---')
            flag = False
        elif H < 0:
            if V < 10:
                print('Congratulations!, you made a successful landing')
                print('Game Over')
                print('---Thanks for playing---')
                flag = False
            else:
                print('You crashed the surface with', '%4d' % (V), 'm/s' )
                print('Game Over')
                print('---Thanks for playing---')
                flag = False
