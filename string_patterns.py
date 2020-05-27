import frameworks as fw

##### Functions #####
def test_consistancy(framework):
    constant = len(framework[0])
    for frame in framework:
        if len(frame) != constant:
            print("Frame", framework.index(frame), "isn't the right size")
            return False
    return True

def tile_framework(framework, num):
    tiled = [frame * num for frame in framework]
    return tiled

def print_framework(framework, num=0):
    if num != 0: # Tile ansi if num is input
        framework = tile_framework(framework, num)
    for frame in framework:
        print(frame)


##### Runtime #####
print_framework(fw.lightning)
print_framework(fw.dna, 3)