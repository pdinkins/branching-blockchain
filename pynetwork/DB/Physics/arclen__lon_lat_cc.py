run = True


def arclength():

    pi = 3.141592653589793
    radius = float(input('radius: '))
    angle = float(input('central angle: '))
    arc_length = (2 * pi * radius) * (angle/360)
    print("Arc length", arc_length)


def lonlat_cc():
    import cmath
    r = 3959
    lat = float(input('latitude: '))
    lon = float(input('longitude: '))
    phi = 90 + lon
    theta = 90 - lat
    xcord = r * cmath.sin(theta) * cmath.cos(phi)
    ycord = r * cmath.sin(theta) * cmath.sin(phi)
    zcord = r * cmath.cos(phi)
    print('x: ', xcord)
    print('y: ', ycord)
    print('z: ', zcord)


while run:
    lonlat_cc()

