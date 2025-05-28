from Circle import Circle
from Rectangle import Rectangle

if __name__ == '__main__':
    
    c=Circle(20)
    print(f"Area e perimetro del cerchio con raggio= {c.raggio()}: ({c.area()}, {c.perimeter()})")

    r=Rectangle(10,30)
    print(f" Area e Perimetro del rettangolo con base={r.base()} ed altezza={r.altezza()}: (area = {r.area()}, perimetro = {r.perimeter()})") 