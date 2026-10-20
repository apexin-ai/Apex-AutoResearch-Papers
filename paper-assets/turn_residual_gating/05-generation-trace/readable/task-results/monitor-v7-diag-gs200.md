# monitor v7 diag gs200

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v7_diag_gs200_20260518T185721_result.json`
- **Structured JSON:** [`ca240c71e5bf74a3eed3.json`](../../sessions/ca/ca240c71e5bf74a3eed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。编译诊断报告：

```
v7 gs200 诊断

=== 1. per-layer gate profile (gs200) ===
L0=0.883  L1=0.898  L2=0.918  L3=0.797  L4=0.809  L5=0.926  L6=0.965  L7=0.844
L8=0.961  L9=0.922  L10=0.977 L11=0.910 L12=0.859 L13=0.902 L14=0.898 L15=0.973
L16=0.918 L17=0.938 L18=0.926 L19=0.965 L20=0.969 L21=0.973 L22=0.984 L23=0.969
L24=0.973 L25=0.977 L26=0.992 L27=0.992
top-3 最低: L3=0.797  L4=0.809  L7=0.844
top-3 最高: L26=0.992 L27=0.992 L22=0.984

=== 2. mean_GAR ===
L_GAR = 0.0004 → mean_GAR = 0.5 - sqrt(0.0004) = 0.5 - 0.020 = 0.480

（对比：gs0 时 L_GAR=0.2342 → mean_GAR=0.016；gs100 时 L_GAR=0.1237 → mean_GAR=0.148）
GAR 已从 0.016 飙升至 0.480，接近目标值 0.5。MSE 驱动力基本耗尽。

=== 3. gate_std / gate_mean ===
mean=0.9291  std=0.0526  min=0.7969  max=0.9922

=== 4. loss (ms1600 = gs200) ===
L_NTP=0.9926  L_GAR=0.0004  L_DIV=0.0000  total=0.9929

=== 5. GAR 最近趋势 (gs150-gs200 范围) ===
ms1150 (gs143.75): L_GAR=0.0044 → mean_GAR=0.434
ms1200 (gs150.00): L_GAR=0.0053 → mean_GAR=0.427
ms1250 (gs156.25): L_GAR=0.0359 → mean_GAR=0.311  ← 偶发 spike
ms1300 (gs162.50): L_GAR=0.0002 → mean_GAR=0.486
ms1350 (gs168.75): L_GAR=0.0001 → mean_GAR=0.490
ms1400 (gs175.00): L_GAR=0.0000 → mean_GAR≈0.500
ms1450 (gs181.25): L_GAR=0.0005 → mean_GAR=0.478
ms1500 (gs187.50): L_GAR=0.0000 → mean_GAR≈0.500
ms1550 (gs193.75): L_GAR=0.0011 → mean_GAR=0.467
ms1600 (gs200.00): L_GAR=0.0004 → mean_GAR=0.480

趋势判断：**已收敛/平台**。GAR 在 gs150 后已基本达到目标 0.5，L_GAR 在 0 附近波动。
偶有 spike（ms1250 的 0.0359，后续 ms1900 的 0.0282）但不影响整体收敛。
MSE 驱动力在 gs150 附近已耗尽，此后 gate 变化主要由 L_NTP 梯度决定。

=== 完整 GATE 时间线 ===
gs0:   mean=0.8097 std=0.0341 min=0.6836 max=0.8672
gs50:  mean=0.8125 std=0.0619 min=0.6797 max=0.9805
gs100: mean=0.8712 std=0.0506 min=0.7773 max=0.9805
gs150: mean=0.9099 std=0.0496 min=0.8203 max=0.9883
gs200: mean=0.9291 std=0.0526 min=0.7969 max=0.9922
gs250: mean=0.9410 std=0.0505 min=0.8086 max=0.9961

L_GAR 完整演化（每 50 micro-step）:
ms0:0.2342  ms50:0.2349  ms100:0.2337  ms150:0.2277  ms200:0.2348
ms250:0.2314 ms300:0.2263 ms350:0.2298 ms400:0.2368 ms450:0.2251
ms500:0.2285 ms550:0.2326 ms600:0.2179 ms650:0.2106 ms700:0.1886
ms750:0.1386 ms800:0.1237 ms850:0.0788 ms900:0.0676 ms950:0.0549
ms1000:0.0454 ms1050:0.0398 ms1100:0.0328 ms1150:0.0044 ms1200:0.0053
ms1250:0.0359 ms1300:0.0002 ms1350:0.0001 ms1400:0.0000 ms1450:0.0005
ms1500:0.0000 ms1550:0.0011 ms1600:0.0004

三个阶段清晰可见：
  Phase A (ms0-ms600, gs0-75): L_GAR ≈ 0.23 平台，GAR 几乎不动 (~0.016-0.032)
  Phase B (ms600-ms1150, gs75-144): L_GAR 快速下降 0.22→0.004，GAR 加速上升
  Phase C (ms1150+, gs144+): L_GAR ≈ 0，GAR ≈ 0.48-0.50 收敛平台

=== gs100 参考 ===
gate: mean=0.8712 std=0.0506 min=0.7773 max=0.9805
profile:
  L0:0.867 L1:0.887 L2:0.887 L3:0.832 L4:0.812 L5:0.875 L6:0.898 L7:0.797
  L8:0.879 L9:0.836 L10:0.895 L11:0.898 L12:0.777 L13:0.789 L14:0.828 L15:0.891
  L16:0.820 L17:0.824 L18:0.832 L19:0.879 L20:0.922 L21:0.883 L22:0.910 L23:0.926
  L24:0.871 L25:0.918 L26:0.980 L27:0.980
L_GAR=0.1237 → mean_GAR=0.148
top-3 最低: L12=0.777 L13=0.789 L7=0.797
top-3 最高: L26=0.980 L27=0.980 L23=0.926

gs0→gs100→gs200 对比（gate mean / GAR）:
  gs0:   0.810 / 0.016
  gs100: 0.871 / 0.148
  gs200: 0.929 / 0.480

关键观察：gate 持续上升但 GAR 已收敛，说明 gs200 后 gate 上移纯由 NTP loss 驱动（更高 gate = 更多 residual = 更低 NTP loss），GAR regularization 已不再提供下拉力。
```

---
