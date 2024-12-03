import builtins
import sys
import typing

__all__ = ["print"]

class PrintColor:
    colors = {
        "black": "\033[30m",
        "darkgray": "\033[90m",  # Dark gray
        "red": "\033[31m",
        "lightred": "\033[91m",
        "yellow": "\033[33m",
        "lightyellow": "\033[93m",
        "green": "\033[32m",
        "lightgreen": "\033[92m",
        "blue": "\033[34m",
        "lightblue": "\033[94m",
        "magenta": "\033[35m",
        "lightmagenta": "\033[95m",
        "cyan": "\033[36m",
        "lightcyan": "\033[96m",
        "gray": "\033[37m",  # Light gray
        "white": "\033[97m",
        "purple": "\033[38;5;93m",  # ???(Start from here are all ANSI 256-color)
        "pink": "\033[38;5;197m",  # pink
        "orange": "\033[38;5;202m",  # light? orange
        "lightgray": "\033[38;5;243m",  # lightgray
        "indigo": "\033[38;5;62m",  # indigo(light?)
    }

    # Abbreviations and aliases
    colors["k"] = colors["black"]
    colors["dg"] = colors["darkgray"]
    colors["r"] = colors["red"]
    colors["lr"] = colors["lightred"]
    colors["y"] = colors["yellow"]
    colors["ly"] = colors["lightyellow"]
    colors["g"] = colors["green"]
    colors["lg"] = colors["lightgreen"]
    colors["b"] = colors["blue"]
    colors["lb"] = colors["lightblue"]
    colors["m"] = colors["magenta"]
    colors["lm"] = colors["lightmagenta"]
    colors["c"] = colors["cyan"]
    colors["lc"] = colors["lightcyan"]
    colors["gr"] = colors["gray"]
    colors["w"] = colors["white"]
    colors["p"] = colors["purple"]
    colors["pi"] = colors["pink"]
    colors["o"] = colors["orange"]
    colors["lig"] = colors["lightgray"]
    colors["i"] = colors["indigo"]

    backgrounds = {
        "black": "\033[40m",
        "darkgray": "\033[100m",
        "red": "\033[41m",
        "lightred": "\033[101m",
        "yellow": "\033[43m",
        "lightyellow": "\033[103m",
        "green": "\033[42m",
        "lightgreen": "\033[102m",
        "blue": "\033[44m",
        "lightblue": "\033[104m",
        "magenta": "\033[45m",
        "lightmagenta": "\033[105m",
        "cyan": "\033[46m",
        "lightcyan": "\033[106m",
        "gray": "\033[47m",
        "white": "\033[107m",
        "purple": "\033[48;5;93m",  # ANSI 256-color start from here
        "pink": "\033[48;5;197m",
        "orange": "\033[48;5;202m",
        "lightgray": "\033[48;5;243m",
        "indigo": "\033[48;5;62m",
    }

    # Abbreviations and aliases
    backgrounds["k"] = backgrounds["black"]
    backgrounds["dg"] = backgrounds["darkgray"]
    backgrounds["r"] = backgrounds["red"]
    backgrounds["lr"] = backgrounds["lightred"]
    backgrounds["y"] = backgrounds["yellow"]
    backgrounds["ly"] = backgrounds["lightyellow"]
    backgrounds["g"] = backgrounds["green"]
    backgrounds["lg"] = backgrounds["lightgreen"]
    backgrounds["b"] = backgrounds["blue"]
    backgrounds["lb"] = backgrounds["lightblue"]
    backgrounds["m"] = backgrounds["magenta"]
    backgrounds["lm"] = backgrounds["lightmagenta"]
    backgrounds["c"] = backgrounds["cyan"]
    backgrounds["lc"] = backgrounds["lightcyan"]
    backgrounds["gr"] = backgrounds["gray"]
    backgrounds["w"] = backgrounds["white"]
    backgrounds["p"] = backgrounds["purple"]
    backgrounds["pi"] = backgrounds["pink"]
    backgrounds["o"] = backgrounds["orange"]
    backgrounds["lig"] = backgrounds["lightgray"]
    backgrounds["i"] = backgrounds["indigo"]

    formats = {"bold": "\033[1m", "underline": "\033[4m", "blink": "\033[5m"}

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print(self):
        color = self.kwargs.pop("color", None)
        if not color:
            color = self.kwargs.pop("colour", None)
        back = self.kwargs.pop("background", None)
        format = self.kwargs.pop("format", None)
        tag = self.kwargs.pop("tag", None)
        tag_color = self.kwargs.pop("tag_color", None)
        tag_format = self.kwargs.pop("tag_format", None)
        if not tag_color:
            tag_color = self.kwargs.pop("tag_colour", None)
        # file = self.kwargs.get('file', sys.stdout)
        result = "¬".join(str(arg) for arg in self.args)

        if color:
            result = self.color(color) + result + self.end
            if format:
                result = self.format(format) + result

        if tag:
            tag = f"[{tag}]"
            if tag_color:
                tag = self.color(tag_color) + tag + self.end
            if tag_format:
                tag = self.format(tag_format) + tag
            result = f"{tag} {result}"
        # result += self.end
        if back:
            builtins.print(self.background(back), file=sys.stdout, end="")

        result += self.end
        builtins.print(*result.split("¬"), **self.kwargs)

    def color(self, color):
        return self.colors.get(color, self.default_color)

    def background(self, back):
        return self.backgrounds.get(back, self.default_color)

    def format(self, fmt):
        if isinstance(fmt, str):
            return self.formats.get(fmt, self.default_color)
        elif isinstance(fmt, list) or isinstance(fmt, tuple):
            return "".join([f for f in [self.formats.get(f, "") for f in fmt]])

    @property
    def end(self):
        return "\033[0m"

    @property
    def default_color(self):
        return "\033[0m"


Color = typing.Literal[
    "black",
    "grey",
    "red",
    "lightred",
    "green",
    "lightgreen",
    "yellow",
    "lightyellow",
    "blue",
    "lightblue",
    "magenta",
    "lightmagenta",
    "cyan",
    "lightcyan",
    "white",
    "purple",
    "pink",
    "orange",
    "lightgray",
    "indigo",
    "k",
    "gr",
    "r",
    "lr",
    "g",
    "lg",
    "y",
    "ly",
    "b",
    "lb",
    "m",
    "lm",
    "c",
    "lc",
    "w",
    "p",
    "pi",
    "o",
    "lig",
    "i",
]

Background = typing.Literal[
    "grey",
    "red",
    "lightred",
    "green",
    "lightgreen",
    "yellow",
    "lightyellow",
    "blue",
    "lightblue",
    "magenta",
    "lightmagenta",
    "cyan",
    "lightcyan",
    "white",
    "purple",
    "pink",
    "orange",
    "lightgray",
    "indigo",
    "gr",
    "r",
    "lr",
    "g",
    "lg",
    "y",
    "ly",
    "b",
    "lb",
    "m",
    "lm",
    "c",
    "lc",
    "w",
    "p",
    "pi",
    "o",
    "lig",
    "i",
]

Format = typing.Literal["bold", "underline", "blink"]


_T_contra = typing.TypeVar("_T_contra", contravariant=True)


class SupportsWrite(typing.Protocol[_T_contra]):
    def write(self, __s: _T_contra) -> typing.Any:
        ...


def print(
    *values: object,
    sep: str = " ",
    end: str = "\n",
    file: SupportsWrite[str] = None,
    flush: bool = False,
    color: Color = None,
    background: Background = None,
    format: Format = None,
    tag: str = None,
    tag_color: Color = None,
    tag_format: Format = None,
    **kwargs,
):
    printcolor = PrintColor(
        *values,
        sep=sep,
        end=end,
        file=file,
        flush=flush,
        color=color,
        background=background,
        format=format,
        tag=tag,
        tag_color=tag_color,
        tag_format=tag_format,
        **kwargs,
    )
    printcolor.print()
