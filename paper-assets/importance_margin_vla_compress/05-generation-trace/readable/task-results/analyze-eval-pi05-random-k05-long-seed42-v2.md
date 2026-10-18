# analyze eval pi05 random k05 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_long_seed42_v2_20260523T213627_result.json`
- **Structured JSON:** [`dec222dd5ebdcd5972f1.json`](../../sessions/de/dec222dd5ebdcd5972f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果报告

### eval_pi05_random_k05_long_seed42_v2

| 指标 | 值 |
|------|-----|
| **Overall SR** | **46.8%** (234/500) |
| **耗时** | 160 min |
| **EXIT_CODE** | 0 |
| **CPU RNG fixed** | Yes |

### Per-task breakdown

| Task | Description | SR |
|------|-------------|-----|
| T0 | alphabet soup + tomato → basket | 70% |
| T1 | cream cheese + butter → basket | 40% |
| T2 | stove + moka pot | 72% |
| T3 | bowl → bottom drawer | 72% |
| T4 | white mug left + yellow mug right | 52% |
| T5 | book → caddy | **20%** |
| T6 | white mug plate + chocolate pudding | **26%** |
| T7 | alphabet soup + cream cheese → basket | 56% |
| T8 | both moka pots → stove | **4%** |
| T9 | yellow mug → microwave | 56% |

### 关键对比

| 对比项 | SR | 备注 |
|--------|-----|------|
| **v2 (CPU RNG fix)** | **46.8%** | 本次 |
| v1 (pre-fix) | 50.2% | **-3.4pp**，CPU RNG 修复导致轻微下降 |
| π0.5 baseline (k=1.0) | 91.6% | 剪掉 50% token 损失 44.8pp |
| π0.5 L2norm k=0.5 Long | 50.2% | — |

### Importance Margin (L2norm vs Random, k=0.5, Long)

**L2norm 50.2% − Random 46.8% = +3.4pp**

L2norm 在 Long 套件 k=0.5 下仅比 Random 高 3.4pp，margin 很小。对比其他 k 值（registry 数据）：
- k=0.3: L2norm 39.0% vs Random 29.0% → **+10.0pp**
- k=0.5: L2norm 50.2% vs Random 46.8% → **+3.4pp**
- k=0.7: L2norm 60.0% vs Random 64.6% → **-4.6pp** (Random 反超)
- k=0.85: L2norm 78.0% vs Random 44.4% → **+33.6pp**
- k=0.9: L2norm 81.0% vs Random 31.8% → **+49.2pp**

Long 套件的 importance margin 在低 k 值处较小（k=0.5 仅 +3.4pp），在高 k 值处 L2norm 大幅领先（因为 Random 在 k=0.85-0.9 出现 disruption collapse）。k=0.7 处 Random 反超 L2norm，显示 Long 套件也存在 non-monotonic 行为。

---
