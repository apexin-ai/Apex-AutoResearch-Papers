# monitor v5 diag step250

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_diag_step250_20260518T172555_result.json`
- **Structured JSON:** [`c108f6f27534ba0984f6.json`](../../sessions/c1/c108f6f27534ba0984f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据充足了。训练已到 step 1250，且新的 [GATE] step=150 刚刷出。重要发现：之前的"step 100 诊断"数据因 stdout 缓冲混淆了不同步数的数据。

```
=== v5 第二次诊断 (@step 250-300, 含最新 step 1250) ===
训练状态: 运行中 (PID 3644)
当前步数: 1250 / 3000

⚠️ 重要修正: 上次"step 100 诊断"的 L_GAR=-0.167/L_NTP=0.82/loss=0.65 
实际对应 step 800，不是 step 100。原因是 [GATE] 统计行因 stdout 
缓冲延迟刷出，与 step 800 的训练日志交错，造成误读。
实际 step 100: L_GAR=-0.0166, L_NTP=1.3074, Loss=1.2908, Gate=0.8110

========================================
步数 250-300 数据 (原定诊断窗口)
========================================
              Step 250    Step 300
L_NTP:        1.1242      1.1170
L_GAR:       -0.0190     -0.0242
总 loss:      1.1052      1.0928 (正值)
Gate_mean:    0.8032      0.8059

gate_std/min/max/per-layer: 不可用 (详细 [GATE] 行尚未刷出)

→ 在 step 250-300: 完全绿灯。L_GAR 极小，远离 -0.8 阈值。

========================================
最新状态 (step 1250)
========================================
gate_std: 0.0286 (趋势: ↓, 0.0341→0.0611→0.0376→0.0286, 来自 [GATE] step=150)
gate_mean: 0.9395 (趋势: ↑, vs step250=0.8032)
gate_min: 0.8711 (来自 [GATE] step=150)
gate_max: 0.9805 (来自 [GATE] step=150)

Per-layer gate: 仅有 [GATE] step=150 的 summary，无 per-layer profile
  (step=150 的 PROFILE 行尚未刷出)

L_GAR 轨迹:
  s0:-0.016 → s250:-0.019 → s600:-0.033 → s700:-0.070 → s750:-0.141
  → s800:-0.167 → s900:-0.275 → s1000:-0.415 → s1150:-0.603
  → s1200:-0.674 → s1250:-0.500 (回弹)

L_NTP: 1.3513 (vs step250=1.1242, 有波动)
总 loss: 0.8513 (正值)

========================================
诊断结论: 黄灯
========================================
L_GAR 饱和: 否 (peak -0.674@s1200, 未破 -0.8)
  但 s600→s1200 加速明显，600 步内从 -0.033 → -0.674
  s1250 回弹至 -0.500，显示有振荡，非单调下坠

gate_std 退化: 否 (0.0286 > 0.02)
  但持续下降中 (0.0376→0.0286)，趋势需警惕
  如果保持下降速率，约 step 1800-2000 可能破 0.02

红灯条件 (L_GAR<-0.8 且 gate_std<0.02): 未触发

分析:
1. v5 与 v3b 走势有本质区别。v3b 的 L_GAR 指数下坠无回弹，
   v5 在 s1200→s1250 出现 -0.674→-0.500 的明显回弹，说明
   GAR loss 没有失控，优化器在 NTP loss 和 GAR loss 间仍有张力

2. Gate mean 0.94 偏高但 gate_std=0.0286 说明层间仍有分化，
   不是所有 gate 都在趋向 1.0

3. 预计风险窗口: step 1500-1800。如果 L_GAR 再次下探 <-0.7
   且 gate_std 同时跌破 0.025，建议准备中途调参方案
   (降低 lambda_gar 或降低 gate_lr_multiplier)

4. 建议: 在 step 1500 进行第三次诊断
```

---
