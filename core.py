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
