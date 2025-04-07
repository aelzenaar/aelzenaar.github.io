def f1(z): return z+1
def g1(z): return z/(2j*z+1)
def f2(z): return z-1
def g2(z): return z/(-2j*z+1)

def make_points(start_point,number_of_points):
    point_list = [start_point]
    for i in range(number_of_points):
        if random() < .25:
            point_list.append(f1(point_list[-1]))
        elif random() < .5:
            point_list.append(f2(point_list[-1]))
        elif random() < .75:
            point_list.append(g1(point_list[-1]))
        else:
            point_list.append(g2(point_list[-1]))
    return point_list


points(make_points(0,5), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=50, color='black',title="5 points").save("plot_0.png")
points(make_points(0,10), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=50, color='black',title="10 points").save("plot_1.png")
points(make_points(0,50), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=50, color='black',title="50 points").save("plot_1b.png")
points(make_points(0,100), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=20, color='black',title="100 points").save("plot_2.png")
points(make_points(0,500), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=20, color='black',title="500 points").save("plot_2b.png")
points(make_points(0,1000), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=5, color='black',title="1000 points").save("plot_3.png")
points(make_points(0,10000), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=5, color='black',title="10000 points").save("plot_4.png")
points(make_points(0,100000), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=2, color='black',title="100000 points").save("plot_5.png")
points(make_points(0,1000000), aspect_ratio=1, xmin=-2,xmax=2,ymin=-2,ymax=2, marker='.', size=1, color='black',title="1000000 points").save("plot_6.png")
