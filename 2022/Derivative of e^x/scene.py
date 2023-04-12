from manim import *
import math

class Scene1(Scene):
    def construct(self):

        imgLE = ImageMobject("LE").scale(0.4).move_to(4*LEFT)
        texLE = Tex("Leonhard Euler(1707-1783)", font_size=35).next_to(imgLE, DOWN)

        imgCG = ImageMobject("CG").scale(0.4).move_to(4*RIGHT)
        texCG = Tex("Christian Goldbach(1690-1764)", font_size=35).next_to(imgCG, DOWN)

        arrow = CurvedArrow(imgLE.get_right(), imgCG.get_left(), color=YELLOW).flip(RIGHT).shift(1.5*UP)

        imgLetter = ImageMobject("letter").scale(0.2).move_to(arrow.get_left())
        e = always_redraw(lambda: Text("e", color=RED, weight=ULTRAHEAVY).move_to(imgLetter.get_center()))

        self.play(FadeIn(imgLE), Write(texLE), FadeIn(imgCG), Write(texCG))
        self.wait(2)
        self.play(Create(arrow), FadeIn(imgLetter), Write(e))
        self.wait(2)
        self.play(MoveAlongPath(imgLetter, arrow), run_time=4)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait(2)

        eQuestion = MathTex("e= ?", font_size=120)
        eValue = MathTex("e=2.718281...", font_size=120)
        definitionQuestion = MathTex("Definition = ???", font_size=120)
        eEqual = MathTex("e= ", font_size=120)
        lightBulb = ImageMobject("lightbulb.png").next_to(eEqual, RIGHT).scale(0.5)
        derivative = MathTex(r"\ v(t)=\lim_{dt \to 0}\frac{d}{dt}(s(t))", font_size = 120)

        self.play(Write(eQuestion))
        self.wait(2)
        self.play(ReplacementTransform(eQuestion, eValue))
        self.wait(2)
        self.play(ReplacementTransform(eValue, definitionQuestion))
        self.wait(2)
        self.play(ReplacementTransform(definitionQuestion, eEqual), FadeIn(lightBulb))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait(2)
        self.play(Write(derivative))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait(2)

        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False, "include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        def func(x):
            return 2**x
        graph = ax.plot(func, color=GREEN)

        functionTex = MathTex("f(x)=2^x", color=GREEN).shift(2*RIGHT)

        x = ValueTracker(5)
        dx = ValueTracker(1)

        secant = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=x.get_value(),
                graph=graph,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dx",
                dy_label="dy",
                secant_line_color=BLUE,
                secant_line_length=8,

            )
        )   
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax.c2p(x.get_value(), graph.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                ax.c2p(
                    (x).get_value() + dx.get_value(),
                    graph.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )

        self.play(Create(ax), Write(labels))
        self.play(Create(graph), Write(functionTex))
        self.wait(2)
        self.play(Create(secant), Create(dot1), Create(dot2), functionTex.animate().shift(1.5*RIGHT))
        self.play(x.animate.set_value(0), dx.animate.set_value(0.0001), run_time=8)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene2(Scene):
    def construct(self):
        
        centuryTitle = Text("17th Century", font_size = 100, color=BLUE_A)

        imgNE = ImageMobject("NewIMG").scale(0.2).move_to(4*LEFT)
        texNE = Tex("Sir Isaac Newton(1643–1727)", font_size=35).next_to(imgNE, DOWN)

        imgLE = ImageMobject("LeipIMG").scale(0.4).move_to(4*RIGHT)
        texLE = Tex("Gottfried Wilhelm Leibniz(1646–1716)", font_size=35).next_to(imgLE, DOWN)

        self.play(Write(centuryTitle))
        self.wait(2)
        self.play(centuryTitle.animate().move_to(3*UP))
        self.wait(2)
        self.play(FadeIn(imgNE), Write(texNE), FadeIn(imgLE), Write(texLE))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait(2)

        sAXIS = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False, "include_numbers": True}
        ).scale(0.3).shift(4.5*LEFT)
        labelsS = sAXIS.get_axis_labels(x_label="t", y_label="s(t)")
        def funcS(x):
            return x**2
        graphS = sAXIS.plot(funcS, color=ORANGE)

        
        vAXIS = Axes(
            x_range=[0, 10], y_range=[0, 50, 5], axis_config={"include_tip": False, "include_numbers": True}
        ).scale(0.3)
        labelsV = vAXIS.get_axis_labels(x_label="t", y_label="v(t)")
        def funcV(x):
            return 2*x
        graphV = vAXIS.plot(funcV, color=ORANGE)


        aAXIS = Axes(
            x_range=[0, 10], y_range=[0, 10, 1], axis_config={"include_tip": False, "include_numbers": True}
        ).scale(0.3).shift(4.5*RIGHT)
        labelsA = aAXIS.get_axis_labels(x_label="t", y_label="a(t)")
        def funcA(x):
            return 2
        graphA = aAXIS.plot(funcA, color=ORANGE)



        distanceTime = VGroup(sAXIS, labelsS, graphS)
        velocity = VGroup(vAXIS, labelsV, graphV)
        acceleration = VGroup(aAXIS, labelsA, graphA)        


        self.play(Create(distanceTime), Create(velocity), Create(acceleration), run_time=4)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait(2)
        
        sCarAxis = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False, "include_numbers": True}
        )
        labelsScar = sCarAxis.get_axis_labels(x_label="t", y_label="s(t)")
        def funcSCar(x):
            return x**2
        graphSCar = sCarAxis.plot(funcSCar, color=BLUE)

        distanceTimCar = VGroup(sCarAxis, labelsScar)

        path = VMobject(color=BLUE)
        dot = Dot().move_to(graphSCar.get_start())
        path.set_points_as_corners([dot.get_center(), dot.get_center()]).move_to(graphSCar.get_start())
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        carIMG = always_redraw(lambda: ImageMobject("Car").scale(0.3).move_to(dot.get_center()))

        self.play(Create(distanceTimCar))
        self.wait(2)
        self.play(FadeIn(carIMG))
        self.wait(2)
        self.add(path)
        self.play(MoveAlongPath(dot, graphSCar), run_time=4)
        self.play(FadeOut(path), run_time=0.0001)
        self.play(FadeIn(graphSCar), run_time=0.001)
        self.wait(2)

        defineMotionTex = Tex("Define the motion?", font_size=80).shift(2*LEFT + 2*UP)

        self.play(Write(defineMotionTex))
        self.wait(2)
        self.play(FadeOut(carIMG),FadeOut(graphSCar), FadeOut(dot))
        self.wait(2)
        
class Scene2_5(Scene):
    def construct(self):


        sCarAxis = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False, "include_numbers": True}
        )
        labelsScar = sCarAxis.get_axis_labels(x_label="t", y_label="s(t)")
        def funcSCar(x):
            return 2*x
        graphSCar = sCarAxis.plot(funcSCar, color=BLUE)

        distanceTimCar = VGroup(sCarAxis, labelsScar)

        path = VMobject(color=BLUE)
        dot = Dot().move_to(graphSCar.get_start())
        path.set_points_as_corners([dot.get_center(), dot.get_center()]).move_to(graphSCar.get_start())
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        carIMG = always_redraw(lambda: ImageMobject("Car").scale(0.3).move_to(dot.get_center()))
        defineMotionTex = Tex("Define the motion?", font_size=80).shift(2*LEFT + 2*UP)

        self.add(defineMotionTex)
        self.add(distanceTimCar)
        self.wait(2)
        self.play(FadeIn(carIMG))
        self.wait(2)
        self.add(path)
        self.play(MoveAlongPath(dot, graphSCar), run_time=4)
        self.play(FadeOut(path), run_time=0.0001)
        self.play(FadeIn(graphSCar), run_time=0.001)
        self.wait(2)

class Scene2_5_5(Scene):

    def construct(self):
        sCarAxis = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False, "include_numbers": True}
        )
        labelsScar = sCarAxis.get_axis_labels(x_label="t", y_label="s(t)")
        def funcSCar(x):
            return (1/2)*x**2
        graphSCar = sCarAxis.plot(funcSCar, color=BLUE)

        distanceTimCar = VGroup(sCarAxis, labelsScar)

        path = VMobject(color=BLUE)
        dot = Dot().move_to(graphSCar.get_start())
        path.set_points_as_corners([dot.get_center(), dot.get_center()]).move_to(graphSCar.get_start())
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        carIMG = always_redraw(lambda: ImageMobject("Car").scale(0.3).move_to(dot.get_center()))
        defineMotionTex = Tex("Define the motion?", font_size=80).shift(2*LEFT + 2*UP)

        self.add(defineMotionTex)
        self.add(distanceTimCar)
        self.wait(2)
        self.play(FadeIn(carIMG))
        self.wait(2)
        self.add(path)
        self.play(MoveAlongPath(dot, graphSCar), run_time=4)
        self.play(FadeOut(path), run_time=0.0001)
        self.play(FadeIn(graphSCar), run_time=0.001)
        self.wait(2)

class Scene2_5_5_5(Scene):
    def construct(self):
        sCarAxis = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False, "include_numbers": True}
        )
        ax = Axes(
            x_range=[0, 10], y_range=[0, 10], axis_config={"include_tip": False, "include_numbers": True}
        )
        labelsScar = sCarAxis.get_axis_labels(x_label="t", y_label="s(t)")
        def funcSCar(x):
            return x
        graphSCar = ax.plot(funcSCar, color=BLUE)

        distanceTimCar = VGroup(sCarAxis, labelsScar)

        path = VMobject(color=BLUE)
        dot = Dot().move_to(graphSCar.get_start())
        path.set_points_as_corners([dot.get_center(), dot.get_center()]).move_to(graphSCar.get_start())
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        carIMG = always_redraw(lambda: ImageMobject("Car").scale(0.3).move_to(dot.get_center()))
        defineMotionTex = Tex("Define the motion?", font_size=80).shift(2*LEFT + 2*UP)

        self.add(defineMotionTex)
        self.add(distanceTimCar)
        self.play(Unwrite(defineMotionTex))
        self.wait(2)
        self.play(ReplacementTransform(sCarAxis, ax), Unwrite(labelsScar))
        self.wait(2)
        self.play(FadeIn(carIMG))
        self.wait(2)
        self.add(path)
        self.play(MoveAlongPath(dot, graphSCar), run_time=4)
        self.play(FadeOut(path), run_time=0.0001)
        self.play(FadeIn(graphSCar), run_time=0.001)
        self.wait(2)

        x = ValueTracker(5)
        dx = ValueTracker(1)

        secant = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=x.get_value(),
                graph=graphSCar,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dt",
                dy_label="ds",
                secant_line_color=BLUE,
                secant_line_length=8,

            )
        )   
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax.c2p(x.get_value(), graphSCar.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                ax.c2p(
                    (x).get_value() + dx.get_value(),
                    graphSCar.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )

        dsdtTex = MathTex(r'\frac{ds}{dt} = v(t) = 1 m/s', color=WHITE,  font_size=50).shift(3*LEFT+1*UP)
        def funcV(x):
            return 1
        graphSCar2 = ax.plot(funcV, color=RED)
        vtText = MathTex("v(t)", color=RED).next_to(graphSCar2.get_center(), DOWN)

        self.play(Create(secant), Create(dot1), Create(dot2))
        self.play(dx.animate.set_value(3), run_time=8)
        self.wait(2)
        self.play(Write(dsdtTex))
        self.wait(2)
        self.play(Create(graphSCar2), Write(vtText))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene3(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False, "include_numbers": True}
        )
        def funcSCar(x):
            return x**2
        graphSCar = ax.plot(funcSCar, color=BLUE)

        distanceTimCar = VGroup(ax)

        path = VMobject(color=BLUE)
        dot = Dot().move_to(graphSCar.get_start())
        path.set_points_as_corners([dot.get_center(), dot.get_center()]).move_to(graphSCar.get_start())
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        carIMG = always_redraw(lambda: ImageMobject("Car").scale(0.3).move_to(dot.get_center()))
        stText = MathTex("s(t)", color=BLUE).next_to(graphSCar.get_center(), RIGHT)

        self.add(distanceTimCar)
        self.wait(2)
        self.play(FadeIn(carIMG))
        self.wait(2)
        self.add(path)
        self.play(MoveAlongPath(dot, graphSCar), run_time=4)
        self.play(FadeOut(path), run_time=0.0001)
        self.play(FadeIn(graphSCar), run_time=0.001)
        self.wait(2)
        self.play(Write(stText))
        self.wait(2)

        x = ValueTracker(5)
        dx = ValueTracker(1)

        x2 = ValueTracker(5)
        dx2 = ValueTracker(1)

        secant = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=x.get_value(),
                graph=graphSCar,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dt",
                dy_label="ds",
                secant_line_color=BLUE,
                secant_line_length=0,

            )
        )   
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax.c2p(x.get_value(), graphSCar.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                ax.c2p(
                    (x).get_value() + dx.get_value(),
                    graphSCar.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )

        secant2 = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=x2.get_value(),
                graph=graphSCar,
                dx=dx2.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dt",
                dy_label="ds",
                secant_line_color=GREEN,
                secant_line_length=9,

            )
        )   
        dot12 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax.c2p(x2.get_value(), graphSCar.underlying_function(x2.get_value())))
        )
        dot22 = always_redraw(
             lambda: Dot()
            .scale(0.7)
            .move_to(
                ax.c2p(
                    (x2).get_value() + dx2.get_value(),
                    graphSCar.underlying_function(x2.get_value() + dx2.get_value()),
                )
            )
        )

        secantVGroup = VGroup(secant, dot1, dot2)
        secantVGroup2 = VGroup(secant2, dot12, dot22)

        limitEquation = MathTex(r"\ v(t)=\lim_{dt \to 0}\frac{d}{dt}(s(t))", font_size=60).shift(3*LEFT+2*UP)

        def funVCar(x):
            return 2*x

        graphVCar = ax.plot(funVCar, color=ORANGE)
        vtText = MathTex("v(t)", color=ORANGE).next_to(graphVCar.get_center(), UP)

        self.play(Create(secantVGroup))
        self.wait(2)
        self.play(x.animate.set_value(9), run_time=4)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=4)
        self.play(FadeOut(secantVGroup))
        self.wait(2)
        self.play(Create(secantVGroup2))
        self.wait(2)
        self.play(x2.animate.set_value(9), run_time=4)
        self.wait(2)
        self.play(x2.animate.set_value(1), run_time=4)
        self.wait(2)
        self.play(x2.animate.set_value(5), run_time=4)
        self.wait(2)
        self.play(dx2.animate.set_value(0.00001), run_time=2)
        self.wait(2)
        self.play(x2.animate.set_value(9), run_time=4)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=8) 
        self.play(Write(limitEquation))
        self.wait(2)
        self.play(Create(graphVCar), Write(vtText))
        self.wait(2)

class Scene4(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10, 10], y_range=[-2, 2], axis_config={"include_tip": False, "include_numbers": True}
        )
        axes_labels = ax.get_axis_labels()

        sin_graph = ax.plot(lambda x: np.sin(x),color=BLUE)
        cos_graph = ax.plot(lambda x: np.cos(x), color=RED)
        exponential = ax.plot(lambda x: np.e**x, color=ORANGE) 

        sin_label = ax.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = ax.get_graph_label(cos_graph, label="\\cos(x)", direction=DOWN)

        e_label = ax.get_graph_label(
            exponential, "e^x", x_val=2, direction=RIGHT
        )

        plot = VGroup(sin_graph, cos_graph)
        labels = VGroup(axes_labels, sin_label, cos_label)
        e = VGroup(exponential, e_label)

        matrix = [[1, 1], [0, 2/3]]

        self.play(Create(ax))
        self.play(Create(plot), run_time=8)
        self.play(Create(labels))
        self.wait(2)
        self.play(FadeOut(plot), FadeOut(labels))
        self.wait(2)
        self.play(Create(e), run_time=4)
        self.wait(2)
        self.play(ax.animate.apply_complex_function(np.exp), e.animate.apply_complex_function(np.exp), run_time=5)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene5(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1, 7], y_range=[-1, 24, 4], axis_config={"include_tip": False, "include_numbers": True},

        )
        ax2 = Axes(
            x_range=[-1, 7], y_range=[-1, 24, 4], axis_config={"include_tip": False}

        )
        axes_labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        axes_labels2 = ax.get_axis_labels(x_label="t", y_label=r"M_{A}(t)")

        twoToTheX = ax.plot(lambda x: 2**x, color=GREEN)
        
        twoToTheXTex = MathTex(r"f(x)=2^{x}", color=GREEN).shift(3.5*RIGHT)
        twoToTheTTex = MathTex(r"M_{A}(t)=2^{t}", color=GREEN).move_to(twoToTheXTex)

        self.play(Create(ax), Create(axes_labels))
        self.wait(2)
        self.play(Create(twoToTheX), Write(twoToTheXTex))
        self.wait(2)
        self.play(ReplacementTransform(axes_labels, axes_labels2), ReplacementTransform(twoToTheXTex, twoToTheTTex))
        self.wait(2)

        labels = VGroup()
        braces = VGroup()

        for i in range(5):

            label = (ax.get_graph_label(
 
            graph=twoToTheX,
            label= MathTex(str(2**i)),
            x_val= i,
            dot=True,
            direction=UR,
            color = ORANGE

            ))
            labels.add(label)

        for i in range(4):
            line = Line(labels[i].get_center()+0.2*LEFT, labels[i+1].get_center()+0.2*LEFT)
            braces.add(Brace(line))
            b1 = Brace(line)
            braces.add(MathTex(r"\times 2", color=ORANGE).next_to(b1, DOWN))
            

        derivative = MathTex(r"M_{A}'(t)=\frac{dM^{A}}{dt}").shift(1.5*LEFT)

        x = ValueTracker(5)
        dx = ValueTracker(1)


        secant = always_redraw(
            lambda: ax2.get_secant_slope_group(
                x=x.get_value(),
                graph=twoToTheX,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dt",
                dy_label="ds",
                secant_line_color=BLUE,
                secant_line_length=0,

            )
        )   
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax2.c2p(x.get_value(), twoToTheX.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                ax2.c2p(
                    (x).get_value() + dx.get_value(),
                    twoToTheX.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )

        secantVgroup = VGroup(secant, dot1, dot2)  

        self.play(Write(labels), run_time=6)
        self.wait(2)
        self.play(ReplacementTransform(ax, ax2))
        self.wait(2)
        self.play(Create(braces), run_time=4)
        self.wait(2)
        self.play(FadeOut(labels), FadeOut(braces))
        self.wait(2)
        self.play(Write(derivative))
        self.wait(2)
        self.play(Create(secantVgroup))
        self.wait(2)

class Scene5_5(Scene):
    def construct(self):
        
        ax2 = Axes(
            x_range=[-1, 7], y_range=[-1, 24, 4], axis_config={"include_tip": False}

        )
        axes_labels2 = ax2.get_axis_labels(x_label="t", y_label=r"M_{A}(t)")
        twoToTheX = ax2.plot(lambda x: 2**x, color=GREEN)
        twoToTheTTex = MathTex(r"M_{A}(t)=2^{t}", color=GREEN).shift(3.5*RIGHT)

        derivative = MathTex(r"M_{A}'(t)=\frac{dM^{A}}{dt}").shift(1.5*LEFT)
        
        alles = VGroup(ax2, axes_labels2, twoToTheTTex, twoToTheX, derivative )

        x = ValueTracker(2)
        dx = ValueTracker(1)


        secant = always_redraw(
            lambda: ax2.get_secant_slope_group(
                x=x.get_value(),
                graph=twoToTheX,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dt",
                dy_label="ds",
                secant_line_color=BLUE,
                secant_line_length=0,

            )
        )   
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax2.c2p(x.get_value(), twoToTheX.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                ax2.c2p(
                    (x).get_value() + dx.get_value(),
                    twoToTheX.underlying_function(x.get_value() + dx.get_value()),                )
            )
        )

        secantVgroup = VGroup(secant,dot1, dot2)

        fourToFive = Text("From 4 to 5", t2c={'4':YELLOW}).shift(2.5*LEFT+2*UP)
        fiveToSix = Text("From 5 to 6", t2c={'5':YELLOW}).shift(2.5*LEFT+2*UP)
        sixtoSeven = Text("From 6 to 7", t2c={'6':YELLOW}).shift(2.5*LEFT+2*UP)

        equation1 = MathTex(r"\frac{16Algea}{1Day}").next_to(fourToFive, 1.5*DOWN)
        equation2 = MathTex(r"\frac{32Algea}{1Day}").next_to(fourToFive, 1.5*DOWN)
        equation3 = MathTex(r"\frac{64Algea}{1Day}").next_to(fourToFive, 1.5*DOWN)

        self.add(alles)
        self.play(Create(secantVgroup))
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=4)
        self.wait(2)
        self.play(x.animate.set_value(2), run_time=4)
        self.wait(2)
        self.play(ReplacementTransform(derivative, fourToFive))
        self.wait(2)
        self.play(Write(equation1))
        self.wait(2)
        self.play(ReplacementTransform(fourToFive, fiveToSix), ReplacementTransform(equation1, equation2))
        self.wait(2)
        self.play(ReplacementTransform(fiveToSix, sixtoSeven), ReplacementTransform(equation2, equation3))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene6(Scene):
    def construct(self):
        ax2 = Axes(
            x_range=[-1, 7], y_range=[-1, 24, 4], axis_config={"include_tip": False}

        )
        axes_labels2 = ax2.get_axis_labels(x_label="t", y_label=r"M_{A}(t)")
        twoToTheX = ax2.plot(lambda x: 2**x, color=GREEN)
        twoToTheTTex = MathTex(r"M_{A}(t)=2^{t}", color=GREEN).shift(3.5*RIGHT)

        function = VGroup(ax2, axes_labels2, twoToTheTTex, twoToTheX)

        equation = MathTex(r"M_{A}'(t)=2^t",
            substrings_to_isolate="t"
        ).shift(2*LEFT+1*UP)
        equation.set_color_by_tex("t", YELLOW)

        equation2 = MathTex(r"\frac{2^{t+dt}-2^{t}}{dt}", font_size=60
        ).move_to(equation)

        x = ValueTracker(4)
        dx = ValueTracker(1)


        secant = always_redraw(
            lambda: ax2.get_secant_slope_group(
                x=x.get_value(),
                graph=twoToTheX,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dt",
                dy_label="ds",
                secant_line_color=BLUE,
                secant_line_length=7,

            )
        )   
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax2.c2p(x.get_value(), twoToTheX.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                ax2.c2p(
                    (x).get_value() + dx.get_value(),
                    twoToTheX.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )

        secantVGruop = VGroup(secant, dot1, dot2)

        brace = Brace(equation, sharpness=1)

        tempting = Tex("Tempting...", font_size=40).next_to(brace, DOWN)


        self.play(Create(function))
        self.wait(2)
        self.play(Write(equation))
        self.wait(2)
        self.play(Create(brace), Write(tempting))
        self.wait(2)
        self.play(Create(secantVGruop))
        self.wait(2)
        self.play(x.animate.set_value(2), run_time=4)
        self.wait(2)
        self.play(dx.animate.set_value(0.0000001), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(equation, equation2), Uncreate(brace), Unwrite(tempting))
        self.wait(2)

class Scene7(Scene):
    def construct(self):

        ax2 = Axes(
            x_range=[-1, 7], y_range=[-1, 24, 4], axis_config={"include_tip": False}

        )
        axes_labels2 = ax2.get_axis_labels(x_label="t", y_label=r"M_{A}(t)")
        twoToTheX = ax2.plot(lambda x: 2**x, color=GREEN)
        twoToTheTTex = MathTex(r"M_{A}(t)=2^{t}", color=GREEN).shift(3.5*RIGHT)

        
        alles = VGroup(ax2, axes_labels2, twoToTheTTex, twoToTheX)  
        
        dx = ValueTracker(0.5)

        rects_right = always_redraw(
            lambda: ax2.get_riemann_rectangles(
            twoToTheX,
            x_range=[0, 4],
            dx=dx.get_value(),
            color=(TEAL, BLUE_B, DARK_BLUE),
            input_sample_type="right",
        ))

        self.play(Create(alles))
        self.wait(2)
        self.play(Create(rects_right))
        self.wait(2)
        self.play(dx.animate.set_value(0.025), run_time=4)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene7_5(Scene):
    def construct(self):

        function = MathTex(r"M_{A}(t) = 2^{t}", substrings_to_isolate="t").shift(5*LEFT+3*UP)
        function.set_color_by_tex("t", YELLOW)

        derivative = MathTex(r"\frac{dM}{dt}(t)=\frac{2^{t+dt}-2^{t}}{dt}").scale(1)
        derivative2 = MathTex(r"\frac{dM}{dt}(t)=\frac{2^{dt}+2^{t}-2^{t}}{dt}").scale(1)
        box = Rectangle(width=1.25, height=0.75, color=GREEN).move_to(derivative.get_center() + 0.35*UP + 0.5*RIGHT)
        box2 = Rectangle(width=2, height=0.75, color=GREEN).move_to(derivative.get_center() + 0.35*UP + 0.5*RIGHT)

        additive = Tex("Additive ideas", color=BLUE_A, font_size=70).shift(3*UP+3.5*RIGHT)
        multiplicative = Tex("Multiplicative ideas", color=BLUE_A, font_size=70).move_to(additive.get_center())

        derivative3 = MathTex(r"\frac{dM}{dt}(t) =2t(\frac{2^{dt}-1}{dt})").scale(1)
        dt = MathTex(r"dt\longmapsto 0",).next_to(derivative3, DOWN)

        equation1 = MathTex(r"(\frac{2^{0.1}-1}{0.1}) = 0.71773462536...").scale(1.5)
        equation2 = MathTex(r"(\frac{2^{0.0001}-1}{0.0001}) = 0.693171...").scale(1.5)
        equation3 = MathTex(r"(\frac{2^{0.00000001}-1}{0.00000001}) = 0.6931472...").scale(1.5) 

        twoDerivative =  MathTex(r"M_{A}'(t) = 2^{t} * (0.6931472...)", substrings_to_isolate="t").scale(1.5)
        twoDerivative.set_color_by_tex("t", YELLOW)

        eigthEquation = MathTex((r"\frac{8^{0.00000001}-1}{0.00000001}) =  2.0794...")).scale(1.5)
        eightDerivative =  MathTex(r"M_{A}'(t) = 8^{t} * (2.0794...)", substrings_to_isolate="t").scale(1.5)
        eightDerivative.set_color_by_tex("t", YELLOW)

        arrow = always_redraw(
            lambda: Arrow(start=twoDerivative.get_center(), end=eightDerivative.get_center(), color=RED)
        )
        arrowText = always_redraw(
            lambda: MathTex(r"\times 3", color=RED).next_to(arrow.get_center(), RIGHT)
        )
        arrowVGroup = VGroup(arrow, arrowText)


        self.play(Write(function), Write(derivative))
        self.wait(2)
        self.play(Create(box))
        self.wait(2)
        self.play(ReplacementTransform(derivative, derivative2), ReplacementTransform(box, box2))
        self.wait(2)
        self.play(Write(additive))
        self.wait(2)
        self.play(ReplacementTransform(additive, multiplicative))
        self.wait(2)
        self.play(Uncreate(box2), ReplacementTransform(derivative2, derivative3))
        self.wait(2)
        self.play(Write(dt), FadeOut(multiplicative))
        self.wait(2)
        self.play(ReplacementTransform(derivative3, equation1), Unwrite(dt))
        self.wait(2)
        self.play(ReplacementTransform(equation1, equation2))
        self.wait(2)
        self.play(ReplacementTransform(equation2, equation3))
        self.wait(2)
        self.play(ReplacementTransform(equation3, twoDerivative))
        self.wait(2)
        self.play(FadeOut(function), twoDerivative.animate.shift(function.get_center()+ 2*RIGHT).scale(0.75))
        self.wait(2)
        self.play(Write(eigthEquation))
        self.wait(2)
        self.play(ReplacementTransform(eigthEquation, eightDerivative))
        self.wait(2)
        self.play((eightDerivative.animate.shift(twoDerivative.get_center()+4*DOWN)).scale(0.75))
        self.wait(2)
        self.play(Create(arrowVGroup))
        self.wait(2)
        self.play(Indicate(twoDerivative))
        self.wait(2)
        self.play(Indicate(eightDerivative))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene8(Scene):
    def construct(self):

        equation1 = MathTex(r"\frac{d (a^{t})}{dt} = a^{t}").scale(1.5)

        thereIs = Tex("There is! It's ", font_size=80, color=BLUE).shift(2.5*UP+2*LEFT)
        e = MathTex(" e =  2.71828…", font_size=80, color=RED).next_to(thereIs, RIGHT)

        equation2 = MathTex(r"\frac{d (e^{t})}{dt} = e^{t} * (1.000000...)").scale(1.5)
        equation3 = MathTex(r"\frac{d (e^{t})}{dt} = e^{t}").scale(1.5)

        self.play(Write(equation1))
        self.wait(2)
        self.play(Indicate(equation1))
        self.wait(2)
        self.play(Write(thereIs))
        self.wait(2)
        self.play(Write(e))
        self.wait(2)
        self.play(ReplacementTransform(equation1, equation2))
        self.wait(2)
        self.play(ReplacementTransform(equation2, equation3))
        self.play(Indicate(equation3))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        ax = Axes(
            x_range=[-2, 7, 0.5], y_range=[-1, 50, 10], axis_config={"include_tip": False}

        )
        axes_labels = ax.get_axis_labels(x_label="t", y_label=r"f(t)")
        eToTheX = ax.plot(lambda x: math.e**x, color=GREEN)
        eToTheTTex = MathTex(r"f(t)=e^{t}", color=GREEN).shift(3.5*RIGHT)

        axes = VGroup(ax, axes_labels, eToTheTTex, eToTheX)

        x = ValueTracker(1)
        dx = ValueTracker(0.000000001)

        secant = always_redraw(
            lambda: ax.get_secant_slope_group(
                x = x.get_value(),
                graph=eToTheX,
                dx=dx.get_value(),
                secant_line_color=YELLOW,
                secant_line_length=8,

            )
        )   


        s1 = always_redraw(lambda: MathTex("Slope = e^t").next_to(secant.get_center(), RIGHT))
        equation4 = MathTex(r"\frac{d (e^{t})}{dt} = e^{t} * (1.000000...)").shift(3.5*RIGHT+2*DOWN)

        self.play(Create(axes), run_time=5)
        self.wait(2)
        self.play(Create(secant))
        self.wait(2)
        self.play(Write(s1))
        self.wait(2)
        self.play(x.animate.set_value(3.75), run_time=5)
        self.wait(2)
        self.play(Write(equation4))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Thumbnail(Scene):
    def construct(self):
        ax2 = Axes(
                x_range=[-1, 5], y_range=[-1, 24, 4], axis_config={"include_tip": False}

            )
        twoToTheX = ax2.plot(lambda x: math.e**x, color=YELLOW)
       

            
        alles = VGroup(ax2,  twoToTheX)  

        self.add(alles)

class Thumbnail1(Scene):
    def construct(self):
        text = MathTex(r"\frac{d (e^{t})}{dt} = e^{t} * (1.000000...)", font_size=120)
        
        self.add(text)