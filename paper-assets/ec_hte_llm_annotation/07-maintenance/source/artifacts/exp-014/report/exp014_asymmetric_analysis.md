# exp-014: Asymmetric Misclassification Verification

## 1. Setup

### Asymmetric Confusion Matrix

For subgroup $s$ with $\text{FPR}_s = P(\hat{Z}=1|Z=0,S=s)$ and $\text{FNR}_s = P(\hat{Z}=0|Z=1,S=s)$:

$$C_s = \begin{pmatrix} 1-\text{FPR}_s & \text{FPR}_s \\ \text{FNR}_s & 1-\text{FNR}_s \end{pmatrix}$$

### Mixing Matrix (Bayesian Inversion)

Under balanced prior $P(Z=0)=P(Z=1)=0.5$:

$$M_s[\hat{z}, z] = P(Z=z \mid \hat{Z}=\hat{z}, S=s)$$

$$M_s = \begin{pmatrix} \frac{1-\text{FPR}_s}{1-\text{FPR}_s+\text{FNR}_s} & \frac{\text{FNR}_s}{1-\text{FPR}_s+\text{FNR}_s} \\ \frac{\text{FPR}_s}{\text{FPR}_s+1-\text{FNR}_s} & \frac{1-\text{FNR}_s}{\text{FPR}_s+1-\text{FNR}_s} \end{pmatrix}$$

### Global Mixing Matrix

$$M_{\text{global}} = \sum_s w_s \, M_s$$

## 2. Bias Formula Derivation

The observed CATE within subgroup $s$ satisfies:

$$\boldsymbol{\tau}_{\text{obs},s} = M_s \, \boldsymbol{\tau}$$

where $\boldsymbol{\tau} = (\tau(0),\;\tau(1))^\top$.

After global correction:

$$\hat{\boldsymbol{\tau}}_s = M_{\text{global}}^{-1} M_s \, \boldsymbol{\tau}$$

**Bias:**

$$\text{bias}(z, s) = \bigl[(M_{\text{global}}^{-1} M_s - I)\,\boldsymbol{\tau}\bigr]_z = [B_s \, \boldsymbol{\tau}]_z$$

where $B_s \equiv M_{\text{global}}^{-1} M_s - I$.

## 3. Product Structure Proof

**Claim.** $\text{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}$ where $\Delta\tau = \tau(1)-\tau(0)$.

**Proof.** Both $M_s$ and $M_{\text{global}}$ are stochastic (rows sum to 1):

$$M_s \mathbf{1} = \mathbf{1},\quad M_{\text{global}} \mathbf{1} = \mathbf{1} \;\Longrightarrow\; M_{\text{global}}^{-1}\mathbf{1} = \mathbf{1}$$

$$\Rightarrow\; B_s \mathbf{1} = (M_{\text{global}}^{-1} M_s - I)\mathbf{1} = \mathbf{1} - \mathbf{1} = \mathbf{0}$$

Decompose $\boldsymbol{\tau} = \tau(0)\,\mathbf{1} + \Delta\tau\,\mathbf{e}_1$ where $\mathbf{e}_1=(0,1)^\top$:

$$\text{bias}(z,s) = \tau(0)\underbrace{[B_s\mathbf{1}]_z}_{=0} + \Delta\tau\,[B_s]_{z,1}$$

$$\boxed{\text{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}}$$

The coefficient $[B_s]_{z,1}$ depends **only** on $\{\text{FPR}_k, \text{FNR}_k, w_k\}$, not on $\Delta\tau$. $\square$

### Numerical Verification

For each (config, subgroup, $z$), the ratio $\text{bias}/\Delta\tau$ is constant:

| Config | Sub | z | Mean ratio | CV |
|--------|-----|---|-----------|----|
| config1 | 0 | 0 | 0.027490 | 2.65e-16 |
| config1 | 0 | 1 | 0.058181 | 6.89e-16 |
| config1 | 1 | 0 | -0.027490 | 6.70e-16 |
| config1 | 1 | 1 | -0.058181 | 8.57e-16 |
| config2 | 0 | 0 | -0.115385 | 8.30e-16 |
| config2 | 0 | 1 | 0.115385 | 5.19e-16 |
| config2 | 1 | 0 | 0.115385 | 6.93e-16 |
| config2 | 1 | 1 | -0.115385 | 1.70e-16 |
| config3 | 0 | 0 | 0.063199 | 1.39e-16 |
| config3 | 0 | 1 | 0.106846 | 3.81e-16 |
| config3 | 1 | 0 | -0.063199 | 1.39e-16 |
| config3 | 1 | 1 | -0.106846 | 3.18e-16 |

CV (coefficient of variation) = 0 confirms exact product structure.

## 4. Connection to the Symmetric Case

When $\text{FPR}_s = \text{FNR}_s = \pi_s$ (symmetric, assumption A2):

$$M_s = \begin{pmatrix} 1-\pi_s & \pi_s \\ \pi_s & 1-\pi_s \end{pmatrix}$$

$$B_s = \frac{\delta_s}{1-2\bar\pi} \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}, \quad \delta_s = \pi_s - \bar\pi$$

and the bias reduces to:

$$\text{bias}(z{=}0,s) = +\frac{\delta_s\,\Delta\tau}{1-2\bar\pi},\quad \text{bias}(z{=}1,s) = -\frac{\delta_s\,\Delta\tau}{1-2\bar\pi}$$

**Key differences in the asymmetric case:**

1. The product structure (bias proportional to $\Delta\tau$) holds in **both** cases.
2. In symmetric: $|{\rm bias}(z{=}0)|=|{\rm bias}(z{=}1)|$. In asymmetric: they differ.
3. In symmetric: error heterogeneity collapses to scalar $\delta_s/(1{-}2\bar\pi)$. In asymmetric: it is the matrix entry $[B_s]_{z,1}$.
4. **Assumption A2 is not required** for the product structure.

## 5. Numerical Results

### R-squared (analytic vs MC bias): **0.991748**

### Bias table

| Config | delta_tau | Sub | z | Analytic | MC | MC SE |
|--------|----------|-----|---|----------|-----|-------|
| config1 | 0.1 | 0 | 0 | +0.002749 | +0.005527 | 0.002385 |
| config1 | 0.1 | 0 | 1 | +0.005818 | +0.002734 | 0.002703 |
| config1 | 0.1 | 1 | 0 | -0.002749 | -0.001893 | 0.002514 |
| config1 | 0.1 | 1 | 1 | -0.005818 | -0.005667 | 0.002438 |
| config1 | 0.2 | 0 | 0 | +0.005498 | +0.005684 | 0.002313 |
| config1 | 0.2 | 0 | 1 | +0.011636 | +0.011247 | 0.002485 |
| config1 | 0.2 | 1 | 0 | -0.005498 | -0.002833 | 0.002904 |
| config1 | 0.2 | 1 | 1 | -0.011636 | -0.010027 | 0.002504 |
| config1 | 0.3 | 0 | 0 | +0.008247 | +0.007753 | 0.002307 |
| config1 | 0.3 | 0 | 1 | +0.017454 | +0.017905 | 0.002576 |
| config1 | 0.3 | 1 | 0 | -0.008247 | -0.004170 | 0.002405 |
| config1 | 0.3 | 1 | 1 | -0.017454 | -0.021127 | 0.002385 |
| config1 | 0.4 | 0 | 0 | +0.010996 | +0.010926 | 0.002253 |
| config1 | 0.4 | 0 | 1 | +0.023272 | +0.021784 | 0.002422 |
| config1 | 0.4 | 1 | 0 | -0.010996 | -0.012868 | 0.002749 |
| config1 | 0.4 | 1 | 1 | -0.023272 | -0.023415 | 0.002208 |
| config1 | 0.5 | 0 | 0 | +0.013745 | +0.012802 | 0.002458 |
| config1 | 0.5 | 0 | 1 | +0.029091 | +0.027284 | 0.002162 |
| config1 | 0.5 | 1 | 0 | -0.013745 | -0.015324 | 0.002576 |
| config1 | 0.5 | 1 | 1 | -0.029091 | -0.025433 | 0.002290 |
| config2 | 0.1 | 0 | 0 | -0.011538 | -0.010139 | 0.002646 |
| config2 | 0.1 | 0 | 1 | +0.011538 | +0.010403 | 0.002633 |
| config2 | 0.1 | 1 | 0 | +0.011538 | +0.011842 | 0.002404 |
| config2 | 0.1 | 1 | 1 | -0.011538 | -0.014635 | 0.002778 |
| config2 | 0.2 | 0 | 0 | -0.023077 | -0.023546 | 0.002582 |
| config2 | 0.2 | 0 | 1 | +0.023077 | +0.017732 | 0.002500 |
| config2 | 0.2 | 1 | 0 | +0.023077 | +0.023494 | 0.002888 |
| config2 | 0.2 | 1 | 1 | -0.023077 | -0.021575 | 0.002496 |
| config2 | 0.3 | 0 | 0 | -0.034615 | -0.034518 | 0.002934 |
| config2 | 0.3 | 0 | 1 | +0.034615 | +0.035244 | 0.002597 |
| config2 | 0.3 | 1 | 0 | +0.034615 | +0.031412 | 0.002449 |
| config2 | 0.3 | 1 | 1 | -0.034615 | -0.034924 | 0.002486 |
| config2 | 0.4 | 0 | 0 | -0.046154 | -0.050813 | 0.002349 |
| config2 | 0.4 | 0 | 1 | +0.046154 | +0.051606 | 0.002482 |
| config2 | 0.4 | 1 | 0 | +0.046154 | +0.049551 | 0.002618 |
| config2 | 0.4 | 1 | 1 | -0.046154 | -0.048168 | 0.002771 |
| config2 | 0.5 | 0 | 0 | -0.057692 | -0.060048 | 0.002539 |
| config2 | 0.5 | 0 | 1 | +0.057692 | +0.063770 | 0.002542 |
| config2 | 0.5 | 1 | 0 | +0.057692 | +0.063476 | 0.002689 |
| config2 | 0.5 | 1 | 1 | -0.057692 | -0.062490 | 0.002728 |
| config3 | 0.1 | 0 | 0 | +0.006320 | +0.006486 | 0.002103 |
| config3 | 0.1 | 0 | 1 | +0.010685 | +0.009365 | 0.002825 |
| config3 | 0.1 | 1 | 0 | -0.006320 | -0.010770 | 0.002554 |
| config3 | 0.1 | 1 | 1 | -0.010685 | -0.009841 | 0.001949 |
| config3 | 0.2 | 0 | 0 | +0.012640 | +0.014551 | 0.002279 |
| config3 | 0.2 | 0 | 1 | +0.021369 | +0.018645 | 0.002529 |
| config3 | 0.2 | 1 | 0 | -0.012640 | -0.007712 | 0.002583 |
| config3 | 0.2 | 1 | 1 | -0.021369 | -0.023804 | 0.002343 |
| config3 | 0.3 | 0 | 0 | +0.018960 | +0.021452 | 0.002184 |
| config3 | 0.3 | 0 | 1 | +0.032054 | +0.029665 | 0.002625 |
| config3 | 0.3 | 1 | 0 | -0.018960 | -0.020052 | 0.002273 |
| config3 | 0.3 | 1 | 1 | -0.032054 | -0.029729 | 0.001894 |
| config3 | 0.4 | 0 | 0 | +0.025279 | +0.025040 | 0.002227 |
| config3 | 0.4 | 0 | 1 | +0.042739 | +0.045724 | 0.002569 |
| config3 | 0.4 | 1 | 0 | -0.025279 | -0.022175 | 0.002682 |
| config3 | 0.4 | 1 | 1 | -0.042739 | -0.043056 | 0.001895 |
| config3 | 0.5 | 0 | 0 | +0.031599 | +0.032668 | 0.002606 |
| config3 | 0.5 | 0 | 1 | +0.053423 | +0.050149 | 0.002940 |
| config3 | 0.5 | 1 | 0 | -0.031599 | -0.035924 | 0.002715 |
| config3 | 0.5 | 1 | 1 | -0.053423 | -0.050869 | 0.002228 |

## 6. EC-HTE vs Global Correction

Expert labels per MC run: 250

### Per-cell results

| Config | dt | Sub | z | Method | |Bias| | RMSE | Cov |
|--------|-----|-----|---|--------|-------|------|-----|
| config1 | 0.1 | 0 | 0 | naive | 0.0201 | 0.0275 | 0.86 |
| config1 | 0.1 | 0 | 0 | global_est | 0.0037 | 0.0251 | 0.92 |
| config1 | 0.1 | 0 | 0 | echte | 0.0006 | 0.0260 | 0.92 |
| config1 | 0.1 | 0 | 1 | naive | 0.0132 | 0.0249 | 0.88 |
| config1 | 0.1 | 0 | 1 | global_est | 0.0042 | 0.0282 | 0.96 |
| config1 | 0.1 | 0 | 1 | echte | 0.0005 | 0.0272 | 0.94 |
| config1 | 0.1 | 1 | 0 | naive | 0.0125 | 0.0241 | 0.94 |
| config1 | 0.1 | 1 | 0 | global_est | 0.0036 | 0.0262 | 0.95 |
| config1 | 0.1 | 1 | 0 | echte | 0.0011 | 0.0251 | 0.98 |
| config1 | 0.1 | 1 | 1 | naive | 0.0215 | 0.0291 | 0.77 |
| config1 | 0.1 | 1 | 1 | global_est | 0.0044 | 0.0253 | 0.92 |
| config1 | 0.1 | 1 | 1 | echte | 0.0011 | 0.0269 | 0.93 |
| config1 | 0.2 | 0 | 0 | naive | 0.0365 | 0.0411 | 0.54 |
| config1 | 0.2 | 0 | 0 | global_est | 0.0014 | 0.0257 | 0.93 |
| config1 | 0.2 | 0 | 0 | echte | 0.0047 | 0.0268 | 0.95 |
| config1 | 0.2 | 0 | 1 | naive | 0.0225 | 0.0301 | 0.83 |
| config1 | 0.2 | 0 | 1 | global_est | 0.0155 | 0.0324 | 0.91 |
| config1 | 0.2 | 0 | 1 | echte | 0.0050 | 0.0276 | 0.94 |
| config1 | 0.2 | 1 | 0 | naive | 0.0260 | 0.0352 | 0.74 |
| config1 | 0.2 | 1 | 0 | global_est | 0.0065 | 0.0309 | 0.95 |
| config1 | 0.2 | 1 | 0 | echte | 0.0015 | 0.0315 | 0.91 |
| config1 | 0.2 | 1 | 1 | naive | 0.0417 | 0.0462 | 0.37 |
| config1 | 0.2 | 1 | 1 | global_est | 0.0064 | 0.0273 | 0.93 |
| config1 | 0.2 | 1 | 1 | echte | 0.0048 | 0.0298 | 0.91 |
| config1 | 0.3 | 0 | 0 | naive | 0.0542 | 0.0572 | 0.19 |
| config1 | 0.3 | 0 | 0 | global_est | 0.0038 | 0.0250 | 0.97 |
| config1 | 0.3 | 0 | 0 | echte | 0.0061 | 0.0296 | 0.91 |
| config1 | 0.3 | 0 | 1 | naive | 0.0330 | 0.0388 | 0.68 |
| config1 | 0.3 | 0 | 1 | global_est | 0.0212 | 0.0357 | 0.88 |
| config1 | 0.3 | 0 | 1 | echte | 0.0067 | 0.0296 | 0.92 |
| config1 | 0.3 | 1 | 0 | naive | 0.0382 | 0.0430 | 0.59 |
| config1 | 0.3 | 1 | 0 | global_est | 0.0079 | 0.0264 | 0.96 |
| config1 | 0.3 | 1 | 0 | echte | 0.0002 | 0.0272 | 0.95 |
| config1 | 0.3 | 1 | 1 | naive | 0.0676 | 0.0703 | 0.04 |
| config1 | 0.3 | 1 | 1 | global_est | 0.0182 | 0.0319 | 0.86 |
| config1 | 0.3 | 1 | 1 | echte | 0.0027 | 0.0319 | 0.90 |
| config1 | 0.4 | 0 | 0 | naive | 0.0724 | 0.0747 | 0.03 |
| config1 | 0.4 | 0 | 0 | global_est | 0.0046 | 0.0271 | 0.93 |
| config1 | 0.4 | 0 | 0 | echte | 0.0042 | 0.0335 | 0.84 |
| config1 | 0.4 | 0 | 1 | naive | 0.0457 | 0.0497 | 0.38 |
| config1 | 0.4 | 0 | 1 | global_est | 0.0287 | 0.0421 | 0.80 |
| config1 | 0.4 | 0 | 1 | echte | 0.0069 | 0.0318 | 0.92 |
| config1 | 0.4 | 1 | 0 | naive | 0.0454 | 0.0509 | 0.48 |
| config1 | 0.4 | 1 | 0 | global_est | 0.0188 | 0.0373 | 0.85 |
| config1 | 0.4 | 1 | 0 | echte | 0.0118 | 0.0367 | 0.87 |
| config1 | 0.4 | 1 | 1 | naive | 0.0874 | 0.0892 | 0.01 |
| config1 | 0.4 | 1 | 1 | global_est | 0.0169 | 0.0316 | 0.87 |
| config1 | 0.4 | 1 | 1 | echte | 0.0074 | 0.0346 | 0.90 |
| config1 | 0.5 | 0 | 0 | naive | 0.0898 | 0.0919 | 0.01 |
| config1 | 0.5 | 0 | 0 | global_est | 0.0029 | 0.0309 | 0.86 |
| config1 | 0.5 | 0 | 0 | echte | 0.0132 | 0.0402 | 0.83 |
| config1 | 0.5 | 0 | 1 | naive | 0.0572 | 0.0595 | 0.17 |
| config1 | 0.5 | 0 | 1 | global_est | 0.0367 | 0.0477 | 0.75 |
| config1 | 0.5 | 0 | 1 | echte | 0.0096 | 0.0369 | 0.85 |
| config1 | 0.5 | 1 | 0 | naive | 0.0580 | 0.0616 | 0.27 |
| config1 | 0.5 | 1 | 0 | global_est | 0.0249 | 0.0419 | 0.78 |
| config1 | 0.5 | 1 | 0 | echte | 0.0112 | 0.0400 | 0.81 |
| config1 | 0.5 | 1 | 1 | naive | 0.1059 | 0.1074 | 0.00 |
| config1 | 0.5 | 1 | 1 | global_est | 0.0165 | 0.0336 | 0.79 |
| config1 | 0.5 | 1 | 1 | echte | 0.0135 | 0.0420 | 0.81 |
| config2 | 0.1 | 0 | 0 | naive | 0.0145 | 0.0240 | 0.90 |
| config2 | 0.1 | 0 | 0 | global_est | 0.0125 | 0.0293 | 0.90 |
| config2 | 0.1 | 0 | 0 | echte | 0.0000 | 0.0232 | 0.95 |
| config2 | 0.1 | 0 | 1 | naive | 0.0063 | 0.0221 | 0.95 |
| config2 | 0.1 | 0 | 1 | global_est | 0.0136 | 0.0305 | 0.91 |
| config2 | 0.1 | 0 | 1 | echte | 0.0009 | 0.0235 | 0.96 |
| config2 | 0.1 | 1 | 0 | naive | 0.0269 | 0.0322 | 0.72 |
| config2 | 0.1 | 1 | 0 | global_est | 0.0106 | 0.0270 | 0.98 |
| config2 | 0.1 | 1 | 0 | echte | 0.0038 | 0.0359 | 0.96 |
| config2 | 0.1 | 1 | 1 | naive | 0.0248 | 0.0337 | 0.76 |
| config2 | 0.1 | 1 | 1 | global_est | 0.0128 | 0.0314 | 0.90 |
| config2 | 0.1 | 1 | 1 | echte | 0.0015 | 0.0389 | 0.93 |
| config2 | 0.2 | 0 | 0 | naive | 0.0258 | 0.0327 | 0.74 |
| config2 | 0.2 | 0 | 0 | global_est | 0.0278 | 0.0417 | 0.77 |
| config2 | 0.2 | 0 | 0 | echte | 0.0047 | 0.0270 | 0.91 |
| config2 | 0.2 | 0 | 1 | naive | 0.0158 | 0.0263 | 0.91 |
| config2 | 0.2 | 0 | 1 | global_est | 0.0229 | 0.0357 | 0.83 |
| config2 | 0.2 | 0 | 1 | echte | 0.0006 | 0.0238 | 0.95 |
| config2 | 0.2 | 1 | 0 | naive | 0.0552 | 0.0594 | 0.24 |
| config2 | 0.2 | 1 | 0 | global_est | 0.0207 | 0.0377 | 0.82 |
| config2 | 0.2 | 1 | 0 | echte | 0.0066 | 0.0488 | 0.84 |
| config2 | 0.2 | 1 | 1 | naive | 0.0431 | 0.0478 | 0.42 |
| config2 | 0.2 | 1 | 1 | global_est | 0.0182 | 0.0328 | 0.90 |
| config2 | 0.2 | 1 | 1 | echte | 0.0092 | 0.0440 | 0.89 |
| config2 | 0.3 | 0 | 0 | naive | 0.0411 | 0.0463 | 0.42 |
| config2 | 0.3 | 0 | 0 | global_est | 0.0410 | 0.0557 | 0.63 |
| config2 | 0.3 | 0 | 0 | echte | 0.0049 | 0.0302 | 0.87 |
| config2 | 0.3 | 0 | 1 | naive | 0.0161 | 0.0262 | 0.87 |
| config2 | 0.3 | 0 | 1 | global_est | 0.0418 | 0.0523 | 0.60 |
| config2 | 0.3 | 0 | 1 | echte | 0.0050 | 0.0243 | 0.95 |
| config2 | 0.3 | 1 | 0 | naive | 0.0792 | 0.0811 | 0.02 |
| config2 | 0.3 | 1 | 0 | global_est | 0.0277 | 0.0390 | 0.81 |
| config2 | 0.3 | 1 | 0 | echte | 0.0120 | 0.0466 | 0.89 |
| config2 | 0.3 | 1 | 1 | naive | 0.0674 | 0.0702 | 0.10 |
| config2 | 0.3 | 1 | 1 | global_est | 0.0310 | 0.0409 | 0.80 |
| config2 | 0.3 | 1 | 1 | echte | 0.0093 | 0.0446 | 0.89 |
| config2 | 0.4 | 0 | 0 | naive | 0.0520 | 0.0550 | 0.21 |
| config2 | 0.4 | 0 | 0 | global_est | 0.0588 | 0.0656 | 0.39 |
| config2 | 0.4 | 0 | 0 | echte | 0.0106 | 0.0269 | 0.89 |
| config2 | 0.4 | 0 | 1 | naive | 0.0182 | 0.0276 | 0.85 |
| config2 | 0.4 | 0 | 1 | global_est | 0.0595 | 0.0662 | 0.35 |
| config2 | 0.4 | 0 | 1 | echte | 0.0112 | 0.0268 | 0.92 |
| config2 | 0.4 | 1 | 0 | naive | 0.1114 | 0.1128 | 0.00 |
| config2 | 0.4 | 1 | 0 | global_est | 0.0446 | 0.0540 | 0.60 |
| config2 | 0.4 | 1 | 0 | echte | 0.0051 | 0.0489 | 0.83 |
| config2 | 0.4 | 1 | 1 | naive | 0.0902 | 0.0927 | 0.01 |
| config2 | 0.4 | 1 | 1 | global_est | 0.0432 | 0.0524 | 0.60 |
| config2 | 0.4 | 1 | 1 | echte | 0.0064 | 0.0483 | 0.89 |
| config2 | 0.5 | 0 | 0 | naive | 0.0676 | 0.0700 | 0.06 |
| config2 | 0.5 | 0 | 0 | global_est | 0.0744 | 0.0830 | 0.29 |
| config2 | 0.5 | 0 | 0 | echte | 0.0124 | 0.0374 | 0.79 |
| config2 | 0.5 | 0 | 1 | naive | 0.0229 | 0.0306 | 0.81 |
| config2 | 0.5 | 0 | 1 | global_est | 0.0776 | 0.0849 | 0.27 |
| config2 | 0.5 | 0 | 1 | echte | 0.0161 | 0.0334 | 0.81 |
| config2 | 0.5 | 1 | 0 | naive | 0.1400 | 0.1412 | 0.00 |
| config2 | 0.5 | 1 | 0 | global_est | 0.0546 | 0.0638 | 0.47 |
| config2 | 0.5 | 1 | 0 | echte | 0.0109 | 0.0586 | 0.73 |
| config2 | 0.5 | 1 | 1 | naive | 0.1144 | 0.1165 | 0.00 |
| config2 | 0.5 | 1 | 1 | global_est | 0.0540 | 0.0628 | 0.46 |
| config2 | 0.5 | 1 | 1 | echte | 0.0111 | 0.0606 | 0.72 |
| config3 | 0.1 | 0 | 0 | naive | 0.0205 | 0.0266 | 0.73 |
| config3 | 0.1 | 0 | 0 | global_est | 0.0049 | 0.0231 | 0.98 |
| config3 | 0.1 | 0 | 0 | echte | 0.0013 | 0.0251 | 0.97 |
| config3 | 0.1 | 0 | 1 | naive | 0.0050 | 0.0237 | 0.94 |
| config3 | 0.1 | 0 | 1 | global_est | 0.0113 | 0.0314 | 0.91 |
| config3 | 0.1 | 0 | 1 | echte | 0.0011 | 0.0257 | 0.93 |
| config3 | 0.1 | 1 | 0 | naive | 0.0029 | 0.0214 | 0.96 |
| config3 | 0.1 | 1 | 0 | global_est | 0.0119 | 0.0285 | 0.95 |
| config3 | 0.1 | 1 | 0 | echte | 0.0054 | 0.0245 | 0.94 |
| config3 | 0.1 | 1 | 1 | naive | 0.0239 | 0.0286 | 0.78 |
| config3 | 0.1 | 1 | 1 | global_est | 0.0083 | 0.0214 | 0.95 |
| config3 | 0.1 | 1 | 1 | echte | 0.0026 | 0.0235 | 0.98 |
| config3 | 0.2 | 0 | 0 | naive | 0.0423 | 0.0462 | 0.35 |
| config3 | 0.2 | 0 | 0 | global_est | 0.0103 | 0.0272 | 0.88 |
| config3 | 0.2 | 0 | 0 | echte | 0.0018 | 0.0281 | 0.92 |
| config3 | 0.2 | 0 | 1 | naive | 0.0098 | 0.0229 | 0.95 |
| config3 | 0.2 | 0 | 1 | global_est | 0.0221 | 0.0349 | 0.87 |
| config3 | 0.2 | 0 | 1 | echte | 0.0024 | 0.0253 | 0.97 |
| config3 | 0.2 | 1 | 0 | naive | 0.0173 | 0.0276 | 0.87 |
| config3 | 0.2 | 1 | 0 | global_est | 0.0113 | 0.0291 | 0.96 |
| config3 | 0.2 | 1 | 0 | echte | 0.0000 | 0.0257 | 0.96 |
| config3 | 0.2 | 1 | 1 | naive | 0.0494 | 0.0531 | 0.23 |
| config3 | 0.2 | 1 | 1 | global_est | 0.0207 | 0.0324 | 0.80 |
| config3 | 0.2 | 1 | 1 | echte | 0.0008 | 0.0294 | 0.92 |
| config3 | 0.3 | 0 | 0 | naive | 0.0633 | 0.0658 | 0.04 |
| config3 | 0.3 | 0 | 0 | global_est | 0.0149 | 0.0293 | 0.88 |
| config3 | 0.3 | 0 | 0 | echte | 0.0019 | 0.0272 | 0.94 |
| config3 | 0.3 | 0 | 1 | naive | 0.0132 | 0.0254 | 0.93 |
| config3 | 0.3 | 0 | 1 | global_est | 0.0362 | 0.0451 | 0.75 |
| config3 | 0.3 | 0 | 1 | echte | 0.0047 | 0.0255 | 0.96 |
| config3 | 0.3 | 1 | 0 | naive | 0.0194 | 0.0276 | 0.90 |
| config3 | 0.3 | 1 | 0 | global_est | 0.0265 | 0.0381 | 0.85 |
| config3 | 0.3 | 1 | 0 | echte | 0.0099 | 0.0298 | 0.92 |
| config3 | 0.3 | 1 | 1 | naive | 0.0702 | 0.0721 | 0.03 |
| config3 | 0.3 | 1 | 1 | global_est | 0.0234 | 0.0315 | 0.84 |
| config3 | 0.3 | 1 | 1 | echte | 0.0108 | 0.0325 | 0.90 |
| config3 | 0.4 | 0 | 0 | naive | 0.0822 | 0.0841 | 0.00 |
| config3 | 0.4 | 0 | 0 | global_est | 0.0181 | 0.0311 | 0.84 |
| config3 | 0.4 | 0 | 0 | echte | 0.0058 | 0.0307 | 0.85 |
| config3 | 0.4 | 0 | 1 | naive | 0.0128 | 0.0246 | 0.92 |
| config3 | 0.4 | 0 | 1 | global_est | 0.0542 | 0.0611 | 0.59 |
| config3 | 0.4 | 0 | 1 | echte | 0.0110 | 0.0277 | 0.93 |
| config3 | 0.4 | 1 | 0 | naive | 0.0293 | 0.0370 | 0.78 |
| config3 | 0.4 | 1 | 0 | global_est | 0.0282 | 0.0402 | 0.80 |
| config3 | 0.4 | 1 | 0 | echte | 0.0055 | 0.0294 | 0.91 |
| config3 | 0.4 | 1 | 1 | naive | 0.0958 | 0.0971 | 0.00 |
| config3 | 0.4 | 1 | 1 | global_est | 0.0354 | 0.0407 | 0.67 |
| config3 | 0.4 | 1 | 1 | echte | 0.0085 | 0.0285 | 0.95 |
| config3 | 0.5 | 0 | 0 | naive | 0.1029 | 0.1052 | 0.00 |
| config3 | 0.5 | 0 | 0 | global_est | 0.0219 | 0.0373 | 0.77 |
| config3 | 0.5 | 0 | 0 | echte | 0.0097 | 0.0385 | 0.78 |
| config3 | 0.5 | 0 | 1 | naive | 0.0219 | 0.0327 | 0.82 |
| config3 | 0.5 | 0 | 1 | global_est | 0.0608 | 0.0689 | 0.44 |
| config3 | 0.5 | 0 | 1 | echte | 0.0088 | 0.0305 | 0.92 |
| config3 | 0.5 | 1 | 0 | naive | 0.0299 | 0.0375 | 0.77 |
| config3 | 0.5 | 1 | 0 | global_est | 0.0463 | 0.0566 | 0.60 |
| config3 | 0.5 | 1 | 0 | echte | 0.0155 | 0.0357 | 0.88 |
| config3 | 0.5 | 1 | 1 | naive | 0.1184 | 0.1198 | 0.00 |
| config3 | 0.5 | 1 | 1 | global_est | 0.0406 | 0.0494 | 0.58 |
| config3 | 0.5 | 1 | 1 | echte | 0.0141 | 0.0438 | 0.77 |

### Summary by method

| Method | Mean |Bias| | Mean RMSE | Mean Coverage |
|--------|-----------|-----------|---------------|
| naive | 0.0469 | 0.0530 | 0.48 |
| global_est | 0.0250 | 0.0396 | 0.78 |
| echte | 0.0063 | 0.0329 | 0.90 |

## 7. Conclusions

1. The **product structure** $\text{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}$ holds exactly under asymmetric misclassification.
2. Assumption A2 (FPR = FNR) is **not required** for the bias decomposition; it only simplifies the formula.
3. Analytic formula matches MC with R-squared = 0.991748.
4. EC-HTE (stratified correction) outperforms global correction because it captures per-subgroup asymmetric error structure.
