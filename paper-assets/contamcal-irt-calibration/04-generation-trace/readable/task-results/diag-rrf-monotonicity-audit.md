# diag rrf monotonicity audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_rrf-monotonicity-audit_20260514T232255_result.json`
- **Structured JSON:** [`65898e3d7020d6e220a5.json`](../../sessions/65/65898e3d7020d6e220a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全局数据已收齐。以下是完整审计报告。

---

## Signal 分数对照表

### ARC Challenge

| Model | Scale | Dosage | S1_emb | S2_mkp | S4_sc | RRF_norm | Raw Acc (aligned) |
|-------|-------|--------|--------|--------|-------|----------|-------------------|
| 0.5B_d000 | 0.5B | 0 | 0.5946 | 1.7079 | -0.9538 | 0.1424 | 0.4693 |
| 0.5B_d005 | 0.5B | 5 | 0.6212 | 1.4104 | -0.8949 | 0.1812 | 0.3285 |
| 0.5B_d025 | 0.5B | 25 | 0.6932 | 1.3887 | -0.9105 | 0.1713 | 0.3251 |
| 0.5B_d100 | 0.5B | 100 | 0.8998 | 1.4063 | -0.8793 | 0.2101 | 0.2944 |
| 1.5B_d000 | 1.5B | 0 | 0.5946 | 1.7060 | -0.9127 | 0.1865 | 0.7722 |
| 1.5B_d005 | 1.5B | 5 | 0.6212 | 1.3178 | -0.9267 | 0.1825 | 0.7688 |
| 1.5B_d025 | 1.5B | 25 | 0.6932 | 1.3894 | -0.9156 | 0.1660 | 0.7688 |
| 1.5B_d100 | 1.5B | 100 | 0.8998 | 1.2070 | -0.8913 | 0.2010 | 0.7688 |

### GSM8K

| Model | Scale | Dosage | S1_emb | S2_mkp | S4_sc | RRF_norm | Raw Acc (aligned) |
|-------|-------|--------|--------|--------|-------|----------|-------------------|
| 0.5B_d000 | 0.5B | 0 | 0.6131 | 1.6532 | -0.9408 | 0.1882 | 0.3692 |
| 0.5B_d005 | 0.5B | 5 | 0.6292 | 1.4497 | -0.9044 | 0.1534 | 0.3624 |
| 0.5B_d025 | 0.5B | 25 | 0.6779 | 1.3470 | -0.9444 | 0.2094 | 0.3662 |
| 0.5B_d100 | 0.5B | 100 | 0.8103 | 1.2838 | -0.9106 | 0.1919 | 0.3654 |
| 1.5B_d000 | 1.5B | 0 | 0.6131 | 1.6282 | -0.9640 | 0.1637 | 0.6543 |
| 1.5B_d005 | 1.5B | 5 | 0.6292 | 1.3903 | -0.8861 | 0.1773 | 0.6482 |
| 1.5B_d025 | 1.5B | 25 | 0.6779 | 1.3658 | -0.8389 | 0.1685 | 0.6535 |
| 1.5B_d100 | 1.5B | 100 | 0.8103 | 1.2319 | -0.9374 | 0.1946 | 0.6497 |

## RRF 单调性检验

- **ARC 0.5B**: NOT MONOTONIC — d005(0.181) ≥ d025(0.171)
- **ARC 1.5B**: NOT MONOTONIC — d000(0.187) ≥ d005(0.183) ≥ d025(0.166)
- **GSM8K 0.5B**: NOT MONOTONIC — d000(0.188) ≥ d005(0.153); d025(0.209) ≥ d100(0.192)
- **GSM8K 1.5B**: NOT MONOTONIC — d005(0.177) ≥ d025(0.169)

**S1 (embedding) 单独是单调的**：0.5946 → 0.6212 → 0.6932 → 0.8998（两个 scale 完全相同，因为 S1 是 model-agnostic 的）。RRF 融合后 S2/S4 的噪声破坏了 S1 的单调性。

## load_exp002_signals() 返回值分析

- **返回类型**: scalar（per-model 标量）
- **关键行**: `scores.append(float(rrf.mean()))` — per-item RRF array 被压缩为 mean
- **维度**: 输入 N_items → 输出 1 个 float/model
- **信息损失**: 严重。哪些 item 被污染的信息全部丢失

## build_exposure_matrix 期望输入

```python
def build_exposure_matrix(dosages, tau):
    max_d = dosages.max() if dosages.max() > 0 else 1.0
    return np.outer(dosages / max_d, tau)
```

- **dosages 参数**: 在信号模式下接收 `signal_scores`（per-model 标量数组），形状 `(N_models,)`
- **tau 参数**: per-item 曝光分数，来自 `load_exposure_scores()`。**无 exposure_file 时默认全 1**
- **实际 exposure matrix**: `outer(signal_scores/max_s, ones)` = 所有 item 同等权重的 rank-1 矩阵
- **维度不匹配**: N — 形状 `(N_models, N_items)` 正确，但内容退化为 rank-1

## 代码版本分歧（关键发现）

**Pooled v2 运行日志**显示 D024 baseline=0.5946（= S1_embedding d000 mean），delta 值 [0.0, 0.027, 0.099, 0.305]——完美匹配 S1 embedding 差值。**当前代码**用 RRF 融合（baseline 应为 ~0.14/0.19）。

结论：pooled v2 结果是用 **S1-only 代码**（单调）产出的，当前代码已切换到 **RRF 融合**（不单调）。用 RRF 重跑会更差。

## 根因结论

**Reviewer 假设错误。根因不是 RRF 不单调——是 accuracy 本身随 contamination 下降。**

| Bench | Scale | d0 Acc | d100 Acc | Delta | 方向 |
|-------|-------|--------|----------|-------|------|
| ARC | 0.5B | 0.469 | 0.294 | **-0.175** | 下降 |
| ARC | 1.5B | 0.772 | 0.769 | -0.003 | 持平 |
| GSM8K | 0.5B | 0.369 | 0.365 | -0.004 | 持平 |
| GSM8K | 1.5B | 0.654 | 0.650 | -0.005 | 持平 |

ARC gamma=-2.35 是 **正确的**——LoRA contamination 实际降低了 ARC 成绩（0.5B 从 0.469 暴跌到 0.294）。IRT 模型准确捕捉到了 exposure 与分数的负相关。

GSM8K gamma=0.19 (CI 跨 0) 也正确——contamination 对 GSM8K 基本没影响，gamma 接近 0。

**三层问题**：
1. **实验设计层**：LoRA contamination 导致 catastrophic forgetting（特别是 ARC 0.5B），不是 score inflation。方法假设 contamination 提升分数，但数据说相反。
2. **信号融合层**：RRF 融合 S2/S4 噪声破坏 S1 单调性。当前代码与产出 pooled v2 结果的代码版本不一致。
3. **exposure 维度层**：`float(rrf.mean())` 把 per-item 信号压缩成标量，`tau=ones` 导致 exposure matrix 对所有 item 无差别。丢失了"哪些 item 被污染"的信息。

---
