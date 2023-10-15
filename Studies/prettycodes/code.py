from manim import *
import argparse
parser=argparse.ArgumentParser(description='Call manim to create beautiful code snippets')
parser.add_argument('--theme',choices=['Dark','Light'],default='Dark')
parser.add_argument('--duration',help='Duration of the animation',type=float)
parser.add_argument('--intime',type=float)
parser.add_argument('--outtime',type=float)
parser.add_argument('--file',type=str)
args=parser.parse_args()
theme='vim' if args.theme=='Dark' else 'Default'
in_time=args.intime
out_time=args.outtime
duration=args.duration
file=args.file

class CodeFromFile(Scene):
    def construct(self):
        self.camera.background_color=rgba_to_color([0,0,0,0])
        code_snippet = Code(file_name=file, tab_width=4, background="window",
                             font="Monospace", line_spacing=1,style=theme,
                             generate_html_file=True)
        self.play(Write(code_snippet,run_time=in_time))
        self.wait(duration-(in_time+out_time))
        self.play(Unwrite(code_snippet,out_time))