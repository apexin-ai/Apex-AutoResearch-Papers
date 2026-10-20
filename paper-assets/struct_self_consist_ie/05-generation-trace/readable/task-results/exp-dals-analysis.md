# exp dals analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_dals_analysis_20260518T055923_result.json`
- **Structured JSON:** [`92bdd34b4286d0c552d5.json`](../../sessions/92/92bdd34b4286d0c552d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行完毕，JSON 已保存到 `output/dals_analysis.json`。

## 结果总结

### 1. LP Range 分布

| Stat | SciERC (529) | Few-NERD (32565) | CoNLL (2756) |
|------|:---:|:---:|:---:|
| Mean | 0.062 | 0.088 | 0.077 |
| Median | 0.040 | 0.066 | 0.061 |
| P10/P90 | 0.019 / 0.122 | 0.010 / 0.196 | 0.000 / 0.157 |
| Zero% | 0% | 0.96% | 3.56% |

CoNLL 有最高的完全退化率 (3.6%)，SciERC 没有完全 tied 的 instance。

### 2. DALS Best Threshold 与 F1

| Dataset | Greedy | LP Sel | DALS-LP (best τ) | DALS-SJ | DALS-EM | Oracle |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|
| SciERC | 64.41 | 65.05 | **65.55** (τ=0.05) | 65.15 | 65.19 | 68.01 |
| Few-NERD | 74.90 | **76.25** | 76.24 (τ=0.001) | 76.24 | 76.24 | 77.57 |
| CoNLL | **90.88** | 89.81 | 90.57 (τ=0.10) | 90.08 | 90.47 | 91.39 |

### 3. DALS vs Pure LP vs Oracle

- **SciERC**: DALS 有效。τ=0.05 只放行 39.7% 的 instance 走 LP selection，但 gated set 内 LP 比 greedy 高 +2.88pp。整体 DALS 比 pure LP **+0.51pp**，比 greedy **+1.14pp**。
- **Few-NERD**: LP selection 本身就强 (+1.35pp vs greedy)。DALS 基本无改善，best τ=0.001 等于放行 92.4%，即几乎就是 pure LP。
- **CoNLL**: LP selection 反而 **伤害** F1 (-1.07pp vs greedy)。DALS (τ=0.10) 只放行 25.8% 走 LP，大幅恢复到 90.57，但仍低于 greedy 0.31pp。Oracle 显示只有 43 个 instance LP 更好 vs 117 个 greedy 更好。

### 4. 代理变量对比

LP range 在所有数据集上都是最好的 gating proxy：
- SciERC: LP-range +0.51pp vs LP > EM +0.14pp > SJ +0.10pp
- Few-NERD: 三者基本持平（均 ≈ pure LP）
- CoNLL: LP-range +0.76pp vs LP > EM +0.66pp > SJ +0.27pp

### 5. 核心结论

**DALS 在 LP selection 有正向但不稳定增益的场景（SciERC）有效，在 LP 本身就强或就弱的极端场景无效。** LP range 是最好的 gating signal，但 oracle gap 很大（SciERC: 65.55 vs 68.01），说明 LP range 作为 proxy 噪声仍然很高。DALS 的主要价值是在 CoNLL 这类 LP selection 有害的数据集上「止损」（从 -1.07pp 恢复到 -0.31pp），但无法反超 greedy。

---
