# check loto completion

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_loto-completion_20260516T033309_result.json`
- **Structured JSON:** [`17d2595b532ac1d8416c.json`](../../sessions/17/17d2595b532ac1d8416c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 无需清除（不存在）。

---

## LOTO 实验结果

### 数据分布
- 11 个 task types，总样本 2040
- **4 个 task types 有 det+internal 两类**（可计算 balanced_acc）
- **7 个 task types 全为 deterministic**（balanced_acc 退化，N/A）

### 2-class task types（balanced_acc, 8 seeds mean±std）

| Task Type | Mean bal_acc | Per-seed range | Majority-vote |
|-----------|:---:|:---:|:---:|
| chemistry-mix | **0.5503** | 0.508–0.586 | 0.50 |
| find-non-living-thing | **0.5986** | 0.564–0.638 | 0.50 |
| grow-fruit | **0.6715** | 0.567–0.733 | 0.50 |
| lifespan-longest-lived-then-shortest-lived | **0.5700** | 0.437–0.687 | 0.50 |

### 汇总

| Metric | Value |
|--------|-------|
| Grand mean bal_acc (2-class) | **0.5976 ± 0.0184** |
| Majority-vote baseline | 0.5000 |
| Cross-split reference | 0.4711 ± 0.0221 |

### 单类 task types（全 deterministic，bal_acc N/A）
find-animal, freeze, identify-life-stages-1, identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, measure-melting-point-unknown-substance

### 结论

原假设"router 在未见 task type 上 ≈ 50%（随机）"**未被支持**。LOTO bal_acc = 59.76% 显著高于 majority-vote baseline（50%）和 cross-split reference（47.1%）。Router 在 task-type 内表现出非平凡的泛化能力，routing signal 并非纯粹的 task-type 分类——存在跨样本迁移的特征学习。

不过需注意：7/11 task types 全为 deterministic（单类），只有 4 个 task type 能提供有效的 balanced_acc 评估，结论的覆盖面有限。

---
