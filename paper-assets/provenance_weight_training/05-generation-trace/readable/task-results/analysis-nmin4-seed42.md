# analysis nmin4 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nmin4_seed42_20260515T211842_result.json`
- **Structured JSON:** [`bb9c1b08426edb9dc104.json`](../../sessions/bb/bb9c1b08426edb9dc104.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## nmin4_seed42 实验摘要

### 核心结果

| 指标 | 值 |
|------|-----|
| **eval PPL** | **17.6947** |
| eval loss | 2.8733 |
| train loss | 7.989 |
| b_star | 全程 = 0.0 (24412/24412, 100%) |
| ESS | 全程 = 4.0 (= n_min = batch_size) |
| 训练时长 | 4.54h, 6103 steps |

### 对比基准

| 实验 | eval PPL | vs uniform |
|------|----------|------------|
| uniform_seed42 | 17.6918 | baseline |
| **nmin4_seed42** | **17.6947** | **+0.003** |
| adaptive_fix_seed42 | 17.6527 | -0.039 |
| nmin1_seed42 | 17.789 | +0.097 |

### Hypothesis 验证: **SUCCESS**

n_min=4 (= batch_size) 时 b\*=0 强制退化为 uniform weighting，PPL 与 uniform baseline 仅差 0.003（远在 ±0.02 容差内）。理论预测完全成立。

### n_min robustness 完整图景

- **n_min=1**: 过度 downweight，PPL=17.789（+0.097），有害
- **n_min=2**: 最优点，PPL=17.6527（-0.039），adaptive 发挥最大效果
- **n_min=3**: 有效但受限（ESS 动态范围 [3,4] 较窄）
- **n_min=4**: 退化为 uniform，PPL≈17.69，b\*=0——边界条件验证通过

这证明 n_min 存在一个 sweet spot：太小则过度 reweight（方差过大），太大则约束过强（退化为 uniform），n_min=2 在 batch_size=4 时最优。

---
