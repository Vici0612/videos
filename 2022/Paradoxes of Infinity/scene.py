from manim import *


class Scene1(Scene):
    def construct(self):
        netflix = Tex("A trip to infinity", color=BLUE_A, font_size=150)
        infinity = MathTex(r"\infty ",font_size=250)
        tex1 = Tex("Use of infinite small values", color=BLUE_A, font_size=80)
        paradoxTex1 = MathTex(r"\infty + 1 = \infty", font_size=100)
        paradoxTex2 = MathTex(r"1 = 0", font_size=100)

        axes = (
            Axes(
                x_range=(0,10,1),
                x_length=9,
                y_range=(0,20,5),
                y_length=6,
                axis_config={"include_numbers": True, "include_tip": False}
            )
            .to_edge(DL)
            .set_color(GREY)
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        func = axes.plot(
            lambda x: 0.1 * (x-2) * (x-5) * (x-7) + 7,
            color=BLUE
        )

        x = ValueTracker(7)
        dx = ValueTracker(2)

        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x.get_value(),
                graph=func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dx",
                dy_label="dy",
                secant_line_color=GREEN,
                secant_line_length=8,

            )
        )   
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(), func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                axes.c2p(
                    (x).get_value() + dx.get_value(),
                    func.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )
        dotsSecant = (VGroup(dot1, dot2, secant))

        self.play(Write(netflix), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(netflix, infinity))
        self.wait(2)
        self.play(ReplacementTransform(infinity, paradoxTex1))
        self.wait(2)
        self.play(ReplacementTransform(paradoxTex1, paradoxTex2))
        self.wait(2)
        self.play(ReplacementTransform(paradoxTex2, tex1))
        self.play(tex1.animate.shift(3.25*UP))
        self.play(Create(axes))
        self.play(Create(axes_labels))
        self.play(Create(func))
        self.wait(2)
        self.play(Create(dotsSecant))
        self.wait(2)
        self.play(dx.animate.set_value(0.001), run_time=8)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=5)
        self.wait(2)
        self.play(Uncreate(axes_labels))
        self.play(Uncreate(dotsSecant))
        self.play(Uncreate(axes))
        self.play(Uncreate(func))
        self.play(Uncreate(tex1))
        self.wait(2)

class Scene2(Scene):
    def construct(self):
        circle0 = Circle(radius=3, color=RED)
        line1 = Line(LEFT*3, RIGHT*3)
        line2 = Line(DOWN*3, UP*3)
        smallerCircle = Circle(radius=1, color=WHITE)
        angleAmount = DecimalNumber(360, unit="^{\circ}").next_to(smallerCircle, UR*0.1)
        circleAngle = VGroup(circle0, line1, line2, smallerCircle, angleAmount)

        circle1 = Circle(radius=1.5, color=GREEN).shift(3*RIGHT)
        circleLine = Line(start=[-2,0,0], end=[2,0,0], color=GREEN).shift(3*RIGHT)

        cross1 = Cross(stroke_color=RED, stroke_width=4).shift(3*LEFT).scale(2)
        cross2 = Cross(stroke_color=RED, stroke_width=4).shift(3*RIGHT).scale(2)
        crosses = VGroup(cross1, cross2)

        self.play(Create(circle0))
        self.wait(2)
        self.play(Create(line1))
        self.play(Create(line2))
        self.wait(2)
        self.play(Create(smallerCircle))
        self.play(Write(angleAmount))
        self.wait(2)
        self.play(circleAngle.animate.shift(3*LEFT).scale(0.5))
        self.wait(2)
        self.play(Create(circleLine))
        self.wait(2)
        self.play(ReplacementTransform(circleLine, circle1))
        self.wait(2)
        self.play(Create(crosses))
        self.wait(2)

class Scene3(Scene):
    def construct(self):

        numPlane = NumberPlane()
        numPlane.add_coordinates()
        iLine1 = Line(start=[0,1,0], end=[-3,0,0])
        iLine2 = Line(start=[3,-3,0], end=[6,3,0])

        dot1 = Dot(point=[0,1,0])
        dot2 = Dot(point=[3,-3,0])
        dot3 = Dot(point=[-3,-3,0])
        dots = VGroup(dot1, dot2, dot3)

        line1 = always_redraw(
            lambda: Line(start=dot1.get_center(), end=dot2.get_center())
        )
        line2 = always_redraw(
            lambda: Line(start=dot2.get_center(), end=dot3.get_center())
        )
        line3 = always_redraw(
            lambda: Line(start=dot1.get_center(), end=dot3.get_center())
        )

        lines = VGroup(line1, line2, line3)
            
        angle1 = always_redraw(
            lambda: Angle(line1, line2, quadrant=(-1,1), radius=0.75)
        )
        angle2 = always_redraw(
            lambda: Angle(line3, line2, quadrant=(-1,-1), other_angle=True, radius=0.75)
        )
        angle3 = always_redraw(
            lambda: Angle(line3, line1, radius=0.75)
        )
        
        angles = VGroup(angle2, angle1, angle3)
        
        alpha = always_redraw(
            lambda: MathTex(r"\alpha", color=GREEN).next_to(angle1, UR)
        )
        beta = always_redraw(
            lambda: MathTex(r"\beta", color=RED).next_to(angle2, UR)
        )
        gamma = always_redraw(
            lambda: MathTex(r"\gamma", color=BLUE).next_to(angle3, UR)
        )

        angleNames = VGroup(alpha, beta, gamma)

        triangleEquation = MathTex(r"\alpha + \beta + \gamma = 180^{\circ}", font_size=70).shift(3*UP)
        triangleEquation[0][0:1].set_color(GREEN)
        triangleEquation[0][2:3].set_color(RED)
        triangleEquation[0][4:5].set_color(BLUE)

        self.play(Create(dots))
        self.play(Create(lines))
        self.play(Create(angles))
        self.play(Create(angleNames))
        self.play(Write(triangleEquation))
        self.wait(2)
        self.play(MoveAlongPath(dot1, iLine1), run_time=4)
        self.wait(2)
        self.play(MoveAlongPath(dot2, iLine2), run_time=4)
        self.wait(2)
        self.play(FadeOut(lines, dots, angles, triangleEquation, angleNames))
        self.wait(2)

        #second passage 

        numberOfSidesTex = Tex("Number of Sides: ", font_size=100).shift(3*UP)
        numberOfSides = MathTex(r"4", font_size=100).next_to(numberOfSidesTex, RIGHT)
        numberOfSides2 = MathTex(r"5", font_size=100).next_to(numberOfSidesTex, RIGHT)
        numberOfSides3 = MathTex(r"6", font_size=100).next_to(numberOfSidesTex, RIGHT)

        numberOfSides8 = MathTex(r"8", font_size=100).next_to(numberOfSidesTex, RIGHT)
        numberOfSides15 = MathTex(r"15", font_size=100).next_to(numberOfSidesTex, RIGHT)
        numberOfSides20 = MathTex(r"20", font_size=100).next_to(numberOfSidesTex, RIGHT)
        numberOfSidesInfinity = MathTex(r"\infty", font_size=100).next_to(numberOfSidesTex, RIGHT)

        square = Square(side_length=3, color=BLUE)

        pentagon = RegularPolygon(n=5).scale(1.5)
        hexagon = RegularPolygon(n=6).scale(1.5)
        polygon8 = RegularPolygon(n=8).scale(1.5)
        polygon15 = RegularPolygon(n=15).scale(1.5)
        polygon20 = RegularPolygon(n=20).scale(1.5)
        polygonInfinity = RegularPolygon(n=1000).scale(2)

        setText = MathTex(r"\mathbb{N}= 1;2;3;4;5;6 ...", font_size=100)
        

        self.play(Write(numberOfSidesTex))
        self.play(Write(numberOfSides))
        self.wait(2)
        self.play(Create(square))
        self.wait(2)
        self.play(ReplacementTransform(square, pentagon), ReplacementTransform(numberOfSides, numberOfSides2))
        self.wait(2)
        self.play(ReplacementTransform(pentagon, hexagon), ReplacementTransform(numberOfSides2, numberOfSides3))
        self.wait(2)
        self.play(ReplacementTransform(hexagon, polygon8), ReplacementTransform(numberOfSides3, numberOfSides8))
        self.wait(2)
        self.play(ReplacementTransform(polygon8, polygon15), ReplacementTransform(numberOfSides8, numberOfSides15))
        self.wait(2)
        self.play(ReplacementTransform(polygon15, polygon20), ReplacementTransform(numberOfSides15, numberOfSides20))
        self.wait(2)
        self.play(ReplacementTransform(polygon20, polygonInfinity), ReplacementTransform(numberOfSides20, numberOfSidesInfinity))
        self.wait(2)
        self.play(Indicate(polygonInfinity), Indicate(numberOfSidesInfinity))
        self.wait(2)
        self.play(FadeOut(numberOfSidesTex, numberOfSidesInfinity, polygonInfinity))
        self.wait(2)
        self.play(Write(setText))
        self.wait(2)
        self.play(FadeOut(setText))
        self.wait(2)
        
class Scene4(Scene):
    def construct(self):
        setN = MathTex(r"\mathbb{N} =\left\{ 1,2,3,4,5,... \right\}", font_size=100).shift(2.5*UP)
        square1 = Square(side_length=1, color=BLUE)
        tex1 = MathTex(r"2").move_to(square1.get_center())
        square2 = square1.copy().shift(3*LEFT)
        tex2 = MathTex(r"1").move_to(square2.get_center())
        square3 = square1.copy().shift(3*RIGHT)
        tex3 = MathTex(r"3").move_to(square3.get_center())

        squares = VGroup(square1, square2, square3, tex1, tex2, tex3).scale(2)

        setI = MathTex(r"I^{2} = \left\{x:x\in \mathbb{N},i\in \mathbb{N},x=i^{2} \right\} =\left\{ 1,4,9,16,25,... \right\}",
                font_size=50).shift(1*DOWN)


        texN = Tex("1", "2", "3", "4", "5", "...").arrange(RIGHT, buff=2).shift(2*UP)
        texI = Tex("1", "4", "9", "16", "25", "...").arrange(RIGHT, buff=2).shift(2*DOWN)

        d_arrow1 = DoubleArrow(start=texN[0].get_center(), end=texI[0].get_center(), tip_length=0.2,color=RED)
        d_arrow2 = DoubleArrow(start=texN[1].get_center(), end=texI[1].get_center(), tip_length=0.2, color=RED)
        d_arrow3 = DoubleArrow(start=texN[2].get_center(), end=texI[2].get_center(), tip_length=0.2, color=RED)
        d_arrow4 = DoubleArrow(start=texN[3].get_center(), end=texI[3].get_center(), tip_length=0.2, color=RED)
        d_arrow5 = DoubleArrow(start=texN[4].get_center(), end=texI[4].get_center(), tip_length=0.2,color=RED)

        arrows1 = VGroup(d_arrow1, d_arrow2, d_arrow3, d_arrow4, d_arrow5)
         

        self.play(Write(setN))
        self.wait(2)
        self.play(Create(squares))
        self.wait(2)
        self.play(Uncreate(squares))
        self.wait(2)
        self.play(setN.animate.shift(1.5*DOWN).scale(0.5), Write(setI))
        self.wait(2)
        self.play(Uncreate(setN), Uncreate(setI))
        self.wait(2)
        self.play(Write(texN), Write(texI))
        self.wait(2)
        self.play(Create(arrows1), run_time=3)
        self.wait(2)
        self.play(Uncreate(texI), Uncreate(texN), Uncreate(arrows1))
        self.wait(2)

        #part 2
        texN2 = Tex("1", "2", "3", "4", "5", "...").arrange(RIGHT, buff=2).shift(2*UP)
        texE = Tex("2", "4", "6", "8", "10", "...").arrange(RIGHT, buff=2).shift(2*DOWN)

        arrow1 =  always_redraw(lambda: DoubleArrow(start=texN2[0].get_center(), end=texE[0].get_center(), tip_length=0.2,color=RED))
        arrow2 = always_redraw(lambda: DoubleArrow(start=texN2[1].get_center(), end=texE[1].get_center(), tip_length=0.2, color=RED))
        arrow3 = always_redraw(lambda: DoubleArrow(start=texN2[2].get_center(), end=texE[2].get_center(), tip_length=0.2, color=RED))
        arrow4 = always_redraw(lambda: DoubleArrow(start=texN2[3].get_center(), end=texE[3].get_center(), tip_length=0.2, color=RED))
        arrow5 = always_redraw(lambda: DoubleArrow(start=texN2[4].get_center(), end=texE[4].get_center(), tip_length=0.2,color=RED))

        times2 = MathTex(r"\cdot 2", color=RED)
        times2_1 = always_redraw(
            lambda: times2.copy().next_to(arrow1, RIGHT))
        times2_2 = always_redraw(
            lambda: times2.copy().next_to(arrow2, RIGHT))
        times2_3 = always_redraw(
            lambda: times2.copy().next_to(arrow3, RIGHT))
        times2_4 = always_redraw(
            lambda: times2.copy().next_to(arrow4, RIGHT))
        times2_5 = always_redraw(
            lambda: times2.copy().next_to(arrow5, RIGHT))

        arrows2 = VGroup(arrow1, arrow2, arrow3, arrow4, arrow5, times2_1, times2_2, times2_3, times2_4, times2_5)


        self.play(Write(texN2), Write(texE))
        self.wait(2)
        self.play(Create(arrows2), run_time=3)
        self.wait(2)
        self.play(texE.animate.shift(1.5*RIGHT))
        self.wait(2)
        self.play(texE.animate.shift(1.5*LEFT))
        self.wait(2)

class Scene5(Scene):

    def construct(self):

        title = Tex("Divergent Series", font_size=120, color=BLUE_A).shift(2.75*UP)
        finalEquation = MathTex(r"1+2+4+8...=-1", font_size=70)
        finalEquation2 = MathTex(r"1+2+4+8...=-1", font_size=70)
        questionMark = Tex("?", font_size=150)

        X = MathTex(r"x=1+2+4+8...").shift(1*UP)
        twoX = MathTex(r"2x=2+4+8...").next_to(X, DOWN, buff=0.5)
        twoXPlusOne = MathTex(r"2x+1=1+2+4+8...").next_to(twoX, DOWN, buff=0.5)
        twoXPlusOneEqualToX = MathTex(r"2x+1=x").next_to(twoXPlusOne, DOWN, buff=0.5)
        xEqualToNegativeOne = MathTex(r"x=-1").next_to(twoXPlusOneEqualToX, DOWN, buff=0.5)

        rectangle = Rectangle(height=1, width=2, color=RED).move_to(xEqualToNegativeOne.get_center())
        rectangle2 = Rectangle(height=1, width=5, color=RED).move_to(X.get_center())

        self.play(Write(title))
        self.wait(2)
        self.play(Write(finalEquation), run_time=5)
        self.wait(2)
        self.play(ReplacementTransform(finalEquation, questionMark))
        self.wait(2)
        self.play(ReplacementTransform(questionMark, X))
        self.wait(2)
        self.play(Write(twoX))
        self.wait(2)
        self.play(Write(twoXPlusOne))
        self.wait(2)
        self.play(Write(twoXPlusOneEqualToX))
        self.wait(2)
        self.play(Write(xEqualToNegativeOne))
        self.wait(2)
        self.play(Create(rectangle), Create(rectangle2))
        self.wait(2)
        self.play(Uncreate(X), Uncreate(twoX), Uncreate(twoXPlusOne), Uncreate(twoXPlusOneEqualToX), Uncreate(xEqualToNegativeOne), Uncreate(rectangle), Uncreate(rectangle2))
        self.wait(2)
        self.play(Write(finalEquation2.scale(1.5)))
        self.play(Indicate(finalEquation2))
        self.wait(2)

class Scene6(Scene):
    def construct(self):

        infiniteSet = MathTex(r"x=1+2+4+8...", font_size=80)
        rectangle = Rectangle(height=4.5, width=9, color=BLUE).shift(1*DOWN)

        A = MathTex(r"A").next_to(rectangle, DL*0.1)
        B = MathTex(r"B").next_to(rectangle, UL*0.1)
        C = MathTex(r"C").next_to(rectangle, UR*0.1)
        D = MathTex(r"D").next_to(rectangle, DR*0.1)
        letters = VGroup(A,B,C,D)

        abLine = Line(start=rectangle.get_bottom(), end=rectangle.get_top(), color=RED).shift(rectangle.width*0.5*LEFT)
        bcLine = Line(start=rectangle.get_left(), end=rectangle.get_right(), color=GREEN).shift(rectangle.height*0.5*UP)
        abTex = MathTex(r"\left| AB \right|", color=RED).next_to(abLine, LEFT)
        bcTex = MathTex(r"\left| BC \right|", color=GREEN).next_to(bcLine, UP)
        lines = VGroup(abLine, bcLine, abTex, bcTex)

        equation = MathTex(r"\cdot 2=").shift(3*UP)
        abTexC = abTex.copy()
        bcTexC = bcTex.copy()

        diagonal = Line(start=rectangle.get_bottom() + rectangle.get_left(), end=rectangle.get_right() + rectangle.get_top(),
                        color = ORANGE).shift(1*UP)

        areaEquation = MathTex(r"ABC = CDA").shift(3*UP)


        cross = Cross(stroke_color=RED, stroke_width=4).move_to(areaEquation.get_center())


        self.play(Write(infiniteSet))
        self.wait(2)
        self.play(ReplacementTransform(infiniteSet, rectangle), Write(letters))
        self.wait(2)
        self.play(Create(lines))
        self.play(FadeIn(abTexC), FadeIn(bcTexC))
        self.wait(2)
        self.play(Write(equation), abTexC.animate.next_to(equation, LEFT), bcTexC.animate.next_to(equation, RIGHT))
        self.wait(2)
        self.play(GrowFromEdge(diagonal, DOWN), FadeOut(abTexC), FadeOut(bcTexC),ReplacementTransform(equation, areaEquation))
        self.wait(2)
        self.play(Create(cross))
        self.wait(2)
        self.play(FadeOut(areaEquation), FadeOut(cross), FadeOut(lines))
        self.wait(2)

        #second halft

        rec =   Rectangle(height=2.25, width=4.5, color=BLUE).shift(2.125*DOWN+2.25*LEFT)
        rec2 = rec.copy().scale(0.5).shift(0.55*DOWN+1.125*LEFT)
        rec3 = rec.copy().scale(1.5).shift(0.55*UP+1.125*RIGHT)
        rec4 = rec2.copy().scale(0.5).shift(0.275*DOWN+0.5625*LEFT)

        recs = VGroup(rec,rec2, rec3, rec4)


        eText = MathTex(r"E").next_to(rec, UL*0.5)
        fText = MathTex(r"F").next_to(rec, UR*0.5)
        gText = MathTex(r"G").next_to(rec, DR)

        efText = MathTex(r"\left| EF \right|", color= RED).next_to(rec, UP)
        egText = MathTex(r"\left| FG \right|", color= GREEN).next_to(rec, RIGHT)
        efLine = Line(start=rec.get_left(), end=rec.get_right(), color = RED).shift(1.125*UP)
        egLine = Line(start=rec.get_bottom(), end=rec.get_top(), color = GREEN).shift(2.25*RIGHT)

        lines2 = VGroup(efText, egText, efLine, egLine)

        
        lineSegmentEquation = MathTex(r"\cdot\frac{1}{2}=").shift(3*UP)
        ef = efText.copy()
        eg = egText.copy()

        abc = MathTex(r"ABC").next_to(lineSegmentEquation, LEFT) 
        acd = MathTex(r"ACD").next_to(lineSegmentEquation, RIGHT)

        equal = MathTex(r"ABC = ACD").shift(3*UP)
        notEqual = MathTex(r"ABC \neq ACD").shift(2*UP)

        self.play(Create(recs), Write(eText), Write(fText), Write(gText))
        self.wait(2)
        self.play(Create(lines2))
        self.wait(2)
        self.play(Write(lineSegmentEquation), ef.animate.next_to(lineSegmentEquation, LEFT), eg.animate.next_to(lineSegmentEquation, RIGHT))
        self.wait(2)
        self.play(Indicate(efLine))
        self.wait(2)
        self.play(Indicate(egLine))
        self.wait(2)
        self.play(ReplacementTransform(ef, abc), ReplacementTransform(eg, acd))
        self.wait(2)
        self.play(FadeOut(abc), FadeOut(acd), Write(equal), Write(notEqual), FadeOut(lineSegmentEquation))
        self.wait(2)

class Thumbnail(Scene):
    def construct(self):

        finalEquation = MathTex(r"1+2+4+8...=-1", font_size=120)

        self.add(finalEquation)