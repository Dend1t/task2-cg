import matplotlib.pyplot as plt
import numpy as np
from bezier import BezierCurve



def calculate_bezier_interpolation(x, y, num=500):
    bezier = BezierCurve(x, y)
    params = np.linspace(0.0, 1.0, num)

    result_x, result_y = [], []
    for param in params:
        point_x, point_y = bezier.point(param)
        result_x.append(point_x)
        result_y.append(point_y)

    return result_x, result_y


if __name__ == '__main__':
    x_points = []
    y_points = []
    fig, ax = plt.subplots(figsize=(9, 9), num="Bezier Curve App")

    curve, = ax.plot(x_points, y_points, "-g", label="spline")
    points, = ax.plot(x_points, y_points, "x")

    def on_click(event):
        x_new_point, y_new_point = ax.transData.inverted().transform([event.x, event.y])

        x_points.append(x_new_point)
        y_points.append(y_new_point)

        if len(x_points) > 1 and len(x_points) == len(y_points):
            x_curve_points, y_curve_points = calculate_bezier_interpolation(x_points, y_points, num=500)
            curve.set_xdata(x_curve_points)
            curve.set_ydata(y_curve_points)

        points.set_xdata(x_points)
        points.set_ydata(y_points)

        fig.canvas.draw()

    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()