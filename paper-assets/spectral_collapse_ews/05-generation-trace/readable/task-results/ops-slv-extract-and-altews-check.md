# ops slv extract and altews check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_slv-extract-and-altews-check_20260518T130252_result.json`
- **Structured JSON:** [`508ca33b540732f28470.json`](../../sessions/50/508ca33b540732f28470.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部提取。以下是汇总：

---

## 任务 1: SLV (log_det) 对比表

| Gen | r=0 (exp_001) | r=0.2 (exp_007) | r=0.3 (exp_008) | r=0.5 (exp_004) |
|-----|---------------|-----------------|-----------------|-----------------|
| 0   | 2366.7        | 2366.7          | 2366.7          | 2366.7          |
| 1   | 2464.8        | 2367.5          | 2366.1          | 2366.6          |
| 2   | 2469.9        | -               | -               | 2395.4          |
| 3   | 2440.6        | -               | -               | 2425.6          |
| 4   | 2405.0        | -               | -               | 2451.7          |
| 5   | 2370.2        | -               | -               | 2486.3          |
| 6   | 2335.2        | -               | -               | 2507.6          |
| 7   | 2304.2        | -               | -               | 2525.6          |
| 8   | 2252.1        | -               | -               | 2544.0          |
| 9   | 2207.6        | -               | -               | 2562.1          |
| 10  | 2178.9        | -               | -               | 2573.2          |

**exp_007 (r=0.2) 和 exp_008 (r=0.3) 都只有 Gen 0-1 数据。**

关键观察：
- **r=0**: Gen 0→1 log_det 上升 (+98.1)，之后持续下降至 2178.9 (collapse)
- **r=0.2**: Gen 0→1 几乎不变 (+0.8)
- **r=0.3**: Gen 0→1 微降 (-0.6)
- **r=0.5**: Gen 0→1 不变 (-0.1)，之后持续上升至 2573.2

### eff_rank 对比

| Gen | r=0 (exp_001) | r=0.2 (exp_007) | r=0.3 (exp_008) | r=0.5 (exp_004) |
|-----|---------------|-----------------|-----------------|-----------------|
| 0   | 417.5         | 417.5           | 417.5           | 417.5           |
| 1   | 491.8         | 476.7           | 476.9           | 477.9           |

### PPL 对比

| Gen | r=0 (exp_001) | r=0.2 (exp_007) | r=0.3 (exp_008) | r=0.5 (exp_004) |
|-----|---------------|-----------------|-----------------|-----------------|
| 0   | 9.55          | 9.55            | 9.55            | 9.55            |
| 1   | 11.38         | 10.28           | 10.19           | 10.08           |

---

## 任务 2: alt-EWS v2 文件状态

三个 v2 文件全部存在 (2026-05-18 19:32-19:34 创建)：
- `alternative_ews_v2_exp001.json` (8,372 bytes)
- `alternative_ews_v2_exp004.json` (8,376 bytes)
- `alternative_ews_v2_exp006.json` (8,381 bytes)

### RankMe 趋势

| Gen | r=0 (exp_001) | r=0.5 fixed (exp_004) | r=0.5 adaptive (exp_006) |
|-----|---------------|-----------------------|--------------------------|
| 0   | 707.1         | 712.4                 | 706.3                    |
| 1   | 738.7         | 733.6                 | 733.3                    |
| 2   | 745.1         | 742.3                 | 741.9                    |
| 3   | 744.6         | 752.6                 | 750.1                    |
| 4   | 735.8         | 755.6                 | 756.2                    |
| 5   | 735.5         | 771.0                 | 770.3                    |
| 6   | 728.7         | 776.5                 | 775.9                    |
| 7   | 724.8         | 784.1                 | 779.5                    |
| 8   | 720.7         | 792.0                 | 794.1                    |
| 9   | 717.5         | 804.3                 | 799.7                    |
| 10  | 709.9         | 810.6                 | 810.6                    |

**RankMe 趋势**：
- **r=0**: Gen 0→2 上升后持续下降 (707→745→710)，与 log_det collapse 一致
- **r=0.5 (两种)**: 持续单调上升 (706/712→811)，谱多样性保持扩展

---
