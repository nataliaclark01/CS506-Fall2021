from .lake import draw_lake
from .park import draw_park
from .tree import add_trees

def draw_outdoors():
    add_trees()
    draw_lake()
    draw_park()
    add_trees()
    return
