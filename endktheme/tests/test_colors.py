import endktheme.colors


def valid_hexcolor(x):
    assert len(x) == 7, 'Hex color must be 7 characters long.'
    assert x[0] == '#', 'Hex colors should start with \'#\'.'
    assert int(x[1:], 16), 'Hex color is not valid base 16 value.'


def test_primary():
    for c in endktheme.colors.primary():
        valid_hexcolor(c)


def test_secondary():
    for c in endktheme.colors.secondary():
        valid_hexcolor(c)


def test_excel():
    for c in endktheme.colors.excel():
        valid_hexcolor(c)
