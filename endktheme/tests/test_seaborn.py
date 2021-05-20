import pandas as pd
import endktheme.seaborn
import seaborn as sns


def sample_data():
    return pd.DataFrame({
        'x': [1, 2, 3, 4, 1, 2, 3, 4],
        'y': [2, 4, 3, 5, 6, 4, 5, 3],
        'z': [0.065, 0.62, -0.62, -1.22, 0.70, -0.17, 1.01, -0.53],
        'type': ['a', 'a', 'b', 'c', 'b', 'b', 'c', 'a'],
        'group': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b']
    })


def render(tmp_path, fig):
    fig.savefig(tmp_path / "plot.png", dpi=70)


def test_theme(tmp_path):
    df = sample_data()
    endktheme.seaborn.use_theme()
    p = sns.lineplot(data=df, x="x", y="y", hue="group")
    render(tmp_path, p.get_figure())


def test_palette(tmp_path):
    df = sample_data()
    endktheme.seaborn.use_palette()
    p = sns.lineplot(data=df, x="x", y="y", hue="group")
    render(tmp_path, p.get_figure())
