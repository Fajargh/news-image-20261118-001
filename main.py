# News-image entry for make.fun news-image-20261118.
# The program writes one image summing up the world's news of
# Wednesday 18 November 2026 to /output/entry.png. The image is
# a newspaper front page: the date 18 November 2026 at the top,
# the main story (US strikes on Iran and the Kerch Bridge falling),
# and the day's other big stories (Xi, Putin and Trump meeting in
# Shenzhen; Peltola winning Alaska; the Ebola surge in Congo;
# the US losing measles-free status; the Siberia plane crash;
# Cyclone Xavier). The image itself is entry.png beside this file;
# the program copies it to the output directory. It runs with no
# network, Python 3.13 standard library only.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
# for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(DST_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(DST_DIR, "entry.png"))
