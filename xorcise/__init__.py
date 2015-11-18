import curses

from .character import Character
from .console import Console
from .line import Line
from .attribute import RenditionAttribute, ColorAttribute
from .misc import ESCAPE_CHARS, DELETE_CHARS, BACKSPACE_CHARS, \
                  is_printable_char, char_with_control_key



def turn_on_console(asciize=False, spaces_per_tab=4):
  Line.ASCIIZE = asciize
  Line.SPACES_PER_TAB = spaces_per_tab

  window = curses.initscr()
  curses.noecho()
  curses.cbreak()

  curses.start_color()
  curses.use_default_colors()
  ColorAttribute.initialize()

  return Console(window)


def turn_off_console():
  curses.nocbreak()
  curses.echo()
  curses.endwin()

