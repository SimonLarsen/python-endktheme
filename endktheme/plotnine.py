"""Themes for plotnine."""
import plotnine as p9
import endktheme.colors
import endktheme.style


def theme_energinet() -> p9.themes.theme:
    """Create a simple Energinet theme."""
    return p9.theme(
        text=p9.element_text(family=endktheme.style.font_family()),
        axis_line=p9.element_line(color="black"),
        plot_background=p9.element_blank(),
        panel_background=p9.element_rect(fill="white"),
        legend_background=p9.element_rect(fill="white"),
        legend_key=p9.element_blank(),
        panel_grid=p9.element_blank(),
        axis_ticks=p9.element_blank(),
    )


def scale_color_energinet(**kwargs) -> p9.scale_color_manual:
    """Create a color scale."""
    return p9.scale_color_manual(values=endktheme.colors.excel(), **kwargs)


def scale_fill_energinet(**kwargs) -> p9.scale_fill_manual:
    """Create a fill scale."""
    return p9.scale_fill_manual(values=endktheme.colors.excel(), **kwargs)


def scale_fill_gradient_energinet(
    low: int = 0, high: int = 2, **kwargs
) -> p9.scale_fill_gradient:
    """
    Create a two-point fill gradient.

    Parameters:
        low (int): Index of low color.
        high (int): Index of high color.
    """
    pal = endktheme.colors.excel()
    return p9.scale_fill_gradient(low=pal[low], high=pal[high], **kwargs)


def scale_color_gradient_energinet(
    low: int = 0, high: int = 2, **kwargs
) -> p9.scale_color_gradient:
    """
    Create a two-point color gradient.

    Parameters:
        low (int): Index of low color.
        high (int): Index of high color.
    """
    pal = endktheme.colors.excel()
    return p9.scale_color_gradient(low=pal[low], high=pal[high], **kwargs)


def scale_fill_gradient2_energinet(
    low: int = 0, mid: int = 1, high: int = 2, **kwargs
) -> p9.scale_fill_gradient2:
    """
    Create a three-point fill gradient.

    Parameters:
        low (int): Index of low color.
        mid (int): Index of middle color.
        high (int): Index of high color.
    """
    pal = endktheme.colors.excel()
    return p9.scale_fill_gradient2(
        low=pal[low], mid=pal[mid], high=pal[high], **kwargs
    )


def scale_color_gradient2_energinet(
    low: int = 0, mid: int = 1, high: int = 2, **kwargs
) -> p9.scale_color_gradient2:
    """
    Create a three-point color gradient.

    Parameters:
        low (int): Index of low color.
        mid (int): Index of middle color.
        high (int): Index of high color.
    """
    pal = endktheme.colors.excel()
    return p9.scale_color_gradient2(
        low=pal[low], mid=pal[mid], high=pal[high], **kwargs
    )
