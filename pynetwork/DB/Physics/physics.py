# Physics Calculator
# Parker Dinkins

def force():
    print('\n=====\nFORCE\n=====')
    print('\nF = m * a\n')
    print('F = Force (N = (kg*m)/(s^2) )')
    print('m = Mass (kg)')
    print('a = acceleration (m/s^2)')
    print('Enter the values you know. \nIf the value is unknown press "enter".\n')
    
    # variable inputs
    f = input('F = ')
    m = input('m = ')    
    a = input('a = ')
    
    # finds the unknown and uses the correct equation
    if f == "":
        fm = float(m)
        fa = float(a)
        f = fm * fa
        print('Force=', f, 'N')
    elif m == "":
        ff = float(f)
        ffa = float(a)
        m = ff/ffa
        print('Mass=', m, 'kg')
    elif a == "":
        fff = float(f)
        ffm = float(m)
        a = f/m
        print('Acceleration=', a, 'm/s^2')
    else:
        print('Not enough information')


def velocity():
    print('\nVELOCITY')
    print('\ndf = v*t + di\n')
    print('df = Final Distance (m)')
    print('di = Initial Distance (m)')
    print('v = Velocity (m/s)')
    print('t = Time (s)\n')
    
    # variable inputs
    df = input('df = ')
    di = input('di = ')
    v = input('v = ')
    t = input('t = ')

    # finds the unknown and uses correct equation
    if df == "":
        vf = float(v)
        tf = float(t)
        dif = float(di)
        df = vf*tf + dif
        print('Final Distance = ', df, 'm')
    
    elif di == "":
        dff = float(df)
        vf = float(v)
        tf = float(t)
        di = dff - vf*tf
        print('Initial Distance = ', di, 'm')

    elif v == "":
        dff = float(df)
        dif = float(di)
        tf = float(t)
        v = (dff - dif)/tf
        print('Velocity = ', v, 'm/s')
    elif t == "":
        dff = float(df)
        dif = float(di)
        vf = float(v)
        t = (dff - dif)/vf
        print('Time = ', t, 's')
    else:
        print('Not Enough Info')


def velocity_accel():
    print('\nVELOCITY WITH ACCELERATION')
    print('\nvf = a*t + vi')
    print('\nvf = final velocity (m/s)')
    print('a = acceleration (m/s^2)')
    print('t = time (s)')
    print('vi = initial velocity (m/s)\n')
    
    # variable inputs
    vf = input('vf = ')
    a = input('a = ')
    t = input('t = ')
    vi = input('vi = ')

    if vf == "":
        af = float(a)
        tf = float(t)
        vif = float(vi)
        vf = af*tf + vif
        print('Final Velocity = ', vf, 'm/s')
    
    elif a == "":
        vff = float(vf)
        vif = float(vi)
        tf = float(t)
        a = (vff - vif)/tf
        print('Acceleration = ', a, 'm/s^2')

    elif t == "":
        vff = float(vf)
        vif = float(vi)
        af = float(a)
        t = (vff - vif)/af
        print('Time = ', t, 's')
    
    elif vi == "":
        vff = float(vf)
        af = float(a)
        tf = float(t)
        vi = vff - af*tf
        print('Initial Velocity = ', vi, 'm/s')
    
    else:
        print('Not Enough Info')


def motion_var_def():
    print('Motion Variables')


def total_distance():
    print('\nTotal Distance')
    print('\nd = df - di\n')
    d = input('d = ')
    df = input('df = ')
    di = input('di = ')

    if d == "":
        dff = float(df)
        dif = float(di)
        d = dff - dif
        print('Total Distance = ', d, 'm')
    elif df == "":
        dff = float(d)
        dif = float(di)
        df = dff + dif
        print('Final Distance = ', df, 'm')
    elif di == "":
        df = float(d)
        dff = float(df)
        di = dff - df
        print('Initial Distance = ', di, 'm')
    else:
        print('Not enough info')
    

def v():
    print('\nVelocity')
    print('\nv = d/t\n')
    v = input('v = ')
    d = input('d = ')
    t = input('t = ')

    if v == "":
        df = float(d)
        tf = float(t)
        v = df/tf
        print('Velocity = ', v, 'm/s')
    elif d == "":
        tf = float(t)
        vf = float(v)
        d = vf/tf
        print('Distance = ', d, 'm')
    elif t == "":
        df = float(d)
        vf = float(v)
        t = df/vf
        print('Time = ', t, 's')
    else:
        print('Not enough info')


def timeless():
    import math

    print('\nTimeless Velocity')
    print('\nvf^2 = 2*a*d + vi^2\n')
    vf = input('vf = ')
    a = input('a = ')
    d = input('d = ')
    vi = input('vi = ')

    if vf == "":
        af = float(a)
        df = float(d)
        vif = float(vi)
        vf = math.sqrt(2*af*df + vif**2)
        print('Final Velocity = ', vf, 'm/s')
    elif a == "":
        vff = float(vf)
        df = float(d)
        vif = float(vi)
        a = (vff**2 - vif**2)/(2*df)
        print('Acceleration = ', a, 'm/s^2')
    elif d == "":
        vff = float(vf)
        af = float(a)
        vif = float(vi)
        d = (vff**2 - vif**2)/(2*af)
        print('Total Distance = ', d, 'm')
    elif vi == "":
        af = float(a)
        df = float(d)
        vff = float(vf)
        vi = math.sqrt(vff**2 - 2*af*df)
        print('Initial Velocity = ', vi, 'm/s')
    else:
        print('Not enough info')
        

def motion():
    print('\nGeneral Motion Equation')
    print('\ndf = 0.5*a*t^2 + vi*t + di\n')
    df = input('df = ')
    a = input('a = ')
    t = input('t = ')
    vi = input('vi = ')
    di = input('di = ')

    if t == "":
        print('Time is a required variable for this equation')
    elif df == "":
        af = float(a)
        vif = float(vi)
        tf = float(t)
        dif = float(di)
        df = 0.5*af*tf**2 + vif*tf + dif
        print('Final Distance = ', df, 'm')
    elif a == "":
        dff = float(df)
        vif = float(vi)
        tf = float(t)
        dif = float(di)
        a = (2*(dff - vif*tf - dif))/(tf*tf)
        print('Acceleration = ', a, 'm/s^2')
    elif vi == "":
        dff = float(df)
        af = float(a)
        tf = float(t)
        dif = float(di)
        vi = (dff - 0.5*af*(tf*tf) - dif)/tf
        print('Initial Velocity = ', vi, 'm/s')
    elif di == "":
        dff = float(df)
        af = float(a)
        tf = float(t)
        vif = float(vi)
        di = dff - 0.5*af*(tf*tf) - vif*tf
        print('Initial Distance = ', di, 'm')
    else:
        print('Not enough info')

        
def v_proj_1():
    pass

def v_proj_2():
    pass

def v_proj_3():
    pass

def h_proj_4():
    pass

def h_proj_5():
    pass

def h_proj_6():
    pass

def proj_var_def():
    pass


#============================MENUS===========================#


#====MOTION====#

def motion_title():
    print('\nOne Dimensional Motion')
    print('======================\n')
    print('v. Variable Definitions')        # motion_var_def()
    print('1. d = df - di')                # total_distance()
    print('2. v = d / t')                  # v()
    print('3. df = v*t + di')               # velocity()
    print('4. vf = a*t + vi')               # velocity_accel()
    print('5. vf^2 = 2*a*d + vi^2')        # timeless()
    print('6. df = 0.5*a*t^2 + vi*t + di')  # motion()


def motion_command_input():
    run = input('\n>>\t')
    
    try:
        motion_dict[run]()
    
    except KeyError:
        print("\n***ERROR***\n")
        motion_command_input()


def motion_menu():
    motion_title()
    motion_command_input()


motion_dict = {
    'v': motion_var_def,
    '1': total_distance,
    '2': v,
    '3': velocity,
    '4': velocity_accel,
    '5': timeless,
    '6': motion
}   



#=======PROJECTILE_MOTION========#

def projectile_motion_title():
    print('\n\tProjectile Motion')
    print('\t=================\n')
    print('When it comes to two dimensional motion')
    print('you must analyze each dimension seperately.')
    print('===========================================\n')
    print('v. Variable Definitions\n')
    print('Vertical')
    print('1. ')
    print('2. ')
    print('3. \n')
    print('Horizontal')
    print('4. ')
    print('5. ')
    print('6. ')


def projectile_motion_command_input():
    projrun = input('\n>>\t')
    
    try:
        proj_motion_dict[projrun]()
    
    except KeyError:
        print("\n***ERROR***\n")
        projectile_motion_command_input()


def projectile_motion_menu():
    projectile_motion_title()
    projectile_motion_command_input()


proj_motion_dict = {
    'v': proj_var_def,
    '1': v_proj_1,
    '2': v_proj_2,
    '3': v_proj_3,
    '4': h_proj_4,
    '5': h_proj_5,
    '6': h_proj_6
}   

#=======FORCES=======#

forces_dict = {
    '1': force
}

def forces_title():
    print('\nForces')
    print('======\n')
    print('1. F = m*a')


def force_command_input():
    forcerun = input('\n>>\t')
    
    try:
        forces_dict[forcerun]()
    
    except KeyError:
        print("\n***ERROR***\n")
        force_command_input()

def forces_menu():
    forces_title()
    force_command_input()


#=======HOME======#

home_dict = {
    '1': motion_menu,
    '2': projectile_motion_menu,
    '3': forces_menu
}

def home_title():
    print('\nPhysics Calculator')
    print('==================')
    print('1. One Dimensional Motion')
    print('2. Projectile Motion')
    print('3. Forces')


def home_command_input():
    homerun = input('\n>>\t')
    
    if homerun == 'q':
        quit()
    
    else:    
        try:
            home_dict[homerun]()
    
        except KeyError:
            print("\n***ERROR***\n")
            home_command_input()


def home():
    home_title()
    home_command_input()


#===========LOOP===============# 


while True:
    home()

    