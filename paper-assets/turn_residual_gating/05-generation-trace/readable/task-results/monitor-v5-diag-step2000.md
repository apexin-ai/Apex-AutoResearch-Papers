# monitor v5 diag step2000

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_diag_step2000_20260518T173943_result.json`
- **Structured JSON:** [`0ea471904593330b8686.json`](../../sessions/0e/0ea471904593330b8686.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。以下是诊断报告。

```
=== v5 @step 2000 诊断 ===
训练状态: 运行中（已到 step 2350+）
当前步数: ~2350 / 3000 (epoch 0 ~78%)

--- 核心指标 (optimizer step=250, ~data step 2000) ---
gate_std:  0.0225  (vs s1500=0.0318) ⚠️ 回落，回升未能持续
gate_mean: 0.9586  (vs s1500=0.9442) 继续上升
gate_min:  0.9062  (L??)  (vs s1500=0.8633) min 大幅抬升
gate_max:  0.9961  (vs s1500=0.9883)

--- 最新指标 (optimizer step=300, ~data step 2400) ---
gate_std:  0.0219  (继续微降)
gate_mean: 0.9651  (继续爬升)
gate_min:  0.9180
gate_max:  0.9961

--- Data step 2000 行 ---
L_GAR: -0.8977  (vs s1500=-0.830) 继续下探
L_NTP:  0.7611
总 loss: -0.1365

--- L_GAR 趋势 (s1500→s2350) ---
s1500: -0.830 → s1600: -0.858 → s1700: -0.867 → s1800: -0.880
s1850: -0.889 → s1950: -0.892 → s2000: -0.898 → s2050: -0.901
s2150: -0.912 → s2200: -0.906 → s2300: -0.904 → s2350: -0.914
→ 稳定在 -0.90 ~ -0.91，接近饱和

--- Per-layer gate profile (step=300, 最新) ---
  L0 :0.918   L1 :0.996   L2 :0.988   L3 :0.984
  L4 :0.957   L5 :0.945   L6 :0.961   L7 :0.961
  L8 :0.957   L9 :0.961   L10:0.973   L11:0.953
  L12:0.918   L13:0.926   L14:0.934   L15:0.945
  L16:0.965   L17:0.969   L18:0.973   L19:0.965
  L20:0.977   L21:0.988   L22:0.984   L23:0.988
  L24:0.980   L25:0.973   L26:0.996   L27:0.988

vs step=200 关键变化:
  L0:  0.863→0.918 (+0.055) 不再是明显低点
  L6:  0.910→0.961 (+0.051)
  L7:  0.918→0.961 (+0.043)
  L8:  0.898→0.957 (+0.059)
  L12: 0.895→0.918 (+0.023) 仍为相对低点
  L13: 0.898→0.926 (+0.028) 仍为相对低点
  range: [0.863,0.988]→[0.918,0.996] 区间压缩

趋势总结:
- gate_std: step 200 的回升(0.0318)未持续，重新下滑至 0.022，分化信号衰减
- gate_mean: 持续上升 0.944→0.959→0.965，向 0.97 逼近
- gate_min: 0.863→0.906→0.918，最低层也在快速上涨，底部抬升
- L_GAR: 饱和在 -0.90~-0.91，梯度驱动力不足以维持分化
- Per-layer: 中间层(L6-L14)仍可见微弱的相对低谷，但绝对值全部>0.918
  残存结构: L0/L12/L13 相对最低(~0.92)，首尾层 L1/L26 最高(~0.996)

诊断结论: ⚠️ 黄灯偏红
```

**核心问题**: gate_std 的回升是假信号，已经二次下滑到 0.022。L_GAR 饱和在 -0.91 意味着 GAR loss 的梯度已经很弱，无法阻止 gate 继续向 1.0 收敛。虽然 per-layer profile 仍有微弱结构（L0/L12/L13 相对低），但所有层都已 >0.918，分化幅度只有 ~0.08，对比 step 200 时 ~0.13 的幅度在持续压缩。

按当前趋势，到 epoch 0 结束(step 3000)时 gate_mean 可能达到 0.97+，std 可能降到 <0.02，实质上变成 near-identity residual connections。训练仍在正常运行，但 gating 机制的有效分化正在消失。

---
