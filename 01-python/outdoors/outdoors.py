from .lake import draw_lake
from .park import draw_park
from .tree import draw_tree

def draw_outdoors():
    draw_tree()
    draw_lake()
    draw_park()
    draw_tree()
    return
