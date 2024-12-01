import builtins
import sys
import typing

__all__ = ["print"]

class PrintColor:
    colors = {
        "white": "\033[37m",
        "red": "\033[31m",
        "magenta": "\033[35m",
        "orange": "\033[38;5;202m",
        "yellow": "\033[33m",
        "green": "\033[92m",
        "cyan": "\033[36m",
        "indigo": "\033[38;5;62m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "black": "\033[30m",
        "lightgray": "\033[38;5;243m",
        "pink": "\033[38;5;197m",
    }

    # Abbreviations and aliases
    colors["w"] = colors["white"]
    colors["r"] = colors["red"]
    colors["m"] = colors["magenta"]
    colors["o"] = colors["orange"]
    colors["y"] = colors["yellow"]
    colors["g"] = colors["green"]
    colors["c"] = colors["cyan"]
    colors["b"] = colors["blue"]
    colors["i"] = colors["indigo"]
    colors["p"] = colors["purple"]
    colors["k"] = colors["black"]
    colors["lg"] = colors["lightgray"]
    colors["pi"] = colors["pink"]

    backgrounds = {
        "white": "\033[37m",
        "red": "\033[31m",
        "magenta": "\033[35m",
        "orange": "\033[38;5;202m",
        "yellow": "\033[33m",
        "green": "\033[92m",
        "cyan": "\033[36m",
        "indigo": "\033[38;5;62m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "grey": "\033[40m",
        "black": "\033[30m",
        "pink": "\033[38;5;197m",
    }

    # Abbreviations and aliases
    backgrounds["w"] = backgrounds["white"]
    backgrounds["r"] = backgrounds["red"]
    backgrounds["m"] = backgrounds["magenta"]
    backgrounds["o"] = backgrounds["orange"]
    backgrounds["y"] = backgrounds["yellow"]
    backgrounds["g"] = backgrounds["green"]
    backgrounds["c"] = backgrounds["cyan"]
    backgrounds["b"] = backgrounds["blue"]
    backgrounds["i"] = backgrounds["indigo"]
    backgrounds["gray"] = backgrounds["grey"]
    backgrounds["gr"] = backgrounds["grey"]
    backgrounds["pi"] = backgrounds["pink"]

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
    "purple",
    "blue",
    "indigo",
    "green",
    "yellow",
    "red",
    "magenta",
    "cyan",
    "black",
    "white",
    "orange",
    "lightgray",
    "pink",
    "v",
    "p",
    "b",
    "g",
    "y",
    "r",
    "m",
    "c",
    "k",
    "w",
    "o",
    "li",
    "pi",
]

Background = typing.Literal[
    "grey",
    "red",
    "orange",
    "green",
    "yellow",
    "blue",
    "indigo",
    "magenta",
    "cyan",
    "white",
    "gray",
    "pink",
    "gr",
    "r",
    "o",
    "g",
    "y",
    "b",
    "i",
    "m",
    "c",
    "w",
    "o",
    "pi",
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
