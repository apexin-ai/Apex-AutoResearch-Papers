# analysis deberta status and figure7

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deberta-status-and-figure7_20260522T161516_result.json`
- **Structured JSON:** [`2768724a9b7dbfc1cc45.json`](../../sessions/27/2768724a9b7dbfc1cc45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Task 1: DeBERTa 训练状态

- **进程**: 运行中，PID 640389 + 4 个 DataLoader worker
- **进度**: Step 3,480 / 182,985 (**2%**)，已跑 ~15 分钟
- **速度**: ~3.8–4.0 it/s
- **ETA**: 总计 ~12.7 小时
- **GPU**: 8,295 MiB，利用率 95%
- **Loss**: 日志中尚无 loss 输出（可能在 eval 间隔才打印）
- **错误**: 无

**数据量问题确认**：用了 585,552 全量数据。OWA 过滤失败——代码逻辑是 `if "OWA" in config`，但 ProofWriter 的 config 名称是 `NatLang`, `depth-0`, `depth-1`, ..., `depth-5`, `depth-3ext`, `depth-3ext-NatLang`，**没有任何 config 包含 "OWA" 字符串**，所以过滤器没起作用，回退到了全量数据。

如果要只训练 OWA 子集，需要修改过滤逻辑（ProofWriter OWA 子集不是通过 config 名称区分的，而是通过数据集 split 或其他字段）。

## Task 2: Figure 7 Scatter Plot

`scripts/gen_capability_gap_scatter.py` **不存在**。服务器上也没有任何 scatter/fig7/gap 相关脚本。

---
