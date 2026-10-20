ACDC Top-K Sweep Results

ACDC score distribution is NOT purely binary — it has 6 levels:
  0.01 (background), 0.03, 0.05, 0.07, 0.09, Infinity
  isinf binarization discards all intermediate-level edges.

--- Arithmetic ---
  ACDC non-background edges: 17 inf + 9×0.09 + 8×0.07 + 10×0.05 + 26×0.03 = 70 total
  EAP-IG/EP agreement: J = 0.6949 (high)

| k     | ACDC | 1/3 | 2/3 | 3/3 | J(ei,ep) | J(ei,ac) | J(ep,ac) |
|-------|------|-----|-----|-----|----------|----------|----------|
| isinf |   17 |  36 |  65 |  17 |   0.6949 |   0.1700 |   0.1700 |
| 50    |   50 |  40 |  39 |  44 |   0.6949 |   0.4151 |   0.4286 |
| 75    |   75 |  51 |  31 |  54 |   0.6949 |   0.4463 |   0.4831 |
| 100   |  100 |  76 |  31 |  54 |   0.6949 |   0.3699 |   0.3986 |
| 150   |  150 | 126 |  31 |  54 |   0.6949 |   0.2755 |   0.2953 |

--- IOI (baseline) ---
  ACDC non-background edges: 14 inf + 14×0.09 + 11×0.07 + 50×0.05 + 138×0.03 = 227 total
  EAP-IG/EP agreement: J = 0.3072 (moderate)

| k     | ACDC | 1/3 | 2/3 | 3/3 | J(ei,ep) | J(ei,ac) | J(ep,ac) |
|-------|------|-----|-----|-----|----------|----------|----------|
| isinf |   14 | 103 |  45 |   7 |   0.3072 |   0.0962 |   0.0857 |
| 50    |   50 |  96 |  56 |  14 |   0.3072 |   0.2397 |   0.1719 |
| 75    |   75 |  98 |  60 |  19 |   0.3072 |   0.2868 |   0.2153 |
| 100   |  100 | 108 |  60 |  24 |   0.3072 |   0.2903 |   0.2500 |