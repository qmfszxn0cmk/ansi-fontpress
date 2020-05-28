class MadA:
    def __init__(self, case='lower'):
        canvas = create_canvas()
        x_height = 8
        
        if case == 'lower':
        # change index (0, 2, 6)    
                pass
        if case != 'upper':
            print(unfinished)

"""
mad_d =
mad_e =
mad_s =
mad_n =
"""
class Mad8:
    def __init__(self, h, x_h, width, weight):
        pass

def unfinished():
    return "Sorry, this feature hasn't been completed yet."

def create_canvas(fill='$', width=4, weight=2, letter_height=9, drip_height=2):
    canvas = []
    f = fill * weight
    counter = ' ' * width
    frame = f + counter + f
    drip = '.' * len(frame)

    for i in range(letter_height):
        
        if i == 0: # top cap
            canvas.append(frame.replace(' ', '"'))
            continue
        if i == letter_height - 1: # bottom cap (above drips)
            canvas.append(frame.replace(' ', ','))
            continue
        canvas.append(frame)

    for i in range(drip_height):
        canvas.append(drip)
        
    return canvas

print('\n')
blank_1 = create_canvas()
for frame in blank_1:
    print(frame)