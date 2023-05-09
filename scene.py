from manim import *

class Einheitskreis(Scene):
    def construct(self):
        
        ax = Axes()
        curve = ax.plot(lambda x: np.sin(x), color=GREEN)
        curve2 = ax.plot(lambda x: np.cos(x), color=RED)
        tex = Tex(r"sin(x)", color=GREEN).shift(3*RIGHT+1*UP)
        self.add(ax, curve, tex, curve2)

class Kreise(Scene):
    def construct(self):
        number_plane = NumberPlane(x_range=[-3.5, 3.5], y_range=[-2.1, 2.1]).add_coordinates()
        circle = Circle(radius=1)
        equation = MathTex("0.6^2+0.8^2 = 1").shift(3*RIGHT+3*UP)
        rec = SurroundingRectangle(equation)
        eq = VGroup(rec, equation)
        vecX = Line(start=[0,0,0], end=[0.6, 0,0], color=GREEN)
        vecX.stroke_width = 7
        lableX = MathTex("0.6", color=GREEN).next_to(vecX, DOWN)
        vecy = Line(start=[0.6, 0,0] , end=[0.6,0.8,0], color=BLUE)
        lableY = MathTex("0.8", color=BLUE).next_to(vecy, RIGHT*3)
        vecy.stroke_width = 7
        radius = Line(start=[0,0,0], end=[0.6,0.8,0], color=YELLOW)
        radius.stroke_width = 7

        alles = VGroup(circle, number_plane, vecX, vecy, radius).scale(2)
        

        self.add(alles, eq, lableX, lableY)


class UnitCircle(Scene):
    def construct(self):
        
        circle = Circle(radius=3)

        dot = Dot(point=[1.8,2.4,0])
        

        number_plane = VGroup(Line(start=[-16,0,0], end=[16,0,0]), Line(start=[0,16,0], end=[0,-16,0]))
        number_plane.stroke_width = 1

        vecX = always_redraw(lambda: Line(start=[0,0,0], end=[dot.get_x(), 0,0], color=GREEN))
        vecX.stroke_width = 7
        vecy = always_redraw(lambda: Line(start=[dot.get_x(), 0,0] , end=[dot.get_x(),dot.get_y(),0], color=BLUE))
        vecy.stroke_width = 7
        radius = always_redraw(lambda: Line(start=[0,0,0], end=[dot.get_x(),dot.get_y(),0], color=YELLOW))
        radius.stroke_width = 7
        angle = Angle(vecX, radius, quadrant=(1,1), radius=1)


        lines = VGroup(vecX, vecy, radius)

        self.add(number_plane, lines, circle, dot, angle)
        

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("180^\circ "), MathTex("360^\circ "),
            MathTex("540^\circ"), MathTex("720^\circ")
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=YELLOW)
        
        def get_line_from_x_to_dot():
            return Line(start=[dot.get_x(), 0, 0], end=dot.get_center(), color=BLUE)
        
        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)
        sine = always_redraw(get_line_from_x_to_dot)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line, sine)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)


        