def coordinates(r,g,b) :
    limit = ((r-0)**2+(g-0)**2+(b-0)**2)**(1/2)
    coordinates = 504,1016

    if ((r-193)**2+(g-193)**2+(b-193)**2)**(1/2) < limit :     # light grey
        coordinates = 531,988
        limit = ((r-193)**2+(g-193)**2+(b-193)**2)**(1/2)   

    if ((r-76)**2+(g-76)**2+(b-76)**2)**(1/2) < limit :     # dark grey
        coordinates = 531,1015
        limit = ((r-76)**2+(g-76)**2+(b-76)**2)**(1/2) 

    if ((r-239)**2+(g-19)**2+(b-11)**2)**(1/2) < limit :     # red
        coordinates = 561,986
        limit = ((r-239)**2+(g-19)**2+(b-11)**2)**(1/2)

    if ((r-116)**2+(g-11)**2+(b-7)**2)**(1/2) < limit :     # dark red
        coordinates = 560,1016
        limit = ((r-116)**2+(g-11)**2+(b-7)**2)**(1/2)

    if ((r-255)**2+(g-113)**2+(b)**2)**(1/2) < limit :     # orange
        coordinates = 589,987
        limit = ((r-255)**2+(g-113)**2+(b)**2)**(1/2)

    if ((r-194)**2+(g-56)**2+(b)**2)**(1/2) < limit :     # dark orange
        coordinates = 589,1019
        limit = ((r-194)**2+(g-56)**2+(b)**2)**(1/2)
        
    if ((r-255)**2+(g-228)**2+(b)**2)**(1/2) < limit :     # yellow
        coordinates = 619,989
        limit = ((r-255)**2+(g-228)**2+(b)**2)**(1/2)
    
    if ((r-232)**2+(g-162)**2+(b)**2)**(1/2) < limit :     # dark yellow
        coordinates = 618,1019
        limit = ((r-232)**2+(g-162)**2+(b)**2)**(1/2)
    
    if ((r)**2+(g-204)**2+(b)**2)**(1/2) < limit :     # green
        coordinates = 646,988
        limit = ((r)**2+(g-204)**2+(b)**2)**(1/2)

    if ((r)**2+(g-85)**2+(b-16)**2)**(1/2) < limit :     # dark green
        coordinates = 646,1018
        limit = ((r)**2+(g-85)**2+(b-16)**2)**(1/2)

    if ((r)**2+(g-178)**2+(b-255)**2)**(1/2) < limit :     # cyan
        coordinates = 675,987
        limit = ((r)**2+(g-178)**2+(b-255)**2)**(1/2)

    if ((r)**2+(g-86)**2+(b-158)**2)**(1/2) < limit :     # dark cyan
        coordinates = 675,1016
        limit = ((r)**2+(g-86)**2+(b-158)**2)**(1/2)

    if ((r-35)**2+(g-31)**2+(b-211)**2)**(1/2) < limit :     # blue
        coordinates = 703,989
        limit = ((r-35)**2+(g-31)**2+(b-211)**2)**(1/2)

    if ((r-14)**2+(g-8)**2+(b-101)**2)**(1/2) < limit :     # dark blue
        coordinates = 704,1014
        limit = ((r-14)**2+(g-8)**2+(b-101)**2)**(1/2)

    if ((r-163)**2+(g)**2+(b-186)**2)**(1/2) < limit :     # purple 
        coordinates = 733,987
        limit = ((r-163)**2+(g)**2+(b-186)**2)**(1/2)

    if ((r-85)**2+(g)**2+(b-105)**2)**(1/2) < limit :     # dark purple
        coordinates = 733,1017
        limit = ((r-85)**2+(g)**2+(b-105)**2)**(1/2)

    if ((r-211)**2+(g-124)**2+(b-170)**2)**(1/2) < limit :     # pink
        coordinates = 762,985
        limit = ((r-211)**2+(g-124)**2+(b-170)**2)**(1/2)

    if ((r-167)**2+(g-85)**2+(b-116)**2)**(1/2) < limit :     # dark pink
        coordinates = 761,1015
        limit = ((r-167)**2+(g-85)**2+(b-116)**2)**(1/2)

    if ((r-160)**2+(g-82)**2+(b-45)**2)**(1/2) < limit :     # brown
        coordinates = 791,988
        limit = ((r-160)**2+(g-82)**2+(b-45)**2)**(1/2)

    if ((r-99)**2+(g-48)**2+(b-13)**2)**(1/2) < limit :     # dark brown
        coordinates = 793,1015
        limit = ((r-99)**2+(g-48)**2+(b-13)**2)**(1/2)

    if ((r-255)**2+(g-255)**2+(b-255)**2)**(1/2) < limit :     # white(skip)
        coordinates = 499,987
        limit = ((r-255)**2+(g-255)**2+(b-255)**2)**(1/2)                       
    return coordinates

