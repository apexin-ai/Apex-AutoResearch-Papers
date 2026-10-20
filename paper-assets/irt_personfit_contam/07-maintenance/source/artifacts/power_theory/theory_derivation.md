# Theoretical Power Analysis for lz* Contamination Detection

## 1. Model Setup

### 4PL IRT Model
$$P_i(\theta) = c_i + (d_i - c_i) \cdot \frac{1}{1 + e^{-a_i(\theta - b_i)}}$$

### Contamination Model
Contamination fraction $\pi$ forces a random $\lfloor n\pi \rceil$ items correct:
$$\mathbb{E}[x_i | \theta_0, \pi] = P_i(\theta_0) + \pi \cdot Q_i(\theta_0)$$

### lz* Statistic (Snijders, 2001)
$$lz^* = \frac{l(\hat\theta) - \mathbb{E}[l(\hat\theta)]}{\sqrt{\mathrm{Var}^*(\hat\theta)}}$$
where $\mathrm{Var}^* = \mathrm{Var}_l - C_\theta^2 / I_\theta$ corrects for the estimated $\hat\theta$.

Under the null: $lz^* \sim N(0, 1)$ approximately.

## 2. Expected lz* Under Contamination

### Expected MLE Bias
The expected $\hat\theta$ solves the expected score equation:
$$\sum_{i=1}^n \bigl(\mathbb{E}[x_i] - P_i(\theta)\bigr) \cdot h_i(\theta) = 0$$
where $h_i = P_i' / (P_i Q_i)$.

Since $\mathbb{E}[x_i] > P_i(\theta_0)$ for $\pi > 0$, $\mathbb{E}[\hat\theta] > \theta_0$ (upward bias).

### Mean Shift
$$\delta(\theta_0, \pi) = \frac{\sum_{i=1}^n \bigl(\mathbb{E}[x_i] - P_i(\hat\theta)\bigr) \cdot g_i(\hat\theta)}{\sqrt{\mathrm{Var}^*(\hat\theta)}}$$
where $g_i(\theta) = \log(P_i / Q_i)$.

### Conditional Variance
$$\mathrm{Var}[lz^* | \theta_0, \pi] = \frac{\sum_{i=1}^n \mathrm{Var}[x_i] \cdot g_i(\hat\theta)^2}{\mathrm{Var}^*(\hat\theta)}$$
with $\mathrm{Var}[x_i] = \mathbb{E}[x_i] \cdot Q_i(\theta_0) \cdot (1 - \pi)$.

## 3. Power ∝ √n Scaling (Proposition 1)

**Proposition**: $\delta(\theta_0, \pi) \propto \sqrt{n}$ for fixed $\theta_0$ and $\pi > 0$.

**Proof**: The numerator $\sum_i \epsilon_i = n \cdot \bar\epsilon$ is $O(n)$. The denominator $\sqrt{\mathrm{Var}^*} = \sqrt{\sum_i v_i} = O(\sqrt{n})$. Therefore:
$$\delta = \frac{n \cdot \bar\epsilon}{\sqrt{n \cdot \bar v}} = \sqrt{n} \cdot \underbrace{\frac{\bar\epsilon}{\sqrt{\bar v}}}_{\delta_1}$$

The per-item noncentrality $\delta_1$ is $O(1)$ and depends only on item parameters and $(\theta_0, \pi)$.

**Empirical verification** (E[lz*] regressed on $\sqrt{n}$ across 5 benchmarks):

- π=5%: α=-0.015799, R²=0.8860
- π=10%: α=-0.030571, R²=0.8840
- π=15%: α=-0.044420, R²=0.8821
- π=25%: α=-0.069480, R²=0.8794
- π=50%: α=-0.113481, R²=0.8674

## 4. Marginal Power Formula (Proposition 2)

Integrating over $\theta_0 \sim N(0,1)$ via Gauss-Hermite quadrature ($K=30$ nodes):
$$\mathrm{Power}(n, \pi) = \sum_{k=1}^K w_k \left[\Phi\!\left(\frac{-z_\alpha - \delta_k}{\sigma_k}\right) + 1 - \Phi\!\left(\frac{z_\alpha - \delta_k}{\sigma_k}\right)\right]$$
where $\delta_k = \delta(\theta_k, \pi)$ and $\sigma_k = \sqrt{\mathrm{Var}[lz^*|\theta_k, \pi]}$.

For two-sided detection: $z_\alpha = 1.96$.

## 5. Validation Against Simulation

| Metric | Overall R² | Overall RMSE |
|--------|-----------|-------------|
| two_sided | 0.9572 | 0.0746 |
| left_tail | 0.9764 | 0.0473 |
| right_tail | 0.9846 | 0.0401 |
| mean_lz | 0.9948 | 0.5418 |

Per-benchmark R² (two-sided power):

- MMLU: R² = 0.9831
- HellaSwag: R² = 0.9678
- GSM8K: R² = 0.9709
- ARC-C: R² = 0.8054
- HumanEval: R² = 0.9698

## 6. Key Formulas Summary

For paper citation:

1. **Expected response**: $\mathbb{E}[x_i | \theta_0, \pi] = P_i(\theta_0) + \pi \cdot (1 - P_i(\theta_0))$
2. **Expected θ̂**: Solve $\sum_i (\mathbb{E}[x_i] - P_i(\theta)) h_i(\theta) = 0$
3. **Mean shift**: $\delta(\theta_0, \pi) = \sum_i (\mathbb{E}[x_i] - P_i(\hat\theta)) g_i(\hat\theta) / \sqrt{\mathrm{Var}^*}$
4. **Scaling**: $\delta \propto \sqrt{n}$, so power increases with benchmark size
5. **Power**: Integrate conditional power over $\theta_0 \sim N(0,1)$
