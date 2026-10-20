# ops exp013 completion check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp013-completion-check_20260521T095538_result.json`
- **Structured JSON:** [`4e633d61c8b0a2f92954.json`](../../sessions/4e/4e633d61c8b0a2f92954.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_013 结论：**SUCCESS**

10 代 pure collapse (r=0, seed=44) 全部完成。

### Gen 8-10 Metrics

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss |
|-----|----------|---------|-----|-----------|------------|
| 8 | 454.56 | 2237.81 | 44.48 | 0.1817 | 0.6171 |
| 9 | 444.33 | 2188.92 | 54.34 | 0.1482 | 0.3899 |
| 10 | 432.91 | 2154.34 | 65.70 | 0.1515 | 0.3271 |

趋势一致：eff_rank 从 gen0 的 417→gen2 峰值 496→gen10 的 433 持续下降；ppl 从 9.55 单调升至 65.70；distinct4 从 0.73 降至 0.15；train_loss 持续收敛到 0.33。光谱集中度加剧（top-1 singular value 从 1943→912 先降后升回）。

### cuda:1 状态
已释放 — 0% utilization, 0 MiB memory。

### Registry 已更新
- status: DONE, conclusion: success
- metrics: gen8-10 已补全
- cron 监控已删除

---
