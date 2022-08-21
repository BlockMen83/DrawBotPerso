import json
fileObject = open("data.json", "r")
jsonContent = fileObject.read()
x_and_y = json.loads(jsonContent)

def coordinates(r,g,b) :
    limit = ((r-0)**2+(g-0)**2+(b-0)**2)**(1/2)
    coordinates = (x_and_y[0]['x'], x_and_y[0]['y'])

    if ((r-193)**2+(g-193)**2+(b-193)**2)**(1/2) < limit :     # light grey
        coordinates = (x_and_y[1]['x'], x_and_y[1]['y'])
        limit = ((r-193)**2+(g-193)**2+(b-193)**2)**(1/2)   

    if ((r-76)**2+(g-76)**2+(b-76)**2)**(1/2) < limit :     # dark grey
        coordinates = (x_and_y[2]['x'], x_and_y[2]['y'])
        limit = ((r-76)**2+(g-76)**2+(b-76)**2)**(1/2) 

    if ((r-239)**2+(g-19)**2+(b-11)**2)**(1/2) < limit :     # red
        coordinates = (x_and_y[3]['x'], x_and_y[3]['y'])
        limit = ((r-239)**2+(g-19)**2+(b-11)**2)**(1/2)

    if ((r-116)**2+(g-11)**2+(b-7)**2)**(1/2) < limit :     # dark red
        coordinates = (x_and_y[4]['x'], x_and_y[4]['y'])
        limit = ((r-116)**2+(g-11)**2+(b-7)**2)**(1/2)

    if ((r-255)**2+(g-113)**2+(b)**2)**(1/2) < limit :     # orange
        coordinates = (x_and_y[5]['x'], x_and_y[5]['y'])
        limit = ((r-255)**2+(g-113)**2+(b)**2)**(1/2)

    if ((r-194)**2+(g-56)**2+(b)**2)**(1/2) < limit :     # dark orange
        coordinates = (x_and_y[6]['x'], x_and_y[6]['y'])
        limit = ((r-194)**2+(g-56)**2+(b)**2)**(1/2)
        
    if ((r-255)**2+(g-228)**2+(b)**2)**(1/2) < limit :     # yellow
        coordinates = (x_and_y[7]['x'], x_and_y[7]['y'])
        limit = ((r-255)**2+(g-228)**2+(b)**2)**(1/2)
    
    if ((r-232)**2+(g-162)**2+(b)**2)**(1/2) < limit :     # dark yellow
        coordinates = (x_and_y[8]['x'], x_and_y[8]['y'])
        limit = ((r-232)**2+(g-162)**2+(b)**2)**(1/2)
    
    if ((r)**2+(g-204)**2+(b)**2)**(1/2) < limit :     # green
        coordinates = (x_and_y[9]['x'], x_and_y[9]['y'])
        limit = ((r)**2+(g-204)**2+(b)**2)**(1/2)

    if ((r)**2+(g-85)**2+(b-16)**2)**(1/2) < limit :     # dark green
        coordinates = (x_and_y[10]['x'], x_and_y[10]['y'])
        limit = ((r)**2+(g-85)**2+(b-16)**2)**(1/2)

    if ((r)**2+(g-178)**2+(b-255)**2)**(1/2) < limit :     # cyan
        coordinates = (x_and_y[11]['x'], x_and_y[11]['y'])
        limit = ((r)**2+(g-178)**2+(b-255)**2)**(1/2)

    if ((r)**2+(g-86)**2+(b-158)**2)**(1/2) < limit :     # dark cyan
        coordinates = (x_and_y[12]['x'], x_and_y[12]['y'])
        limit = ((r)**2+(g-86)**2+(b-158)**2)**(1/2)

    if ((r-35)**2+(g-31)**2+(b-211)**2)**(1/2) < limit :     # blue
        coordinates = (x_and_y[13]['x'], x_and_y[13]['y'])
        limit = ((r-35)**2+(g-31)**2+(b-211)**2)**(1/2)

    if ((r-14)**2+(g-8)**2+(b-101)**2)**(1/2) < limit :     # dark blue
        coordinates = (x_and_y[14]['x'], x_and_y[14]['y'])
        limit = ((r-14)**2+(g-8)**2+(b-101)**2)**(1/2)

    if ((r-163)**2+(g)**2+(b-186)**2)**(1/2) < limit :     # purple 
        coordinates = (x_and_y[15]['x'], x_and_y[15]['y'])
        limit = ((r-163)**2+(g)**2+(b-186)**2)**(1/2)

    if ((r-85)**2+(g)**2+(b-105)**2)**(1/2) < limit :     # dark purple
        coordinates = (x_and_y[16]['x'], x_and_y[16]['y'])
        limit = ((r-85)**2+(g)**2+(b-105)**2)**(1/2)

    if ((r-211)**2+(g-124)**2+(b-170)**2)**(1/2) < limit :     # pink
        coordinates = (x_and_y[17]['x'], x_and_y[17]['y'])
        limit = ((r-211)**2+(g-124)**2+(b-170)**2)**(1/2)

    if ((r-167)**2+(g-85)**2+(b-116)**2)**(1/2) < limit :     # dark pink
        coordinates = (x_and_y[18]['x'], x_and_y[18]['y'])
        limit = ((r-167)**2+(g-85)**2+(b-116)**2)**(1/2)

    if ((r-160)**2+(g-82)**2+(b-45)**2)**(1/2) < limit :     # brown
        coordinates = (x_and_y[19]['x'], x_and_y[19]['y'])
        limit = ((r-160)**2+(g-82)**2+(b-45)**2)**(1/2)

    if ((r-99)**2+(g-48)**2+(b-13)**2)**(1/2) < limit :     # dark brown
        coordinates = (x_and_y[20]['x'], x_and_y[20]['y'])
        limit = ((r-99)**2+(g-48)**2+(b-13)**2)**(1/2)

    if ((r-255)**2+(g-255)**2+(b-255)**2)**(1/2) < limit :     # white(skip)
        coordinates = (x_and_y[21]['x'], x_and_y[21]['y'])
        limit = ((r-255)**2+(g-255)**2+(b-255)**2)**(1/2)                       
    return coordinates

