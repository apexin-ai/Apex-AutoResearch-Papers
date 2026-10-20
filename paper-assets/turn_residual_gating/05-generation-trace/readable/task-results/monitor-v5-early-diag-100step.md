# monitor v5 early diag 100step

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_early_diag_100step_20260518T171240_result.json`
- **Structured JSON:** [`add0e603465fb68a0ac8.json`](../../sessions/ad/add0e603465fb68a0ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是完整诊断报告。

```
=== v5 早期诊断 (@optimizer step 100, batch step 800) ===
训练状态: 运行中 (PID 3644)
当前步数: optimizer step 100 / 3000

gate_std: 0.0376 (趋势: ↑ from 0.0341@s0, peaked 0.0611@s50, 回落但仍 >0.02)
gate_mean: 0.8737 (趋势: ↑ from 0.8097@s0, 稳步上升)
gate_min:  0.8125 (from 0.6836@s0, 大幅上升)
gate_max:  0.9766 (from 0.8672@s0, 已接近饱和)

Per-layer gate @step100:
  最低: L12=0.812, L13=0.820, L4=0.824, L16=0.828
  最高: L27=0.977, L26=0.961, L23=0.914, L20=0.910
  (对比 step0: L27 从 0.684→0.977，最大变化 +0.293；L12 仅 +0.023)

L_GAR:  -0.1673 (趋势: ↑↑ 加速增强)
  s0:-0.016 → s50:-0.022 → s75:-0.070 → s93:-0.141 → s100:-0.167
L_NTP:  0.8166 (趋势: ↓ 正常下降, from 2.03@s0)
总 loss: 0.6493 (正值 ✓)
GPU 显存: 83.5 GB / 95.6 GB (87%)

诊断结论: 绿灯 🟢 (带观察点)

分析:
1. gate_std=0.0376 > 0.02 阈值，远好于 v3 的 0.001。gates 在分化，
   但模式是"全体上升、不同速率"而非"有升有降"。后层 (L25-L27) 上升
   最快，中层 (L12-L14) 最慢。这是有结构意义的分化模式——后层 residual
   对 goal-awareness 更关键。

2. L_GAR=-0.167 刚进入目标区间 [-0.1, -0.5]，且呈加速趋势。
   与 v3b (500步时饱和到 -0.96) 对比，v5 的 λ=1.0 明显避免了早期饱和。
   ⚠️ 但 L_GAR 增速为指数型，需关注 step 200-300 是否进入饱和。

3. L_NTP 从 2.03 下降到 0.82，NTP 训练正常。

4. 总 loss=0.65 保持正值，成功避免了 v3b 的负 loss 病态。

5. 与 v3/v3b 对比:
   - v3 @500步: gate_std=0.001（死平）→ 失败
   - v3b @500步: gate_std=0.087（分化）→ 但 L_GAR=-0.96（饱和）
   - v5 @100步: gate_std=0.0376（分化中）, L_GAR=-0.167（健康）
   v5 在 100 步就展现出 v3 500 步未达到的分化水平，同时 L_GAR 远未饱和。

建议: 继续跑。下一检查点建议在 step 250-300 (batch step ~2000-2400):
  - 重点关注 L_GAR 是否进入饱和 (< -0.5)
  - gate_std 是否继续下降 (如降到 <0.02 则需警惕)
  - 后层 gate (L26/L27) 是否完全饱和到 1.0
```

---
