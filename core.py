from math import pi, sqrt

class Circle:
    def radiusFromDiam(d):
        if type(d) != int and type(d) != float:
            try:
                d = float(d)
                r = d / 2
                return r
            except:
                return 'Invalid Value'
        else:
            r = d / 2
            return r

    def radiusFromCircum(c):
        if type(c) != int and type(c) != float:
            try:
                c = float(c)
                r = (c / pi) / 2
                return r
            except:
                return 'Invalid Value'
        else:
            r = (c / pi) / 2
            return r

    def radiusFromArea(a):
        if type(a) != int and type(a) != float:
            try:
                a = float(a)
                r = sqrt(a / pi)
                return r
            except:
                return 'Invalid Value'
        else:
            r = sqrt(a / pi)
            return r

    def diamFromRadius(r):
        if type(r) != int and type(r) != float:
            try:
                r = float(r)
                d = r * 2
                return d
            except:
                return 'Invalid Value'
        else:
            d = r * 2
            return d

    def diamFromCircum(c):
        if type(c) != int and type(c) != float:
            try:
                c = float(c)
                d = c / pi
                return d
            except:
                return 'Invalid Value'
        else:
            d = c / pi
            return d

    def diamFromArea(a):
        if type(a) != int and type(a) != float:
            try:
                a = float(a)
                d = sqrt(a / pi) * 2
                return d
            except:
                return 'Invalid Value'
        else:
            d = sqrt(a / pi) * 2
            return d

    def circumFromRadius(r):
        if type(r) != int and type(r) != float:
            try:
                r = float(r)
                c = (r * 2) * pi
                return c
            except:
                return 'Invalid Value'
        else:
            c = (r * 2) * pi
            return c

    def circumFromDiam(d):
        if type(d) != int and type(d) != float:
            try:
                d = float(d)
                c = d * pi
                return c
            except:
                return 'Invalid Value'
        else:
            c = d * pi
            return c

    def circumFromArea(a):
        if type(a) != int and type(a) != float:
            try:
                a = float(a)
                c = 2 * pi * sqrt(a / pi)
                return c
            except:
                return 'Invalid Value'
        else:
            c = 2 * pi * sqrt(a / pi)
            return c

    def areaFromRadius(r):
        if type(r) != int and type(r) != float:
            try:
                r = float(r)
                a = pi * r ** 2
                return a
            except:
                return 'Invalid Value'
        else:
            a = pi * r ** 2
            return a
    
    def areaFromDiam(d):
        if type(d) != int and type(d) != float:
            try:
                d = float(d)
                a = pi * (d / 2) ** 2
                return a
            except:
                return 'Invalid Value'
        else:
            a = pi * (d / 2) ** 2
            return a
    
    def areaFromCircum(c):
        if type(c) != int and type(c) != float:
            try:
                c = float(c)
                a = pi * ((c / pi) / 2) ** 2
                return a
            except:
                return 'Invalid Value'
        else:
            a = pi * ((c / pi) / 2) ** 2

class Line:
    def slope(xy1, xy2):
        if type(xy1) != tuple or type(xy2) != tuple:
            return 'Values must be in tuple pairs'
        elif (type(xy1[0]) != int and type(xy1[0]) != float) or (
              type(xy1[1]) != int and type(xy1[1]) != float) or (
              type(xy2[0]) != int and type(xy2[0]) != float) or (
              type(xy2[1]) != int and type(xy2[1]) != float):
            try:
                xy1[0] = float(xy1[0])
                xy1[1] = float(xy1[1])
                xy2[0] = float(xy2[0])
                xy2[1] = float(xy2[1])
                slope = (xy2[1] - xy1[1]) / (xy2[0] - xy1[0])
                return slope
            except:
                return 'Invalid Value(s)'
        else:
            slope = (xy2[1] - xy1[1]) / (xy2[0] - xy1[0])
            return slope
