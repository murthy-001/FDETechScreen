# FDETechScreen

## Function
`sort(width, height, length, mass) -> str`

Returns one of the stack catagories: `STANDARD`, `SPECIAL`, `REJECTED`

## Given (from the description)
- Dimensions are in centimeters(cm) and mass is in kilograms(kg).
- Thresholds are inclusive (≥).
- Bulky if volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm.
- Heavy if mass ≥ 20 kg.

## Stack catagories
- Both bulky and heavy -> REJECTED
- Either bulky or heavy -> SPECIAL
- Otherwise -> STANDARD

## Assumptions (my choices for this submission)
- Inputs are finite and non-negative numbers.
- Zero values are allowed.

## Steps to run tests
    python -m pip install pytest
    pytest -q


