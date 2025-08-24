# test_sorter.py
# basic coverage for the outcomes and threshould edges

from sorter import sort

def test_standard_basic():
    # neither heavy nor bulky
    assert sort(10, 10, 10, 1) == "STANDARD"

def test_bulky_byvolume_equalto_threshould():
    # volume = 1000000 cm^3
    assert sort(100, 100, 100, 1) == "SPECIAL"

def test_bulky_bydimension_equalto_threshould():
    # any side = 150 cm
    assert sort(150, 1, 100, 1) == "SPECIAL"

def test_heavy_only_equalto_threshould():
    # mass = 20 kg
    assert sort(40, 50, 45, 20) == "SPECIAL"

def test_both_bulky_and_heavy():
    # volume >= 1000000 cm^3 and mass >= 20 kg
    assert sort(200, 200, 10, 25) == "REJECTED"

def test_zero_values_allowed():
    # Zeros are allowed; not bulky/heavy
    assert sort(0, 0, 0, 0) == "STANDARD"

def test_float_thresholds_and_edges():
    assert sort(150.0, 1.0, 11.1, 11.03) == "SPECIAL"           # bulky by dimension
    assert sort(149.9999, 1.0, 11.1, 11.0) == "STANDARD"

    assert sort(100.0, 100.0, 100.0, 11.0) == "SPECIAL"         # 1,000,000 cm^3
    assert sort(10.0, 100.0, 99.9999, 11.0) == "STANDARD"

    assert sort(10.0, 10.0, 10.0, 20.0) == "SPECIAL"            # heavy only
    assert sort(10.0, 10.0, 10.0, 19.999) == "STANDARD"

    assert sort(150.0, 2.5, 2.5, 20.0) == "REJECTED"            # bulky by dimension and heavy

    assert sort(10.5, 20.25, 30.75, 5.5) == "STANDARD"
    assert sort(0.0, 0.0, 151.0, 0.0) == "SPECIAL"              # zero dims allowed but bulky by dimension
    assert sort(0.0, 0.0, 0.0, 0.0) == "STANDARD"
