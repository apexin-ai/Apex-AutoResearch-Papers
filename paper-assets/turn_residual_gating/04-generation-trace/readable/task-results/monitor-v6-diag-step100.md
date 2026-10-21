# monitor v6 diag step100

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v6_diag_step100_20260518T175925_result.json`
- **Structured JSON:** [`5cdca0ab28ed4af6b6ea.json`](../../sessions/5c/5cdca0ab28ed4af6b6ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是诊断结果。

---

## v6 step 100 诊断

**注意：** 日志中 "Step X" 是 micro-batch step，`[GATE] step=X` 是 global_step（每 8 micro-batch +1）。以下按 global_step 报告。

### gate 统计
| | mean | std | min | max |
|---|---|---|---|---|
| step=0 | 0.8097 | 0.0341 | 0.6836 | 0.8672 |
| step=50 | 0.8117 | 0.0612 | 0.6836 | 0.9805 |
| step=100 | 0.8737 | 0.0367 | 0.8164 | 0.9766 |

### gate profile (step=100)
```
L0:0.863  L1:0.871  L2:0.883  L3:0.848  L4:0.824  L5:0.871  L6:0.879
L7:0.836  L8:0.859  L9:0.848  L10:0.875 L11:0.891 L12:0.816 L13:0.824
L14:0.840 L15:0.891 L16:0.832 L17:0.891 L18:0.863 L19:0.891 L20:0.906
L21:0.871 L22:0.883 L23:0.914 L24:0.855 L25:0.902 L26:0.961 L27:0.977
```
- **Top-3 最低:** L12:0.816, L4:0.824, L13:0.824
- **Top-3 最高:** L27:0.977, L26:0.961, L23:0.914

### loss (micro-step 800 ≈ global_step 100)
L_NTP=0.8151, L_GAR=-0.1580, total Loss=0.6571

### 趋势
| 指标 | step 0 → 50 → 100 | 方向 |
|---|---|---|
| gate_mean | 0.810 → 0.812 → 0.874 | ↑ 加速上升 |
| gate_std | 0.034 → 0.061 → 0.037 | ↑↓ 先升后降 |
| gate_min | 0.684 → 0.684 → 0.816 | ↑ 大幅上升 |
| L_GAR | -0.016 → -0.013 → -0.158 | ↓ 加速下降 |

**更晚的数据（训练已到 micro-step 1150 ≈ global_step ~143）：**
```
Step 1000: L_GAR=-0.3072, Gate=0.8896
Step 1150: L_GAR=-0.3876, Gate=0.9227
```

### 判断

1. **gate_std >0.05?** **否。** step 50 时短暂达到 0.061，但 step 100 已回落到 0.037。gates 正在收敛，smooth_saturation **未能阻止退化**。

2. **L_GAR 有界?** **否。** L_GAR 从 -0.016 → -0.158 (gs100) → -0.388 (gs~143)，加速下降中。未出现在 target=0.5 附近减速的预期行为。按此趋势会重蹈 v5 覆辙（v5 同期约 -0.91）。

3. **layer pattern:** 最低 gate 在 **L12, L4, L13**。L4 与 Dongre L4/L5 goal-encoding onset 部分吻合，但 L12（mid-network）才是最低，不符合预期。**反转现象：** step 0 时 L27 最低（0.684），step 100 时 L27 变为最高（0.977），完全翻转。

### 核心问题

**所有 gate 正在被推向 1.0。** gate_mean 从 0.81 → 0.87 → 0.92（持续上升），gate_min 从 0.68 → 0.82。L_GAR 持续变负意味着优化器在通过拉高 gate 来降低 total loss。smooth_saturation 的 target=0.5 约束没有生效，GAR loss 仍然在无限制地奖励更高的 gate 值。

### 原始数据
```
[GATE] step=0 mean=0.8097 std=0.0341 min=0.6836 max=0.8672
[GATE-PROFILE] step=0 L0:0.816 L1:0.867 L2:0.816 L3:0.801 L4:0.805 L5:0.812 L6:0.820 L7:0.789 L8:0.832 L9:0.793 L10:0.812 L11:0.812 L12:0.789 L13:0.801 L14:0.816 L15:0.832 L16:0.781 L17:0.828 L18:0.770 L19:0.832 L20:0.855 L21:0.832 L22:0.812 L23:0.832 L24:0.793 L25:0.773 L26:0.863 L27:0.684
[GATE] step=50 mean=0.8117 std=0.0612 min=0.6836 max=0.9805
[GATE] step=100 mean=0.8737 std=0.0367 min=0.8164 max=0.9766
[GATE-PROFILE] step=100 L0:0.863 L1:0.871 L2:0.883 L3:0.848 L4:0.824 L5:0.871 L6:0.879 L7:0.836 L8:0.859 L9:0.848 L10:0.875 L11:0.891 L12:0.816 L13:0.824 L14:0.840 L15:0.891 L16:0.832 L17:0.891 L18:0.863 L19:0.891 L20:0.906 L21:0.871 L22:0.883 L23:0.914 L24:0.855 L25:0.902 L26:0.961 L27:0.977

Epoch 0 Step 0   | L_NTP=2.0275 L_GAR=-0.0161 Loss=2.0114 | Gate=0.8097
Epoch 0 Step 400  | L_NTP=1.1114 L_GAR=-0.0134 Loss=1.0981 | Gate=0.8178
Epoch 0 Step 800  | L_NTP=0.8151 L_GAR=-0.1580 Loss=0.6571 | Gate=0.8715
Epoch 0 Step 1000 | L_NTP=0.8992 L_GAR=-0.3072 Loss=0.5920 | Gate=0.8896
Epoch 0 Step 1150 | L_NTP=1.0418 L_GAR=-0.3876 Loss=0.6542 | Gate=0.9227
```

---
