# critical exp029b fix and postprocess

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_exp029b_fix_and_postprocess_20260518T024623_result.json`
- **Structured JSON:** [`cdbd6446b629781735ee.json`](../../sessions/cd/cdbd6446b629781735ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 全部完成。下面是完整结果汇报。

---

## Step 4: 完整结果汇报

### 1. 训练状态

| 项目 | 值 |
|------|-----|
| Total steps | 1170/1170 |
| Epoch | 10.0 |
| Final loss | 0.0084 |
| Best checkpoint | None (未开启 eval-based selection) |
| 训练时长 | ~58 min |

### 2. 10-epoch 核心指标

| Metric | Value |
|--------|-------|
| **Degeneracy (CF1 gold-filtered)** | **47.83%** |
| Greedy F1 | 0.6491 |
| Oracle F1 | 0.7331 |
| Headroom | 8.40 pp |
| LP selection F1 | 0.6567 (+0.75 pp) |
| Within-instance rho(LP,F1) mean | 0.0685 |
| Within-instance rho(LP,F1) median | 0.1201 |
| LP range mean | 0.033337 |
| LP range median | 0.023715 |
| Valid within-rho instances | 276/529 (52.2%) |

### 3. 3-point Epoch Curve 对比表

| Metric | 3-epoch (029a) | 5-epoch (baseline) | 10-epoch (029b) |
|--------|---------------|-------------------|----------------|
| **Degeneracy %** | **6.43%** | **17.58%** | **47.83%** |
| Greedy F1 | 0.6501 | 0.6094 | 0.6491 |
| Oracle F1 | 0.7998 | N/A | 0.7331 |
| LP sel delta (pp) | -1.18 | -0.07 | **+0.75** |
| Within-inst med rho | 0.3172 | 0.2474 | 0.1201 |
| LP range mean | 0.085427 | N/A | 0.033337 |
| FK rho | 0.5302 | N/A | 0.3413 |
| SJ rho | 0.5160 | N/A | 0.3441 |

### 4. 单调递增趋势确认

**CONFIRMED**: 10ep (47.83%) > 5ep (17.58%) > 3ep (6.43%)

Degeneracy 呈强单调递增趋势。从 3ep 到 10ep 增长了 41.4pp，加速效应明显（3→5 增长 11.2pp，5→10 增长 30.2pp）。

附带观察：
- LP range 随 epoch 单调递减（0.085 → 0.033），说明 logprob 多样性急剧下降
- Within-instance rho 随 epoch 单调递减（0.317 → 0.247 → 0.120），LP 的 F1 区分能力随过拟合恶化
- LP selection 从负变正（-1.18 → -0.07 → +0.75），但这不代表 LP 更好用，而是因为 oracle headroom 从 15pp 缩小到 8.4pp，天花板大幅降低

---
