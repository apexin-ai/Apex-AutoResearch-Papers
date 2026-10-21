# analysis r11 q3 tost logit

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-q3-tost-logit_20260517T100020_result.json`
- **Structured JSON:** [`2fb5b20204bb6a8ed2c6.json`](../../sessions/2f/2fb5b20204bb6a8ed2c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果很有意义，审稿人的 concern 有一定道理。

## 结果摘要

### Comparison Table

| Metric | Linear | Logit |
|---|---|---|
| Interaction coeff | 0.47 pp | 0.111 logit units |
| SE | 0.90 pp | 0.055 logit |
| p (H0: coeff=0) | 0.608 | **0.047** |
| R-squared | 0.523 | 0.536 |
| 90% CI | [-1.04, 1.97] pp | [0.019, 0.203] logit |
| TOST margin | ±3.00 pp | ±0.156 logit (≈±3pp at median) |
| TOST p | **0.003** | 0.209 |
| TOST conclusion | **equivalent** | **inconclusive** |

### 关键发现

1. **Floor effect 确实存在**: Logit scale 上 interaction 边际显著 (p=0.047)，而 linear scale 上完全不显著 (p=0.608)。90% CI 在 logit scale 上整体为正 [0.019, 0.203]，不穿越零。

2. **Back-transformed interaction at different baselines**:
   - 在 p=0.51 (floor)：2.78 pp
   - 在 p=0.65 (中位数附近)：2.53 pp
   - 在 p=0.75：2.09 pp
   - Linear scale 观测值：0.47 pp
   - Ratio = 4.6x — 线性标度显著压缩了真实 interaction

3. **TOST 结论翻转**: Linear scale TOST passes (p=0.003)，但 logit scale TOST fails (p=0.209)。这意味着在校正 floor compression 后，无法确认 interaction 可以忽略。

4. **不过 back-transformed interaction 仍在 3pp 以内** (2.78pp at worst case p=0.51)，只是 CI 太宽导致 TOST 没有足够 power 来 reject。

### 数据分布

- High BCS batches 更接近 floor：mean=0.68, min=0.50, 3/33 batches < 55%
- Low BCS batches：mean=0.80, min=0.61
- count=40 的 batches 最接近 floor (mean=0.59)

### 对论文的影响

审稿人的 concern 有实质内容。建议在 response 中：
- 承认 logit scale 上 interaction 更大
- 报告 back-transformed 值 (2.78pp at floor) 仍在 3pp margin 以内
- 解释 TOST inconclusive 是 power 问题 (n=69, wide CI)，不是 effect size 问题
- 可以补充：即使在 logit scale，point estimate 仍然 modest，只是 sample size 不足以排除 equivalence

---
