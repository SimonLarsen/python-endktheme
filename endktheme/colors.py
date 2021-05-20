"""Energinet color themes."""
from typing import List


def primary() -> List[str]:
    """Primary color scheme."""
    return ["#00A58D", "#008A8B", "#9FCD91", "#09505D", "#00587C"]


def secondary() -> List[str]:
    """Secondary color scheme."""
    return [
        "#83CCD8",
        "#00A6BC",
        "#C2E4F0",
        "#FFD424",
        "#F8AE3C",
        "#A0C1C2",
        "#293A4C",
    ]


def excel() -> List[str]:
    """Excel color scheme. Use this for plot aesthetics."""
    return [
        "#09505D",
        "#00A58D",
        "#FFD424",
        "#83CCD8",
        "#008A8B",
        "#F8AE3C",
        "#A0C1C2",
        "#9FCD91",
        "#CC493E",
    ]
