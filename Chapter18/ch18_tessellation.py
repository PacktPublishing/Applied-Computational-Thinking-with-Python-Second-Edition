import math
import cmath
import cairo

#Define the configuration of the image.
canvas_size = (500, 500)
number_subdivisions = 4

gr = (1 + math.sqrt(5)) / 2 #Golden Ratio

def subdivide(triangles):
    result = []
    for color, A, B, C in triangles:
        if color == 0:
            P = A + (B - A) / gr
            result.extend ([(0, C, P, B), (1, P, C, A)])
        else:
                Q = B + (A - B) / gr
                R = B + (C - B) / gr
                result += [(1, R, C, A), (1, Q, R, B), (0, R, Q, A)]
                return result
            
def setup_canvas(size):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, size[0],
                                 size[1])
    cr = cairo.Context(surface)
    cr.translate(size[0] / 2.0, size[1] / 2.0)
    wheel_radius = 1.2 * math.sqrt((size[0] / 2.0) ** 2 +
                                   (size[1] / 2.0) ** 2)
    cr.scale(wheel_radius, wheel_radius)
    return surface, cr            

def create_initial_triangles():
    triangles = []
    for i in range(10):
        B = cmath.rect(1, (2 * i - 1) * math.pi / 10)
        C = cmath.rect(1, (2 * i + 1) * math.pi / 10)
        if i % 2 == 0:
            B, C = C, B
            triangles.append((0, 0j, B, C))
            return triangles
        
def draw_triangles(cr, triangles, color_code, r, g, b):
    for color, A, B, C in triangles:
        if color == color_code:
            cr.move_to(A.real, A.imag)
            cr.line_to(B.real, B.imag)
            cr.line_to(C.real, C.imag)
            cr.close_path()
            cr.set_source_rgb(r, g, b)
            cr.fill()
            
def draw_borders(cr, triangles):
    color, A, B, C = triangles[0]
    cr.set_line_width(abs(B - A) / 10.0)
    cr.set_line_join(cairo.LINE_JOIN_ROUND)
    for color, A, B, C in triangles:
        cr.move_to(C.real, C.imag)
        cr.line_to(A.real, A.imag)
        cr.line_to(B.real, B.imag)
        cr.set_source_rgb(0.3, 0.5, 0.3)
        cr.stroke()            
        
def save_image(surface, file_path):
    surface.write_to_png(file_path)
    # Main Execution
    triangles = create_initial_triangles()
    for _ in range(number_subdivisions):
        triangles = subdivide(triangles)
        surface, cr = setup_canvas(canvas_size)
        draw_triangles(cr, triangles, 0, .2, .8, .8) # teal triangles
        draw_triangles(cr, triangles, 1, 0.7, 0, 0.7) #purple triangles
        draw_borders(cr, triangles) #The Triangle borders
        save_image(surface, r'C:\\...\\tessellation.png')
       
