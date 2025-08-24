# FDETechScreen

## Requirements (summary)
Sort packages into stacks based on size and mass.

## Function
`sort(width, height, length, mass) -> str`

Returns one of the stack catagories: `STANDARD`, `SPECIAL`, `REJECTED`

## Given (from the description)
- Dimensions are in centimeters(cm) and mass is in kilograms(kg).
- Thresholds are inclusive (≥).
- Bulky if volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm.
- Heavy if mass ≥ 20 kg.

## Stacks
- Both bulky and heavy -> REJECTED
- Either bulky or heavy -> SPECIAL
- Otherwise -> STANDARD

## Assumptions (my choices for this submission)
- Inputs are finite and non-negative numbers.
- Zero values are allowed.

## 1-click Replit demo
Run in your browser: [Replit Demo](https://replit.com/@murthy01/FDETechScreen)

## Steps to run tests
```bash
python -m pip install pytest
pytest -q


