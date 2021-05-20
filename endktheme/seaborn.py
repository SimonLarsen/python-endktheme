"""Themes for seaborn."""
import seaborn
import endktheme.colors
import endktheme.style


def use_theme() -> None:
    """Use Energinet theme."""
    seaborn.set_style(
        "ticks",
        {
            "xtick.top": False,
            "xtick.right": False,
            "xtick.bottom": False,
            "ytick.left": False,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.bottom": True,
            "axes.spines.left": True,
            "font.family": ["sans-serif"],
            "font.sans-serif": endktheme.style.font_family(),
        },
    )


def use_palette() -> None:
    """Use Energinet color palette."""
    seaborn.set_palette(endktheme.colors.excel())
