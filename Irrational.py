from manim import *

class Intro(Scene):
    def construct(self):

        text1 = Tex("Prove that an irrational number like ", font_size=45)
        pi = MathTex(r"\pi,e,\sqrt2", font_size=55)
        text2 = Tex("to the power of an irrational number is equal to a rational number.", font_size=45)

        equation1 = MathTex(r"\ irr^{irr}=rat", font_size=80)
        equation2 = MathTex(r"\ \pi^{\pi}=?", font_size=80)
        equation3 = MathTex(r"\ \pi^{\pi}=36.4621596072079...", font_size=80)

        self.play(Write(VGroup(text1, pi, text2).arrange(DOWN)), run_time=6)
        self.wait(2)
        self.play(FadeOut(text1,text2), run_time=2)
        self.play(ReplacementTransform(pi, equation1), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(equation1, equation2), run_time=2)
        self.wait(2)
        self.play(Transform(equation2, equation3))
        self.wait(2)
        self.play(FadeOut(equation2), run_time=2)
        self.wait(2)

class Scene2(Scene):
    def construct(self):

        heading = Tex("Law of excluded middle", color=BLUE_A, font_size=90)
        text1 = Tex("?", font_size=200)
        text2 = MathTex(r"2=0", color=RED, font_size=80)
        text3 = MathTex(r"2\neq 0", color=GREEN, font_size=80)

        equation1 = MathTex(r"\ irr^{irr}=irr", font_size=80)
        equation2 = MathTex(r"\ irr^{irr}=rat", font_size=80)         


        self.play(Write(heading), run_time=2)
        self.play(heading.animate.shift(3*UP))
        self.wait(2)
        self.play(Write(text1))
        self.wait(2)
        self.play(Transform(text1, VGroup(text2,text3).arrange(DOWN)), run_time=2)
        self.wait(2)
        self.play(FadeOut(text1,text2), run_time=0.000000001)
        self.play(ReplacementTransform(VGroup(text2,text3).arrange(DOWN), equation1))
        self.wait(2)
        self.play(ReplacementTransform(equation1, equation2))
        self.wait(2)
        self.play(FadeOut(heading, equation2))
        self.wait(2)


class Scene3(Scene):
    def construct(self):
        
        #first half
        text1 = MathTex(r"2", font_size=80)
        text2 = MathTex(r"\sqrt2", font_size=80)
        text2Half = text2.copy()
        text3 = Tex("irrational", font_size=80).shift(4.75*RIGHT)
        text4 = MathTex(r"\sqrt2 \neq \frac{71}{50}", font_size=80)
        text5 = MathTex(r"\sqrt2 = 1.41421356237...", font_size=80)

        circle = Circle(radius=1)
        arrow = Arrow(start=LEFT, end=RIGHT, color=RED).shift(2*RIGHT)
        rectangle = Rectangle(width=4.25, height=1.3, color=RED).shift(3*UP+4.5*LEFT)


        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1, text2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text5))
        self.wait(2)
        self.play(ReplacementTransform(text5, text4))
        self.wait(2)
        self.play(ReplacementTransform(text4, text2Half))
        self.play(Create(circle))
        self.play(Indicate(circle))
        self.wait(2)
        self.play(Create(arrow))
        self.wait(2)
        self.play(Write(text3))
        self.play(text2Half.animate().shift(3*UP+6*LEFT).scale(0.5),
                    circle.animate().shift(3*UP+6*LEFT).scale(0.5),
                    arrow.animate().shift(3*UP+7*LEFT).scale(0.5),
                    text3.animate().shift(3*UP+8.25*LEFT).scale(0.5),
                    Create(rectangle))
        self.wait(2)



        #second half
        a = MathTex(r"a = \sqrt2")
        b = MathTex(r"b= \sqrt2")
        equation1 = MathTex("a^b = rational").shift(1*DOWN)
        equation2 = MathTex("a^b = irratinal").shift(1*DOWN) 
        rec1 = Rectangle(height=2.75, width= 3.25,stroke_color=GREEN).shift(0.5*DOWN)
        rec2 = Rectangle(height=2.75, width= 3.25,stroke_color=RED).shift(0.5*DOWN)
        ab = VGroup(a, b).arrange(DOWN)

        self.play(Write(ab))
        self.wait(2)
        self.play(Write(equation1))
        self.wait(2)
        self.play(Create(rec1))
        self.wait(2)
        self.play(ReplacementTransform(equation1,equation2))
        self.wait(2)
        self.play(FadeOut(rec1), FadeIn(rec2), run_time=0.0000001)
        self.play(Indicate(rec2))
        self.wait(2)
        self.play(FadeOut(ab, equation2, rec2))
        self.wait(2)


        #third half
        aPrime = MathTex(r"a' = \sqrt2^{\sqrt2}")
        bPrime = MathTex(r"b' = \sqrt2")
        abPrime = VGroup(aPrime, bPrime).arrange(DOWN)
        
        equation1 = MathTex(r"a^b = \sqrt2^{\sqrt2^{\sqrt2}}")
        equation2 = MathTex(r"a^b = \sqrt2^2")
        equation3 = MathTex(r"a^b = 2")
        equations = VGroup(equation1, equation2, equation3).arrange(DOWN)

        
        self.play(Write(abPrime))
        self.wait(2)
        self.play(abPrime.animate().shift(2.5*UP))
        self.play(Write(equations))
        self.wait(2)

class Thanks(Scene):
    def construct(self):
        heading = Tex("Thanks for watching", color=BLUE_A, font_size=90).shift(3*UP)

        self.play(Write(heading), run_time=2)
        self.wait(2)

class Thumbnail(Scene):
    def construct(self):

        equation1 = MathTex(r"\sqrt2^{\sqrt2^{\sqrt2}}", font_size=200)

        self.add(equation1)






class MyBeautifulGraph(Scene):
    def construct(self):
        axes = Axes()
        x = [0, 1, 2, 3, 4]
        y = [1, 2, 4, 2, 3]
        line = axes.plot_line_graph(x, y, add_vertex_dots=False)
        self.add(axes, line)
