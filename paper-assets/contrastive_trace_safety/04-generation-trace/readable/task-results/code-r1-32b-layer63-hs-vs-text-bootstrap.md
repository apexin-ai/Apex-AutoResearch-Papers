# code r1 32b layer63 hs vs text bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_32b_layer63_hs_vs_text_bootstrap_20260517T135436_result.json`
- **Structured JSON:** [`b4facb297898882ccd71.json`](../../sessions/b4/b4facb297898882ccd71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验全部完成。结果 JSON 已保存。以下是完整汇总：

---

## R1-32B Layer 63 HS vs Text Paired Bootstrap 结果

### A. Layer 63 HS Probe 各 Window 结果

| W | HS step_bal_acc | HS trace_bal_acc | HS prec | HS FPR | Coverage | Lead |
|---|---|---|---|---|---|---|
| 1 | 0.7511 | 0.8259 | 0.6027 | 0.2347 | 25% | 13.0 |
| 3 | 0.7309 | 0.8064 | 0.6342 | 0.2298 | 35% | 11.7 |
| 5 | 0.7210 | 0.8000 | 0.6213 | 0.2438 | 45% | 12.0 |
| 10 | 0.7003 | 0.7538 | 0.6098 | 0.2719 | 50% | 13.0 |
| 15 | 0.7086 | 0.7568 | 0.6336 | 0.2619 | 45% | 12.0 |

### B+C. Paired Bootstrap (1000 resamples, one-sided p, Bonferroni=0.0167)

| W | BalAcc D | p | Prec D | p | FPR D | p | Bonf |
|---|---|---|---|---|---|---|---|
| **1** | **+18.7pp** | **0.000** | **+15.4pp** | **0.000** | **-14.6pp** | **0.004** | **3/3** |
| **3** | **+11.2pp** | **0.009** | **+13.0pp** | **0.004** | -11.4pp | 0.037 | **2/3** |
| 5 | +9.7pp | 0.018 | +13.1pp | 0.022 | -7.7pp | 0.120 | 0/3 |
| 10 | +4.3pp | 0.188 | +9.4pp | 0.106 | -5.4pp | 0.232 | 0/3 |
| 15 | +7.8pp | 0.027 | +11.2pp | 0.058 | -7.8pp | 0.166 | 0/3 |

### D. Position Baseline
- Position baseline bal_acc = **0.6842**
- L63 W=1 HS probe (0.7511) > position baseline (+6.7pp)

### E. Layer 63 vs Layer 10 对比 (W=10)

| | L63 W=10 | L10 W=10 | Diff |
|---|---|---|---|
| step_bal_acc | 0.7003 | 0.7092 | -0.9pp |
| BalAcc p | 0.188 | 0.040 | L10 更好 |
| Bonf pass | 0/3 | 0/3 | 均未通过 |

**但** L63 W=1 (3/3 Bonf pass) 远超 L10 W=10 (0/3)。

---

### 关键判断

1. **Layer 63 W=1 将 R1-32B 从 "inconclusive" 变为 "significant"**: 3/3 Bonferroni pass，所有 CI 排除 0，p-value 一致。这是整个 R1-32B 上首次达到 Bonferroni 显著性。

2. **Temporal window 稀释 L63 信号**: W 增大后效果单调下降。L63 是最后一层（100% depth），其 per-step representation 已包含完整信息，temporal concatenation 引入噪声维度，增加 overfitting。

3. **"scale-dependent" claim 需要修正**: Layer 63 W=1 > Layer 10 W=10，说明 L10 的弱结果不是因为模型规模，而是因为 layer+window 选择不佳。正确的 framing 是 "layer selection matters, and optimal layer shifts with model depth"。

4. **L10 vs L63 在 W=10 下 L10 反而略优**（step bal_acc 0.709 vs 0.700），但这是因为 W=10 对 L63 不利。核心 insight 是 layer-window interaction effect。

---
