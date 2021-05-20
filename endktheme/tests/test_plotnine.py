import pandas as pd
import plotnine as p9
import endktheme.plotnine


def sample_data():
    return pd.DataFrame({
        'x': [1, 2, 3, 4, 1, 2, 3, 4],
        'y': [2, 4, 3, 5, 6, 4, 5, 3],
        'z': [0.065, 0.62, -0.62, -1.22, 0.70, -0.17, 1.01, -0.53],
        'type': ['a', 'a', 'b', 'c', 'b', 'b', 'c', 'a'],
        'group': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b']
    })


def render(tmp_path, p):
    p.save(tmp_path / 'plot.png', width=5, height=5, verbose=False)


def test_theme(tmp_path):
    x = sample_data()
    p = p9.ggplot(x, p9.aes(x='x', y='y', color='group')) + p9.geom_line()
    p = p + endktheme.plotnine.theme_energinet()
    render(tmp_path, p)


def test_color(tmp_path):
    x = sample_data()
    p = (p9.ggplot(x, p9.aes(x='x', y='y', color='group')) +
         p9.geom_line() +
         endktheme.plotnine.scale_color_energinet())
    render(tmp_path, p)


def test_fill(tmp_path):
    x = sample_data()
    p = (p9.ggplot(x, p9.aes(x='group', fill='factor(type)')) +
         p9.geom_bar() +
         endktheme.plotnine.scale_fill_energinet())
    render(tmp_path, p)


def test_fill_gradient(tmp_path):
    x = sample_data()
    p = (p9.ggplot(x, p9.aes(x='x', y='y', fill='z')) +
         p9.geom_tile())

    p1 = p + endktheme.plotnine.scale_fill_gradient_energinet()
    render(tmp_path, p1)

    p2 = p + endktheme.plotnine.scale_fill_gradient2_energinet()
    render(tmp_path, p2)


def test_color_gradient(tmp_path):
    x = sample_data()
    p = (p9.ggplot(x, p9.aes(x='x', y='y', color='z')) +
         p9.geom_point())

    p1 = p + endktheme.plotnine.scale_color_gradient_energinet()
    render(tmp_path, p1)

    p2 = p + endktheme.plotnine.scale_color_gradient2_energinet()
    render(tmp_path, p2)
