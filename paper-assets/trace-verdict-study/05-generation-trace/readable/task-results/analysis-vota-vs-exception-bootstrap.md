# analysis vota vs exception bootstrap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vota_vs_exception_bootstrap_20260519T112524_result.json`
- **Structured JSON:** [`ca276b3273eff09f7457.json`](../../sessions/ca/ca276b3273eff09f7457.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

```
Per-seed results:
  seed42:  exc=99.83%, vota=99.41%, diff=+0.42pp, bootstrap p=0.0629, McNemar χ²=2.78, p=0.0956
  seed123: exc=99.83%, vota=98.66%, diff=+1.18pp, bootstrap p=0.0002, McNemar χ²=10.89, p=0.0010
  seed456: exc=99.83%, vota=99.08%, diff=+0.76pp, bootstrap p=0.0047, McNemar χ²=6.23,  p=0.0126

Aggregate:
  Mean diff: +0.78pp ± 0.31pp
  Range: [0.42, 1.18]pp
```

关键发现：
- **seed123 和 seed456** 均显著（bootstrap p < 0.005, McNemar p < 0.013）
- **seed42** 差异最小（+0.42pp），bootstrap p=0.063, McNemar p=0.096，未达 0.05 显著性门槛——因为 exception_only 和 VOTA 在 seed42 上都接近天花板，discordant pairs 只有 9 个
- 所有 3 个 seed 方向一致：exception_only > VOTA，且 discordant pairs 中 exc_right_vota_wrong 始终远多于反向（7:2, 16:2, 11:2）
- 论文中可以这样写：2/3 seeds 达到统计显著（p < 0.05），第三个 seed 方向一致但因天花板效应未达显著性；跨 seed 平均差异 +0.78 ± 0.31pp

---
