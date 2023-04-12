from manim import *
import math
import sympy as sp


class Scene1(Scene):
    def construct(self):
        
        ax = Axes(
            x_range=[-2, 2], y_range=[-2, 8], x_length=4,  axis_config={"include_tip": False, "include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        def func(x):
            return x**5+x**2-x-0.5
        graph = ax.plot(func, color=BLUE)
    
        function = VGroup(labels, graph)
        function2 = VGroup(labels, graph, ax)

        equation = MathTex(r"f(x)=x^","5","+x^2-x-0.5", font_size=60).shift(3*LEFT+2.5*UP)
        equation2 = MathTex(r"R(x)=x^5+x^2-x-0.5=0", font_size=60).shift(2.5*LEFT+2.5*UP)
        
        fiveRectangle = SurroundingRectangle(equation[1], color=RED)

        equation3 = MathTex("R(","-1.1427",")=...", font_size=60).next_to(equation2, DOWN).shift(0.5*DOWN+0.5*LEFT)
        equation3[1].set_color(YELLOW)
        equation4 = MathTex("R(","-0.3700",")=...", font_size=60).next_to(equation3, DOWN).shift(0.5*DOWN)
        equation4[1].set_color(YELLOW)
        equation5 = MathTex("R(","+0.8998",")=...", font_size=60).next_to(equation4, DOWN).shift(0.5*DOWN)
        equation5[1].set_color(YELLOW)


        equations = VGroup(equation3, equation4, equation5)

        rectangle = SurroundingRectangle(equation2, color=BLUE, buff=0.2)

        eq = VGroup(equation, rectangle)
        dot1 = Dot(ax.coords_to_point(-1.1427, 0), color=YELLOW)
        dot2 = Dot(ax.coords_to_point(-0.3700, 0), color=YELLOW)
        dot3 = Dot(ax.coords_to_point(0.89987, 0), color=YELLOW)
        dots = VGroup(
            dot1, dot2, dot3
        ).shift(3.5*RIGHT)

        question = Tex("Computing ?", font_size=80).shift(3*LEFT)
        how = Tex("How....?", font_size=80).move_to(question)
        
        self.play(Create(ax), Create(labels), run_time=5)
        self.wait(2)
        self.play(Create(graph), run_time=8)
        self.wait(2)
        self.play(Write(equation), function2.animate.shift(3.5*RIGHT), run_time=3)
        self.wait(2)
        self.play(Create(fiveRectangle))
        self.wait(2)
        self.play(Uncreate(fiveRectangle), ReplacementTransform(equation, equation2), Create(rectangle))
        self.wait(2)
        self.play(Create(dots), run_time=4)
        self.wait(2)
        self.play(Write(equations), run_time=5)
        self.wait(2)
        self.play(ReplacementTransform(equations, question))
        self.wait(2)
        self.play(ReplacementTransform(question, how))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

def sphere_ray_intersection(ray_origin, ray_direction, sphere_center, sphere_radius):
    
    ray_origin = np.array(ray_origin)
    ray_direction = np.array(ray_direction)
    sphere_center = np.array(sphere_center)

    # Compute the vector from the ray origin to the sphere center
    oc = ray_origin - sphere_center

    # Compute coefficients of the quadratic equation
    a = np.dot(ray_direction, ray_direction)
    b = 2.0 * np.dot(oc, ray_direction)
    c = np.dot(oc, oc) - sphere_radius**2

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # If the discriminant is negative, no intersection
    if discriminant < 0:
        return []

    # Otherwise, calculate the intersection point(s)
    t1 = (-b + math.sqrt(discriminant)) / (2*a)
    t2 = (-b - math.sqrt(discriminant)) / (2*a)
    intersection_point_1 = tuple(ray_origin + t1 * ray_direction)
    intersection_point_2 = tuple(ray_origin + t2 * ray_direction)

    # If t1 and t2 are the same, only one intersection point
    if t1 == t2:
        return [intersection_point_1]
    else:
        return [intersection_point_1, intersection_point_2]


class Scene2(ThreeDScene):
    
    def construct(self):
        
        axes = ThreeDAxes()
        axes_lables = axes.get_axis_labels()
        graphicsTex = Tex("Computer Graphics", color=BLUE, font_size=120).shift(UP*3)

        sphereradius = 2
        sphere_center = [0,0,0]
        ray_start = [0,-4,-4]
        ray_end = [0,4,4]

        sphere = Sphere(radius=sphereradius, center=sphere_center)
        ray = Line(start=ray_start, end=ray_end)

        intersectionsPoints = sphere_ray_intersection(ray_direction=ray_end, ray_origin=ray_start, sphere_center=sphere_center, sphere_radius=sphereradius)

        dots = VGroup()
        for point in intersectionsPoints:
            dot = Dot3D(point, radius=0.12, color=YELLOW)
            dots.add(dot)  

        self.play(Write(graphicsTex))
        self.wait(2)
        self.play(Create(axes_lables), Create(axes))
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.play(Unwrite(graphicsTex))
        self.wait(20)
        self.play(Create(sphere))
        self.wait(2)
        self.play(Create(ray))
        self.wait(2)
        self.play(Create(dots))
        self.wait(10)
        self.play(Indicate(dots))
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(sphere))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene3(Scene):
    def construct(self):
        
        ax = Axes(
            x_range=[-3.5, 3.5], y_range=[-2, 8], x_length=4,  axis_config={"include_tip": False, "include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        def func(x):
            return x**2-1
        graph = ax.plot(func, color=BLUE)
        function = VGroup(labels, ax)
        function2 = VGroup(labels, graph, ax).move_to(3.5*LEFT+0.5*UP)

        waysToCompute = Tex("We have ways to compute roots, don't we?", font_size=70).move_to(3*UP)
        yesNo = Tex("Yes and no...", font_size=100).move_to(waysToCompute)
        functionTex = MathTex(r"f(x)=",r"a",r"x^2+",r"b",r"x+c").move_to(3*RIGHT+2*UP)
        functionTex[1].set_color(GREEN_A)
        functionTex[3].set_color(BLUE_A)
        rectangle = SurroundingRectangle(functionTex, color=BLUE)

        quadraticFormula = MathTex(r"R(x)=\frac{-b\pm \sqrt{b^2-4ac}}{2a}").next_to(functionTex, DOWN).shift(0.5*DOWN)

        def func2(x):
            return -2*x**3-3*x**2+x+3
        graph2 = ax.plot(func2, color=RED)
        functionTex2 = MathTex(r"f(x)=ax^3+bx^2+cx+d").move_to(3*RIGHT+2*UP)
        rectangle2 = SurroundingRectangle(functionTex2, color=RED)

        cubicFormula1 = MathTex(r"R(x) = \sqrt[3]{-\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^{2} + \left(\frac{p}{3}\right)^{3}}}} ").next_to(functionTex2, DOWN).shift(0.5*DOWN)
        cubicFormula2 = MathTex(r"+ \sqrt[3]{-\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^{2} + \left(\frac{p}{3}\right)^{3}}}} - \frac{b}{3a}").next_to(cubicFormula1, DOWN)
        cubicFormula = VGroup(cubicFormula1, cubicFormula2)

        def func3(x):
            return -(x**4-2*x**2)+4
        graph3 = ax.plot(func3, color=GREEN)
        functionTex3 = MathTex(r"f(x)=ax^4+bx^3+cx^2+dx+e").move_to(3*RIGHT+2*UP)
        rectangle3 = SurroundingRectangle(functionTex3, color=GREEN)

        quartic = Tex(r"R(x)= ...(its a weird extisting one)").move_to(quadraticFormula)

        def func4(x):
            return x**5-5*x**4+5*x**3+5*x**2-6*x+2
        graph4 = ax.plot(func4, color=YELLOW)
        functionTex4 = MathTex(r"f(x)=ax^5+bx^4+cx^3+dx^2+ex+f").move_to(2.7*RIGHT+2*UP)
        rectangle4 = SurroundingRectangle(functionTex4, color=YELLOW)

        quintic = Tex(r"R(x)= cannot be found").move_to(quadraticFormula)

        self.play(Write(waysToCompute))
        self.wait(2)
        self.play(ReplacementTransform(waysToCompute, yesNo))
        self.wait(2)
        self.play(Unwrite(yesNo))
        self.play(Write(functionTex), Create(rectangle))
        self.play(Create(function))
        self.play(Create(graph), run_time=5)
        self.wait(2)
        self.play(Write(quadraticFormula))
        self.wait(2)
        self.play(ReplacementTransform(graph, graph2), ReplacementTransform(rectangle, rectangle2), ReplacementTransform(functionTex, functionTex2), ReplacementTransform(quadraticFormula, cubicFormula))
        self.wait(2)
        self.play(ReplacementTransform(graph2, graph3), ReplacementTransform(rectangle2, rectangle3), ReplacementTransform(functionTex2, functionTex3), ReplacementTransform(cubicFormula, quartic))
        self.wait(2)
        self.play(ReplacementTransform(graph3, graph4), ReplacementTransform(rectangle3, rectangle4), ReplacementTransform(functionTex3, functionTex4), ReplacementTransform(quartic, quintic))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene4(Scene):
    def construct(self):

        def newtonsMethod(func, Dfunc, iterations, time_in_between, x0, ax, tangentText="", lineText="", graphColor=BLUE, text_position=[-3,0,0], numberEquation=False, bool_equation=True, secant_lenght=4):
            
                graph = ax.plot(func, color=graphColor)
                self.play(Create(graph))
                for i in range(iterations):
                    x0_round = round(x0,3)
                    dot = ax.get_T_label(x_val=x0, graph=graph, label=MathTex(round(x0,3), color=YELLOW).scale(0.75), triangle_color=YELLOW, triangle_size=0.125, line_color=WHITE)
                    tangent = ax.get_secant_slope_group(
                        x=x0,
                        graph=graph,
                        dx=0.00000000001,
                        secant_line_color=RED,
                        secant_line_length= secant_lenght
                        )
                    if numberEquation == True:
                        equation = MathTex(
                        r"x_{" + str(i + 1) + r"}={" + str(x0_round) + r"}-\frac{f({" + str(x0_round) + r"})}{f'({" + str(x0_round) + r"})}"
                        ).move_to(text_position)
                    else:
                        equation = MathTex(
                        r"x_{" + str(i + 1) + r"}=x_{" + str(i) + r"}-\frac{f(x_{" + str(i) + r"})}{f'(x_{" + str(i) + r"})}"
                        ).move_to(text_position)

                    if iterations == 1:
                        tangentTexta = Tex(tangentText, color=RED).move_to(tangent).rotate(math.atan(Dfunc(x0))).shift(0.5*LEFT)
                        lineTexta = MathTex(lineText).next_to(dot, RIGHT)
                    else:
                        tangentTexta = Tex("")
                        lineTexta = MathTex("")

                    souroundRec = SurroundingRectangle(equation)
                    all = VGroup(dot, tangent, tangentTexta, lineTexta, equation, souroundRec)
                    secondAll = VGroup(dot, tangent, tangentTexta, lineTexta)
                    self.play(Create(dot), Create(lineTexta))
                    if bool_equation == True:
                        self.play(Write(equation), Create(souroundRec))
                    self.wait(time_in_between)
                    
                    self.play(Create(tangent), Create(tangentTexta))
                    x0 = x0 - (func(x0)/Dfunc(x0))
                    self.wait(time_in_between)
                    if iterations != 1:
                        if bool_equation == True:
                            self.play(FadeOut(all))
                        else: 
                            self.play(FadeOut(secondAll))
             
        ax = Axes(
            x_range=[-2, 2], y_range=[-2, 6], x_length=7, y_length=7, axis_config={"include_tip": False, "include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        axes = VGroup(ax, labels).shift(RIGHT*2.5)
        def func(x):
            return x**5+x**2-x-0.5
        def Dfunc(x):
           return 5*x**4+2*x-1 
        
        x0 = 1.3
        self.play(Create(axes))
        
        tex = "Tangent"
        tex2 = "f(x_0)" 
        functionTex = MathTex(r"f(x)=x^5+x^2-x-0.5").move_to(3.5*LEFT+3*UP)
        rec2 = SurroundingRectangle(functionTex, color=BLUE)
        dfuncTex = MathTex(r"f'(x)=5x^4+2x-1").next_to(functionTex, DOWN*2)
        slopeEq = MathTex(r"Slope=\frac{f(x_0)}{Step}").move_to(3*LEFT)
        slopeEq2 = MathTex(r"f'(x)=\frac{f(x_0)}{Step}").move_to(slopeEq)
        stepEq = MathTex(r"Step=\frac{f(x_0)}{f'(x_0)}").move_to(slopeEq2)
        rec = SurroundingRectangle(stepEq)
        
        self.play(Write(functionTex), Create(rec2))
        newtonsMethod(func=func, Dfunc=Dfunc, iterations=1, x0=x0, ax=ax, time_in_between=0.1, tangentText=tex, lineText=tex2, graphColor=BLUE, text_position=[-4,0,0], numberEquation=False
                      , bool_equation=False, secant_lenght=8)
        self.wait(2)
        self.play(Create(dfuncTex))
        self.wait(2)
        self.play(Create(slopeEq), Create(rec))  
        self.play(ReplacementTransform(slopeEq, slopeEq2))
        self.wait(2)
        self.play(ReplacementTransform(slopeEq2, stepEq))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        self.wait(2)
        self.play(Create(functionTex), Create(rec2), Create(axes), Create(dfuncTex))
        newtonsMethod(func=func, Dfunc=Dfunc, iterations=6, x0=x0, ax=ax, time_in_between=0.1, tangentText=tex, lineText=tex2, graphColor=BLUE, text_position=[-4,0,0], numberEquation=False
                      , bool_equation=True, secant_lenght=4)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        def func2(x):
            return x**5+x**2-x+1
        
        funTex2 = MathTex(r"f(x)=x^5+x^2-x+1").move_to(3.5*LEFT+3*UP)
        ax2 = Axes(
            x_range=[-7, 7], y_range=[-2, 6], x_length=5, y_length=7, axis_config={"include_tip": False, "include_numbers": False}
        )
        labels2 = ax2.get_axis_labels(x_label="x", y_label="f(x)")
        axes2 = VGroup(ax2, labels2).shift(RIGHT*2.5)
        self.play(Write(funTex2), Create(SurroundingRectangle(funTex2, color=BLUE)), Write(dfuncTex), Create(axes2))

        newtonsMethod(func=func2, Dfunc=Dfunc, iterations=40, x0=x0, ax=ax2, time_in_between=0.1, tangentText=tex, lineText=tex2, graphColor=BLUE, text_position=[-4,0,0], numberEquation=False
                      , bool_equation=True, secant_lenght=4)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        def func3(x):
            return x**2-6
        def Dfunc3(x):
            return 2*x
        ax3 = Axes(
            x_range=[-3, 3], y_range=[-7, 4], x_length=10, y_length=7, axis_config={"include_tip": True, "include_numbers": True}
        )
        funTex3 = MathTex(r"f(x)=x^2-6").move_to(5*LEFT+2*DOWN)
        rec5 = SurroundingRectangle(funTex3, color=BLUE)
        self.play(Create(ax3), Write(funTex3), Create(rec5))

        newtonsMethod(func=func3, Dfunc=Dfunc3, iterations=6, x0=x0, ax=ax3, time_in_between=0.1, tangentText=tex, lineText=tex2, graphColor=BLUE, text_position=[-4,-2,0], numberEquation=False
                      , bool_equation=False, secant_lenght=4)
        self.play(*[FadeOut(mob)for mob in self.mobjects])        

class Scene5(Scene):    
    def construct(self):
        rec = Rectangle(color=YELLOW, height=5, width=2)

        self.play(Create(rec))
        self.wait(2)
        self.play(Uncreate(rec))
