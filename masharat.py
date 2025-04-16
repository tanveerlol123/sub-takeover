from manim import *

class Squares(Scene):
    def construct(self):

        Rect1 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1).shift(LEFT*5)
        Rect2 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1).move_to([5, 0, 0])


        r1 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r2 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r3 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r4 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r5 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)

        group = VGroup(r1, r2, r3, r4, r5)
        group.arrange()
        group.set_color_by_gradient(BLUE, PURE_GREEN, YELLOW, ORANGE, PURE_RED)

        g2 = VGroup(Rect1, Rect2)

        
        self.play(Write(Rect1))
        self.play(Write(Rect2))

        self.play(Rect2.animate.next_to(Rect1, RIGHT))
        self.play(ReplacementTransform(g2, group))

        s1 = SurroundingRectangle(group, color=WHITE)
        s2 = SurroundingRectangle(s1, color=WHITE)

        self.play(Write(s1))
        self.play(Write(s2))

        t = Text("1 2 3 4 5", font = "Arial").next_to(s2, UP, buff = 0.3).scale(1.5)
        self.play(Write(t))

        self.play(Indicate(t[0], color = BLUE), Indicate(r1, color = BLUE, scale_factor = 0.3)) 
        self.play(Indicate(t[1], color = PURE_GREEN), Indicate(r2, color = PURE_GREEN, scale_factor = 0.3)) 
        self.play(Indicate(t[2], color = YELLOW), Indicate(r3, color = YELLOW, scale_factor = 0.3)) 
        self.play(Indicate(t[3], color = ORANGE), Indicate(r4, color = ORANGE, scale_factor = 0.3)) 
        self.play(Indicate(t[4], color = RED), Indicate(r5, color = RED, scale_factor = 0.3)) 

        g3 = VGroup(group, t, s1, s2)

        d = Dot(color = RED)

        self.play(ReplacementTransform(g3, d))
        self.play(d.animate.scale(151))
        self.play(FadeOut(d))

        self.wait(1)
